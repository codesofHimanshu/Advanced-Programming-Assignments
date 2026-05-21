# test_registration_service.py

import pytest
from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)


# Shared fixture
@pytest.fixture
def service():
    return RegistrationService()


# Successful registration test
def test_successful_registration(service):
    assert service.register_user("john@example.com", 22) is True


# Invalid email format test
def test_invalid_email_format(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("johnexample.com", 22)


# Empty email test
def test_empty_email(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("", 22)


# Underage user test
def test_underage_user(service):
    with pytest.raises(UnderageError):
        service.register_user("john@example.com", 16)


# None email test (assert statement)
def test_none_email(service):
    with pytest.raises(AssertionError):
        service.register_user(None, 22)