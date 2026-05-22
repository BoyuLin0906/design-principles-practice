class Order:
    def __init__(self, customer_email: str) -> None:
        self.customer_email = customer_email
        self.items: list[dict] = []

    def add_item(self, name: str, price: float) -> None:
        self.items.append({"name": name, "price": price})

    def total(self) -> float:
        return sum(item["price"] for item in self.items)


class EmailService:
    # Email logic is kept in a focused service.
    def send_confirmation(self, order: Order) -> None:
        print(f"Sending confirmation email to {order.customer_email}")


class ShippingService:
    # Shipping logic stays separate from order data.
    def print_label(self, order: Order) -> None:
        print(f"Printing shipping label for {len(order.items)} items")


if __name__ == "__main__":
    order = Order("andy@example.com")
    order.add_item("Keyboard", 99.0)
    order.add_item("Mouse", 45.0)

    # Each class now serves one clearer purpose.
    print(f"Order total: ${order.total():.2f}")

    email_service = EmailService()
    shipping_service = ShippingService()
    email_service.send_confirmation(order)
    shipping_service.print_label(order)
