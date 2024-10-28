from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def product_addition_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDITION_MESSAGE)
        print("Сообщение о добавлении в корзину есть")

    def price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE)
        print("Сообщение о цене товара есть")

    def product_name_is_correct(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_message == product_name
        print("Наименование товара корректно")

    def price_name_is_correct(self):
        price_name_in_message = self.browser.find_element(*ProductPageLocators.PRICE_NAME_IN_MESSAGE).text
        price_name = self.browser.find_element(*ProductPageLocators.PRICE_NAME).text
        assert price_name_in_message == price_name
        print("Цена товара корректна")

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.PRODUCT_ADDITION_MESSAGE)
        print("Сообщение о добавлении в корзину есть, но не должно быть")

    def is_disappeared_success_message(self):
        assert not self.is_disappeared(*ProductPageLocators.PRODUCT_ADDITION_MESSAGE)
        print("Сообщение о добавлении в корзину есть, должно уйти со временем, но отображается")