class Bird:
    def walk(self) -> str:
        return "Walking on the ground."

    def fly(self) -> str:
        return "Flying through the sky."


class Sparrow(Bird):
    pass


class Penguin(Bird):
    def fly(self) -> str:
        raise ValueError("Penguins cannot fly.")


def make_bird_fly(bird: Bird) -> None:
    # This function assumes every Bird can fly.
    print(bird.fly())


if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)
    print(sparrow.walk())

    penguin = Penguin()
    print(penguin.walk())
    make_bird_fly(penguin)
