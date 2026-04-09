from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config
import time

class ShopPage(BasePage):

    # --- AGE MODAL ---
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class='modal-content']/input[@type='text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class='modal-content']//button[text()='Confirm']")
    AGE_VERIFICATION_SUCCESS_ALERT = (
        By.XPATH,
        f"//div[@role='status' and contains(text(), '{Config.AGE_VERIFICATION_SUCCESS_ALERT}')]"
    )
    AGE_VERIFICATION_FAIL_ALERT = (
        By.XPATH,
        f"//div[@role='status' and contains(text(), '{Config.AGE_VERIFICATION_FAIL_ALERT}')]"
    )
    MODAL_OVERLAY = (By.CLASS_NAME, "modal-overlay")

    # --- PRODUCTS ---
    PRODUCT_CARD = ".product-card"
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    NO_ALCOHOLIC_PRODUCTS = (By.XPATH, "//div[@class='no-products-card']")
    ALCOHOL_CATEGORY_XPATH = (By.XPATH, "//a[text()='Alocohol']")

    # --- SHOP NAV ---
    SHOP_XPATH = (By.XPATH, "//ul[@class='anim-nav']//a[@href='/store']")

    # --- PAGE LOAD ---
    def load(self):
        """Load shop page safely, waiting for any modal overlays to disappear"""
        self.wait_for_overlay_to_disappear()
        self.safe_click(self.SHOP_XPATH)
        self.wait_for_overlay_to_disappear()
        return self

    # --- AGE MODAL ---
    def enter_date_age_modal(self, date_of_birth):
        """Enter DOB in age modal fields"""
        day, month, year = date_of_birth.split("-")
        self.type_text((By.ID, "dob-day"), day)
        self.type_text((By.ID, "dob-month"), month)
        self.type_text((By.ID, "dob-year"), year)
        return self

    def confirm_age_modal(self):
        """Click confirm on age modal and wait for overlay to disappear"""
        self.safe_click(self.AGE_VERIFICATION_CONFIRM_BUTTON)
        self.wait_for_overlay_to_disappear()
        return self

    def get_age_verification_message(self, message_type):
        """Return success/failure message text"""
        xpath_map = {
            "success": self.AGE_VERIFICATION_SUCCESS_ALERT,
            "failure": self.AGE_VERIFICATION_FAIL_ALERT,
        }
        locator = xpath_map.get(message_type.lower())
        if not locator:
            raise ValueError(f"Invalid message_type: {message_type}")
        try:
            message = self.find(locator)
            return message.text.strip()
        except:
            return None

    # --- AGE CONFIRM HELPER ---
   
    def confirm_age(shop_page, date_of_birth):
        """Helper to enter DOB and confirm age modal"""
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()

    # --- PRODUCTS ---
    def get_all_products_on_page(self):
        return [el.get_attribute("alt") for el in self.driver.find_elements(By.CSS_SELECTOR, ".product-card img[alt]")]

    def find_product(self, product_name):
        """Handle pagination and find product by name"""
        while True:
            cards = self.driver.find_elements(By.CSS_SELECTOR, ".product-card")
            for card in cards:
                if product_name.lower() in card.text.lower():
                    return card
            # Pagination
            try:
                next_buttons = self.driver.find_elements(*self.NEXT_PAGE_BUTTON)
                if next_buttons and next_buttons[0].is_enabled():
                    next_buttons[0].click()
                    time.sleep(1)
                else:
                    return None
            except:
                return None

    def is_product_visible(self, product_name):
        return self.find_product(product_name) is not None

    def get_add_to_cart_xpath_for_product(self, product):
        return (By.XPATH, f"//div[@class='card']//img[@alt='{product}']/parent::div[@class='card']//button[contains(text(),'Add to Cart')]")

    def get_quantity_xpath_for_product(self, product):
        return (By.XPATH, f"//div[@class='card']//img[@alt='{product}']/parent::div[@class='card']//input[@type='number']")

    def add_product_to_cart(self, product_name, quantity=1):
        self.wait_for_overlay_to_disappear()
        add_btn_locator = self.get_add_to_cart_xpath_for_product(product_name)

        # Set quantity if more than 1
        if int(quantity) > 1:
            quantity_locator = self.get_quantity_xpath_for_product(product_name)
            quantity_input = self.find(quantity_locator)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))

        self.safe_click(add_btn_locator)

    def view_product_info(self, product_name):
        product_card = self.find_product(product_name)
        if not product_card:
            raise Exception(f"Product '{product_name}' not found.")
        product_image = product_card.find_element(By.TAG_NAME, "img")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_image)
        product_image.click()

    def are_alcoholic_products_not_viewable(self):
        """
        Returns True if alcoholic products are NOT viewable (blocked),
        i.e., the "no products" card is visible.
        Returns False if alcoholic products are visible.
        """
        try:
            # If the "no-products-card" element is displayed, then products are blocked
            element = self.find(self.NO_ALCOHOLIC_PRODUCTS)
            return element.is_displayed()
        except:
            # If element is not found, products are visible
            return False