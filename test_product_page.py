import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.basket_guest
class TestGuestBasketFromProductPage:

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.correct_item_has_been_added_to_the_basket()
        page.the_cost_of_the_basket_equals_the_item_price()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-kicked-the-hornets-nest_199/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket()
        page.should_not_be_items_in_the_basket()
        page.should_be_text_your_basket_is_empty()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-kicked-the-hornets-nest_199/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.success_message_should_disappear()


@pytest.mark.basket_user
class TestUserBasketFromProductPage:
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.correct_item_has_been_added_to_the_basket()
        page.the_cost_of_the_basket_equals_the_item_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@gmail.com"
        password = str(time.time())
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        yield browser


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
