import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    PASSWORD_INPUT,
    REGISTER_BUTTON,
    LOGIN_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    ACCOUNT_BUTTON,
)
from data_generation import generate_email, generate_password
from settings import WAIT_SECONDS, BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get(f"{BASE_URL}/register")
    driver.find_element(*NAME_INPUT).send_keys("Арсен")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_BUTTON).click()

    WebDriverWait(driver, WAIT_SECONDS).until(
        expected_conditions.visibility_of_element_located(LOGIN_BUTTON)
    )

    return email, password


@pytest.fixture
def logged_in_user(driver, registered_user):
    email, password = registered_user

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, WAIT_SECONDS).until(
        expected_conditions.visibility_of_element_located(ACCOUNT_BUTTON)
    )
    return email, password
