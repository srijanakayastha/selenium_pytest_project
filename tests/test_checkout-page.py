from os import times
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.helpers import login_and_verify, confirm_age, parse_price
import pytest

from utils.test_data import TEST_VALID_USER_1


@pytest.mark.parametrize(
    "user, dob, product_name, quantity, expected_shipping",
    [
        (TEST_VALID_USER_1, "01-10-1990", "Cherries", "6", 0),
        (TEST_VALID_USER_1, "01-10-1990", "Celery", "1", 5),
        (TEST_VALID_USER_1, "01-10-1990", "Ginger", "1", 5),
        (TEST_VALID_USER_1, "01-10-1990", "Large Flat Mushrooms", "18", 0),
    ]
)


def test_shipping_cost_changes(driver,user, dob, product_name, quantity,expected_shipping):
    home_page, _ = login_and_verify(driver, user["email"], user["password"])
    checkout_page =CheckoutPage(driver)
    checkout_page.load()
    checkout_page.clear_cart()
    time.sleep(1)

    driver.refresh()
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, dob)
    shop_page.add_product(product_name, quantity)
    checkout_page = home_page.open_cart_by_icon()
    shipment = checkout_page.get_shipment()
    actual_shipping = parse_price(shipment)

    assert actual_shipping == expected_shipping

# Test Case: Verify that shipping cost is calculated dynamically when items are added to the basket. As a user of MarketMate,
# I can see the shipping cost is calculated dynamically when items are added to the basket.

@pytest.mark.parametrize(
    "user, dob, extra_mushrooms, initial_shipping, final_shipping",
    [
        (TEST_VALID_USER_1, "16-04-2000", 17, 5.0, 0.0),
    ]
)
def test_shipping_cost_calculation_dynamic(driver, user, dob, extra_mushrooms, initial_shipping, final_shipping):
    home_page, _ = login_and_verify(driver, user["email"], user["password"])

    # 1. Clean the cart
    checkout_page = CheckoutPage(driver).load()
    checkout_page.clear_cart()
    driver.refresh()

    # 2. Add a few items
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, dob)
    shop_page.add_product("Ginger", 1)
    shop_page.add_product("Large Flat Mushrooms", 1)

    # 3. CHECK INITIAL (The "Before" state)
    checkout_page = home_page.open_cart_by_icon()
    assert parse_price(checkout_page.get_shipment()) == initial_shipping

    # 4. Add items until it's free
    for _ in range(extra_mushrooms):
        checkout_page.increase_quantity("Large Flat Mushrooms", 1)

    # 5. CHECK FINAL (The "After" state)
    # Wait until the shipping text actually changes to the final number
    WebDriverWait(driver, 10).until(
        lambda d: str(int(final_shipping)) in d.find_element(*checkout_page.SHIPMENT_VALUE).text
    )

    assert parse_price(checkout_page.get_shipment()) == final_shipping


# Test Case: Verify that free shipping cost is not kept after the Product Total drops below 20€.
# As a user of MarketMate, I can see the shipping cost is being added back when Product Total drops below 20€.

def test_shipping_reapplied_below_threshold(driver):
    home_page, _ = login_and_verify(driver, TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"])

    # Setup: Ensure cart is fresh
    checkout_page = CheckoutPage(driver) .load()
    checkout_page.clear_cart()
    driver.refresh()


    # 5-7. Shop Page & Age Verification (Today - 19 years)
    shop_page = ShopPage(driver).load()
    confirm_age(shop_page, "16-04-2007")

    # 8. Add Ginger and Large Flat Mushrooms
    shop_page.add_product("Ginger", 1)
    shop_page.add_product("Large Flat Mushrooms", 1)

    # 9. Go to cart
    checkout_page = home_page.open_cart_by_icon()

    # 10. Click + 17 times for Mushrooms (Total becomes 20.40€)
    checkout_page.increase_quantity("Large Flat Mushrooms", 17)

    # Verify Free Shipping (Step 10 outcome)
    free_shipment = checkout_page.get_shipment()
    assert parse_price(free_shipment) == 0, "Shipping should be free at 20.40€"

    # 11. Click - once for Mushrooms (Total drops to 19.30€)
    checkout_page.decrease_quantity("Large Flat Mushrooms", 1)
    WebDriverWait(driver, 10).until(
        lambda d: "5" in d.find_element(*checkout_page.SHIPMENT_VALUE).text
    )

    # 12. Verify Shipment is back to 5€
    reapplied_shipment = checkout_page.get_shipment()
    actual_shipping = parse_price(reapplied_shipment)

    assert actual_shipping == 5, f"Expected 5€ shipping below 20€, but got {actual_shipping}€"
