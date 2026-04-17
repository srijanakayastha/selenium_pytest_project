import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="function")
def driver():
    """PyTest fixture to set up and tear down the Selenium WebDriver."""

    chrome_options = webdriver.ChromeOptions()

    # Avoid Google Password Manager pop-up
    chrome_options.add_argument("--guest")

    # # Zoom out to ensure all UI elements are visible
    # chrome_options.add_argument("--force-device-scale-factor=0.8")

    # Start browser maximized
    chrome_options.add_argument("--start-maximized")

    # Optional: run headless in CI
    if os.getenv("HEADLESS") == "1":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

    driver = None

    try:

        driver = webdriver.Chrome( options=chrome_options)

        # Basic stability improvement
        driver.implicitly_wait(5)

        driver.delete_all_cookies()

        yield driver

    finally:
        if driver:
            driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots on setup or test failure
    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Unique filename (handles parametrized tests)
            file_name = f"{item.nodeid.replace('::', '_').replace('/', '_')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)