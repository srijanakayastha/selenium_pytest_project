import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.test_data import (
    TEST_VALID_USER_1, TEST_VALID_USER_2,
    TEST_INVALID_USER, ADDRESS, CARD, COMMENT
)
from utils.config import Config

# ---------- Helpers ----------

def login_and_verify(driver, email, password):
    """Log in and assert logout button visible"""
    login_page = LoginPage(driver).load()
    home_page = HomePage(driver)
    login_page.login(email, password)
    home_page.open_auth_profile_by_icon()
    assert login_page.is_visible_logout_button()
    driver.back()
    return home_page, login_page


def confirm_age(shop_page, date_of_birth):
    """Enter date of birth and confirm age modal"""
    shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()

def rate_product_flow(shop_page, product_name, rating, comment, username):
    """Rate and comment on a product, handling existing ratings"""
    shop_page.rate_product(product_name, rating, comment)

def update_rating(shop_page, product, rating, comment, username):
        """Rate and comment on a product, handling existing ratings"""
        shop_page.rate_product(product, rating, comment)


# ---------- Tests ----------

@pytest.mark.parametrize(
    "user, product_name, rating, comment",
    [
        (TEST_VALID_USER_1, "celery", "1", "celery"),

    ]
)
def test_logged_user_rates_bought_product(driver, user, product_name, rating, comment):
    home_page, _ = login_and_verify(driver, user["email"], user["password"])
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)
    home_page.open_shop_by_page()
    rate_product_flow(shop_page, product_name, rating, comment, user["username"])

@pytest.mark.parametrize("email, password, should_login", [
    (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True),
    (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False)
])
def test_logged_user_rates_not_bought_product(driver, email, password, should_login):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()

    login_page.login(email, password)

    if should_login:
        home_page.open_auth_profile_by_icon()
        assert login_page.is_visible_logout_button()
        driver.back()

        shop_page = ShopPage(driver).load()
        confirm_age(shop_page, Config.AGE_20)

        shop_page.view_product_info("gala apples")
        assert shop_page.get_rating_restriction_text() == Config.ITEM_NOT_YET_BOUGHT_MESSAGE
    else:
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


def test_logged_out_user_rates_product(driver):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()

    assert login_page.get_email() == ''

    login_page.open_home_by_link()
    home_page.open_shop_by_page()

    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)

    shop_page.view_product_info("kale")
    assert shop_page.get_rating_restriction_text() == Config.ITEM_NOT_YET_BOUGHT_MESSAGE


def test_logged_user_rates_product_2_times(driver):
    user = TEST_VALID_USER_1
    home_page, _ = login_and_verify(driver, user["email"], user["password"])

    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)
    home_page.open_shop_by_page()
    rate_product_flow(shop_page, "cauliflower", "5", COMMENT["cauliflower"], user["username"])


def test_user_sees_rate_of_another_user(driver):
    user1 = TEST_VALID_USER_1
    user2 = TEST_VALID_USER_2

    # User 1 rates product
    home_page, login_page = login_and_verify(driver, user1["email"], user1["password"])
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)


    home_page.open_shop_by_page()
    rate_product_flow(shop_page, "asparagus", "3", COMMENT["asparagus"], user1["username"])

    # Logout User 1
    shop_page.open_auth_profile_by_icon()
    login_page.logout()
    login_page.wait_for_confirmation_message(Config.LOGGED_OUT_MESSAGE)
    assert login_page.get_confirmation_message() == Config.LOGGED_OUT_MESSAGE

    # User 2 views rating
    login_and_verify(driver, user2["email"], user2["password"])
    home_page.open_shop_by_page()
    shop_page.view_product_info("asparagus")

    assert shop_page.get_rating_user() == user1["username"]
    assert shop_page.get_rating() == Config.RATING["3"]
    assert shop_page.get_comment_text() == COMMENT["asparagus"]