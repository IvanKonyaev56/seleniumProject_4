import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = '//button[@class = "__shadow"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions

    def click_checkout_button(self):
        time.sleep(3)
        self.get_checkout_button().click()
        print('Checkout_button clicked')
        # Добавить проверу что введены корректные данные пользователя и сумма

    # Methods

    def checkout(self):
        self.click_checkout_button()
        # self.assert_url('https://usmall.ru/checkout')
