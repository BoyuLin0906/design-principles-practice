from abc import ABC, abstractmethod


class AudioSource(ABC):
    @abstractmethod
    def load(self, song_id: str) -> str:
        raise NotImplementedError


class LocalMusicSource(AudioSource):
    def load(self, song_id: str) -> str:
        songs = {
            "song-1": "/music/city-lights.mp3",
            "song-2": "/music/morning-rain.mp3",
        }
        return f"local file {songs[song_id]}"


class StreamingSource(AudioSource):
    def load(self, song_id: str) -> str:
        streams = {
            "song-1": "https://stream.example.com/city-lights",
            "song-2": "https://stream.example.com/morning-rain",
        }
        return f"stream {streams[song_id]}"


class MusicPlayer:
    def __init__(self, audio_source: AudioSource) -> None:
        self.audio_source = audio_source

    def play(self, song_id: str) -> None:
        audio = self.audio_source.load(song_id)
        print(f"Playing audio from {audio}")


if __name__ == "__main__":
    local_player = MusicPlayer(LocalMusicSource())
    local_player.play("song-1")

    streaming_player = MusicPlayer(StreamingSource())
    streaming_player.play("song-2")
