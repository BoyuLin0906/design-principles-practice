# Rule of Explicitness

## Intent

Prefer explicit solutions over implicit ones, so behavior is stated clearly instead of being hidden in side effects, indirection, or values that readers must interpret.

## Problem

When code uses raw numbers or strings with hidden meaning, readers must remember what each value stands for. That slows down reviews and makes mistakes easier when conditions or business rules change.

## Bad Example

The bad example uses status values like `0`, `1`, and `2` directly in several parts of the payment flow. The code works, but the meaning of those numbers is not obvious unless the reader already knows the convention.

## Refactored Example

The refactored example replaces magic numbers with a `PaymentStatus` enum. Conditions such as `PaymentStatus.PAID` and `PaymentStatus.PENDING` explain the intent directly in shipping, reminder, and status-message logic.

## Trade-offs

Being explicit adds a small amount of structure. In return, the code becomes easier to read, safer to refactor, and less dependent on shared memory.
