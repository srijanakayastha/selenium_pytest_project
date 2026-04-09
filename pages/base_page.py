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

#Constructor (__init__)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.DEFAULT_TIMEOUT)

    # self.driver → browser instance
    # self.wait → wait helper
    # So every page automatically has driver + wait.


    # -- NAVIGATION --
    # Opens a webpage.
    # Browser goes to that URL
    def open(self, url):
        self.driver.get(url)
        return self

  # Returns page title.
    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    # -- FINDING ELEMENTS --
    # Waits until an element exists in the DOM.
    def find(self, locator):
        """ Wait and return a single element."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
  # Returns multiple elements.
    def find_all(self, locator):
        """ Return all matching elements."""
        self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

# Check if Element is Visible
    # Checks if element appears on screen.
    # It also handles TimeoutException safely.
    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # -- INTERACTIONS --
    # Wait until element clickable
    #  Click it
    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()



    # 1 # Wait until element visible
    # 2 Clear old text
    # 3 # Type new text

    def type_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
 # Returns text from an element.
    def get_text(self, locator):
        return self.find(locator).text.strip()

 # Waits until browser URL changes.
    def wait_for_url(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )
  # Takes screenshot.
    def screenshot(self, name="screenshot"):
        self.driver.save_screenshot(f"{name}.png")

        # Wait for alert popup
        #  Accept it

    def wait_and_accept_alert(self, timeout=10):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()

    def safe_click(self, locator, timeout=10):
        """Wait for element to be clickable and any overlay to disappear."""
        self.wait_for_overlay_to_disappear()
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def wait_for_overlay_to_disappear(self, timeout=10):
        """Wait for modal/overlay to disappear before interacting."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-overlay"))
            )
        except:
            pass  # overlay not present, continue

    def find(self, locator, timeout=10):
        """Find element with wait"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )