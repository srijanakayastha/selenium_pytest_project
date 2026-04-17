import time

import self
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config
# Wait until all remove icons are gone from the page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    """
    Page object for the checkout/cart page.
    """

    MINUS_BUTTON = (By.XPATH, "//button[@class = 'minus']")
    PLUS_BUTTON = (By.XPATH, "//button[@class = 'plus']")
    SHIPMENT_VALUE = (By.XPATH, "//div[@class = 'shipment-container']/h5[2]")
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
    REMOVE_ICON = (By.XPATH,"//a[@class='remove-icon']")
    EMPTY_CART_CONTAINER = (By.XPATH,"//div[@class = 'empty-cart-container']")


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

    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_CONTAINER)

    def clear_cart(self):
        if not self.is_cart_empty():
           remove_button =  self.find_all(self.REMOVE_ICON)
           for button in remove_button:
               button.click()
           WebDriverWait(self.driver, 10).until(
               EC.invisibility_of_element_located(self.REMOVE_ICON))





    def adjust_quantity(self, product_name, direction="plus"):
        """
        Finds the specific product card and clicks its +/- button.
        """
        # 1. Find the container (card) that holds the product name
        basket_items_container_xpath = f"//div[contains(@class, 'basket-items-container')]"
        container = self.driver.find_element(By.XPATH, basket_items_container_xpath)

        # 2. Find the requested button INSIDE that specific container
        if direction == "plus":
            container.find_element(*self.PLUS_BUTTON).click()
        else:
            container.find_element(*self.MINUS_BUTTON).click()
    def increase_quantity(self, product_name, count):
        for _ in range(int(count)):
            self.adjust_quantity(product_name, "plus")

    def decrease_quantity(self, product_name, count):
        """Clicks the minus button for a product a specific number of times."""
        for _ in range(count):
            self.adjust_quantity(product_name, "minus")
            # Minor wait to let the total recalculate
            time.sleep(0.5)



