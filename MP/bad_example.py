orders: list[dict[str, str]] = []


def place_order(order_id: str, product_sku: str) -> None:
    orders.append(
        {
            "id": order_id,
            "product_sku": product_sku,
        }
    )


def delete_order(product_sku: str) -> None:
    for index, order in enumerate(orders):
        if order["product_sku"] == product_sku:
            del orders[index]
            return


if __name__ == "__main__":
    place_order("ORD-100", "SKU-CHAIR")
    place_order("ORD-101", "SKU-CHAIR")

    # We only wanted to remove ORD-101 during data cleanup.
    delete_order("SKU-CHAIR")

    print("orders:", orders)
