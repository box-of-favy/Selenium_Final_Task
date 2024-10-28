from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert True, "Ссылка на адрес корректна"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "Форма логина есть"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        login_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert True, "Форма регистрации есть"
        