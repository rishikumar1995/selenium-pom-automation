import pytest
from pages.login_page import LoginPage
from test_data.test_data import INVALID_LOGIN_DATA

@pytest.mark.regression
@pytest.mark.parametrize("login_data", INVALID_LOGIN_DATA)

def test_invalid_login(driver, base_url, login_data):
    login_page = LoginPage(driver, base_url)

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    error_message = login_page.get_error_message()

    assert login_data["expected_error"] in error_message