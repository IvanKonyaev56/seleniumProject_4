import time
from selenium.common import TimeoutException
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
    new_page_header = '//div[@class="p-checkout-heading"]'
    user_last_name = '//input[@name="last_name"]'
    user_first_name = '//input[@name="first_name"]'
    user_phone = '//input[@name="phone"]'
    user_email = '//input[@name="email"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_new_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_page_header)))

    def get_user_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_last_name)))

    def get_user_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_first_name)))

    def get_user_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_phone)))

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    # Actions

    def click_checkout_button(self):
        time.sleep(3)
        self.get_checkout_button().click()
        print('Checkout_button clicked')

    def assert_user_parameters(self):
        while True:
            try:
                user_last_name_text = self.get_user_last_name().get_attribute('value')
                user_first_name_text = self.get_user_first_name().get_attribute('value')
                user_phone_text = self.get_user_phone().get_attribute('value')
                user_email_text = self.get_user_email().get_attribute('value')
                break
            except TimeoutException:
                continue

        assert user_last_name_text == 'Иванов'
        assert user_first_name_text == 'Иван'
        assert user_phone_text == '+7 (996) 333-88-05'
        assert user_email_text == 'zefyecaspe@gufum.com'

        print('Указаны корректные данные пользователя!')

    # Methods

    def checkout(self):
        self.click_checkout_button()
        self.get_assert_word(self.get_new_page_header(), 'Оформление заказа')
        self.assert_url('https://usmall.ru/checkout')
        self.assert_user_parameters()
        self.get_screenshot()
