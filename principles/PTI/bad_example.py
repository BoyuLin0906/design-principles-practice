class LocalMusicSource:
    def get_file_path(self, song_id: str) -> str:
        songs = {
            "song-1": "/music/city-lights.mp3",
            "song-2": "/music/morning-rain.mp3",
        }
        return songs[song_id]


class MusicPlayer:
    def __init__(self, music_source: LocalMusicSource) -> None:
        self.music_source = music_source

    def play(self, song_id: str) -> None:
        file_path = self.music_source.get_file_path(song_id)
        print(f"Playing audio from local file: {file_path}")


if __name__ == "__main__":
    player = MusicPlayer(LocalMusicSource())
    player.play("song-1")
