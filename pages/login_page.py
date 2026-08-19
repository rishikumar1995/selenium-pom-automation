from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger(__name__)

class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message_locator = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        logger.info("Opening login page")
        self.driver.get(self.base_url)

    def login(self, username, password):
        logger.info("Entering username")
        self.enter_text(self.username, username)

        logger.info("Entering password")
        self.enter_text(self.password, password)

        logger.info("Clicking login button")
        self.click(self.login_button)

        logger.info("Login completed")

    def get_error_message(self):
        return self.get_text(self.error_message_locator)