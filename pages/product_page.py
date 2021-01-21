from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = \
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def correct_item_has_been_added_to_the_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        elements = self.browser.find_elements(*ProductPageLocators.ITEM_ADDED_TO_THE_BASKET)
        item_added_to_the_basket = elements[0]
        assert item_name.text == item_added_to_the_basket.text, \
            f"Wrong item has been added to the basket - {item_added_to_the_basket.text}, \
            url - {self.browser.current_url}"

    def the_cost_of_the_basket_equals_the_item_price(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_IS_NOW).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert basket_total == item_price, \
            f"The cost of the basket - {basket_total} - is not the same as the price of the item - {item_price}, " \
            f"url - {self.browser.current_url}"




