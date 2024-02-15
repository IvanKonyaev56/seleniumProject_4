import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('E:\\1_QAA\\stepick\\resourses\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print('*** Start Test 1 ***')

    mp = MainPage(driver)
    mp.authorisation()
    mp.search_the_mens_jacket()


