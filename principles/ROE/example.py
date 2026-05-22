from enum import IntEnum


class PaymentStatus(IntEnum):
    PENDING = 0
    PAID = 1
    FAILED = 2


def can_ship_order(order: dict[str, object]) -> bool:
    return order["status"] == PaymentStatus.PAID


def should_send_payment_reminder(order: dict[str, object]) -> bool:
    return order["status"] == PaymentStatus.PENDING


def payment_status_message(order: dict[str, object]) -> str:
    status = order["status"]

    if status == PaymentStatus.PENDING:
        return "Waiting for payment"
    if status == PaymentStatus.PAID:
        return "Paid"
    if status == PaymentStatus.FAILED:
        return "Payment failed"
    return "Unknown status"


if __name__ == "__main__":
    pending_order = {"id": "ORD-100", "status": PaymentStatus.PENDING}
    paid_order = {"id": "ORD-101", "status": PaymentStatus.PAID}
    failed_order = {"id": "ORD-102", "status": PaymentStatus.FAILED}

    for order in [pending_order, paid_order, failed_order]:
        print(order["id"], payment_status_message(order))
        print("ship:", can_ship_order(order))
        print("remind:", should_send_payment_reminder(order))
