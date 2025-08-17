import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators
from data import Credentials


@pytest.fixture
def driver():
    # Создаем опции для Chrome
    driver = webdriver.Chrome()
    driver.set_window_size(1200,600)  # Задаем размер окна
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(AUTH_PAGE)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.EMAIL))

    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.SIGN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_TITLE))

    return driver

