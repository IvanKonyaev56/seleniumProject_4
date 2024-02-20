import datetime
from selenium.webdriver import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    '''Method move to element'''
    # Пришлось добавить данный метод, т.к. из-за того, что после первого выбранного фильтра появляется панель с кнопкой
    # "Применить". Из-за неё геттеры хоть и видят элемент по коду, но не могут на него кликнуть.
    # Как я понял, как раз из-за этой панели. Поэтому перед применением очередного фильтра, я перемещаюсь немного ниже.

    def move_to_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()

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
