class UserStore:
    def __init__(self) -> None:
        self.users: dict[str, dict[str, str]] = {
            "ava@example.com": {
                "email": "ava@example.com",
                "name": "Ava",
            }
        }

    def find_by_email(self, email: str) -> dict[str, str] | None:
        return self.users.get(email)

    def get_or_create_guest(self, email: str) -> dict[str, str]:
        user = self.find_by_email(email)
        if user is not None:
            return user

        guest = {"email": email, "name": "Guest"}
        self.users[email] = guest
        return guest


if __name__ == "__main__":
    store = UserStore()

    print(store.find_by_email("ava@example.com"))
    print(len(store.users))

    print(store.find_by_email("new@example.com"))
    print(len(store.users))

    print(store.get_or_create_guest("new@example.com"))
    print(len(store.users))
