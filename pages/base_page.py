import math
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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

