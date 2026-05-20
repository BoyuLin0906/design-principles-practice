class Speaker:
    def play_music(self, song: str) -> None:
        print(f"Playing '{song}' through the built-in player.")


class BluetoothSpeaker(Speaker):
    def connect_bluetooth(self, device_name: str) -> None:
        print(f"Connected to {device_name} with Bluetooth.")


class SmartSpeaker(Speaker):
    def ask_assistant(self, question: str) -> None:
        print(f"Assistant answer for: {question}")


class BluetoothSmartSpeaker(Speaker):
    # A new feature combination needs a whole new subclass.
    def connect_bluetooth(self, device_name: str) -> None:
        print(f"Connected to {device_name} with Bluetooth.")

    def ask_assistant(self, question: str) -> None:
        print(f"Assistant answer for: {question}")


if __name__ == "__main__":
    speaker = BluetoothSmartSpeaker()
    speaker.connect_bluetooth("Andy's Phone")
    speaker.play_music("City Lights")
    speaker.ask_assistant("What is the weather today?")
