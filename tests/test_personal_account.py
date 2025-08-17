from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *

class TestPersonalAccount:
    def test_go_to_profile_clic_personal_account(self, driver):
        wait = WebDriverWait(driver, 5)
        driver.get(MAIN_PAGE)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_go_to_constructor_from_personal_account(self, login):
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON)).click()
        assert MAIN_PAGE in login.current_url

    def test_go_to_main_from_personal_account_clic_logo(selfself, login):
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.LOGO_LINK)).click()
        assert MAIN_PAGE in login.current_url

    def test_logout_from_personal_account(self, login):
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(login, 5).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        assert MAIN_PAGE in login.current_url