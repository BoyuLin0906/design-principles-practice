class InventoryService:
    def reserve(self, order: dict[str, str]) -> None:
        print(f"Reserved item {order['item_id']}")


class PaymentService:
    def charge(self, order: dict[str, str]) -> None:
        print(f"Charged customer {order['customer_id']}")


class EmailService:
    def send_confirmation(self, order: dict[str, str]) -> None:
        print(f"Sent confirmation for order {order['order_id']}")


def process_order(order: dict[str, str]) -> None:
    inventory_service = InventoryService()
    payment_service = PaymentService()
    email_service = EmailService()

    inventory_service.reserve(order)
    payment_service.charge(order)
    email_service.send_confirmation(order)


if __name__ == "__main__":
    order = {
        "order_id": "ORD-100",
        "customer_id": "CUST-42",
        "item_id": "BOOK-7",
    }
    process_order(order)
