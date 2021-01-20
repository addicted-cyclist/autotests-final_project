from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
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
            self.browser.find_element(*MainPageLocators.LOGIN_LINK)
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

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
