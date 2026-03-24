from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from utils.config import Config


class ShopPage(HomePage):
    """
    Page object for the shop page.
    """
    # --- AGE VERIFICATION ---
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class = 'modal-content']/input[@type = 'text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class = 'modal-content']/button[text() = 'Confirm']")
    AGE_VERIFICATION_TEXT = (By.XPATH, "//div[@class = 'modal-content']//p")
    UNDERAGE_NOTICE = (By.XPATH, "//div[@class = 'card-body']/p")

    CONFIRMATION_MSG = (By.XPATH, "//div[@role = 'status']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")
    FIRST_PRODUCT_NAME = (By.XPATH, "//p[@class = 'lead']")

    # --- RATING SYSTEM ---
    COMMENT_INPUT = (By.XPATH, "//textarea[@class = 'new-review-form-control ']")
    SEND_RATING_BUTTON = (By.XPATH, "//button[@class = 'new-review-btn new-review-btn-send']")
    COMMENT_OPTIONS = (By.XPATH, "//div[@class = 'menu-icon']")
    COMMENT_TEXT = (By.XPATH, "//div[@class = 'comment'][1]/div[@class = 'comment-body']//p")
    EDIT_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[1]")
    DELETE_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[2]")
    RATING_RESTRICTION = (By.XPATH, "//div[@class = 'reviewRestriction']/p")
    RATING_USER = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'comment-header']//strong")
    CUSTOM_RATING = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'custom-rating']/span[@class = 'star full']")
    RATING_STARS = {
        "1": (By.XPATH, "//div[@class = 'interactive-rating']/span[1]"),
        "2": (By.XPATH, "//div[@class = 'interactive-rating']/span[2]"),
        "3": (By.XPATH, "//div[@class = 'interactive-rating']/span[3]"),
        "4": (By.XPATH, "//div[@class = 'interactive-rating']/span[4]"),
        "5": (By.XPATH, "//div[@class = 'interactive-rating']/span[5]")
    }

    # --- PAGINATION ---
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Next']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Previous']")
    PAGE_BUTTON = {
        "2": (By.XPATH, "//button[@class = 'pagination-link' and text() = '2']"),
        "3": (By.XPATH, "//button[@class = 'pagination-link' and text() = '3']"),
        "4": (By.XPATH, "//button[@class = 'pagination-link' and text() = '4']")
    }

    CATEGORY = {
        "all": (By.XPATH, "//ul//a[text() = 'All']"),
        "vegetables": (By.XPATH, "//ul//a[text() = 'Fresh Vegetables']"),
        "meat": (By.XPATH, "//ul//a[text() = 'Meat & Poultry']"),
        "meat free": (By.XPATH, "//ul//a[text() = 'Meat Free']"),
        "bakery": (By.XPATH, "//ul//a[text() = 'Bakery']"),
        "chilled": (By.XPATH, "//ul//a[text() = 'Chilled']"),
        "cupboard": (By.XPATH, "//ul//a[text() = 'Food Cupboard']"),
        "alcohol": (By.XPATH, "//ul//a[text() = 'Alocohol']"),
        "frozen": (By.XPATH, "//ul//a[text() = 'Frozen Foods']"),
        "fish": (By.XPATH, "//ul//a[text() = 'Fish']"),
        "cleaning": (By.XPATH, "//ul//a[text() = 'Cleaning House']"),
        "pet": (By.XPATH, "//ul//a[text() = 'Pet Care']")
    }

    # --- PRODUCT ---
    ADD_TO_CART_BUTTON = {
        "celery": (By.XPATH, "//img[@alt='Celery']/following::button[@class = 'btn btn-primary btn-cart']"),
        "cauliflower": (By.XPATH, "//img[@alt='Cauliflower']/following::button[@class = 'btn btn-primary btn-cart']"),
        "asparagus": (By.XPATH, "//img[@alt='Asparagus']/following::button[@class = 'btn btn-primary btn-cart']"),
        "gala apples": (By.XPATH, "//img[@alt='Gala Apples']/following::button[@class = 'btn btn-primary btn-cart']"),
        "pink lady apples": (By.XPATH,
                             "//img[@alt='Pink Lady Apples']/following::button[@class = 'btn btn-primary btn-cart']"),
        "birchwood quarter pounders": (By.XPATH,
                                       "//img[@alt='Birchwood Quarter Pounders']/following::button[@class = 'btn btn-primary btn-cart']"),
        "ginger": (By.XPATH, "//img[@alt='Ginger']/following::button[@class = 'btn btn-primary btn-cart']"),
        "large flat mushrooms": (By.XPATH,
                                 "//img[@alt='Large Flat Mushrooms']/following::button[@class = 'btn btn-primary btn-cart']"),
        "kale": (By.XPATH, "//img[@alt='Kale']/following::button[@class = 'btn btn-primary btn-cart']")
    }

    ADD_TO_FAVOURITE_BUTTON = {
        "celery": (By.XPATH, "//img[@alt='Celery']/following::button[@class = 'btn btn-outline-dark ']")
    }

    PRODUCT_INFO = {
        "celery": (By.XPATH, "//img[@alt='Celery']"),
        "gala apples": (By.XPATH, "//img[@alt='Gala Apples']"),
        "kale": (By.XPATH, "//img[@alt='Kale']"),
        "cauliflower": (By.XPATH, "//img[@alt='Cauliflower']"),
        "asparagus": (By.XPATH, "//img[@alt='Asparagus']")
    }

    QUANTITY_INPUT_PRODUCT = {
        "celery": (By.XPATH, "//img[@alt='Celery']/following::input[@type = 'number']")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_into_view(self, locator):
        """
        Scroll the element located by `locator` into view using JavaScript.
        """
        element = self.find(locator)  # assumes self.find(locator) returns a WebElement
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def load(self):
        return self.open(Config.SHOP_PAGE_URL)

    def get_age_modal_text(self):
        return self.get_text(self.AGE_VERIFICATION_TEXT)

    def enter_date_age_modal(self, date):
        self.type_text(self.AGE_VERIFICATION_INPUT, date)
        return self

    def confirm_age_modal(self):
        self.click(self.AGE_VERIFICATION_CONFIRM_BUTTON)

    def get_confirmation_message(self):
        if self.is_visible(self.CONFIRMATION_MSG):
            return self.get_text(self.CONFIRMATION_MSG)
        return None

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return None

    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)

    def add_product_to_cart(self, product, quantity=None):
        found = self.find_product(product)
        if not found:
            raise Exception(f"Product '{product}' not found!")

        # only change quantity if needed
        if quantity is not None:
            input_locator = self.QUANTITY_INPUT_PRODUCT.get(product)
            if not input_locator:
                raise ValueError(f"Unknown product: {product}")
            self.type_text(input_locator, quantity)

        button_locator = self.ADD_TO_CART_BUTTON.get(product)
        if not button_locator:
            raise ValueError(f"Unknown product: {product}")

        self.scroll_into_view(button_locator)
        self.click(button_locator)

    def add_to_favourites(self, product):
        if product not in self.ADD_TO_FAVOURITE_BUTTON:
            raise ValueError(f"Unknown product: {product}")
        self.scroll_into_view(self.ADD_TO_FAVOURITE_BUTTON[product])
        self.click(self.ADD_TO_FAVOURITE_BUTTON[product])

    def get_next_page_button(self):
        button = self.find(self.NEXT_PAGE_BUTTON)
        self.scroll_into_view(self.NEXT_PAGE_BUTTON)
        return button

    def next_page(self):
        self.scroll_into_view(self.NEXT_PAGE_BUTTON)
        self.click(self.NEXT_PAGE_BUTTON)

    def previous_page(self):
        self.scroll_into_view(self.PREVIOUS_PAGE_BUTTON)
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def page(self, page_number):
        locator = self.PAGE_BUTTON.get(page_number)
        if not locator:
            raise ValueError(f"Invalid page number: {page_number}")
        self.scroll_into_view(locator)
        self.click(locator)

    def view_category_products(self, category):
        locator = self.CATEGORY.get(category)
        if not locator:
            raise ValueError(f"Invalid category: {category}")
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def view_product_info(self, product):
        self.find_product(product)
        self.scroll_into_view(self.PRODUCT_INFO[product])
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_INFO[product])).click()

    def rate_stars(self, stars):
        self.click(self.RATING_STARS[stars])

    def comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    def send_rating(self):
        self.click(self.SEND_RATING_BUTTON)

    def delete_rating(self):
        self.wait.until(
            EC.element_to_be_clickable(self.COMMENT_OPTIONS)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_COMMENT)
        ).click()

        self.wait_and_accept_alert()

        self.wait.until(
            EC.invisibility_of_element_located(self.COMMENT_OPTIONS)
        )

    def has_existing_rating(self, username):
        user = self.get_rating_user()
        if user.lower() == username.lower():
            return True
        return False

    def get_rating_restriction_text(self):
        return self.get_text(self.RATING_RESTRICTION)

    def get_rating_user(self):
        return self.get_text(self.RATING_USER)

    def get_underage_notice_text(self):
        return self.get_text(self.UNDERAGE_NOTICE)

    def get_rating(self):
        rating = self.find_all(self.CUSTOM_RATING)
        return len(rating)

    def get_comment_text(self):
        try:
            return self.get_text(self.COMMENT_TEXT)
        except TimeoutException:
            print("Comment not found!")

    def wait_for_confirmation_message(self, text):
        self.wait.until(
            EC.text_to_be_present_in_element(self.CONFIRMATION_MSG, text)
        )

    def wait_for_confirmation_to_disappear(self):
        self.wait.until(
            EC.invisibility_of_element(self.CONFIRMATION_MSG)
        )

    def wait_for_user_rating(self, username):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RATING_USER, username.capitalize()
                                             )
        )

    def is_product_visible(self, product):
        locator = self.ADD_TO_CART_BUTTON.get(product)
        if not locator:
            raise ValueError(f"Unknown product: {product}")

        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    def find_product(self, product):
        while True:
            if self.is_product_visible(product):
                return True

            next_button = self.get_next_page_button()

            if not next_button.is_enabled():
                return False

            next_button.click()

            # wait for new products to load
            self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//img[@alt]"))
            )