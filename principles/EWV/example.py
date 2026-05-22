from abc import ABC, abstractmethod


class ShippingPolicy(ABC):
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class StandardShipping(ShippingPolicy):
    def cost(self) -> float:
        return 5.0


class ExpressShipping(ShippingPolicy):
    def cost(self) -> float:
        return 15.0


class OvernightShipping(ShippingPolicy):
    def cost(self) -> float:
        return 25.0


class Checkout:
    def __init__(self, shipping_policy: ShippingPolicy) -> None:
        self.shipping_policy = shipping_policy

    def total_with_shipping(self, items: list[dict]) -> float:
        subtotal = sum(item["price"] * item["quantity"] for item in items)
        return subtotal + self.shipping_policy.cost()


if __name__ == "__main__":
    checkout = Checkout(shipping_policy=ExpressShipping())
    order_total = checkout.total_with_shipping(
        items=[
            {"name": "Notebook", "price": 12.0, "quantity": 2},
            {"name": "Pen", "price": 2.5, "quantity": 3},
        ]
    )
    print(f"Total: ${order_total:.2f}")
