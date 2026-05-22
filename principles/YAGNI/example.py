def export_users_to_csv(users: list[dict[str, str]]) -> str:
    rows = ["name,email"]

    for user in users:
        rows.append(f"{user['name']},{user['email']}")

    return "\n".join(rows)

if __name__ == "__main__":
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]
    print(export_users_to_csv(users))
