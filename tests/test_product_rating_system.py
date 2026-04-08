
import pytest

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.test_data import TEST_VALID_USER_1, ADDRESS, CARD, TEST_INVALID_USER, COMMENT, TEST_VALID_USER_2
from utils.config import Config


@pytest.mark.parametrize("email, password, date_of_birth, should_login, street, city,"
                         "postal_code, card_number, name_on_card, expiration, cvv, celery_comment, username", [
                             (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], Config.AGE_20, True, ADDRESS["street"], ADDRESS["city"],
                              ADDRESS["postal_code"], CARD["number"], CARD["name"], CARD["expiration"], CARD["cvv"], COMMENT["celery"], TEST_VALID_USER_1["username"]),
                             (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], Config.AGE_20, False, '', '', '', '', '', '', '', '',
                              '')
                         ])
def test_logged_user_rates_bought_product(driver, email, password, date_of_birth, should_login, street, city, postal_code,
                                          card_number, name_on_card, expiration, cvv, celery_comment, username):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.screenshot("after_login")
        home_page.open_auth_profile_by_icon()
        login_page.screenshot("before_assert_is_user_logged_in")
        assert login_page.is_visible_logout_button()
        driver.back()
        shop_page = ShopPage(driver).load()
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        shop_page.screenshot("before_assert_age_confirmation_message")
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.add_product_to_cart("celery")
        shop_page.screenshot("after_add_to_cart")
        shop_page.wait_for_confirmation_message(Config.ITEM_ADDED_MESSAGE)
        shop_page.screenshot("before_assert_item_added_message")
        assert shop_page.get_confirmation_message() == Config.ITEM_ADDED_MESSAGE
        checkout_page = CheckoutPage(driver)
        checkout_page.load()
        checkout_page.screenshot("before_assert_is_buy_now_button_visible")
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.complete_checkout(street, city, postal_code, card_number, name_on_card, expiration, cvv)
        checkout_page.screenshot("after_purchase")
        home_page.open_shop_by_page()
        shop_page.view_product_info("celery")
        if shop_page.has_existing_rating(username):
            shop_page.delete_rating()
        shop_page.rate_stars("4")
        shop_page.comment(celery_comment)
        shop_page.send_rating()
        shop_page.wait_for_user_rating(username)
        shop_page.screenshot("before_asserts_new_rating")
        assert shop_page.get_rating() == Config.RATING["4"]
        assert shop_page.get_rating_user().lower() == username.lower()
        assert shop_page.get_comment_text() == celery_comment
        assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE
        shop_page.delete_rating()
    else:
        login_page.login(email, password)
        login_page.screenshot("before_assert_login_error_message")
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


@pytest.mark.parametrize("email, password, should_login, date_of_birth", [
    (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_20),
    (TEST_INVALID_USER["email"], TEST_INVALID_USER["password"], False, Config.AGE_20)
])
def test_logged_user_rates_not_bought_product(driver, email, password, should_login, date_of_birth):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.screenshot("after_login")
        home_page.open_auth_profile_by_icon()
        home_page.screenshot("before_assert_is_user_logged_in")
        assert login_page.is_visible_logout_button()
        driver.back()
        shop_page = ShopPage(driver).load()
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        shop_page.screenshot("before_assert_age_confirmation_message")
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.view_product_info("gala apples")
        shop_page.screenshot("before_assert_item_not_bought_message")
        assert shop_page.get_rating_restriction_text() == Config.ITEM_NOT_YET_BOUGHT_MESSAGE
    else:
        login_page.login(email, password)
        login_page.screenshot("before_assert_login_error_message")
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE


def test_logged_out_user_rates_product(driver, date_of_birth=Config.AGE_20):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    login_page.screenshot("before_assert_user_not_logged_in")
    assert login_page.get_email() == ''
    login_page.open_home_by_link()
    home_page.open_shop_by_page()
    shop_page = ShopPage(driver)
    shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
    shop_page.screenshot("before_assert_age_confirmation_message")
    assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
    shop_page.wait_for_confirmation_to_disappear()
    shop_page.view_product_info("kale")
    shop_page.screenshot("before_assert_item_not_yet_bought_message")
    assert shop_page.get_rating_restriction_text() == Config.ITEM_NOT_YET_BOUGHT_MESSAGE


@pytest.mark.parametrize("email, password, should_login, date_of_birth, confirmation_added_to_cart,"
                         " street, city, postal_code, card_number, name_on_card, expiration_card,"
                         " cvv, cauliflower_comment, username",[
    (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_20,
     Config.ITEM_ADDED_MESSAGE,ADDRESS["street"], ADDRESS["city"], ADDRESS["postal_code"],
     CARD["number"], CARD["name"], CARD["expiration"], CARD["cvv"], COMMENT["cauliflower"], TEST_VALID_USER_1["username"])
])
def test_logged_user_rates_product_2_times(driver, email, password, should_login, date_of_birth, confirmation_added_to_cart,
                                           street, city, postal_code, card_number, name_on_card, expiration_card,
                                           cvv, cauliflower_comment, username):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email, password)
        home_page.screenshot("after_login")
        home_page.open_auth_profile_by_icon()
        home_page.screenshot("before_assert_user_is_logged_in")
        assert login_page.is_visible_logout_button()
        driver.back()
        shop_page = ShopPage(driver).load()
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        shop_page.screenshot("before_assert_age_confirmation_message")
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.wait_for_confirmation_to_disappear()
        shop_page.add_product_to_cart("cauliflower")
        shop_page.wait_for_confirmation_message(confirmation_added_to_cart)
        shop_page.screenshot("before_assert_added_to_cart_confirmation_message")
        assert shop_page.get_confirmation_message() == confirmation_added_to_cart
        checkout_page = CheckoutPage(driver)
        checkout_page.load()
        checkout_page.screenshot("before_assert_is_buy_now_button_visible")
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.complete_checkout(street, city, postal_code, card_number, name_on_card, expiration_card, cvv)
        checkout_page.screenshot("after_purchase")
        home_page.open_shop_by_page()
        shop_page.view_product_info("cauliflower")
        if shop_page.has_existing_rating(username):
            shop_page.delete_rating()
        shop_page.rate_stars("5")
        shop_page.comment(cauliflower_comment)
        shop_page.send_rating()
        shop_page.wait_for_user_rating(username)
        shop_page.screenshot("before_asserts_is_rating_displayed")
        assert shop_page.get_rating() == Config.RATING["5"]
        assert shop_page.get_rating_user().lower() == username.lower()
        assert shop_page.get_comment_text() == cauliflower_comment
        assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE
        shop_page.delete_rating()
    else:
        login_page.login(email, password)
        login_page.screenshot("before_assert_login_error_message")
        assert login_page.get_error_message() == Config.LOGIN_ERROR_MESSAGE

@pytest.mark.parametrize("email_1, password_1, should_login, date_of_birth, confirmation_added_to_cart,"
                         " street, city, postal_code, card_number, name_on_card, expiration_card,"
                         " cvv, asparagus_comment, username, email_2, password_2, confirmation_logged_out",[
    (TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"], True, Config.AGE_20,
     Config.ITEM_ADDED_MESSAGE,ADDRESS["street"], ADDRESS["city"], ADDRESS["postal_code"],
     CARD["number"], CARD["name"], CARD["expiration"], CARD["cvv"], COMMENT["asparagus"], TEST_VALID_USER_1["username"],
     TEST_VALID_USER_2["email"], TEST_VALID_USER_2["password"], Config.LOGGED_OUT_MESSAGE)
])
def test_user_sees_rate_of_another_user(driver, email_1, password_1, should_login, date_of_birth, confirmation_added_to_cart,
                                           street, city, postal_code, card_number, name_on_card, expiration_card,
                                           cvv, asparagus_comment, username, email_2, password_2, confirmation_logged_out):
    home_page = HomePage(driver).load()
    login_page = LoginPage(driver).load()
    if should_login:
        login_page.login(email_1, password_1)
        home_page.screenshot("after_login")
        home_page.open_auth_profile_by_icon()
        login_page.screenshot("before_assert_is_logout_button_visible")
        assert login_page.is_visible_logout_button()
        driver.back()
        shop_page = ShopPage(driver).load()
        shop_page.enter_date_age_modal(date_of_birth).confirm_age_modal()
        shop_page.screenshot("before_assert_age_confirmation_message")
        assert shop_page.get_confirmation_message() == Config.AGE_CONFIRMATION_MESSAGE
        shop_page.wait_for_confirmation_to_disappear()
        shop_page.add_product_to_cart("asparagus")
        shop_page.wait_for_confirmation_message(confirmation_added_to_cart)
        shop_page.screenshot("before_assert_added_to_cart_confirmation_message")
        assert shop_page.get_confirmation_message() == confirmation_added_to_cart
        shop_page.open_cart_by_icon()
        checkout_page = CheckoutPage(driver)
        checkout_page.load()
        checkout_page.screenshot("before_assert_buy_now_button_visible")
        assert checkout_page.is_visible_buy_now_button()
        checkout_page.complete_checkout(street, city, postal_code, card_number, name_on_card, expiration_card, cvv)
        checkout_page.screenshot("after_purchase")
        home_page.open_shop_by_page()
        shop_page.view_product_info("asparagus")
        if shop_page.has_existing_rating(username):
            shop_page.delete_rating()
        shop_page.rate_stars("3")
        shop_page.comment(asparagus_comment)
        shop_page.send_rating()
        shop_page.wait_for_user_rating(username)
        shop_page.screenshot("before_asserts_rating_added")
        assert shop_page.get_rating() == Config.RATING["3"]
        assert shop_page.get_rating_user().lower() == username.lower()
        assert shop_page.get_comment_text() == asparagus_comment
        assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE
        shop_page.open_auth_profile_by_icon()
        login_page.logout()
        login_page.wait_for_confirmation_message(confirmation_logged_out)
        login_page.screenshot("before_assert_confirmation_logged_out_user")
        assert login_page.get_confirmation_message() == confirmation_logged_out
        login_page.login(email_2, password_2)
        home_page.open_auth_profile_by_icon()
        login_page.screenshot("before_assert_logout_button_visible")
        assert login_page.is_visible_logout_button()
        driver.back()
        home_page.open_shop_by_page()
        shop_page.view_product_info("asparagus")
        shop_page.screenshot("before_assert_rating_of_other_user")
        assert shop_page.get_rating_user() == username
        assert shop_page.get_rating() == Config.RATING["3"]
        assert shop_page.get_comment_text() == asparagus_comment
