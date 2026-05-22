# Single Responsibility Principle

## Intent

One class or module should have one clear responsibility.

## Problem

When one class handles validation, storage, and notifications at the same time, small changes become risky. The code becomes harder to test and harder to update without side effects.

## Bad Example

The bad example uses one `UserService` class to validate input, save the user, and send a welcome email. It looks convenient at first, but it mixes several responsibilities in one place.

## Refactored Example

The refactored example separates validation, storage, and email sending into focused classes. `UserService` keeps the workflow, but each supporting class has one clear job.

## Trade-offs

Using SRP often creates more classes and files. That can feel heavier in very small scripts, but it usually makes changes easier once the code starts to grow.
