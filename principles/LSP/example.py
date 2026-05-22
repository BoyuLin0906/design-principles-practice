from abc import ABC


class Bird(ABC):
    def walk(self) -> str:
        return "Walking on the ground."


class FlyingBird(Bird):
    def fly(self) -> str:
        return "Flying through the sky."


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    def swim(self) -> str:
        return "Swimming through the water."


def make_bird_fly(bird: FlyingBird) -> None:
    # The function now depends only on birds that really support flying.
    print(bird.fly())


if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)
    print(sparrow.walk())

    penguin = Penguin()
    print(penguin.walk())
    print(penguin.swim())
