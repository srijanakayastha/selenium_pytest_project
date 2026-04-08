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
    AGE_VERIFICATION_SUCCESS_ALERT = "You are of age. You can now view all products, even alcohol products."
    AGE_VERIFICATION_FAIL_ALERT = "You are underage. You can still browse the site, but you will not be able to view alcohol products."
    UNDERAGE_NOTICE_TEXT = "You are underage and cannot view alcohol products. Please wait until you are 18 or older to access these products."
    LOGIN_ERROR_MESSAGE = "Invalid username or password"
    ITEM_ADDED_MESSAGE = "Item added to cart!"
    ALREADY_REVIEWED_MESSAGE = "You have already reviewed this product."
    ITEM_NOT_YET_BOUGHT_MESSAGE = "You need to buy this product to tell us your opinion!"
    LOGGED_OUT_MESSAGE = "Logged out successfully."
    RATING = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5
    }