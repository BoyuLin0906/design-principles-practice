class CreateOrderRequest:
    # Request-specific parsing stays near the input boundary.
    def parse(self, payload: dict) -> dict:
        return {
            "customer_email": payload["customer_email"].strip().lower(),
            "items": payload["items"],
        }


class OrderRepository:
    def save(self, order: dict) -> None:
        print(f"Saving order to database: {order}")


class OrderService:
    # Order creation logic stays in one focused place.
    def __init__(self, repository: OrderRepository) -> None:
        self.repository = repository

    def create_order(self, data: dict) -> dict:
        total = sum(item["price"] * item["quantity"] for item in data["items"])

        order = {
            "id": 101,
            "customer_email": data["customer_email"],
            "items": data["items"],
            "total": total,
        }

        self.repository.save(order)
        return order


class NotificationService:
    # Side effects can change without touching request or response code.
    def send_order_created(self, order: dict) -> None:
        print(f"Sending admin notification for order {order['id']}")


class OrderResponseBuilder:
    # Response formatting stays separate from order creation.
    def build(self, order: dict) -> dict:
        return {
            "message": "Order created successfully.",
            "order_id": order["id"],
            "total": order["total"],
        }


class OrderController:
    def __init__(
        self,
        request_parser: CreateOrderRequest,
        order_service: OrderService,
        notification_service: NotificationService,
        response_builder: OrderResponseBuilder,
    ) -> None:
        self.request_parser = request_parser
        self.order_service = order_service
        self.notification_service = notification_service
        self.response_builder = response_builder

    def create_order(self, request: dict) -> dict:
        data = self.request_parser.parse(request)
        order = self.order_service.create_order(data)
        self.notification_service.send_order_created(order)
        return self.response_builder.build(order)


if __name__ == "__main__":
    controller = OrderController(
        request_parser=CreateOrderRequest(),
        order_service=OrderService(repository=OrderRepository()),
        notification_service=NotificationService(),
        response_builder=OrderResponseBuilder(),
    )
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
