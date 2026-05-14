# AGENTS.md

## Repository Goal

- This repository is for practicing design principles in a simple and repeatable way.
- Focus on small, clear examples instead of large or production-style implementations.
- Prefer examples that are easy to compare, discuss, and revisit later.

## Current Project Context

- The repository currently uses Python with `uv`.
- A local virtual environment is expected at `.venv/`.
- Project metadata is managed in `pyproject.toml`.
- Workspace editor preferences may be stored in `.vscode/settings.json`.

## Writing Rules

- Write all repository content in English.
- Keep explanations short, clear, and easy to follow.
- Prefer practical examples over theory-heavy descriptions.
- Use `README.md` to explain each principle in a simple way.

## Principle Structure

- Each design principle should have its own directory.
- Use a clear and predictable directory name such as `SRP` or `OCP`.
- A principle directory should normally include:
  - `README.md`
  - `example.py`
  - `bad_example.py`
- Use `example.py` to show a better or cleaner approach.
- Use `bad_example.py` to show what should be avoided.
- Keep the structure consistent across principles.

## Example Guidelines

- Keep examples small enough to understand in one reading.
- Make the bad example look reasonable at first, not intentionally messy.
- Make the refactored example directly address the problems in the bad example.
- Avoid over-engineering the refactored version.
- If no language is specified, use Python.

## README Guidelines

- Include the full principle name, even if the directory uses an abbreviation.
- Explain the intent in simple language.
- Describe the problem the principle helps prevent.
- Briefly compare the bad example and the refactored example.
- Mention trade-offs when they are relevant.
