class MySQLDatabase:
    def insert_order(self, user_id: int, items: list[str]) -> None:
        print(f"Saved order for user {user_id} with {len(items)} items to MySQL")


class EmailSender:
    def send_order_created(self, user_id: int) -> None:
        print(f"Sent order-created email to user {user_id}")


class OrderService:
    def create_order(self, user_id: int, items: list[str]) -> None:
        # The service is tightly coupled to concrete implementations.
        db = MySQLDatabase()
        db.insert_order(user_id, items)

        email = EmailSender()
        email.send_order_created(user_id)


if __name__ == "__main__":
    order_service = OrderService()
    order_service.create_order(7, ["Keyboard", "Mouse"])
