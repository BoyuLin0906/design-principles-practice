#!/usr/bin/env bash

set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

collect_changed_paths() {
  if git rev-parse --verify HEAD >/dev/null 2>&1; then
    git diff --name-only --diff-filter=ACMR HEAD --
  fi
  git ls-files --others --exclude-standard
}

run_check() {
  changed_paths="$(collect_changed_paths)"
  principle_dirs=()

  while IFS= read -r path; do
    [[ -z "$path" ]] && continue

    case "$path" in
      .agents/*|.codex/*|.githooks/*)
        continue
        ;;
      .*|README.md|AGENTS.md)
        continue
        ;;
    esac

    if [[ "$path" != */* ]]; then
      continue
    fi

    principle_dir="${path%%/*}"

    if [[ ! -d "$principle_dir" ]]; then
      continue
    fi

    already_added=false
    for existing_dir in "${principle_dirs[@]}"; do
      if [[ "$existing_dir" == "$principle_dir" ]]; then
        already_added=true
        break
      fi
    done

    if [[ "$already_added" == false ]]; then
      principle_dirs+=("$principle_dir")
    fi
  done <<< "$changed_paths"

  if [[ "${#principle_dirs[@]}" -eq 0 ]]; then
    return 0
  fi

  missing_any=false

  for principle_dir in "${principle_dirs[@]}"; do
    missing_items=()

    [[ -f "$principle_dir/README.md" ]] || missing_items+=("README.md")
    [[ -f "$principle_dir/example.py" ]] || missing_items+=("example.py")
    [[ -f "$principle_dir/bad_example.py" ]] || missing_items+=("bad_example.py")

    if [[ "${#missing_items[@]}" -gt 0 ]]; then
      missing_any=true
      printf 'Principle directory "%s" is missing: %s\n' \
        "$principle_dir" \
        "$(IFS=', '; echo "${missing_items[*]}")"
    fi
  done

  if [[ "$missing_any" == true ]]; then
    echo "Check failed. Each changed principle directory must contain README.md, example.py, and bad_example.py."
    return 1
  fi
}

if run_check >/tmp/codex-principle-check.out 2>/tmp/codex-principle-check.err; then
  printf '{"continue":true}\n'
  exit 0
fi

message="$(cat /tmp/codex-principle-check.err /tmp/codex-principle-check.out 2>/dev/null | tr '\n' ' ' | sed 's/[[:space:]]\+/ /g' | sed 's/^ //; s/ $//')"
message="${message//\"/\\\"}"

if [ -z "$message" ]; then
  message="Principle structure check failed."
fi

echo "Stop hook failed: $message" >&2

printf '{"continue":false,"stopReason":"Principle structure check failed","systemMessage":"%s"}\n' "$message"
