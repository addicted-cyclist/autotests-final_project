from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = \
            self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        login_url = self.browser.current_url
        assert "accounts/login/" in login_url, \
            f"Login link {login_url} do not contains 'accounts/login/'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form does not exist"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form does not exist"

    def register_new_user(self, email, password):
        login_link = \
            self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_REGISTER).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()



