import  math
from selenium import  webdriver
import time


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    input1 = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(2)
    x = browser.find_element_by_css_selector("span.nowrap#input_value").text
    txt = str(math.log(abs(12*math.sin(int(x)))))
    input2 = browser.find_element_by_css_selector("input#answer").send_keys(txt)
    input3 = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    time.sleep(2)
    alert_text = browser.switch_to.alert.text.split()[-1]
    print(alert_text)

finally:
    time.sleep(2)
    browser.quit()
