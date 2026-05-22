from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str


@dataclass(frozen=True)
class Order:
    order_id: str
    product: Product


class OrderStore:
    def __init__(self) -> None:
        self._orders: dict[str, Order] = {}

    def add_order(self, order: Order) -> None:
        self._orders[order.order_id] = order

    def delete_order(self, order_id: str) -> None:
        del self._orders[order_id]

    def list_orders(self) -> list[Order]:
        return list(self._orders.values())


if __name__ == "__main__":
    chair = Product("SKU-CHAIR")
    order_store = OrderStore()

    order_store.add_order(Order("ORD-100", chair))
    order_store.add_order(Order("ORD-101", chair))
    order_store.delete_order("ORD-101")

    print("orders:", order_store.list_orders())
