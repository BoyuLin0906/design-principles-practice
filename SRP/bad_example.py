class UserService:
    # This class mixes several responsibilities in one place.
    def create_user(self, name: str, email: str) -> dict:
        if not name:
            raise ValueError("Name is required.")

        if "@" not in email:
            raise ValueError("Email is invalid.")

        user = {
            "id": 1,
            "name": name,
            "email": email,
        }

        # User creation also handles persistence and notification.
        self._save_to_database(user)
        self._send_welcome_email(user)
        return user

    def _save_to_database(self, user: dict) -> None:
        print(f"Saving user to database: {user}")

    def _send_welcome_email(self, user: dict) -> None:
        print(f"Sending welcome email to {user['email']}")


if __name__ == "__main__":
    service = UserService()
    created_user = service.create_user("Andy", "andy@example.com")
    print(created_user)
