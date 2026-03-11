import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config


@pytest.mark.parametrize("email, password, date_of_birth, should_login, street, city,"
                         "postal_code, card_number, name_on_card, expiration, cvv, celery_comment, username", [
                             ('test123@test.com', '123456', Config.AGE_20, True, 'Baker street, 57', 'New York',
                              '89210', '1111111111111111', 'Test Test', '02/2028', '111', 'Fresh', 'test123'),
                             ('invalid_user@test.com', '123456', Config.AGE_20, False, '', '', '', '', '', '', '', '',
                              '')
                         ])
def test_logged_user_rates_bought_product(driver, email, password, date_of_birth, should_login, street, city,
                                          postal_code,
                                          card_number, name_on_card, expiration, cvv, celery_comment, username):
    home_page = HomePage(driver)
    home_page.load()
    login_page = LoginPage(driver)
    login_page.load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        driver.back()
        shop_page = ShopPage(driver)
        shop_page.load()
        shop_page.enter_date_age_modal(date_of_birth)
        shop_page.confirm_age_modal()
        assert shop_page.get_confirmation_message() == "You are of age. You can now view all products, even alcohol products."
        shop_page.next_page()
        shop_page.add_to_cart_celery()
        shop_page.wait_for_confirmation_message("Item added to cart!")
        assert shop_page.get_confirmation_message() == "Item added to cart!"
        checkout_page = CheckoutPage(driver)
        checkout_page.load()
        checkout_page.enter_street(street)
        checkout_page.enter_city(city)
        checkout_page.enter_postal_code(postal_code)
        checkout_page.enter_card_number(card_number)
        checkout_page.enter_name_on_card(name_on_card)
        checkout_page.enter_expiration_card(expiration)
        checkout_page.enter_cvv_card(cvv)
        checkout_page.buy_now()
        home_page.open_shop_by_page()
        shop_page.next_page()
        shop_page.view_product_info_celery()
        shop_page.rate_4_stars()
        shop_page.comment(celery_comment)
        shop_page.send_rating()
        shop_page.wait_for_product_rating()
        assert shop_page.get_rating() == 4
        assert shop_page.get_rating_user().lower() == username.lower()
        assert shop_page.get_comment_text() == "Fresh"
        assert shop_page.get_rating_restriction_text() == "You have already reviewed this product."
        shop_page.delete_rating()
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == "Invalid username or password"


@pytest.mark.parametrize("email, password, should_login, date_of_birth", [
    ('test123@test.com', '123456', True, Config.AGE_20),
    ('invalid_user@test.com', '123456', False, Config.AGE_20)
])
def test_logged_user_rates_not_bought_product(driver, email, password, should_login, date_of_birth):
    home_page = HomePage(driver)
    home_page.load()
    login_page = LoginPage(driver)
    login_page.load()
    if should_login:
        login_page.login(email, password)
        home_page.open_auth_profile_by_icon()
        driver.back()
        home_page.open_shop_by_page()
        shop_page = ShopPage(driver)
        shop_page.enter_date_age_modal(date_of_birth)
        shop_page.confirm_age_modal()
        assert shop_page.get_confirmation_message() == "You are of age. You can now view all products, even alcohol products."
        shop_page.view_product_info_gala_apples()
        assert shop_page.get_rating_restriction_text() == "You need to buy this product to tell us your opinion!"
    else:
        login_page.login(email, password)
        assert login_page.get_error_message() == "Invalid username or password"