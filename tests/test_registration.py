import time

from pages.registration_page import RegistrationPage


def test_creating_new_user(driver):
    registration = RegistrationPage(driver)
    registration.load()
    time.sleep(2)
    registration.switch_to_registration()
    time.sleep(2)
    registration.enter_name("Test")
    registration.enter_email("test@test.net")
    registration.enter_password("123456")
    registration.submit()
    assert registration.get_confirmation_message() == 'Username already exists'