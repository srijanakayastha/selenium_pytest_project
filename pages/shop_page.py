from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from utils.config import Config

class ShopPage(HomePage):
    """
    Page object for the shop page.
    """
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class = 'modal-content']/input[@type = 'text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class = 'modal-content']/button[text() = 'Confirm']")
    CONFIRMATION_MSG = (By.XPATH, "//div[@role = 'status']")
    ERROR_MSG = (By.XPATH, "//div[@role = 'status']")
    QUANTITY_INPUT_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[1]/input")
    ADD_TO_CART_BUTTON_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[2]/button")
    ADD_TO_FAVORITES_BUTTON_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]/div/div[2]/div[3]/div/div[3]/button")
    PRODUCT_INFO_CELERY = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[7]")
    RATING_4_STARS = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[4]")
    COMMENT_INPUT = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/textarea")
    SEND_RATING_BUTTON = (By.XPATH, "//*[@id='root']/div/section/section[1]/div[2]/div/div/div/div/div[3]/button[2]")
    COMMENT_OPTIONS = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div")
    COMMENT_TEXT = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/p")
    DELETE_COMMENT = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/div[2]/button[2]")
    RATING_RESTRICTION = (By.XPATH, "//*[@id='root']/div/section/div[3]/p")
    RATING_USER = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[1]/h5/strong")
    CUSTOM_RATING = (By.XPATH, "//*[@id='root']/div/section/section/div/div[1]/div/div[2]/div/div/div[1]/span[contains(@class,'full')]")
    PRODUCT_INGO_GALA_APPLES = (By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div/div[2]/div[10]")
    CATEGORY_FILTER_LIST = (By.XPATH, f"//h4[@class = 'widget-title']/following-sibling::ul/li[{Config.ALL_CATEGORY}]")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Next']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//button[@class = 'pagination-link' and text() = 'Previous']")
    PAGE_BUTTON_2 = (By.XPATH, "//button[@class = 'pagination-link' and text() = '2']")


    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        return self.open(Config.SHOP_PAGE_URL)

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

    def enter_quantity_input_celery(self, quantity):
        self.type_text(self.QUANTITY_INPUT_CELERY, quantity)
        return self

    def add_to_cart_celery(self):
        self.click(self.ADD_TO_CART_BUTTON_CELERY)

    def add_to_favourites_celery(self):
        self.click(self.ADD_TO_FAVORITES_BUTTON_CELERY)

    def select_category_list(self):
        self.click(self.CATEGORY_FILTER_LIST)

    def next_page(self):
        self.click(self.NEXT_PAGE_BUTTON)

    def previous_page(self):
        self.click(self.PREVIOUS_PAGE_BUTTON)

    def page_2(self):
        self.click(self.PAGE_BUTTON_2)

    def view_product_info_celery(self):
        self.click(self.PRODUCT_INFO_CELERY)

    def view_product_info_gala_apples(self):
        self.click(self.PRODUCT_INGO_GALA_APPLES)

    def rate_4_stars(self):
        self.click(self.RATING_4_STARS)

    def comment(self, comment):
        self.type_text(self.COMMENT_INPUT, comment)

    def send_rating(self):
        self.click(self.SEND_RATING_BUTTON)

    def delete_rating(self):
        self.click(self.COMMENT_OPTIONS)
        self.click(self.DELETE_COMMENT)
        self.wait_and_accept_alert()

    def get_rating_restriction_text(self):
        return self.get_text(self.RATING_RESTRICTION)

    def get_rating_user(self):
        return self.get_text(self.RATING_USER)

    def get_rating(self):
        rating = self.find_all(self.CUSTOM_RATING)
        return len(rating)

    def get_comment_text(self):
        return self.get_text(self.COMMENT_TEXT)

    def wait_for_confirmation_message(self, text):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(
            EC.text_to_be_present_in_element(self.CONFIRMATION_MSG, text)
        )

    def wait_for_product_rating(self):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.presence_of_all_elements_located(self.CUSTOM_RATING))