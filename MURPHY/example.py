REQUIRED_FIELDS = ("tracking_number", "item_count", "status")
ALLOWED_STATUSES = {"in_transit", "delayed", "delivered"}


def validate_update(update: dict) -> tuple[bool, str]:
    for field in REQUIRED_FIELDS:
        if field not in update:
            return False, f"Missing field: {field}"

    try:
        item_count = int(update["item_count"])
    except (TypeError, ValueError):
        return False, "Item count must be a whole number"

    if item_count < 0:
        return False, "Item count cannot be negative"

    status = str(update["status"]).lower()
    if status not in ALLOWED_STATUSES:
        return False, f"Unknown shipment status: {update['status']}"

    return True, ""


def apply_shipment_update(update: dict) -> None:
    is_valid, message = validate_update(update)
    if not is_valid:
        print(f"Rejected shipment update: {message}")
        return

    tracking_number = update["tracking_number"]
    item_count = int(update["item_count"])
    status = update["status"].lower()

    print(f"Updating shipment {tracking_number}")

    if status == "delivered":
        print(f"Marked {item_count} items as delivered")
    elif status == "delayed":
        print("Sent delay notice to customer")
    else:
        print("Shipment is in progress")


if __name__ == "__main__":
    updates = [
        {
            "tracking_number": "PKG-2048",
            "item_count": "three",
            "status": "Delivered",
        },
        {
            "tracking_number": "PKG-2049",
            "item_count": "3",
            "status": "Delivered",
        },
    ]

    for update in updates:
        apply_shipment_update(update)
