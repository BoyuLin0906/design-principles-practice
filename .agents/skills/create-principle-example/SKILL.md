---
name: create-principle-example
description: Create or update a design principle example in this repository with a clear README, a realistic bad example, and a simple refactored example.
---

# Create Principle Example

Use this skill when the task is to add or update a design principle example in this repository.

## Goal

Create a small, clear principle example with practical code.

## Structure

Create one principle directory with:

- `README.md`
- `example.py`
- `bad_example.py`

The directory name may use a clear abbreviation.

## Writing Style

- Write everything in English.
- Keep explanations short and simple.
- Prefer practical examples over theory.

## README Sections

The principle `README.md` should usually include:

- The full principle name, even if the directory uses an abbreviation.
- Intent
- Problem
- Bad Example
- Refactored Example
- Trade-offs

## Bad Example Rules

- Make the bad example look reasonable at first.
- Show problems that appear as the code grows or changes.
- Avoid obviously silly or sloppy code.

## Refactor Rules

- Make the refactored example fix the bad example directly.
- Do not over-engineer the solution.
- Keep the improvement easy to understand.

## Notes

- Keep directory names clear and predictable.
- Do not make the example too large unless the user asks for more detail.
- If no language is specified, choose a simple one that fits the repository.
- Use flat example files when possible to keep the structure easy to scan.
- Add a few short comments in both `example.py` and `bad_example.py` to highlight the design lesson, but avoid heavy or line-by-line commentary.
