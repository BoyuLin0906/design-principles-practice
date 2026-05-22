# Tell, Don't Ask

## Intent

Prefer telling an object what outcome you need instead of pulling out its state and deciding everything from the outside.

## Problem

When other parts of the code keep asking an object for internal details, decision-making spreads across the system. That makes rules harder to find and easier to duplicate.

## Bad Example

The bad example has `follow_up_ticket` inspect a ticket's status, age, and assignee before deciding what action to take. The workflow knows too much about the ticket's internal state.

## Refactored Example

The refactored example moves the follow-up decision into `SupportTicket.follow_up`. The workflow tells the ticket to handle follow-up, and the ticket decides whether to close, escalate, or ping the assigned agent.

## Trade-offs

Following this principle can move more behavior into domain objects. That usually improves cohesion, but very small data-only structures may not need that extra behavior.
