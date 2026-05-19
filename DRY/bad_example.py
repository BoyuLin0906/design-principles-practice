class ReportPrinter:
    def print_sales_report(self, sales: list[dict]) -> None:
        print("=== Sales Report ===")

        total = 0
        for sale in sales:
            print(f"{sale['name']}: ${sale['amount']}")
            total += sale["amount"]

        print("--------------------")
        print(f"Total: ${total}")
        print()

    def print_inventory_report(self, items: list[dict]) -> None:
        print("=== Inventory Report ===")

        total = 0
        for item in items:
            print(f"{item['name']}: {item['quantity']} units")
            total += item["quantity"]

        print("--------------------")
        print(f"Total: {total}")
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
