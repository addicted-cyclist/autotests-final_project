# Проект по автоматизации тестирования интернет-магазина с помощью Selenium+Python

Ссылка на магазин: http://selenium1py.pythonanywhere.com/

Все тесты написаны с использованием паттерна **Page Object** - то есть каждая страница web-приложения описана в виде класса, в котором содержатся пользовательские методы взаимодействия со страницей (Selenium-методы взаимодействия с браузером и страницей). Для каждой страницы web-приложения выделен отдельный тест-файл, в котором описывается только логика тестового сценария (остальной код скрыт под "капотом"). 

Реализована поддержка 3 популярных браузеров: **Google Chrome**, **Opera**, **Firefox**. 

    pytest --browser_name=opera 

Для корректной работы вам нужно установить драйвер для взаимодействия с браузером: 
* https://chromedriver.chromium.org/downloads - Chrome
* https://github.com/mozilla/geckodriver/releases - Firefox
* https://github.com/operasoftware/operachromiumdriver/releases - Opera

Вы можете запустить тестирование web-страницы на **разных языках**.

    pytest --language=ru
    
В **main_page.py**, **login_page.py**, **product_page.py** описаны пользовательские методы взаимодействия с главной страницей, страницей логина-регистрации, страницей товара соответственно. В **base_page.py** описаны общие для всех страниц методы взаимодействия. 

В **test_main_page.py**, **test_login_page.py**, **test_product_page.py** содержатся тесты для главной страницы, страницы логина-регистрации, страницы товара соответственно.

Приведем код и *тестовый сценарий* для теста **"Гость может добавить товар в корзину"** из **test_product_page.py**:
1. Открыть страницу http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0
2. Добавить товар в корзину.
3. Решить капчу, которая появляется в виде alert, ввести код в поле, нажать "OK". 
4. Проверить, что в корзину был добавлен товар по ссылке из п.1
5. Проверить, что сумма корзины совпадает с ценой товара из п.1


        def test_guest_can_add_product_to_basket(self, browser):
            link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
            page = ProductPage(browser, link)
            page.open()
            page.add_to_basket()
            page.solve_quiz_and_get_code()
            page.correct_item_has_been_added_to_the_basket()
            page.the_cost_of_the_basket_equals_the_item_price()

Как мы видим, использование паттерна **Page Object** помогает сделать код похожим на тестовый сценарий на английском языке. 

Все локаторы для поиска web-элементов находятся в **locators.py**, что помогает легко править их в одном месте при изменении верстки страниц. 

