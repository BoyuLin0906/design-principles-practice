class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[dict[str, float]] = []

    def add_item(self, name: str, price: float) -> None:
        self.items.append({"name": name, "price": price})

    def remove_item(self, name: str) -> None:
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                break

    @property
    def item_count(self) -> int:
        return len(self.items)

    @property
    def total_price(self) -> float:
        return sum(item["price"] for item in self.items)


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Keyboard", 50.0)
    cart.add_item("Mouse", 20.0)

    print(cart.item_count, cart.total_price)

    cart.remove_item("Mouse")

    print(cart.item_count, cart.total_price)
