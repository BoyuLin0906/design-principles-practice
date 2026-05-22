class CheckoutSummary:
    def subtotal(self, items: list[dict[str, float]]) -> float:
        return sum(item["price"] for item in items)

    def tax(self, items: list[dict[str, float]]) -> dict[str, float]:
        return {"amount": self.subtotal(items) * 0.1}

    def shipping(self, destination: str) -> str:
        if destination == "local":
            return "5.00"
        return "12.00"

    def total(self, items: list[dict[str, float]], destination: str) -> float:
        subtotal = self.subtotal(items)
        tax = self.tax(items)["amount"]
        shipping = float(self.shipping(destination))
        return subtotal + tax + shipping


if __name__ == "__main__":
    items = [
        {"name": "Keyboard", "price": 50.0},
        {"name": "Mouse", "price": 20.0},
    ]

    checkout = CheckoutSummary()
    print(checkout.total(items, "local"))
