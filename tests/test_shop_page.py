import time

from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config
from utils.test_data import COMMENT
from utils.test_data import TEST_VALID_USER_1

def test_rate_celery(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("test123@test.com", "123456")
    login_page.screenshot("after_login")
    time.sleep(2)
    shop_page = ShopPage(driver)
    shop_page.load()
    time.sleep(2)
    shop_page.enter_date_age_modal("25-03-1987").confirm_age_modal()
    time.sleep(2)
    shop_page.add_product_to_cart("celery", 5)
    shop_page.screenshot("after_add_to_cart")
    shop_page.view_product_info("celery")
    shop_page.rate_stars("4")
    shop_page.comment(COMMENT["celery"])
    shop_page.send_rating()
    time.sleep(2)
    shop_page.screenshot("before_assert_already_reviewed_message")
    assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE
    time.sleep(2)
    shop_page.screenshot("before_assert_rating_user")
    assert shop_page.get_rating_user() == TEST_VALID_USER_1["username"]
    time.sleep(2)
    shop_page.screenshot("before_assert_rating")
    assert shop_page.get_rating() == Config.RATING["4"]
    time.sleep(2)
    shop_page.delete_rating()
    time.sleep(2)