# Program to an Interface, Not an Implementation

## Intent

Write client code against a small shared contract instead of tying it to one concrete class.

## Problem

When code depends on one specific implementation, it often learns too much about that class. Adding a second implementation then forces changes in the client code instead of letting both versions be used the same way.

## Bad Example

The bad example builds `MusicPlayer` directly around `LocalMusicSource`. It knows that songs come from file paths, so the player is tied to local files.

## Refactored Example

The refactored example introduces an `AudioSource` abstraction. `MusicPlayer` only asks for playable audio data, so it can work with `LocalMusicSource`, `StreamingSource`, or other sources that follow the same contract.

## Trade-offs

This style usually adds an extra interface or abstract base class. That can feel like more setup in a tiny example, but it keeps the player easier to extend when new sources appear.
