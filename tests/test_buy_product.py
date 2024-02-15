import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.basket_page import BasketPage
from pages.clothes_page import ClothesPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('E:\\1_QAA\\stepick\\resourses\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('*** Start Test 1 ***')

    mp = MainPage(driver)
    mp.authorisation()
    mp.go_to_clothes_page()

    cp = ClothesPage(driver)
    cp.search_the_jacket()

    pp = ProductPage(driver)
    pp.checkout_to_basket()

    bp = BasketPage(driver)
    bp.checkout()
