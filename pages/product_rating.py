from selenium.webdriver.common.by import By
# --- RATING SYSTEM ---
COMMENT_INPUT = (By.XPATH, "//textarea[@class = 'new-review-form-control ']")
SEND_RATING_BUTTON = (By.XPATH, "//button[@class = 'new-review-btn new-review-btn-send']")
COMMENT_OPTIONS = (By.XPATH, "//div[@class = 'menu-icon']")
COMMENT_TEXT = (By.XPATH, "//div[@class = 'comment'][1]/div[@class = 'comment-body']//p")
EDIT_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[1]")
DELETE_COMMENT = (By.XPATH, "//div[@class = 'dropdown-menu']/button[2]")
RATING_RESTRICTION = (By.XPATH, "//div[@class = 'reviewRestriction']/p")
RATING_USER = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'comment-header']//strong")
CUSTOM_RATING = (By.XPATH, "//div[@class = 'comment'][1]//div[@class = 'custom-rating']/span[@class = 'star full']")
RATING_STARS = {
    "1": (By.XPATH, "//div[@class = 'interactive-rating']/span[1]"),
    "2": (By.XPATH, "//div[@class = 'interactive-rating']/span[2]"),
    "3": (By.XPATH, "//div[@class = 'interactive-rating']/span[3]"),
    "4": (By.XPATH, "//div[@class = 'interactive-rating']/span[4]"),
    "5": (By.XPATH, "//div[@class = 'interactive-rating']/span[5]")
}