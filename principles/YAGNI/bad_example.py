import json


class CsvExporter:
    def export(self, users: list[dict[str, str]]) -> str:
        rows = ["name,email"]

        for user in users:
            rows.append(f"{user['name']},{user['email']}")

        return "\n".join(rows)


class JsonExporter:
    def export(self, users: list[dict[str, str]]) -> str:
        return json.dumps(users, indent=2)


class XmlExporter:
    def export(self, users: list[dict[str, str]]) -> str:
        lines = ["<users>"]

        for user in users:
            lines.append("  <user>")
            lines.append(f"    <name>{user['name']}</name>")
            lines.append(f"    <email>{user['email']}</email>")
            lines.append("  </user>")

        lines.append("</users>")
        return "\n".join(lines)


class UserExporter:
    def __init__(self) -> None:
        # The current requirement only needs CSV, but the code already
        # prepares extra formats for possible future needs.
        self.exporters = {
            "csv": CsvExporter(),
            "json": JsonExporter(),
            "xml": XmlExporter(),
        }

    def export(self, users: list[dict[str, str]], format_name: str = "csv") -> str:
        exporter = self.exporters[format_name]
        return exporter.export(users)


if __name__ == "__main__":
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    exporter = UserExporter()
    print(exporter.export(users))
