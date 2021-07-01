from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("form > h2 > span#num1").text
    input2 = browser.find_element_by_css_selector("form > h2 > span#num2").text
    txt = int(input1) + int(input2)
    spisok = browser.find_element_by_css_selector("select#dropdown.custom-select").click()
    spisok2 = browser.find_element_by_css_selector(f"select#dropdown.custom-select option[value='{txt}']").click()
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
