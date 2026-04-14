from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import Config
from pages import product_rating
import time
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

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
        self.type_text(self.AGE_VERIFICATION_INPUT, f"{day}--{month}--{year}")
        return self

    def confirm_age_modal(self):
        """Click confirm on age modal and wait for overlay to disappear"""
        self.safe_click(self.AGE_VERIFICATION_CONFIRM_BUTTON)
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
   
    def confirm_age(self, date_of_birth):
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
        return (By.XPATH, f"//div[@class='card']//img[@alt='{product}']/parent::div[@class='card']//input[@type='number' and @class='quantity']")

    def add_product_to_cart(self, product_name, quantity=1):
        wait = WebDriverWait(self.driver, 10)
        product_add_to_cart_xpath = self.get_add_to_cart_xpath_for_product(product_name)
        add_to_cart_btn = self.find(product_add_to_cart_xpath)


        # Set quantity if more than 1
        if int(quantity) > 1:
            product_quantity_xpath = self.get_quantity_xpath_for_product(product_name)
            quantity_input = self.find(product_quantity_xpath)
            quantity_input.clear()
            quantity_input.send_keys(str(quantity))

        add_to_cart_btn.click()

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

    def has_existing_rating(self):
        try:
            menu = self.find(product_rating.COMMENT_OPTIONS)
            if menu.is_displayed():
                return True
            return False
        except(TimeoutException, NoSuchElementException):
            print("Menu icon not found due to error")

    def delete_rating(self):
        try:
            menu = self.find(product_rating.COMMENT_OPTIONS)
            if menu.is_displayed():
                menu.click()
                self.find(product_rating.DELETE_COMMENT).click()
                alert = self.wait.until(EC.alert_is_present())
                alert.accept()
        except Exception as e:
            print(f"Delete rating failed: {e}")

    def rate_stars(self, rating):
        stars_rating = str(rating)
        if stars_rating not in product_rating.RATING_STARS:
            raise ValueError(f"Invalid rating: {stars_rating}")

        star_locator = product_rating.RATING_STARS[stars_rating]
        star = self.find(star_locator)
        star.click()

    def add_comment(self,comment):
        self.type_text(product_rating.COMMENT_INPUT, comment)

    def save_rating(self):
       self.click(product_rating.SEND_RATING_BUTTON)


    def rate_product(self, product_name, rating, comment):
        """Rate and comment on a product, handling existing ratings"""

        self.view_product_info(product_name)
        if self.has_existing_rating():
            self.delete_rating()
        self.rate_stars(rating)
        if comment.strip() != "":
            self.add_comment(comment)
            self.save_rating()

    def update_rating(self, product_name, rating, comment):
        """Rate and comment on a product, handling existing ratings"""
        self.view_product_info(product_name)
        if self.has_existing_rating():
           self.update_rating()
        self.rate_stars(rating)
        if comment.strip() != "":
            self.add_comment(comment)
            self.save_rating()





