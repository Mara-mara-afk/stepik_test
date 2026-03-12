from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR,'input.first[required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR,'input.second[required]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
    input3.send_keys("test@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()