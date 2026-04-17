from pages.home_page import HomePage
from pages.login_page import LoginPage


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

def parse_price(text):
    return float(text.replace("€", "").strip())