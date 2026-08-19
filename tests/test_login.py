import pytest
from pages.login_page import LoginPage
from test_data.test_data import LOGIN_DATA
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.parametrize("login_data", LOGIN_DATA)
def test_login(driver, base_url, login_data):

    login_page = LoginPage(driver, base_url)

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    if login_data["expected"] == "success":

        home_page = HomePage(driver, base_url)

        assert home_page.get_products_title() == "Products"
        assert home_page.is_visible(home_page.products_title_locator)

    else:
        assert login_page.get_error_message() == \
            "Epic sadface: Sorry, this user has been locked out."