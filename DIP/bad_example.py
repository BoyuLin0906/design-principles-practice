class EmailService:
    def send(self, address: str, message: str) -> None:
        print(f"Sending email to {address}: {message}")


class OrderNotifier:
    def __init__(self) -> None:
        self.email_service = EmailService()

    def notify(self, customer_email: str, order_id: str) -> None:
        message = f"Your order {order_id} has been shipped."
        self.email_service.send(customer_email, message)


if __name__ == "__main__":
    notifier = OrderNotifier()
    notifier.notify("customer@example.com", "A-1024")
