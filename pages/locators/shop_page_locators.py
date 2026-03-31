from selenium.webdriver.common.by import By


class ShopPageLocators:
    # --- AGE VERIFICATION ---
    AGE_VERIFICATION_INPUT = (By.XPATH, "//div[@class='modal-content']/input[@type='text']")
    AGE_VERIFICATION_CONFIRM_BUTTON = (By.XPATH, "//div[@class='modal-content']//button[text()='Confirm']")
    AGE_VERIFICATION_TEXT = (By.XPATH, "//div[@class='modal-content']//p")
    UNDERAGE_NOTICE = (By.XPATH, "//div[@class='card-body']/p")

    # --- MESSAGES ---
    CONFIRMATION_MSG = (By.XPATH, "//div[@role='status']")
    ERROR_MSG = (By.XPATH, "//div[@role='status']")

    # --- PRODUCTS ---
    FIRST_PRODUCT_NAME = (By.XPATH, "//p[@class='lead']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")

    # --- COMMENTS ---
    COMMENT_TEXT = (By.XPATH, "//p[@class='comment-text']")

    # --- PAGINATION ---
    NEXT_PAGE_BUTTON = (By.XPATH, "//button[contains(text(),'Next')]")

    # --- RATINGS / COMMENTS ---
    COMMENT_TEXT_AREA = (By.XPATH, "//textarea[@id='comment']")
    SEND_RATING_BUTTON = (By.XPATH, "//button[text()='Send']")
    DELETE_RATING_BUTTON = (By.XPATH, "//button[text()='Delete']")
    RATING_STARS = "//i[contains(@class,'fa-star')][{}]"
    RATING_RESTRICTION = (By.XPATH, "//div[@class='rating-restriction']")
    RATING_USER = (By.XPATH, "//span[@class='rating-user']")
    CUSTOM_RATING = (By.XPATH, "//i[contains(@class,'fa-star')]")
    COMMENT_TEXT = (By.XPATH, "//p[@class='comment-text']")

    # --- RATINGS / COMMENTS ---
    COMMENT_TEXT_AREA = (By.XPATH, "//textarea[@id='comment']")
    SEND_RATING_BUTTON = (By.XPATH, "//button[text()='Send']")
    DELETE_RATING_BUTTON = (By.XPATH, "//button[text()='Delete']")
    RATING_STARS = "//i[contains(@class,'fa-star')][{}]"
    RATING_RESTRICTION = (By.XPATH, "//div[@class='rating-restriction']")
    RATING_USER = (By.XPATH, "//span[@class='rating-user']")
    CUSTOM_RATING = (By.XPATH, "//i[contains(@class,'fa-star')]")
    COMMENT_TEXT = (By.XPATH, "//p[@class='comment-text']")