import pytest
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from utils.config import Config
import time
from utils.test_data import COMMENT, TEST_VALID_USER_1

# Products to test (must match alt attributes exactly)
PRODUCTS_TO_TEST = [
    {"name": "Celery", "quantity": 5}
     # {"name": "Loose Pears", "quantity": 3},
     # {"name": "Cherries", "quantity": 2},
]

@pytest.mark.parametrize("product", PRODUCTS_TO_TEST, ids=[p["name"] for p in PRODUCTS_TO_TEST])
def test_rate_product(driver, product):
    product_name = product["name"]
    quantity = product["quantity"]

    # --- LOGIN ---
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(TEST_VALID_USER_1["email"], TEST_VALID_USER_1["password"])
    login_page.screenshot(f"after_login_{product_name}")

    # --- SHOP PAGE & AGE MODAL ---
    shop_page = ShopPage(driver)
    shop_page.load()
    shop_page.enter_date_age_modal("25-03-1987").confirm_age_modal()


    # --- ADD TO CART ---
    shop_page.add_product_to_cart(product_name, quantity=quantity)
    shop_page.screenshot(f"after_add_to_cart_{product_name}")
    time.sleep(5)



    # # --- ASSERTIONS ---
    # assert shop_page.get_rating_restriction_text() == Config.ALREADY_REVIEWED_MESSAGE, \
    #     f"Rating restriction message mismatch for {product_name}"
    # assert shop_page.get_rating_user() == TEST_VALID_USER_1["username"], \
    #     f"Rating user mismatch for {product_name}"
    # assert shop_page.get_rating() == Config.RATING["4"], \
    #     f"Rating stars count mismatch for {product_name}"
    #
    # # --- CLEANUP ---
    # shop_page.delete_rating()
    # shop_page.screenshot(f"after_delete_rating_{product_name}")