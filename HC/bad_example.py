class Order:
    def __init__(self, customer_email: str) -> None:
        self.customer_email = customer_email
        self.items: list[dict] = []

    def add_item(self, name: str, price: float) -> None:
        self.items.append({"name": name, "price": price})

    def total(self) -> float:
        return sum(item["price"] for item in self.items)

    # Email behavior does not really belong to the order data itself.
    def send_confirmation_email(self) -> None:
        print(f"Sending confirmation email to {self.customer_email}")

    # Shipping behavior is another separate concern mixed into this class.
    def print_shipping_label(self) -> None:
        print("Printing shipping label")


if __name__ == "__main__":
    order = Order("andy@example.com")
    order.add_item("Keyboard", 99.0)
    order.add_item("Mouse", 45.0)

    # One class now handles order data, email, and shipping.
    print(f"Order total: ${order.total():.2f}")
    order.send_confirmation_email()
    order.print_shipping_label()
