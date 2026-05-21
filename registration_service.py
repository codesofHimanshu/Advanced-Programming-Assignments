# registration_service.py

import re


class InvalidEmailError(ValueError):
    """Raised when the email is invalid."""

    def __init__(self, email):
        super().__init__(f"Invalid email address provided: {email}")


class UnderageError(Exception):
    """Raised when user age is below 18."""

    def __init__(self, age):
        super().__init__(f"User must be at least 18 years old. Provided age: {age}")


class RegistrationService:

    def register_user(self, email: str, age: int) -> bool:

        # Internal invariant check
        assert email is not None, "System invariant failed: email cannot be None"

        # Check empty email
        if email.strip() == "":
            raise InvalidEmailError(email)

        # Email regex validation
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.match(email_pattern, email):
            raise InvalidEmailError(email)

        # Age validation
        if age < 18:
            raise UnderageError(age)

        return True