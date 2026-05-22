def apply_large_order_discount(subtotal: float) -> float:
    if subtotal >= 100:
        return subtotal * 0.9

    return subtotal


if __name__ == "__main__":
    print(apply_large_order_discount(120))
