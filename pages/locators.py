from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, """//*[@id="default"]/header/div[1]/div/div[2]/span/a""")
    BASKET_NOT_EMPTY = (By.XPATH, """//*[@class="col-sm-6 h3"]""")
    EMPTY_BASKET_TEXT = (By.XPATH, """//*[@id="content_inner"]""")
    USER_ICON = (By.XPATH, """//*[@class="icon-user"]""")


#class MainPageLocators:



class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER = (By.XPATH, """//*[@name="registration-email"]""")
    PASSWORD_REGISTER = (By.XPATH, """//*[@name="registration-password1"]""")
    PASSWORD_CONFIRMATION_REGISTER = (By.XPATH, """//*[@name="registration-password2"]""")
    REGISTER_BUTTON = (By.XPATH, """//*[@name="registration_submit"]""")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ITEM_NAME = (By.XPATH, """//*[@class="col-sm-6 product_main"]/h1""")
    BASKET_TOTAL_IS_NOW = (By.XPATH, """//*[@id="messages"]/div[3]/div/p/strong""")
    ITEM_PRICE = (By.XPATH, """//*/p[@class="price_color"]""")
    ITEM_ADDED_TO_THE_BASKET = (By.XPATH, """//*[@class="alert alert-safe alert-noicon alert-success  fade in"]/div/strong""")
    SUCCESS_MESSAGE = (By.XPATH, """//*[@class="alert alert-safe alert-noicon alert-success  fade in"]/div""")
