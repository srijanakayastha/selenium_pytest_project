from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config


class LoginPage(BasePage):
    """
    Page object for the login form.
    """
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    SIGNIN_BUTTON = (By.XPATH, "//button[@type = 'submit' and text() = 'Sign In']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")

    def __init__(self, driver):
        super().__init__(driver)

    # -- ACTIONS --
    def load(self):
        return self.open(Config.AUTH_URL)

    def enter_email(self, email):
        self.type_text(self.EMAIL_FIELD, email)
        return self

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)
        return self

    def submit(self):
        self.click(self.SIGNIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.submit()
        # return the instance of DashboardPOM

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return None