import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

class ProductPage(BasePage):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BTN).click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message_with_product_name(self, expected_name):
        message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert expected_name in message, f"Expected '{expected_name}' in message, got '{message}'"

    def should_be_basket_total_equal_product_price(self, expected_price):
        total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert total == expected_price, f"Expected basket total '{expected_price}', got '{total}'"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()

    page.should_be_success_message_with_product_name(product_name)
    page.should_be_basket_total_equal_product_price(product_price)