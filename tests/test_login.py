import time

from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("test123@test.com", "123456")
    time.sleep(2)


def test_login_invalid(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("i@email.com", "123456")
    assert login_page.get_error_message().lower() == "invalid username or password"