from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def save(self, user_id: int, items: list[str]) -> None:
        pass


class Notifier(ABC):
    @abstractmethod
    def notify_order_created(self, user_id: int) -> None:
        pass


class MySQLOrderRepository(OrderRepository):
    def save(self, user_id: int, items: list[str]) -> None:
        print(f"Saved order for user {user_id} with {len(items)} items to MySQL")


class EmailNotifier(Notifier):
    def notify_order_created(self, user_id: int) -> None:
        print(f"Sent order-created email to user {user_id}")


class SMSNotifier(Notifier):
    def notify_order_created(self, user_id: int) -> None:
        print(f"Sent order-created SMS to user {user_id}")


class OrderService:
    def __init__(self, order_repository: OrderRepository, notifier: Notifier) -> None:
        self.order_repository = order_repository
        self.notifier = notifier

    def create_order(self, user_id: int, items: list[str]) -> None:
        self.order_repository.save(user_id, items)
        self.notifier.notify_order_created(user_id)


if __name__ == "__main__":
    email_order_service = OrderService(MySQLOrderRepository(), EmailNotifier())
    email_order_service.create_order(7, ["Keyboard", "Mouse"])

    sms_order_service = OrderService(MySQLOrderRepository(), SMSNotifier())
    sms_order_service.create_order(8, ["Monitor"])
