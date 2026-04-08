
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
from utils.config import Config
from selenium.webdriver.common.by import By
import time

class ShopPage(BasePage):
    """
    Page object for the shop page. Handles age modal, pagination, add-to-cart, product info, and ratings.
    """

    # --- AGE MODAL ---
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class='modal-content']/input[@type='text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class='modal-content']//button[text()='Confirm']")
    AGE_VERIFICATION_TEXT = (By.XPATH, "//div[@class='modal-content']//p")
    AGE_VERIFICATION_SUCCESS_ALERT = (
        By.XPATH,
        f"//div[@role='status' and contains(text(), '{Config.AGE_VERIFICATION_SUCCESS_ALERT}')]"
    )
    AGE_VERIFICATION_FAIL_ALERT = (
        By.XPATH,
        f"//div[@role='status' and contains(text(), '{Config.AGE_VERIFICATION_FAIL_ALERT}')]"
    )
    ALCOHOL_CATEGORY_XPATH =(By.XPATH, "//a[text()='Alocohol']")
    NO_ALCOHOLIC_PRODUCTS = (By.XPATH,"//div[@class='no-products-card']")

    # --- PAGINATION ---
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")

    # --- MESSAGES ---
    CONFIRMATION_MSG = (By.XPATH, "//div[@role='status']")

    SHOP_XPATH = (By.XPATH,"//ul[@class='anim-nav']//a[@href='/store']")



    # ----------------- INIT -----------------
    def __init__(self, driver):
        super().__init__(driver)

    # ----------------- PAGE NAVIGATION -----------------
    def load(self):
        """Open the shop page URL"""
        self.click(self.SHOP_XPATH)
        return self

    # ----------------- AGE MODAL -----------------
    def enter_date_age_modal(self, date):
        self.type_text(self.AGE_VERIFICATION_INPUT, date)
        return self

    def confirm_age_modal(self):
        self.click(self.AGE_VERIFICATION_CONFIRM_BUTTON)
        # Wait for modal to disappear
        # WebDriverWait(self.driver, 5).until(
        #     EC.invisibility_of_element_located(self.AGE_VERIFICATION_INPUT)
        # )
        return self

    # ----------------- PRODUCT LOCATORS -----------------
    def get_all_products_on_page(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-card img[alt]")
        return [el.get_attribute("alt") for el in elements]

    # ----------------- PRODUCT ACTIONS -----------------
    def find_product(self, product_name):
        """Find product card by name, handles pagination."""
        while True:
            cards = self.driver.find_elements(By.CSS_SELECTOR, ".product-card")
            for card in cards:
                if product_name.lower() in card.text.lower():
                    return card
            # Try next page
            try:
                next_buttons = self.driver.find_elements(*self.NEXT_PAGE_BUTTON)
                if next_buttons and next_buttons[0].is_enabled():
                    next_buttons[0].click()
                    time.sleep(1)  # wait for new products to load
                else:
                    return None
            except:
                return None


    def add_product_to_cart(self, product_name, quantity=1):
        wait = WebDriverWait(self.driver, 10)
        product_add_to_cart_xpath = self.get_add_to_cart_xpath_for_product(product_name)
        add_to_cart_btn = self.find(product_add_to_cart_xpath)


        #Handle_quantity
        if int(quantity) > 1:
            product_quantity_xpath = self.get_quantity_xpath_for_product(product_name)
            quantity_input = self.find(product_quantity_xpath)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))

        add_to_cart_btn.click()



    def view_product_info(self, product_name):
        """Click on the product image to view details"""
        product_card = self.find_product(product_name)
        if not product_card:
            raise Exception(f"Product '{product_name}' not found on any page.")

        product_image = product_card.find_element(By.TAG_NAME, "img")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_image)
        product_image.click()

    # ----------------- PRODUCT VISIBILITY -----------------
    def is_product_visible(self, product_name):
        try:
            product_card = self.find_product(product_name)
            return product_card is not None
        except:
            return False

    # ----------------- UTILITY -----------------
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


    def get_add_to_cart_xpath_for_product(self,product):
        return (By.XPATH, f"//div[@class='card']//img[@alt='{product}']/parent::div[@class='card']//button[contains(text(),'Add to Cart')]")

    def get_quantity_xpath_for_product(self,product):
        return (By.XPATH,f"//div[@class='card']//img[@alt='{product}']/parent::div[@class='card']//input[@type='number and @class=quantity']")

    def get_age_verification_message(self, message_type):
        xpath_map = {
            "success": self.AGE_VERIFICATION_SUCCESS_ALERT,
            "failure": self.AGE_VERIFICATION_FAIL_ALERT,
        }

        message_type = message_type.lower()

        if message_type not in xpath_map:
            raise ValueError(f"Invalid message_type: {message_type}")

        try:
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(xpath_map[message_type])
            )
            return message.text.strip()

        except (TimeoutException, NoSuchElementException):
            return None

    def are_alcoholic_products_not_viewable(self):
        self.find(self.ALCOHOL_CATEGORY_XPATH).click()
        try:
            self.find(self.NO_ALCOHOLIC_PRODUCTS)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

        def get_error_message(self):
            # Wait until the alert is visible, then return text
            element = self.driver.find_element(*self.AGE_VERIFICATION_FAIL_ALERT)
            return element.text






