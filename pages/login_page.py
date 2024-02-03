from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    username = '//input[@id="username"]'
    password = '//input[@id="password"]'
    login_button = '//button[@id="kc-login"]'

    # Getters

    def get_user_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions

    def fill_in_the_user_name_field(self):
        self.get_user_name_field().send_keys('xqcthlh537@1secmail.ru')
        print('User_name_field filled')

    def fill_in_the_password_field(self):
        self.get_password_field().send_keys('marvel56')
        print('Password_field filled')

    def click_login_button(self):
        self.get_login_button().click()
        print('Login_button clicked')

    # Methods

    def authorisation(self):
        self.fill_in_the_user_name_field()
        self.fill_in_the_password_field()
        self.click_login_button()
        self.get_current_url()
