class Address:
    def __init__(self, city: str, postal_code: str) -> None:
        self.city = city
        self.postal_code = postal_code

    def shipping_destination(self) -> str:
        return f"{self.city} {self.postal_code}"


class Customer:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def display_name(self) -> str:
        return self.name

    def shipping_destination(self) -> str:
        return self.address.shipping_destination()


class Order:
    def __init__(self, order_number: str, customer: Customer) -> None:
        self.order_number = order_number
        self.customer = customer

    def customer_name(self) -> str:
        return self.customer.display_name()

    def shipping_destination(self) -> str:
        return self.customer.shipping_destination()


class ShippingService:
    def prepare_label(self, order: Order) -> None:
        print(
            f"Preparing label for order {order.order_number}: "
            f"{order.customer_name()}, {order.shipping_destination()}"
        )


if __name__ == "__main__":
    address = Address("Taipei", "100")
    customer = Customer("Ava", address)
    order = Order("ORD-1001", customer)

    shipping_service = ShippingService()
    shipping_service.prepare_label(order)
