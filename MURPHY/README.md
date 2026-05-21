# Murphy's Law

## Intent

Assume that inputs, dependencies, or timing can fail, and design the code so those failures are handled safely.

## Problem

Code that only works when everything goes right often looks simple at first. Once real data is missing or malformed, the same code can crash in confusing ways or produce partial results.

## Bad Example

The bad example processes a shipment update by assuming the payload always contains a tracking number, an item count, and a valid status. It works for happy-path input, but it fails as soon as one field is missing or invalid.

## Refactored Example

The refactored example validates the payload before applying the update. It rejects missing fields, prevents invalid counts, and handles unknown statuses with clear messages.

## Trade-offs

Planning for failure adds a little more branching and validation code. That extra effort is usually worth it when the code deals with external input or unreliable systems.
