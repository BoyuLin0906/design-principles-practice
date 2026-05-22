from datetime import datetime, timedelta


class NotificationService:
    def send_now(self, recipient: str, message: str) -> None:
        print(f"Sending to {recipient} now: {message}")

    def schedule(self, recipient: str, message: str, send_at: datetime) -> None:
        print(
            f"Scheduling message for {recipient} at "
            f"{send_at:%Y-%m-%d %H:%M}: {message}"
        )


if __name__ == "__main__":
    service = NotificationService()
    send_time = datetime.now() + timedelta(hours=2)

    service.send_now("ava@example.com", "Invoice ready")
    service.schedule("ben@example.com", "Reminder", send_time)
