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


    # --- SHOP PAGE & AGE MODAL ---
    shop_page = ShopPage(driver)
    shop_page.load()
    shop_page.enter_date_age_modal("25-03-1987").confirm_age_modal()


    # --- ADD TO CART ---
    shop_page.add_product_to_cart(product_name, quantity=quantity)

    # Wait to observe result (optional for debugging)
    time.sleep(5)





