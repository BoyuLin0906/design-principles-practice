class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[dict[str, float]] = []
        self.item_count = 0
        self.total_price = 0.0

    def add_item(self, name: str, price: float) -> None:
        self.items.append({"name": name, "price": price})
        self.item_count += 1
        self.total_price += price

    def remove_item(self, name: str) -> None:
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                # Bug: total_price is updated, but item_count is not.
                self.total_price -= item["price"]
                break


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Keyboard", 50.0)
    cart.add_item("Mouse", 20.0)

    print(len(cart.items), cart.item_count, cart.total_price)

    cart.remove_item("Mouse")

    print(len(cart.items), cart.item_count, cart.total_price)
