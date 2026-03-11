import datetime

class Config:
    HOME_PAGE_URL = "https://grocerymate.masterschool.com/"
    AUTH_URL = HOME_PAGE_URL + "auth"
    SHOP_PAGE_URL = HOME_PAGE_URL + "store"
    CHECKOUT_PAGE_URL = HOME_PAGE_URL + "checkout"
    DEFAULT_TIMEOUT = 10
    ALL_CATEGORY = 1  # All, by default
    ITEM_QUANTITY = 5
    AGE_20 = datetime.datetime.today().replace(year=datetime.datetime.today().year - 20).strftime("%d-%m-%Y")