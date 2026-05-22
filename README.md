# Design Principles Practice

This repository is a place to collect useful design principles and keep short notes and examples for each one.
The main goal is to make them easy to review later, compare side by side, and revisit when needed.

## Project Structure

All principle examples live under `principles/`.

```text
principles/
  SRP/
    README.md
    example.py
    bad_example.py
  OCP/
  SOC/
  ...
README.md
pyproject.toml
uv.lock
```

This keeps the repository root focused on project-level files and makes it easier to grow the collection over time.

## Principle Index

| Code | Principle |
| --- | --- |
| `COI` | Composition Over Inheritance |
| `DIP` | Dependency Inversion Principle |
| `DRY` | Don't Repeat Yourself |
| `ETUHM` | Easy to Use and Hard to Misuse |
| `EWV` | Encapsulate What Varies |
| `FF` | Fail Fast |
| `GP` | Generalization Principle |
| `HC` | High Cohesion |
| `HOLLYWOOD` | Hollywood Principle |
| `IAP` | Invariant Avoidance Principle |
| `ISP` | Interface Segregation Principle |
| `KISS` | Keep It Simple, Stupid |
| `LC` | Low Coupling |
| `LOD` | Law of Demeter |
| `LSP` | Liskov Substitution Principle |
| `MIMC` | More Is More Complex |
| `MP` | Model Principle |
| `MURPHY` | Murphy's Law |
| `OCP` | Open/Closed Principle |
| `POLA` | Principle of Least Astonishment |
| `PSU` | Principle Of Separate Understandability |
| `PTI` | Program to an Interface, Not an Implementation |
| `ROE` | Rule of Explicitness |
| `SLA` | Single Level of Abstraction |
| `SOC` | Separation of Concerns |
| `SRP` | Single Responsibility Principle |
| `TDA` | Tell, Don't Ask |
| `UP` | Uniformity Principle |
| `YAGNI` | You Aren't Gonna Need It |

## How To Read This Repository

Start with any principle directory in `principles/`.
Read `README.md` first, then compare `bad_example.py` with `example.py`.

That flow is meant to keep the lessons concrete:

1. Understand the problem.
2. See the weaker design.
3. See the cleaner revision.
