import time
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    auth_button = '//button[@class="c-header__btn __i-guest"]'
    username = '//input[@name="email"]'
    password = '//input[@name="password"]'
    login_button = '//button[@class="__btn-submit __shadow"]'
    popup_body = '//div[@class="popmechanic-js-wrapper"]'
    popup_close_button = '//div[@class="popmechanic-close"]'
    men_header = '//a[contains(text(), "Мужчины")]'
    men_jacket = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/a[2]'
    cookie_banner_button = '//button[@data-btn="minor"]'
    new_page_header = '//*[@id="__layout"]/div/section/div[1]/div[2]/h1'

    # Getters

    def get_auth_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.auth_button)))

    def get_user_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_popup_close_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_close_button)))

    def get_popup_body(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_body)))

    def get_men_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.men_header)))

    def get_men_jacket_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.men_jacket)))

    def get_cookie_banner_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_banner_button)))

    def get_new_page_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_page_header)))

    # Actions

    def click_auth_button(self):
        self.get_auth_button().click()
        print('Auth_button click')

    def fill_in_the_user_name_field(self):
        self.get_user_name_field().send_keys('zefyecaspe@gufum.com')
        print('User_name_field filled')

    def fill_in_the_password_field(self):
        self.get_password_field().send_keys('marvel56')
        print('Password_field filled')

    def click_login_button(self):
        self.get_login_button().click()
        print('Login_button clicked')

    def click_popup_close_button(self):
        # Пришлось добавить цикл, т.к. часто клик происходил "успешно", но окно не закрывалось.
        while True:
            try:
                self.get_popup_body()
                time.sleep(1)
                self.get_popup_close_button().click()
                print('Popup_close button clicked')
                break
            except TimeoutException:
                continue
            except ElementClickInterceptedException:
                continue

    def move_to_men_header(self):
        self.move_to_element(self.get_men_header())
        print('Move to men_header')

    def click_men_jacket_header(self):
        self.get_men_jacket_header().click()
        print('Men_jacket_header clicked')

    def click_cookie_banner_button(self):
        self.get_cookie_banner_button().click()
        print('Cookie_banner_button clicked')

    # Methods

    def authorisation(self):
        self.click_auth_button()
        self.fill_in_the_user_name_field()
        self.fill_in_the_password_field()
        self.click_login_button()
        self.click_popup_close_button()
        self.click_cookie_banner_button()

    def go_to_clothes_page(self):
        self.move_to_men_header()
        self.click_men_jacket_header()
        self.get_assert_word(self.get_new_page_header(), 'Мужские пуховики')
        self.assert_url('https://usmall.ru/products/men/clothes/down-insulated-coats')
