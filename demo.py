from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)

service = RegistrationService()

try:
    email = input("Enter email: ")
    age = int(input("Enter age: "))

    if service.register_user(email, age):
        print("Registration successful!")

except InvalidEmailError as e:
    print(e)

except UnderageError as e:
    print(e)

except AssertionError as e:
    print(e)