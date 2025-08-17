from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from helper import *
from locators import Locators
from curl import *

class TestRegistration:

    def test_registration_redirect_to_login(self, driver):
        driver.get(REG_PAGE)
        wait = WebDriverWait(driver, 10)

        name, email, password = generate_valid_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()

        wait.until(expected_conditions.url_contains("/login"))
        assert driver.current_url == AUTH_PAGE

