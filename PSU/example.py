class Order:
    def __init__(self, order_id: str, amount: float) -> None:
        self.order_id = order_id
        self.amount = amount


class CsvOrderRow:
    def __init__(self, order: Order, row_number: int) -> None:
        self.order = order
        self.row_number = row_number


class OrderValidator:
    def validate(self, csv_order_row: CsvOrderRow) -> str | None:
        order = csv_order_row.order

        if order.amount <= 0:
            return f"Row {csv_order_row.row_number}: amount must be positive"

        return None


if __name__ == "__main__":
    order = Order(order_id="A-100", amount=-20.0)
    csv_order_row = CsvOrderRow(order=order, row_number=7)
    validator = OrderValidator()
    print(validator.validate(csv_order_row))
