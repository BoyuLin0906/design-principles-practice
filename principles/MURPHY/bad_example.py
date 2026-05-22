def apply_shipment_update(update: dict) -> None:
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
    update = {
        "tracking_number": "PKG-2048",
        "item_count": "three",
        "status": "Delivered",
    }
    # This crashes on purpose because the bad example assumes the input is always valid.
    apply_shipment_update(update)
