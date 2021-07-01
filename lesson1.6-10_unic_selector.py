from selenium import webdriver
import time

# Я счел, что указание старшего родителя(first_block) для искомого поля - необходимое и достаточное условие,
# чтобы уникально его идентифицировать, не используя Xpath и текст сообщения
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block .first_class input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second_class input.second")
    input2.send_keys("Stogov")
    input3 = browser.find_element_by_css_selector(".first_block .third_class input.third")
    input3.send_keys("mail@mail.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
