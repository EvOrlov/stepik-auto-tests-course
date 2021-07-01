from selenium import webdriver
import time
import unittest

# объявляем переменные
LINKS = ["https://suninjuly.github.io/registration1.html",
         'http://suninjuly.github.io/registration2.html']

PERSONAL_INFORMATION = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@eg.net',
    'phone': '111-111-111',
    'adress': 'Dull State 5'
}

SELECTORS = {

    'first_name': ['first', 'first'],
    'last_name': ['first', 'second'],
    'email': ['first', 'third'],
    'phone': ['second', 'first'],
    'adress': ['second', 'second']
}

SELECTORS_TEMPLATE = '.{}_block .{}'


def get_result(url):
    with webdriver.Chrome() as browser:
        browser.get(url=url)

        # Заполняем поля ввода
        for key, selector in SELECTORS.items():
            inputx = browser.find_element_by_css_selector(
                SELECTORS_TEMPLATE.format(*selector))
            inputx.send_keys(PERSONAL_INFORMATION.get(key))

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        return browser.find_element_by_tag_name("h1").text


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        cases = LINKS
        with self.subTest():
            for case in cases:
                welcome_text = get_result(case)
                self.assertEqual(
                    welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()