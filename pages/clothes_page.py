import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class ClothesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    discount_30_radio_button = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[4]'
    price_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div/div[3]/div[1]/span'
    price_from = '//input[@class="textfield"][1]'
    price_up_to = '//input[@class="textfield"][2]'
    shop_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div/div[4]/div[1]/span'
    macys_shop = '//div[@class="ui-filters__facet-list __market"]/child::div[@data-id="4"]'
    brand_input_field = '//div[@class="ui-filters__facet __brand"]/descendant::input[@class="searchfield"]'
    columbia_brand = '//div[@data-id="273"]'
    blue_color = '//div[@data-id="22866"]'
    xl_size = '//div[@data-id="77"]'
    color_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]'
    ru_size_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[8]/div[1]/span'
    word_size_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[6]'
    accept_button = '//button[@class="ui-filters__submit-btn"]'
    target_jacket = '//div[@class = "product-preview item __gglrec small-50 medium-33 xlarge-25"]'
    coat_material_button = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/div'
    material_menu = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[8]'
    sport_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[11]/div'

    # Getters

    def get_word_size_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.word_size_title)))

    def get_material_menu(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.material_menu)))

    def get_target_jacket(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.target_jacket)))

    def get_accept_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.accept_button)))

    def get_ru_size_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.ru_size_title)))

    def get_color_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.color_title)))

    def get_discount_30_radio_button(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_30_radio_button)))

    def get_price_title(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.price_title)))

    def get_shop_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.shop_title)))

    def get_price_from_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_up_to(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.price_up_to)))

    def get_macys_shop(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.macys_shop)))

    def get_brand_input_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.brand_input_field)))

    def get_colambia_brand(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.columbia_brand)))

    def get_blue_color(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.blue_color)))

    def get_xl_size(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.xl_size)))

    def get_sport_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.sport_title)))

    def get_material_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.coat_material_button)))

    # Actions

    def click_discount_30_radio_button(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_price_title()).perform()
        self.get_discount_30_radio_button().click()
        print('Discount_30_radio_button clicked')

    def input_price_from_field(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_shop_title()).perform()
        self.get_price_from_field().send_keys('1000')
        print('Input_price_from_field filled')

    def input_price_up_to_field(self):
        self.get_price_up_to().send_keys('15000')
        print('Input_price_up_to_field filled')

    def choose_macys_shop(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_brand_input_field()).perform()
        self.get_macys_shop().click()
        print('Macys_shop choose')

    def enter_brand_name(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_color_title()).perform()
        self.get_brand_input_field().send_keys('columbia')
        print('Brand_name entered')

    def choose_brand_name(self):
        self.get_colambia_brand().click()
        print('Columbia brand choose')

    def choose_blue_color(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_word_size_title()).perform()
        self.get_blue_color().click()
        print('Blue_color choose')

    def choose_size(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_ru_size_title()).perform()
        self.get_xl_size().click()
        print('XXL_size choose')

    def click_accept_button(self):
        self.get_accept_button().click()
        print('Accept_button clicked')

    def click_material_menu(self):
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_sport_title()).perform()
        self.get_material_menu().click()
        print('Coat_material_menu clicked')

    def click_material_button(self):
        self.get_material_button().click()
        print('Coat_features_button clicked')

    def click_target_jacket(self):
        self.get_target_jacket().click()
        print('Target_jacket clicked')
        # Добавить проверки того что было в фильтрах и того что есть в выбранной куртке.

    # Methods

    def search_the_jacket(self):
        self.click_discount_30_radio_button()
        self.input_price_from_field()
        self.input_price_up_to_field()
        self.choose_macys_shop()
        self.enter_brand_name()
        self.choose_brand_name()
        self.choose_blue_color()
        self.choose_size()
        self.click_accept_button()
        self.click_material_menu()
        self.click_material_button()
        self.click_accept_button()
        self.click_target_jacket()
