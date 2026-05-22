class Order:
    def __init__(self, order_id: str, amount: float, csv_row_number: int) -> None:
        # Business data for the order itself.
        self.order_id = order_id
        self.amount = amount
        # Import-specific context is mixed into the domain model here.
        self.csv_row_number = csv_row_number


class OrderValidator:
    def validate(self, order: Order) -> str | None:
        if order.amount <= 0:
            # Validation needs the CSV row number, but that does not mean
            # the Order object should own that piece of information.
            return f"Row {order.csv_row_number}: amount must be positive"
        return None


if __name__ == "__main__":
    order = Order(order_id="A-100", amount=-20.0, csv_row_number=7)
    validator = OrderValidator()
    print(validator.validate(order))
