---
name: git-conventional-commits
description: Review git changes, suggest logical commit splits, and write or create commit messages that follow the Conventional Commits 1.0.0 format.
---

# Git Conventional Commits

Use this skill when the task is to review git changes, split them into sensible commits, or write commit messages in Conventional Commits format.

## Goal

Keep git history clear, reviewable, and consistent with Conventional Commits 1.0.0.

## Format

Use:

`<type>[optional scope]: <description>`

Examples:

- `feat: add SRP example`
- `docs(readme): sync root project structure`
- `chore(vscode): add workspace python interpreter`

For breaking changes:

- use `!` before `:`, such as `feat(api)!: rename user endpoint`
- or add a footer starting with `BREAKING CHANGE:`

## Rules

- Every commit must start with a type.
- Use `feat` for new features and `fix` for bug fixes.
- Common extra types: `docs`, `chore`, `refactor`, `test`, `perf`, `style`, `build`, `ci`, `revert`.
- Use a scope only when it adds useful context.
- Keep the description short, specific, and imperative.
- Do not end the description with a period.

## Workflow

1. Check changes with `git status --short`, `git diff --stat`, and targeted `git diff`.
2. Group changes by intent, not by file count.
3. If setup, docs, tooling, and feature work are mixed, recommend separate commits.
4. If asked to commit, stage only one logical group at a time and use non-interactive git commands.

## Repository Fit

Helpful scopes in this repository include `readme`, `srp`, `vscode`, `hooks`, and `agents`.

Common commit patterns here:

- `chore: initialize python project with uv`
- `docs: define repository conventions for principle examples`
- `chore(hooks): enforce principle file structure`
- `feat(srp): add single responsibility principle example`

## Notes

- If one change contains multiple intents, split it into multiple commits.
- When the user asks for a commit plan, suggest commit groups before suggesting messages.
