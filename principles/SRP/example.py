class UserValidator:
    # Validation rules live in one focused class.
    def validate(self, name: str, email: str) -> None:
        if not name:
            raise ValueError("Name is required.")

        if "@" not in email:
            raise ValueError("Email is invalid.")


class UserRepository:
    # Storage logic has its own responsibility.
    def save(self, user: dict) -> None:
        print(f"Saving user to database: {user}")


class EmailSender:
    # Notification logic is separated from user creation.
    def send_welcome_email(self, email: str) -> None:
        print(f"Sending welcome email to {email}")


class UserService:
    def __init__(
        self,
        validator: UserValidator,
        repository: UserRepository,
        email_sender: EmailSender,
    ) -> None:
        self.validator = validator
        self.repository = repository
        self.email_sender = email_sender

    def create_user(self, name: str, email: str) -> dict:
        # UserService coordinates the workflow instead of doing every job itself.
        self.validator.validate(name, email)

        user = {
            "id": 1,
            "name": name,
            "email": email,
        }

        self.repository.save(user)
        self.email_sender.send_welcome_email(email)
        return user


if __name__ == "__main__":
    service = UserService(
        validator=UserValidator(),
        repository=UserRepository(),
        email_sender=EmailSender(),
    )
    created_user = service.create_user("Andy", "andy@example.com")
    print(created_user)
