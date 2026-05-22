class AgeInput:
    def __init__(self, value: int) -> None:
        self.value = value


class AgeChecker:
    def is_greater_than_or_equal(self, age: int, limit: int) -> bool:
        return age >= limit


class AdultRule:
    def __init__(self) -> None:
        self.checker = AgeChecker()

    def matches(self, age_input: AgeInput) -> bool:
        return self.checker.is_greater_than_or_equal(age_input.value, 18)


class AdultStatusService:
    def __init__(self) -> None:
        self.rule = AdultRule()

    def is_adult(self, age_input: AgeInput) -> bool:
        return self.rule.matches(age_input)


if __name__ == "__main__":
    service = AdultStatusService()
    print(service.is_adult(AgeInput(20)))
    print(service.is_adult(AgeInput(15)))
