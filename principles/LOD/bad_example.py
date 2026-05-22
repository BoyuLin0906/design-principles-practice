class Address:
    def __init__(self, city: str, postal_code: str) -> None:
        self.city = city
        self.postal_code = postal_code


class Customer:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address


class Order:
    def __init__(self, order_number: str, customer: Customer) -> None:
        self.order_number = order_number
        self.customer = customer


class ShippingService:
    def prepare_label(self, order: Order) -> None:
        # The service reaches through multiple objects to get what it needs.
        customer_name = order.customer.name
        city = order.customer.address.city
        postal_code = order.customer.address.postal_code

        print(
            f"Preparing label for order {order.order_number}: "
            f"{customer_name}, {city} {postal_code}"
        )


if __name__ == "__main__":
    address = Address("Taipei", "100")
    customer = Customer("Ava", address)
    order = Order("ORD-1001", customer)

    shipping_service = ShippingService()
    shipping_service.prepare_label(order)
