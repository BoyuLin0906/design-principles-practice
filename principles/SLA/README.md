# Single Level of Abstraction

## Intent

Keep each function focused on one level of detail instead of mixing high-level steps with low-level implementation work.

## Problem

When one function jumps between business steps and formatting details, it becomes harder to scan, explain, and change. Small low-level changes can make an important workflow harder to follow.

## Bad Example

The bad example puts the whole weekly summary process inside `publish_weekly_summary`. The method decides which tasks are ready, builds the heading, formats each line, and prints the message all in one place.

## Refactored Example

The refactored example keeps `publish_weekly_summary` at the workflow level. Helper methods handle task selection, title creation, body formatting, and delivery, so each method stays at a more consistent level of abstraction.

## Trade-offs

Following this principle can add a few more small methods. That is usually a good trade when it makes the main workflow easier to read.
