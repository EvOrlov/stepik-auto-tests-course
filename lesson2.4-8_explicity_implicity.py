from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
try:
    browser.implicitly_wait(1)
    browser.get(link)
    button = browser.find_element_by_css_selector("#book.btn")
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button.click()
    x = browser.find_element_by_css_selector("#input_value").text
    txt = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_css_selector("#answer").send_keys(txt)
    submit = browser.find_element_by_css_selector("#solve")
    submit.location_once_scrolled_into_view
    submit.click()
    print(browser.switch_to.alert.text.split()[-1])
except Exception as e:
    print(f"The traceback is: {e}")
finally:
    time.sleep(2)
    browser.quit()



