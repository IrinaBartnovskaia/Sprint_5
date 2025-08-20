import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from curl import MAIN_PAGE
from locators import Locators


class TestConstructor:

    @pytest.mark.parametrize(
        "first_tab, second_tab, expected",
        [
            (Locators.SAUCES_SECTION,  Locators.BUNS_SECTION,     "Булки"),
            (Locators.FILLINGS_SECTION,    Locators.SAUCES_SECTION,   "Соусы"),
            (Locators.BUNS_SECTION,    Locators.FILLINGS_SECTION, "Начинки"),
        ],
    )
    def test_burger_constructor_choosing_tabs(self, driver, first_tab, second_tab, expected):
        wait = WebDriverWait(driver, 10)
        driver.get(MAIN_PAGE)

        wait.until(expected_conditions.element_to_be_clickable(first_tab)).click()
        wait.until(expected_conditions.element_to_be_clickable(second_tab)).click()
        wait.until(expected_conditions.visibility_of_element_located(second_tab))
        assert driver.find_element(*second_tab).text == expected


