from abc import ABC, abstractmethod


class OfficeMachine(ABC):
    @abstractmethod
    def print_document(self, content: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def scan_document(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def fax_document(self, content: str) -> None:
        raise NotImplementedError


class BasicPrinter(OfficeMachine):
    def print_document(self, content: str) -> None:
        print(f"Printing: {content}")

    def scan_document(self) -> str:
        raise NotImplementedError("This printer cannot scan.")

    def fax_document(self, content: str) -> None:
        raise NotImplementedError("This printer cannot fax.")


if __name__ == "__main__":
    printer = BasicPrinter()
    printer.print_document("Monthly report")
