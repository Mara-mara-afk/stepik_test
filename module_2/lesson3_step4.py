from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
     
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    option1.click()

    alert = browser.switch_to.alert
    alert.accept()
            
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
