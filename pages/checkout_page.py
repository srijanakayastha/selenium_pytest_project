from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config

class CheckoutPage(BasePage):
    """
    Page object for the checkout/cart page.
    """

    MINUS_BUTTON = (By.XPATH, "//button[@class = 'minus']")
    PLUS_BUTTON = (By.XPATH, "//button[@class = 'plus']")
    SHIPMENT_VALUE = (By.XPATH, "//*[@id='root']/div/section/div/div[1]/div/div[2]/h5[2]/text()[1]")
    PRODUCT_TOTAL = (By.XPATH, "//*[@id='root']/div/section/div/div[1]/div/div[3]/h5[2]/text()[1]")
    TOTAL = (By.XPATH, "//*[@id='root']/div/section/div/div[1]/div/div[4]/h5[2]/text()[1]")
    STREET_FIELD = (By.XPATH, "//input[@name = 'street']")
    CITY_FIELD = (By.XPATH, "//input[@name = 'city']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@name = 'postalCode']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@name = 'cardNumber']")
    NAME_ON_CARD_FIELD = (By.XPATH, "//input[@name = 'nameOnCard']")
    EXPIRATION_CARD_FIELD = (By.XPATH, "//input[@name = 'expiration']")
    CVV_CARD_FIELD = (By.XPATH, "//input[@name = 'cvv']")
    BUY_NOW_BUTTON = (By.XPATH, "//button[@class = 'btn-buy-now']")


    def __init__(self, driver):
        super().__init__(driver)

    # -- ACTIONS --
    def load(self):
        return self.open(Config.CHECKOUT_PAGE_URL)

    def enter_street(self, street):
        self.type_text(self.STREET_FIELD, street)
        return self

    def enter_city(self, city):
        self.type_text(self.CITY_FIELD, city)
        return self

    def enter_postal_code(self, postal_code):
        self.type_text(self.POSTAL_CODE_FIELD, postal_code)
        return self

    def enter_card_number(self, card_number):
        self.type_text(self.CARD_NUMBER_FIELD, card_number)
        return self

    def enter_name_on_card(self, name_on_card):
        self.type_text(self.NAME_ON_CARD_FIELD, name_on_card)
        return self

    def enter_expiration_card(self, expiration_card):
        self.type_text(self.EXPIRATION_CARD_FIELD, expiration_card)
        return self

    def enter_cvv_card(self, cvv_card):
        self.type_text(self.CVV_CARD_FIELD, cvv_card)
        return self

    def buy_now(self):
        self.click(self.BUY_NOW_BUTTON)

    def click_minus_button(self):
        self.click(self.MINUS_BUTTON)

    def click_plus_button(self):
        self.click(self.PLUS_BUTTON)

    def get_shipment(self):
        return self.get_text(self.SHIPMENT_VALUE)

    def get_product_total(self):
        return self.get_text(self.PRODUCT_TOTAL)

    def get_total(self):
        return self.get_text(self.TOTAL)

    def is_visible_buy_now_button(self):
        return self.is_visible(self.BUY_NOW_BUTTON)