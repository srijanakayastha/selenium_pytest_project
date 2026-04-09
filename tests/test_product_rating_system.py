import pytest

from pages.checkout_page import CheckoutPage
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
    shop_page.wait_for_age_modal_to_disappear()


def buy_product(driver, product, address, card):
    """Add product to cart and complete checkout"""
    shop_page = ShopPage(driver)

    shop_page.add_product_to_cart(product)
    shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
    assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE

    checkout_page = CheckoutPage(driver).load()
    assert checkout_page.is_visible_buy_now_button()

    checkout_page.complete_checkout(
        address["street"],
        address["city"],
        address["postal_code"],
        card["number"],
        card["name"],
        card["expiration"],
        card["cvv"]
    )


def rate_product(shop_page, product, rating, comment, username):
    """Rate and comment on a product, handling existing ratings"""
    shop_page.view_product_info(product)

    if shop_page.has_existing_rating(username):
        shop_page.delete_rating()

    shop_page.rate_stars(rating)
    shop_page.comment(comment)
    shop_page.send_rating()
    shop_page.wait_for_user_rating(username)

    assert shop_page.get_rating() == Config.RATING[rating]
    assert shop_page.get_rating_user().lower() == username.lower()
    assert shop_page.get_comment_text() == comment
    assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE


# ---------- Tests ----------

@pytest.mark.parametrize("user", [TEST_VALID_USER_1])
def test_logged_user_rates_bought_product(driver, user):
    home_page, _ = login_and_verify(driver, user["email"], user["password"])

    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)

    buy_product(driver, "celery", ADDRESS, CARD)

    home_page.open_shop_by_page()
    rate_product(shop_page, "celery", "4", COMMENT["celery"], user["username"])


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

    buy_product(driver, "cauliflower", ADDRESS, CARD)

    home_page.open_shop_by_page()
    rate_product(shop_page, "cauliflower", "5", COMMENT["cauliflower"], user["username"])


def test_user_sees_rate_of_another_user(driver):
    user1 = TEST_VALID_USER_1
    user2 = TEST_VALID_USER_2

    # User 1 rates product
    home_page, login_page = login_and_verify(driver, user1["email"], user1["password"])
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, Config.AGE_20)

    buy_product(driver, "asparagus", ADDRESS, CARD)
    home_page.open_shop_by_page()
    rate_product(shop_page, "asparagus", "3", COMMENT["asparagus"], user1["username"])

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