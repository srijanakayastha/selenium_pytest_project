import time

from pages.home_page import HomePage

def test_open_profile_auth(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_auth_profile_by_icon()
    time.sleep(2)

def test_open_favorites_by_icon(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_favorites_list_by_icon()
    time.sleep(2)

def test_open_favorites_by_page(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_favorites_list_by_page()
    time.sleep(2)

def test_open_cart_by_icon(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_cart_by_icon()
    time.sleep(2)

def test_open_shop_by_page(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_shop_by_page()
    time.sleep(2)

def test_open_contact_by_page(driver):
    home_page = HomePage(driver)
    home_page.load()
    home_page.open_contact_page()
    time.sleep(2)