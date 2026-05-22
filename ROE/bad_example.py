def can_ship_order(order: dict[str, object]) -> bool:
    return order["status"] == 1


def should_send_payment_reminder(order: dict[str, object]) -> bool:
    return order["status"] == 0


def payment_status_message(order: dict[str, object]) -> str:
    if order["status"] == 0:
        return "Waiting for payment"
    if order["status"] == 1:
        return "Paid"
    if order["status"] == 2:
        return "Payment failed"
    return "Unknown status"


if __name__ == "__main__":
    pending_order = {"id": "ORD-100", "status": 0}
    paid_order = {"id": "ORD-101", "status": 1}
    failed_order = {"id": "ORD-102", "status": 2}

    for order in [pending_order, paid_order, failed_order]:
        print(order["id"], payment_status_message(order))
        print("ship:", can_ship_order(order))
        print("remind:", should_send_payment_reminder(order))
