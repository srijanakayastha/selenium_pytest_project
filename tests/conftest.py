import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    """
        PyTest fixture to set up and tear down the Selenium WebDriver.
    """
    # Instantiate the web driver for Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--guest") # To workaround Google Password Manager pop-up

    # Start driver (Selenium 4 style)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(3)  # Implicit wait to handle timing issues

    # Yield the driver instance for use in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()