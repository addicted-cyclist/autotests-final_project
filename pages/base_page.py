import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        prompt = self.browser.switch_to.alert
        x = prompt.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        prompt.send_keys(answer)
        prompt.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        ### в течение 4 секунд ждем появления элемента на странице
        ### если элемент обнаружен, возвращаем False
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        ### в течение 4 секунд ждем исчезновения элемента на странице
        ### если элемент все еще присутствует по истечении 4 с., возвращаем False
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


