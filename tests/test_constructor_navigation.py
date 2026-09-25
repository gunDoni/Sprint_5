from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ACCOUNT_BUTTON, CONSTRUCTOR_LINK_BACK, LOGO, BUNS_TAB, LOGOUT_BUTTON
from settings import WAIT_SECONDS, BASE_URL


class TestConstructorNavigation:
    def test_constructor_link(self, driver, logged_in_user):
        driver.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(*CONSTRUCTOR_LINK_BACK).click()
        WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(BUNS_TAB))
        assert driver.current_url == BASE_URL + "/"

    def test_logo(self, driver, logged_in_user):
        driver.find_element(*ACCOUNT_BUTTON).click()
        WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(*LOGO).click()
        WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(BUNS_TAB))
        assert driver.current_url == BASE_URL + "/"
