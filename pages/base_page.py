from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def enter_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def is_visible(self, locator):
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False