import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_button = '//button[@class = "p-product__btn-submit"]'
    checkout_button = '//a[@class = "__shadow"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Cart_button clicked')
        # Добавить проверу что появился попап с предложением перехода в корзину и информацией что товар добавлен

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Checkout_button clicked')
        # Добавить проверу что произошёл переход в корзину и что там нужный нам товар

    # Methods

    def checkout_to_basket(self):
        self.click_cart_button()
        self.click_checkout_button()
        # self.assert_url('https://usmall.ru/basket')
