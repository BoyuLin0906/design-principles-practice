# Encapsulate What Varies

## Intent

Identify the part of the code that is most likely to change and place it behind a focused abstraction.

## Problem

When stable workflow code is mixed with rules that change often, every new variation forces edits in the same place. That makes the code harder to extend and easier to break.

## Bad Example

The bad example keeps checkout logic and shipping-price rules inside one `Checkout` class. It works for a few shipping methods, but adding or changing a rule means modifying the checkout flow itself.

## Refactored Example

The refactored example keeps the checkout flow stable and moves each shipping rule into its own policy class. `Checkout` only coordinates the order total and asks the selected policy for the shipping cost.

## Trade-offs

Encapsulating variation usually adds a few more classes. That extra structure may feel unnecessary for a tiny script, but it helps when the changing rules start to grow faster than the rest of the workflow.
