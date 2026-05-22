class UserStore:
    def __init__(self) -> None:
        self.users: dict[str, dict[str, str]] = {
            "ava@example.com": {
                "email": "ava@example.com",
                "name": "Ava",
            }
        }

    def find_by_email(self, email: str) -> dict[str, str]:
        user = self.users.get(email)
        if user is None:
            user = {"email": email, "name": "Guest"}
            self.users[email] = user
        return user


if __name__ == "__main__":
    store = UserStore()

    print(store.find_by_email("ava@example.com"))
    print(len(store.users))

    print(store.find_by_email("new@example.com"))
    print(len(store.users))
