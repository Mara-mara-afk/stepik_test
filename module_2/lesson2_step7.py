import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    wait = WebDriverWait(browser, 10)
    browser.get(link)

    # Заполняем поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivanpetrov@mail.ru")

    # 📁 Создаём txt-файл автоматически
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "w") as file:
        file.write("")

    # Загружаем файл
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждём алерт
    alert = wait.until(EC.alert_is_present())
    print(alert.text)
    alert.accept()
