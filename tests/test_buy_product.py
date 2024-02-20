import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.basket_page import BasketPage
from pages.clothes_page import ClothesPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_buy_product():
    """Аннотация к проекту"""
    # Привет, Алекс!
    # Сразу скажу слова благодарности. Спасибо тебе за твой курс! Он для меня уже не первый.
    # Что именно писать в аннотации я не понял и в описании задания не было.
    # Поэтому постараюсь написать, что счёл нужным.
    # В данном проекте я проходил путь заказа куртки в магазине usmall.ru
    # Местами добавил asserts и свои собственные проверочные функции.
    # В методе assert_parameters_target_jacket класса ClothesPage оставил вопрос.
    # Если будет время, пожалуйста, посмотри.
    # Также, местами оставил комментарии, почему сделал именно так.
    # К сожалению, тест не совсем стабильный. Бывают ложные срабатывания.
    # Но я старался себя проявить.
    # С уважением, твой студент Иван.

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('E:\\1_QAA\\stepick\\resourses\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    url = 'https://usmall.ru/'
    driver.get(url)
    driver.maximize_window()

    print('*** Start Test ***')

    mp = MainPage(driver)
    mp.authorisation()
    mp.go_to_clothes_page()

    cp = ClothesPage(driver)
    cp.search_the_jacket()

    pp = ProductPage(driver)
    pp.checkout_to_basket()

    bp = BasketPage(driver)
    bp.checkout()
