import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname").send_keys('Ivan')
    input2 = browser.find_element_by_name("lastname").send_keys('Ivanov')
    input3 = browser.find_element_by_name("email").send_keys('mail@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)
    input4 = browser.find_element_by_name("file").send_keys(file_path)

    button = browser.find_element_by_tag_name("button").click()
    time.sleep(3)
    print(browser.switch_to.alert.text)

finally:
    time.sleep(1)
    browser.quit()
