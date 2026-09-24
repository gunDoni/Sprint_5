from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ACCOUNT_BUTTON, LOGOUT_BUTTON, LOGIN_BUTTON
from settings import WAIT_SECONDS

def test_logout(driver, logged_in_user):
    driver.find_element(*ACCOUNT_BUTTON).click()
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
    driver.find_element(*LOGOUT_BUTTON).click()
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))
    assert driver.find_element(*LOGIN_BUTTON).is_displayed()