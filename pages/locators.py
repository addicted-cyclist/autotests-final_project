from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, \
                     "//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ITEM_NAME = (By.XPATH, \
                               """//*[@class="col-sm-6 product_main"]/h1""")
    BASKET_TOTAL_IS_NOW = (By.XPATH, \
                           """//*[@id="messages"]/div[3]/div/p/strong""")
    ITEM_PRICE = (By.XPATH, \
                  """//*/p[@class="price_color"]""")
    ITEM_ADDED_TO_THE_BASKET = (By.XPATH, \
                               """//*[@class="alert alert-safe alert-noicon alert-success  fade in"]/div/strong""")


