# Keep It Simple, Stupid

## Intent

Prefer the simplest solution that clearly solves the current problem.

## Problem

Code becomes harder to read and change when a very small task is wrapped in too many classes or steps. Extra structure can make simple behavior feel more complicated than it really is.

## Bad Example

The bad example checks whether a user is an adult, but it does that through multiple small classes. It works, yet a simple age check becomes harder to follow.

## Refactored Example

The refactored example uses one small function for the same rule. The logic stays in one place, so the behavior is easier to read and change.

## Trade-offs

Keeping code simple does not mean avoiding structure forever. When requirements truly grow, adding a small abstraction can help, but it should solve a real problem instead of anticipating one too early.
