from abc import ABC, abstractmethod


class DiscountRule(ABC):
    @abstractmethod
    def apply(self, original_price: float) -> float:
        raise NotImplementedError


class RegularDiscount(DiscountRule):
    def apply(self, original_price: float) -> float:
        return original_price


class MemberDiscount(DiscountRule):
    def apply(self, original_price: float) -> float:
        return original_price * 0.9


class PremiumDiscount(DiscountRule):
    def apply(self, original_price: float) -> float:
        return original_price * 0.8


class Checkout:
    # Checkout works with any discount rule that follows the same contract.
    def calculate_price(
        self, discount_rule: DiscountRule, original_price: float
    ) -> float:
        return discount_rule.apply(original_price)


if __name__ == "__main__":
    checkout = Checkout()

    print(checkout.calculate_price(RegularDiscount(), 100.0))
    print(checkout.calculate_price(MemberDiscount(), 100.0))
    print(checkout.calculate_price(PremiumDiscount(), 100.0))
