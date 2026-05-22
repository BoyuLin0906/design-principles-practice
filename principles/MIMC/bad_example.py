class EmailNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"Send email to {recipient}: {message}")


class SmsNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"Send SMS to {recipient}: {message}")


class PushNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"Send push notification to {recipient}: {message}")


class NotificationManager:
    def __init__(self) -> None:
        # The current requirement only needs email, but the code already
        # prepares several channels and selection logic for future guesses.
        self.notifiers = {
            "email": EmailNotifier(),
            "sms": SmsNotifier(),
            "push": PushNotifier(),
        }

    def send(self, channel: str, recipient: str, message: str) -> None:
        notifier = self.notifiers[channel]
        notifier.send(recipient, message)


if __name__ == "__main__":
    manager = NotificationManager()
    manager.send("email", "mia@example.com", "Your report is ready.")
