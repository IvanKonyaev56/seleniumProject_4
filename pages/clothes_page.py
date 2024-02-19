import time

from selenium.common import TimeoutException
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
    target_jacket_brand = '//*[@id="__layout"]/div/section/div[1]/div[2]/div[3]/div[1]/div[2]/div/a[2]'
    target_jacket_name = '//div[@data-cid="_1ffc323fpux"]/child::div[@title="Men\'s Puffect Quilted Full-Zip Corduroy Jacket"]'
    target_jacket_discount_price = '//*[@id="__layout"]/div/section/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span[1]'
    target_jacket_full_price = '//*[@id="__layout"]/div/section/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/span[2]'
    target_jacket = '//div[@class = "product-preview item __gglrec small-50 medium-33 xlarge-25"]'
    coat_material_button = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[8]/div[2]/div'
    material_menu = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[8]'
    sport_title = '//*[@id="__layout"]/div/section/div[1]/div[1]/div[2]/div[1]/div[11]/div'

    # Getters

    def get_word_size_title(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.word_size_title)))

    def get_material_menu(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.material_menu)))

    def get_target_jacket_brand(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.target_jacket_brand)))

    def get_target_jacket_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.target_jacket_name)))

    def get_target_jacket_discount_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.target_jacket_discount_price)))

    def get_target_jacket_full_price(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.target_jacket_full_price)))

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
        self.move_to_element(self.get_price_title())
        self.get_discount_30_radio_button().click()
        print('Discount_30_radio_button clicked')

    def input_price_from_field(self):
        self.move_to_element(self.get_shop_title())
        self.get_price_from_field().send_keys('1000')
        print('Input_price_from_field filled')

    def input_price_up_to_field(self):
        self.get_price_up_to().send_keys('15000')
        print('Input_price_up_to_field filled')

    def choose_macys_shop(self):
        time.sleep(3)  # Попробовал разные методы у геттеров, но в итоге прощё всего добавить явно через time.sleep,
        # чтобы тесты не падали. Тесты падают часто по ошибке ElementClickInterceptedException.
        # Как я понимаю из-за того, что хоть в коде локатор и есть, но нажать на него нельзя из-за "скелетона".
        self.move_to_element(self.get_brand_input_field())
        self.get_macys_shop().click()
        print('Macys_shop choose')

    def enter_brand_name(self):
        time.sleep(3)
        self.move_to_element(self.get_color_title())
        self.get_brand_input_field().send_keys('columbia')
        print('Brand_name entered')

    def choose_brand_name(self):
        self.get_colambia_brand().click()
        print('Columbia brand choose')

    def choose_blue_color(self):
        time.sleep(3)
        self.move_to_element(self.get_word_size_title())
        self.get_blue_color().click()
        print('Blue_color choose')

    def choose_size(self):
        time.sleep(3)
        self.move_to_element(self.get_ru_size_title())
        self.get_xl_size().click()
        print('XXL_size choose')

    def click_accept_button(self):
        self.get_accept_button().click()
        print('Accept_button clicked')

    def click_material_menu(self):
        time.sleep(3)
        self.move_to_element(self.get_sport_title())
        self.get_material_menu().click()
        print('Coat_material_menu clicked')

    def click_material_button(self):
        self.get_material_button().click()
        print('Coat_features_button clicked')

    def parameters_target_jacket(self):
        name_the_jacket = self.get_target_jacket_name().text
        print(name_the_jacket)
        while True:
            try:
                brand_the_jacket = self.get_target_jacket_brand().text
                print(brand_the_jacket)

                fprice_the_jacket = self.get_target_jacket_full_price().text
                fprice_the_jacket_new = fprice_the_jacket.replace('₽', '')
                fprice_the_jacket_new = int(fprice_the_jacket_new.replace(' ', ''))
                print(fprice_the_jacket_new)

                price_the_jacket = self.get_target_jacket_discount_price().text
                price_the_jacket_new = price_the_jacket.replace('₽', '')
                price_the_jacket_new = int(price_the_jacket_new.replace(' ', ''))
                print(price_the_jacket_new)
                break
            except TimeoutException:
                continue

        assert price_the_jacket_new <= 15000 and price_the_jacket_new >= 1000
        print('Цена корректна')
        assert price_the_jacket_new <= fprice_the_jacket_new * 0.7
        print('Скидка корректна')
        assert brand_the_jacket == 'COLUMBIA'
        print('Бренд корректен')

        print('Фильтры вернули корректный товар!')

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
        self.parameters_target_jacket()
        self.click_target_jacket()
        time.sleep(2) # Сюда лучше добавить проверку заголовка новой страницы. И тогда будет нужная задержка.
        self.assert_url('https://usmall.ru/product/5976292-mens-puffect-quilted-full-zip-corduroy-jacket-columbia')
