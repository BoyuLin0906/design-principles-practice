# Easy to Use and Hard to Misuse

## Intent

Design APIs so the correct way to use them is clear, and incorrect usage is difficult or impossible.

## Problem

When a function accepts several flags or values that can be combined in invalid ways, callers must remember hidden rules. That makes mistakes easier, especially when the code is read quickly or reused in a different context.

## Bad Example

The bad example uses one `deliver` method for both immediate and scheduled delivery. Callers can pass `send_now=True` together with a scheduled time, or forget both options, so the method has to deal with confusing combinations.

## Refactored Example

The refactored example splits the API into `send_now` and `schedule`. Each method matches one clear action, so the caller does not need to remember which argument combinations are valid.

## Trade-offs

Making misuse harder often means adding a little more structure to the API. That extra structure is usually worth it when it removes invalid states and makes the code easier to understand.
