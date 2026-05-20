class BluetoothConnection:
    def connect(self, device_name: str) -> None:
        print(f"Connected to {device_name} with Bluetooth.")


class VoiceAssistant:
    def answer(self, question: str) -> None:
        print(f"Assistant answer for: {question}")


class Speaker:
    def __init__(self, connection=None, assistant=None) -> None:
        # has-a: a speaker can have a connection strategy.
        self.connection = connection
        # has-a: a speaker can also have an assistant feature.
        self.assistant = assistant

    def play_music(self, song: str) -> None:
        print(f"Playing '{song}' through the built-in player.")

    def connect(self, device_name: str) -> None:
        if self.connection is None:
            print("This speaker has no external connection feature.")
            return

        self.connection.connect(device_name)

    def ask_assistant(self, question: str) -> None:
        if self.assistant is None:
            print("This speaker has no voice assistant feature.")
            return

        self.assistant.answer(question)


if __name__ == "__main__":
    # This example avoids an is-a chain like BluetoothSpeaker -> Speaker.
    # Instead, Speaker has-a BluetoothConnection and has-a VoiceAssistant.
    smart_bluetooth_speaker = Speaker(
        connection=BluetoothConnection(),
        assistant=VoiceAssistant(),
    )
    smart_bluetooth_speaker.connect("Andy's Phone")
    smart_bluetooth_speaker.play_music("City Lights")
    smart_bluetooth_speaker.ask_assistant("What is the weather today?")

    simple_speaker = Speaker()
    simple_speaker.play_music("Quiet Morning")
