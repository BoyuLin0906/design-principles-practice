---
name: git-conventional-commits
description: Load when the user wants help splitting changes into commits, writing a Conventional Commit message, or staging commits logically.
---

# Git Conventional Commits

Use this skill for commit planning and commit messages, not for general git help.

## Core behavior

- Check the working tree before suggesting a message.
- Group changes by intent, not by file count.
- If multiple intents are mixed, suggest commit groups before exact messages.
- If asked to commit, stage only one logical group at a time.

## Commit format

Use `<type>[optional scope]: <description>`.

- Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`, `style`, `build`, `ci`, `revert`
- Use scope only when it adds useful context.
- Keep the subject short and imperative.
- Do not end the subject with a period.
- For breaking changes, use `!` or a `BREAKING CHANGE:` footer.

## Repository cues

- Useful scopes here include `readme`, `srp`, `vscode`, `hooks`, and `agents`.
- Prefer the type that matches the user-visible intent.

## Gotchas

- Do not assume a small diff should be one commit.
- Do not group changes only by folder when the intent differs.
- Do not write a message before checking the diff.
- Do not default everything to `chore`.
- Do not commit if the user only asked for a plan or suggestion.

## Eval hints

### Positive examples

- "Help me split these changes into sensible commits."
- "Write a Conventional Commit message for this diff."
- "Review my changes and suggest commit groups."
- "Stage this logically and make the commit."

### Negative examples

- "Explain what Conventional Commits are."
- "Show me the last three commits."
- "Rebase this branch onto main."
- "Fix the failing tests before we commit."

### Known failures

- The agent may load this skill for any git-related request, even when the user is not asking about commits.
- The agent may collapse mixed docs, tooling, and feature changes into one commit.
- The agent may overuse `chore` when a better type exists.
- The agent may suggest a message without reading the actual diff.

### Neighbor confusion

- Requests about branch cleanup, rebase, merge conflicts, or git recovery are general git tasks, not commit-structuring tasks.
- Requests to review code quality or bugs belong to code review or implementation work, even if a commit happens later.
- Requests to add or revise repository principle examples belong to `create-principle-example`.
