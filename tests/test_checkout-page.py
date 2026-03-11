import time

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage


def test_checkout_page(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("test123@test.com", "123456")
    time.sleep(2)
    shop_page = ShopPage(driver)
    shop_page.load()
    time.sleep(2)
    shop_page.enter_date_age_modal("23-10-1990")
    shop_page.confirm_age_modal()
    time.sleep(2)
    shop_page.next_page()
    shop_page.enter_quantity_input_celery(5)
    time.sleep(2)
    shop_page.add_to_cart_celery()
    time.sleep(2)
    checkout_page = CheckoutPage(driver)
    checkout_page.load()
    time.sleep(2)
    checkout_page.click_plus_button()
    time.sleep(2)
    checkout_page.click_minus_button()
    time.sleep(2)
    checkout_page.buy_now()
    time.sleep(2)