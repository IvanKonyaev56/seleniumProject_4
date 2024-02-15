import time

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common import actions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):
    url = 'https://usmall.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    auth_button = '//button[@class="c-header__btn __i-guest"]'
    username = '//input[@name="email"]'
    password = '//input[@name="password"]'
    login_button = '//button[@class="__btn-submit __shadow"]'
    popup_close_button = '//div[@class="popmechanic-close"]'
    men_header = '//a[contains(text(), "Мужчины")]'
    men_jacket = '/html/body/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/a[2]'
    cookie_banner_button = '//button[@data-btn="minor"]'
    discount_30_radio_button = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[4]'
    discount_80_radio_button = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[7]'
    price_from = '//input[@class="textfield"][1]'
    price_up_to = '//input[@class="textfield"][2]'
    macys_shop = '//div[@class="ui-filters__facet-list __market"]/child::div[@data-id="4"]'
    brand_input_field = '//div[@class="ui-filters__facet __brand"]/descendant::input[@class="searchfield"]'
    columbia_brand = '//div[@data-id="273"]'
    blue_color = '//div[@data-id="22866"]'
    xxl_size = '//div[@data-id="79"]'
    care_method = '//div[@data-id="79"]'

    # Getters

    def get_auth_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.auth_button)))

    def get_user_name_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_popup_close_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.popup_close_button)))

    def get_men_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.men_header)))

    def get_men_jacket_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.men_jacket)))

    def get_cookie_banner_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_banner_button)))

    def get_discount_30_radio_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_30_radio_button)))

    def get_discount_80_radio_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_80_radio_button)))

    def get_price_from_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_up_to(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_up_to)))

    def get_macys_shop(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.macys_shop)))

    def get_brand_input_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_input_field)))

    def get_colambia_brand(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.columbia_brand)))

    def get_blue_color(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.blue_color)))

    def get_xxl_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xxl_size)))

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
        time.sleep(1)
        self.get_popup_close_button().click()
        print('Popup_close button clicked')

    def move_to_men_header(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_men_header()).perform()
        print('Move to men_header')

    def click_men_jacket_header(self):
        self.get_men_jacket_header().click()
        print('Men_jacket_header clicked')

    def click_cookie_banner_button(self):
        self.get_cookie_banner_button().click()
        print('Cookie_banner_button clicked')

    def click_discount_30_radio_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_discount_80_radio_button()).perform()
        self.get_discount_30_radio_button().click()
        print('Discount_30_radio_button clicked')

    def input_price_from_field(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_price_from_field()).perform()
        self.get_price_from_field().send_keys('1000')
        print('Input_price_from_field clicked')

    def input_price_up_to_field(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_price_up_to()).perform()
        self.get_price_up_to().send_keys('15000')
        print('Input_price_up_to_field clicked')

    def choose_macys_shop(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_brand_input_field()).perform()
        self.get_macys_shop().click()
        print('Macys_shop clicked')

    def enter_brand_name(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_blue_color()).perform()
        self.get_brand_input_field().send_keys('columbia')
        print('Brand_name entered')

    def choose_brand_name(self):
        self.get_colambia_brand().click()
        print('Columbia brand choose')

    def choose_blue_color(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_xxl_size()).perform()
        self.get_blue_color().click()
        print('Blue_color choose')

    def choose_size(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_xxl_size()).perform()
        self.get_xxl_size().click()
        print('XXL_size choose')

    # Methods

    def authorisation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_auth_button()
        self.fill_in_the_user_name_field()
        self.fill_in_the_password_field()
        self.click_login_button()
        self.get_current_url()
        self.click_popup_close_button()
        self.click_cookie_banner_button()

    def get_coats_page(self):
        pass

    def search_the_mens_jacket(self):
        self.move_to_men_header()
        self.click_men_jacket_header()
        self.click_discount_30_radio_button()
        self.input_price_from_field()
        self.input_price_up_to_field()
        self.choose_macys_shop()
        self.enter_brand_name()
        self.choose_brand_name()
        self.choose_blue_color()
        self.choose_size()

