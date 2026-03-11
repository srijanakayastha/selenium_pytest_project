import time

from pages.login_page import LoginPage
from pages.shop_page import ShopPage

def test_rate_celery(driver):
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
    shop_page.view_product_info_celery()
    shop_page.rate_celery_4_stars()
    shop_page.comment_celery()
    shop_page.send_rating_celery()
    time.sleep(2)
    assert shop_page.get_celery_rating_restriction_text() == "You have already reviewed this product."
    time.sleep(2)
    assert shop_page.get_celery_rating_user() == "Test123"
    time.sleep(2)
    assert shop_page.get_celery_rating() == 4
    time.sleep(2)
    shop_page.delete_rating_celery()
    time.sleep(2)