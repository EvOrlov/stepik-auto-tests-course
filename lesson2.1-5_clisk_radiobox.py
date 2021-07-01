from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("h2 > #treasure")
    x = input1.get_attribute("valuex")
    txt = calc(x)
    s_txt = browser.find_element_by_css_selector("#answer[type='text']")
    s_txt.send_keys(txt)
    input2 = browser.find_element_by_css_selector("input.check-input#robotCheckbox")
    input2.click()
    input3 = browser.find_element_by_css_selector(" input.check-input#robotsRule")
    input3.click()

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
     #успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла