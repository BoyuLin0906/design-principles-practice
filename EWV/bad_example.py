class Checkout:
    def total_with_shipping(self, items: list[dict], shipping_method: str) -> float:
        subtotal = sum(item["price"] * item["quantity"] for item in items)

        # Shipping rules change more often than the checkout flow,
        # but they are mixed together here.
        if shipping_method == "standard":
            shipping_cost = 5.0
        elif shipping_method == "express":
            shipping_cost = 15.0
        elif shipping_method == "overnight":
            shipping_cost = 25.0
        else:
            raise ValueError(f"Unknown shipping method: {shipping_method}")

        return subtotal + shipping_cost


if __name__ == "__main__":
    checkout = Checkout()
    order_total = checkout.total_with_shipping(
        items=[
            {"name": "Notebook", "price": 12.0, "quantity": 2},
            {"name": "Pen", "price": 2.5, "quantity": 3},
        ],
        shipping_method="express",
    )
    print(f"Total: ${order_total:.2f}")
