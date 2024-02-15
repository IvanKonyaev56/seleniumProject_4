import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver


    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current URL ' + get_url)

    '''Method assert word'''

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    '''Method Screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('E:\\1_QAA\\stepick\\seleniumProject_4\\screen\\' + name_screenshot)

    '''Method assert URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value URL')
