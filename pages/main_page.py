from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):
    url = 'https://leroymerlin.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    auth_button = '//button[@data-qa="auth-button"]'

    # Getters

    def get_auth_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.auth_button)))

    # Actions

    def click_auth_button(self):
        self.get_auth_button().click()
        print('Auth_button click')

    # Methods

    def go_to_auth_page(self):
        self.driver.get(self.url)
