import time
from selenium.webdriver.common.by import By

def test_product_page_has_add_to_basket_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(30)
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена на странице"