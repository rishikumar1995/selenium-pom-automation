LOGIN_DATA = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "expected": "success"
    },
    {
        "username": "locked_out_user",
        "password": "secret_sauce",
        "expected": "failure"
    }
]

INVALID_LOGIN_DATA = [
    {
        "username": "wrong_user",
        "password": "wrong_password",
        "expected_error": "Username and password do not match"
    },
    {
        "username": "abc",
        "password": "wrong_password",
        "expected_error": "Username and password do not match"
    },
    {
        "username": "",
        "password": "secret_sauce",
        "expected_error": "Username is required"
    }
]

VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce"
}