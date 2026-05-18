def calculate_price(customer_type: str, original_price: float) -> float:
    # New discount types require editing this function.
    if customer_type == "regular":
        discount = 0.0
    elif customer_type == "member":
        discount = 0.1
    elif customer_type == "premium":
        discount = 0.2
    else:
        raise ValueError(f"Unsupported customer type: {customer_type}")

    return original_price * (1 - discount)


if __name__ == "__main__":
    print(calculate_price("regular", 100.0))
    print(calculate_price("member", 100.0))
    print(calculate_price("premium", 100.0))
