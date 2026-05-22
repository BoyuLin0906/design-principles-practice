from datetime import datetime, timedelta


class NotificationService:
    def deliver(
        self,
        recipient: str,
        message: str,
        *,
        send_now: bool = False,
        scheduled_for: datetime | None = None,
    ) -> None:
        if send_now and scheduled_for is not None:
            print(
                f"Sending to {recipient} now. "
                f"The scheduled time {scheduled_for:%H:%M} is ignored."
            )
            return

        if send_now:
            print(f"Sending to {recipient} now: {message}")
            return

        if scheduled_for is not None:
            print(
                f"Scheduling message for {recipient} at "
                f"{scheduled_for:%Y-%m-%d %H:%M}: {message}"
            )
            return

        raise ValueError("Choose send_now=True or provide scheduled_for.")


if __name__ == "__main__":
    service = NotificationService()
    send_time = datetime.now() + timedelta(hours=2)

    service.deliver("ava@example.com", "Invoice ready", send_now=True)
    service.deliver(
        "ben@example.com",
        "Reminder",
        send_now=True,
        scheduled_for=send_time,
    )
