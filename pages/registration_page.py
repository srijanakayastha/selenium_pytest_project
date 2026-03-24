from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config

class RegistrationPage(BasePage):
    """
    Page object for the registration form.
    """
    SWITCH_TO_REGISTRATION_LINK = (By.XPATH, "//a[@class = 'switch-link']")
    NAME_FIELD = (By.XPATH, "//input[@type = 'text']")
    EMAIL_FIELD = (By.XPATH, "//input[@type = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type = 'password']")
    SIGNUP_BUTTON = (By.XPATH, "//button[@type = 'submit' and text() = 'Sign Up']")
    SUCCESSFUL_MSG = (By.XPATH, "//div[@role = 'status']")


    def __init__(self, driver):
        super().__init__(driver)

    # -- ACTIONS --
    def load(self):
        return self.open(Config.AUTH_URL)

    def switch_to_registration(self):
        self.scroll_into_view(self.SWITCH_TO_REGISTRATION_LINK)
        self.click(self.SWITCH_TO_REGISTRATION_LINK)

    def enter_name(self, name):
        self.type_text(self.NAME_FIELD, name)
        return self

    def enter_email(self, email):
        self.type_text(self.EMAIL_FIELD, email)
        return self

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)
        return self

    def submit(self):
        self.scroll_into_view(self.SIGNUP_BUTTON)
        self.click(self.SIGNUP_BUTTON)

    def get_confirmation_message(self):
        if self.is_visible(self.SUCCESSFUL_MSG):
            return self.get_text(self.SUCCESSFUL_MSG)
        return None