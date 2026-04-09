import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config
from utils.test_data import TEST_VALID_USER_1, TEST_INVALID_USER


@pytest.mark.parametrize("dob, result", [
    ("1-2-1990", "success"),
    ("1-3-2019", "failure")
])
def test_age_verification(driver, dob, result):

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"])

    shop_page = ShopPage(driver)
    shop_page.load()
    shop_page.enter_date_age_modal(dob).confirm_age_modal()

    age_verification_message = shop_page.get_age_verification_message(result)

    if result == "success":
        assert Config.AGE_VERIFICATION_SUCCESS_ALERT == age_verification_message
        assert shop_page.are_alcoholic_products_not_viewable() is False
    else:
        assert Config.AGE_VERIFICATION_FAIL_ALERT == age_verification_message
        assert shop_page.are_alcoholic_products_not_viewable() is True


@pytest.mark.parametrize("date_of_birth", [
    Config.AGE_VERIFICATION_FAIL_ALERT
])
def test_user_17_years_old_cannot_view_alcoholic_products(driver, date_of_birth):
    HomePage(driver).load()
    shop_page = ShopPage(driver).load()
    shop_page.screenshot("before_assert_underage_message")
    assert shop_page.get_error_message() == Config.AGE_VERIFICATION_FAIL_ALERT
    shop_page.view_category_products("alcohol")
    shop_page.screenshot("before_assert_underage_notice_text")
    assert shop_page.get_underage_notice_text() == Config.UNDERAGE_NOTICE_TEXT


