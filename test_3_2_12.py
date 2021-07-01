import unittest
from selenium import webdriver
import time

def fill_form(url):
    with webdriver.Chrome() as browser:
        browser.get(url)
        browser.implicitly_wait(5)
        browser.find_element_by_css_selector(".first_block .first_class input.first").send_keys("John")
        browser.find_element_by_css_selector(".first_block .second_class input.second").send_keys("Doe")
        browser.find_element_by_css_selector(".first_block .third_class input.third").send_keys("mail@mail.ru")
        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        return browser.find_element_by_tag_name("h1").text


class TestsPages(unittest.TestCase):
    def test_page1(self):
        welcome_text = fill_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Not registered!")

    def test_page2(self):
        welcome_text = fill_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Not registered!")


if __name__ == "__main__":
    unittest.main()