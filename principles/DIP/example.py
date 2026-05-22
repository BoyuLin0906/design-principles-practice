from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        raise NotImplementedError


class EmailSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending email to {recipient}: {message}")


class SmsSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")


class OrderNotifier:
    def __init__(self, message_sender: MessageSender) -> None:
        self.message_sender = message_sender

    def notify(self, recipient: str, order_id: str) -> None:
        message = f"Your order {order_id} has been shipped."
        self.message_sender.send(recipient, message)


if __name__ == "__main__":
    email_notifier = OrderNotifier(EmailSender())
    email_notifier.notify("customer@example.com", "A-1024")

    sms_notifier = OrderNotifier(SmsSender())
    sms_notifier.notify("+1-555-0100", "B-2048")
