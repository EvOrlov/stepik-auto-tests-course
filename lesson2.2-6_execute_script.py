import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = math.log(abs(12 * math.sin(int(x_element.text))))

    browser.find_element_by_xpath("//input[@id='answer']").send_keys(str(x))

    elements = ["//input[@id='robotCheckbox']", "//input[@id='robotsRule']", "//button[text()=\"Submit\"]"]
    for element in elements:
        item = browser.find_element_by_xpath(element)
        item.location_once_scrolled_into_view
        item.click()
    time.sleep(3)
    print(browser.switch_to.alert.text)

finally:
    time.sleep(1)
    browser.quit()