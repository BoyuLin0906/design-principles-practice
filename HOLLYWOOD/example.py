class WorkflowStep:
    def handle(self, order: dict[str, str]) -> None:
        raise NotImplementedError


class OrderWorkflow:
    def __init__(self) -> None:
        self.steps: list[WorkflowStep] = []

    def register(self, step: WorkflowStep) -> None:
        self.steps.append(step)

    def run(self, order: dict[str, str]) -> None:
        for step in self.steps:
            step.handle(order)


class InventoryStep(WorkflowStep):
    def handle(self, order: dict[str, str]) -> None:
        print(f"Reserved item {order['item_id']}")


class PaymentStep(WorkflowStep):
    def handle(self, order: dict[str, str]) -> None:
        print(f"Charged customer {order['customer_id']}")


class ConfirmationStep(WorkflowStep):
    def handle(self, order: dict[str, str]) -> None:
        print(f"Sent confirmation for order {order['order_id']}")


if __name__ == "__main__":
    order = {
        "order_id": "ORD-100",
        "customer_id": "CUST-42",
        "item_id": "BOOK-7",
    }

    workflow = OrderWorkflow()
    workflow.register(InventoryStep())
    workflow.register(PaymentStep())
    workflow.register(ConfirmationStep())
    workflow.run(order)
