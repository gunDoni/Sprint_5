from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_BUTTON,
    PASSWORD_ERROR_TEXT,
)
from data_generation import generate_email, generate_password
from settings import WAIT_SECONDS, BASE_URL


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*NAME_INPUT).send_keys("Арсен")

        email = generate_email()
        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)

        password = generate_password()
        driver.find_element(*PASSWORD_INPUT).send_keys(password)

        driver.find_element(*REGISTER_BUTTON).click()

        assert WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

    def test_registration_with_short_password(self, driver):
        driver.get(f"{BASE_URL}/register")

        driver.find_element(*NAME_INPUT).send_keys("Арсен")

        driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_email())

        driver.find_element(*PASSWORD_INPUT).send_keys("1234")

        driver.find_element(*REGISTER_BUTTON).click()

        assert WebDriverWait(driver, WAIT_SECONDS).until(expected_conditions.visibility_of_element_located(PASSWORD_ERROR_TEXT))