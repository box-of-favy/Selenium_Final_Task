from .base_page import BasePage
from .locators import LoginPageLocators
import time 

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
        
    def register_new_user(self, email, password):
        reg_field_email = self.browser.find_element(*LoginPageLocators.REG_FIELD_EMAIL)
        reg_field_email.send_keys(email)
        reg_field_password_1 = self.browser.find_element(*LoginPageLocators.REG_FIELD_PASSWORD_1)
        reg_field_password_1.send_keys(password)
        reg_field_password_2 = self.browser.find_element(*LoginPageLocators.REG_FIELD_PASSWORD_2)
        reg_field_password_2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
        