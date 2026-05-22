# Principle Of Separate Understandability

## Intent

Keep each module understandable on its own, without forcing it to carry data that only makes sense in some other context.

## Problem

When a class contains fields that are only meaningful to another module or workflow, the class becomes harder to understand in isolation. Readers have to ask why that data is there and whether it belongs to the class at all.

## Bad Example

The bad example stores `csv_row_number` inside `Order`. That means the order model also carries CSV import context: which row this order came from.

## Refactored Example

The refactored example keeps `Order` focused on order data only. `CsvOrderRow` is the object that says which CSV row produced which order.

## Trade-offs

Following this principle can introduce an extra wrapper object such as `CsvOrderRow`. That small cost is often worth it when it keeps the core model cleaner and easier to reason about.
