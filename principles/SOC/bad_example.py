class OrderController:
    def create_order(self, request: dict) -> dict:
        # Request handling, data creation, side effects, and response building
        # all live together here.
        customer_email = request["customer_email"].strip().lower()
        items = request["items"]

        total = sum(item["price"] * item["quantity"] for item in items)

        order = {
            "id": 101,
            "customer_email": customer_email,
            "items": items,
            "total": total,
        }

        self._save_order(order)
        self._send_admin_notification(order)

        return {
            "message": "Order created successfully.",
            "order_id": order["id"],
            "total": order["total"],
        }

    def _save_order(self, order: dict) -> None:
        print(f"Saving order to database: {order}")

    def _send_admin_notification(self, order: dict) -> None:
        print(f"Sending admin notification for order {order['id']}")


if __name__ == "__main__":
    controller = OrderController()
    response = controller.create_order(
        {
            "customer_email": "Andy@Example.com ",
            "items": [
                {"name": "Keyboard", "price": 60, "quantity": 1},
                {"name": "Mouse", "price": 25, "quantity": 2},
            ],
        }
    )
    print(response)
