# Don't Repeat Yourself

## Intent

Avoid duplicating the same logic in multiple places.

## Problem

When the same rule or formatting logic appears in several methods, small changes must be repeated everywhere. That increases the chance of inconsistent behavior and missed updates.

## Bad Example

The bad example builds a sales report and an inventory report with nearly identical formatting code. It works, but changing the report layout means editing both methods.

## Refactored Example

The refactored example moves the shared formatting into one helper method. Each report still provides its own title and rows, but the layout logic lives in one place.

## Trade-offs

Applying DRY too early can create abstractions that hide simple code. It helps most when the duplication is real, stable, and likely to change together.
