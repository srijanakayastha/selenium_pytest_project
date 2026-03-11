from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Config
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """
    Parent class for all page objects.
    Provides shared browser interaction helpers so individual page objects
    can focus purely on page-specific behavior.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)

    # -- NAVIGATION --
    def open(self, url):
        self.driver.get(url)
        return self

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    # -- FINDING ELEMENTS --
    def find(self, locator):
        """ Wait and return a single element."""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_all(self, locator):
        """ Return all matching elements."""
        self.wait.until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # -- INTERACTIONS --
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text.strip()

    def wait_for_url(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def screenshot(self, name="screenshot"):
        self.driver.save_screenshot(f"{name}.png")

    def wait_and_accept_alert(self, timeout=10):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()