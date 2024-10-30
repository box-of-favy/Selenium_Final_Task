from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FIELD_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REG_FIELD_PASSWORD_1 = (By.XPATH, "//input[@name='registration-password1']")
    REG_FIELD_PASSWORD_2 = (By.XPATH, "//input[@name='registration-password2']")
    REG_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_ADDITION_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")
    PRICE_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRICE_NAME_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRICE_NAME = (By.XPATH, "//p[@class='price_color']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")

class BasketPageLocators():
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")