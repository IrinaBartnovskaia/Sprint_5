from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import Credentials
from locators import Locators
from curl import *

class TestLogin:
    def test_login_main_page(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(MAIN_PAGE)

        driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL)).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        assert MAIN_PAGE in driver.current_url

    def test_login_personal_account(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(MAIN_PAGE)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL)).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        assert MAIN_PAGE in driver.current_url

    def test_registration_form(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(REG_PAGE)

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL)).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        assert MAIN_PAGE in driver.current_url

    def test_login_forgot_password(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(FORGOT_PASSWORD_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.EMAIL)).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.SIGN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        assert MAIN_PAGE in driver.current_url







