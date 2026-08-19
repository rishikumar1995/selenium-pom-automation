import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.test_data import VALID_USER

@pytest.mark.smoke
def test_logout(driver, base_url):
    login_page = LoginPage(driver, base_url)

    login_page.open()

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    home_page = HomePage(driver, base_url)

    login_page = home_page.logout()

    login_page.open()

    assert login_page.get_current_url() == login_page.base_url
