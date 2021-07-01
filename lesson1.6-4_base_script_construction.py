from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    time.sleep(2)
    button.click()
    time.sleep(2)
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
