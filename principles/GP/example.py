def apply_discount(subtotal: float, threshold: float, rate: float) -> float:
    if subtotal >= threshold:
        return subtotal * (1 - rate)

    return subtotal


if __name__ == "__main__":
    print(apply_discount(120, threshold=100, rate=0.1))
    print(apply_discount(80, threshold=50, rate=0.05))
