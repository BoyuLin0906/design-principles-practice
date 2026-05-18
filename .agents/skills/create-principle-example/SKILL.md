---
name: create-principle-example
description: Load when the user wants to add or revise a design-principle example in this repo, usually a folder with `README.md`, `example.py`, and `bad_example.py`. Common requests mention SRP, OCP, SOLID, or bad-vs-good practice examples.
---

# Create Principle Example

Use this skill for repo example creation, not general theory.

## Core behavior

- Keep one principle per directory, usually with a clear abbreviation such as `SRP` or `OCP`.
- Default structure: `README.md`, `example.py`, and `bad_example.py`.
- Write all repository content in English.
- Keep examples small and practical.
- If the user does not specify a language, use Python.

## README guidance

- Include the full principle name, even if the directory uses an abbreviation.
- Explain the intent in simple language.
- Describe the problem the principle helps prevent.
- Briefly compare the bad and refactored examples.
- Mention trade-offs only when they are relevant.

## Example guidance

- Make the bad example look reasonable at first glance.
- Show a problem that appears as the code grows or changes.
- Let the refactor directly address that problem.
- Keep the improvement simple.
- Add only a few short comments when they help.

## Gotchas

- Do not turn the README into a theory-heavy essay.
- Do not make the bad example obviously silly.
- Do not solve unrelated problems in the refactor.
- Do not over-engineer the "good" version.
- Do not drift from the standard repository structure unless the user asks for a variant.
- If the folder name is abbreviated, still spell out the full principle name in the README.

## Eval hints

### Positive examples

- "Add an OCP example to this repo."
- "Create a new principle folder with a README, bad example, and improved example."
- "Revise the SRP example to make the bad and good versions easier to compare."
- "Make a small Python practice example for the Dependency Inversion Principle."

### Negative examples

- "Explain the Open/Closed Principle."
- "Generate a long tutorial about SOLID."
- "Refactor this production service for maintainability."
- "Add tests for the SRP example."

### Known failures

- The agent may load this skill when the user only wants an explanation.
- The agent may make examples too large or abstract.
- The agent may make the bad example too obviously wrong.
- The agent may write theory instead of helping compare the code.

### Neighbor confusion

- Requests to explain a principle belong to the base agent unless the user also wants repository content created or updated.
- Requests to refactor an existing application or service are software-change tasks, not principle-example tasks.
- Requests about commit messages or commit splitting belong to `git-conventional-commits`.
