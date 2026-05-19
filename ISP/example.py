from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self, content: str) -> None:
        raise NotImplementedError


class Scanner(ABC):
    @abstractmethod
    def scan_document(self) -> str:
        raise NotImplementedError


class FaxMachine(ABC):
    @abstractmethod
    def fax_document(self, content: str) -> None:
        raise NotImplementedError


class BasicPrinter(Printer):
    def print_document(self, content: str) -> None:
        print(f"Printing: {content}")


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print_document(self, content: str) -> None:
        print(f"Printing: {content}")

    def scan_document(self) -> str:
        return "Scanned contract"

    def fax_document(self, content: str) -> None:
        print(f"Faxing: {content}")


if __name__ == "__main__":
    basic_printer = BasicPrinter()
    basic_printer.print_document("Monthly report")

    office_machine = MultiFunctionPrinter()
    office_machine.print_document("Project update")
    print(office_machine.scan_document())
    office_machine.fax_document("Signed agreement")
