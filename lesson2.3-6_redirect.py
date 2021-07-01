import  math
from selenium import  webdriver
import time


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    time.sleep(2)
    browser.find_element_by_css_selector("button.trollface").click()
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("span#input_value").text
    txt = str(math.log(abs(12*math.sin(int(x)))))
    input2 = browser.find_element_by_css_selector("input#answer").send_keys(txt)
    input3 = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    time.sleep(2)
    alert_text = browser.switch_to.alert.text.split()[-1]
    print(alert_text)

finally:
    time.sleep(2)
    browser.quit()
