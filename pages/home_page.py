from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    products_title_locator = (By.CLASS_NAME, "title")
    menu_button_locator = (By.ID, "react-burger-menu-btn")
    logout_link_locator = (By.ID, "logout_sidebar_link")


    def get_products_title(self):
        return self.get_text(self.products_title_locator)

    def logout(self):
        self.click(self.menu_button_locator)
        self.click(self.logout_link_locator)

        from pages.login_page import LoginPage

        return LoginPage(self.driver, self.base_url)
