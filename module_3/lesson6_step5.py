import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN = "DanteCrifir5@gmail.com"
PASSWORD = "Smb159357258456"

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

fragments = []

try:
    # --- Авторизация ---
    driver.get("https://stepik.org/catalog")
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    login_button.click()
    time.sleep(1)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    password_input = driver.find_element(By.NAME, "password")
    email_input.send_keys(LOGIN)
    password_input.send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    # --- Проходим все задания ---
    for link in links:
        driver.get(link)
        time.sleep(1)

        # Попробуем найти textarea на странице
        try:
            textarea = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
            )
        except:
            # Если не найдено, проверяем iframe
            try:
                iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
                driver.switch_to.frame(iframe)
                textarea = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
                )
            except:
                print(f"[{link}] Не удалось найти поле для ввода.")
                driver.switch_to.default_content()
                continue

        textarea.clear()
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.submit-submission")
        submit_button.click()

        feedback = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )
        feedback_text = feedback.text

        if feedback_text != "Correct!":
            fragments.append(feedback_text)

        print(f"[{link}] Feedback: {feedback_text}")
        time.sleep(1)
        driver.switch_to.default_content()

finally:
    driver.quit()

if fragments:
    message = "".join(fragments)
    print("\n=== Собранное послание от инопланетян ===")
    print(message)
else:
    print("\nВсе задания прошли без ошибок — послание не найдено.")