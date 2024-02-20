from selenium.common import TimeoutException
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
    new_page_header = '//*[@id="__layout"]/div/section/div/div/div[1]/div[1]/div[1]'
    target_jacket_name = '//div[@class = "p-basket-item__name"]'
    target_jacket_discount_price = '//div[@class = "p-basket-item__price"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_new_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_page_header)))

    def get_target_jacket_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.target_jacket_name)))

    def get_target_jacket_discount_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.target_jacket_discount_price)))

    # Actions

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Cart_button clicked')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Checkout_button clicked')

    def assert_parameters_target_jacket(self):
        while True:
            try:
                price_the_jacket = self.get_target_jacket_discount_price().text
                price_the_jacket_new = price_the_jacket.replace('₽', '')
                price_the_jacket_new = int(price_the_jacket_new.replace(' ', ''))
                break
            except TimeoutException:
                continue

        assert price_the_jacket_new == 14230

        print('В корзине корректный товар!')

    # Methods

    def checkout_to_basket(self):
        self.click_cart_button()
        self.click_checkout_button()
        self.get_assert_word(self.get_new_page_header(), 'Корзина')
        self.assert_url('https://usmall.ru/basket')
        self.get_assert_word(self.get_target_jacket_name(), 'Men\'s Puffect Quilted Full-Zip Corduroy Jacket')
        self.assert_parameters_target_jacket()

