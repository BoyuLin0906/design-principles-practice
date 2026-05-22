class CheckoutSummary:
    def subtotal(self, items: list[dict[str, float]]) -> float:
        return sum(item["price"] for item in items)

    def tax(self, items: list[dict[str, float]]) -> float:
        return self.subtotal(items) * 0.1

    def shipping(self, destination: str) -> float:
        if destination == "local":
            return 5.0
        return 12.0

    def total(self, items: list[dict[str, float]], destination: str) -> float:
        return self.subtotal(items) + self.tax(items) + self.shipping(destination)


if __name__ == "__main__":
    items = [
        {"name": "Keyboard", "price": 50.0},
        {"name": "Mouse", "price": 20.0},
    ]

    checkout = CheckoutSummary()
    print(checkout.total(items, "local"))
