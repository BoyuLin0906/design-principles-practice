# Fail Fast

## Intent

Detect invalid state or invalid input as early as possible and stop before more work depends on it.

## Problem

When code accepts bad input and keeps going, the real error often appears later in a less obvious place. That makes debugging harder and can waste time on work that should never have started.

## Bad Example

The bad example lets `BackupJob` start running with raw configuration data. It only discovers that `compression_level` is invalid after the job has already started.

## Refactored Example

The refactored example validates the backup configuration when `BackupConfig` is created. If the input is invalid, the program fails immediately with a clear message before the job begins.

## Trade-offs

Failing fast can feel strict because invalid input is rejected right away. That is usually helpful, but it means callers must be ready to handle validation errors sooner.
