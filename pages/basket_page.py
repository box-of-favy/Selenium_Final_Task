from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY)
        print("Текст о том, что корзина пуста присутствует")

    def not_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        print("Товар в корзине отсутствует")



