
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class HomePage(BasePage):
    """
    Page object for the home page.
    """
    AUTH_PROFILE_ICON = (By.XPATH, "//div[@class = 'headerIcon'][1]")
    FAVORITES_ICON = (By.XPATH, "//div[@class = 'headerIcon'][2]")
    CART_ICON = (By.XPATH, "//div[@class = 'headerIcon'][3]")
    SHOP_PAGE = (By.XPATH, "//*[@id='root']//ul/li[2]/a")


    def __init__(self, driver):
        super().__init__(driver)

    # -- ACTIONS --
    def load(self):
        return self.open(Config.HOME_PAGE_URL)

    def open_auth_profile_by_icon(self):
        self.click(self.AUTH_PROFILE_ICON)

    def open_favorites_list_by_icon(self):
        self.click(self.FAVORITES_ICON)

    def open_favorites_list_by_page(self):
        self.click(self.FAVORITES_PAGE)

    def open_cart_by_icon(self):
        self.click(self.CART_ICON)

    def open_shop_by_page(self):
        self.click(self.SHOP_PAGE)

    def open_contact_page(self):
        self.click(self.CONTACT_PAGE)

