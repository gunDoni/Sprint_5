from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import SAUCES_TAB, SAUCES_TAB_ACTIVE, BUNS_TAB, BUNS_TAB_ACTIVE, FILLINGS_TAB, FILLINGS_TAB_ACTIVE
from settings import WAIT_SECONDS, BASE_URL

def test_constructor_sauces(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(BUNS_TAB_ACTIVE))
    driver.find_element(*SAUCES_TAB).click()
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(SAUCES_TAB_ACTIVE))
    assert driver.find_element(*SAUCES_TAB_ACTIVE).is_displayed()

def test_constructor_buns(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(BUNS_TAB_ACTIVE))
    assert driver.find_element(*BUNS_TAB_ACTIVE).is_displayed()

def test_constructor_fillings(driver):
    driver.get(BASE_URL)
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(BUNS_TAB_ACTIVE))
    driver.find_element(*FILLINGS_TAB).click()
    WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(FILLINGS_TAB_ACTIVE))
    assert driver.find_element(*FILLINGS_TAB_ACTIVE).is_displayed()
