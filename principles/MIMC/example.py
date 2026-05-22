class Notifier:
    def send(self, recipient: str, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, recipient: str, message: str) -> None:
        print(f"Send email to {recipient}: {message}")


def notify_report_ready(notifier: Notifier, recipient: str) -> None:
    notifier.send(recipient, "Your report is ready.")


if __name__ == "__main__":
    notifier = EmailNotifier()
    notify_report_ready(notifier, "mia@example.com")
