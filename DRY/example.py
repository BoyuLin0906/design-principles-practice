class ReportPrinter:
    def print_sales_report(self, sales: list[dict]) -> None:
        rows = [f"{sale['name']}: ${sale['amount']}" for sale in sales]
        total = sum(sale["amount"] for sale in sales)
        self._print_report("Sales Report", rows, f"Total: ${total}")

    def print_inventory_report(self, items: list[dict]) -> None:
        rows = [f"{item['name']}: {item['quantity']} units" for item in items]
        total = sum(item["quantity"] for item in items)
        self._print_report("Inventory Report", rows, f"Total: {total}")

    def _print_report(self, title: str, rows: list[str], total_line: str) -> None:
        # Shared layout logic lives in one place.
        print(f"=== {title} ===")

        for row in rows:
            print(row)

        print("--------------------")
        print(total_line)
        print()


if __name__ == "__main__":
    printer = ReportPrinter()

    sales = [
        {"name": "Keyboard", "amount": 120},
        {"name": "Mouse", "amount": 45},
    ]
    inventory = [
        {"name": "Keyboard", "quantity": 8},
        {"name": "Mouse", "quantity": 15},
    ]

    printer.print_sales_report(sales)
    printer.print_inventory_report(inventory)
