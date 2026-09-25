from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    MAIN_LOGIN_BUTTON,
    ACCOUNT_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON,
    REGISTER_LOGIN_LINK,
    FORGOT_PASSWORD_LINK,
    FORGOT_LOGIN_LINK,
    LOGOUT_BUTTON,
)
from settings import WAIT_SECONDS, BASE_URL


def perform_login(driver, email, password):
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, WAIT_SECONDS).until(
        expected_conditions.visibility_of_element_located(ACCOUNT_BUTTON)
    )
    assert driver.find_element(*ACCOUNT_BUTTON).is_displayed()


class TestLogin:
    def test_login_from_main_page(self, driver, registered_user):
        email, password = registered_user

        driver.get(BASE_URL)
        driver.find_element(*MAIN_LOGIN_BUTTON).click()

        perform_login(driver, email, password)

    def test_login_from_account_button(self, driver, registered_user):
        email, password = registered_user

        driver.get(BASE_URL)
        driver.find_element(*ACCOUNT_BUTTON).click()

        perform_login(driver, email, password)

    def test_login_from_register_form(self, driver, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/register")
        driver.find_element(*REGISTER_LOGIN_LINK).click()

        perform_login(driver, email, password)

    def test_login_from_forgot_password_form(self, driver, registered_user):
        email, password = registered_user

        driver.get(f"{BASE_URL}/forgot-password")
        driver.find_element(*FORGOT_LOGIN_LINK).click()

        perform_login(driver, email, password)