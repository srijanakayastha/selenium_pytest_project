
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

    # --- PAGINATION ---
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")

    # --- MESSAGES ---
    CONFIRMATION_MSG = (By.XPATH, "//div[@role='status']")



    # ----------------- INIT -----------------
    def __init__(self, driver):
        super().__init__(driver)

    # ----------------- PAGE NAVIGATION -----------------
    def load(self):
        """Open the shop page URL"""
        return self.open(Config.SHOP_PAGE_URL)

    # ----------------- AGE MODAL -----------------
    def enter_date_age_modal(self, date):
        self.type_text(self.AGE_VERIFICATION_INPUT, date)
        return self

    def confirm_age_modal(self):
        self.click(self.AGE_VERIFICATION_CONFIRM_BUTTON)
        # Wait for modal to disappear
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.AGE_VERIFICATION_INPUT)
        )

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

        # REWRITE THIS LINE EXACTLY:
        # It must have one [ for contains and one [ for descendant.
        card_xpath = f"//div[contains(@class,'product-card')]   "

        # Wait for the card
        product_card = wait.until(EC.presence_of_element_located((By.XPATH, card_xpath)))

        # Handle Quantity
        if int(quantity) > 1:
            # Use partial name match for the dynamic ID 'quantity_...'
            qty_input = product_card.find_element(By.XPATH, ".//input[contains(@name, 'quantity')]")
            qty_input.clear()
            qty_input.send_keys(str(quantity))

            # 3. Wait for the button INSIDE the card to be clickable, then click
            # This is the most reliable way to ensure the click actually registers
            button_xpath = ".//button[contains(@class, 'btn-cart')]"

            # We find the element first, then wait for it to be clickable
            add_button = product_card.find_element(By.XPATH, button_xpath)
            wait.until(EC.element_to_be_clickable(add_button))

           # 4. Optional: Small sleep to let the AJAX request finish
            import time
            time.sleep(1)



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