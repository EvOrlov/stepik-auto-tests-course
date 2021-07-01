from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'

class MixSelenium:

    def __init__(self, link):
        self.link = link
        self.br = webdriver.Chrome()
        self.start_test_page()


    def start_test_page(self):
        """Старт теста"""
        try:
            self.br.get(self.link)
            self.actions(self.br)
        finally:
            self.time_out(10)
            self.br.quit()
            print("Test confirm!")

    @staticmethod
    def actions(br):
        one = br.find_element_by_css_selector("#num1").text
        two = br.find_element_by_css_selector("#num2").text
        i = int(one) + int(two)
        select = Select(br.find_element_by_tag_name("select"))
        select.select_by_value(f"{i}")
        br.find_element_by_css_selector('.btn.btn-default').click()

    @staticmethod
    def time_out(a):
        return sleep(a)


if __name__ == '__main__':
    MixSelenium(link)
    MixSelenium(link2)