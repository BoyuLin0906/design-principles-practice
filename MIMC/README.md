# More Is More Complex

## Intent

Avoid making code more complex than the current problem requires. Start with a simple design that solves today's need clearly, and let the structure evolve when real new requirements appear.

## Problem

When developers design for many imagined future needs too early, the code often gains extra layers, options, and setup before those things are useful. That makes the current solution harder to understand and change.

## Bad Example

The bad example only needs to send email notifications, but it already introduces multiple notifier classes, a registry, and channel selection logic for future possibilities. The code becomes more complicated even though the real requirement is still small.

## Refactored Example

The refactored example keeps a small notifier abstraction and one email implementation. It stays simple for today while still making future changes easier if another notification type becomes a real requirement.

## Trade-offs

Keeping the design smaller may mean adding structure later when the system grows. That is often a better trade-off than carrying extra complexity before it solves a real problem.
