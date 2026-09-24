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


def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")

    # Введи имя
    driver.find_element(*NAME_INPUT).send_keys("Арсен")

    # Введи email
    email = generate_email()
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)

    # Введи пароль
    password = generate_password()
    driver.find_element(*PASSWORD_INPUT).send_keys(password)

    # Нажми кнопку регистрации
    driver.find_element(*REGISTER_BUTTON).click()

    # Дождись появления формы авторизации
    WebDriverWait(driver, WAIT_SECONDS).until(
        expected_conditions.visibility_of_element_located(LOGIN_BUTTON)
    )

    # Проверь, что появилась кнопка «Войти»
    assert driver.find_element(*LOGIN_BUTTON).is_displayed()


def test_registration_with_short_password(driver):
    driver.get(f"{BASE_URL}/register")

    # Введи имя
    driver.find_element(*NAME_INPUT).send_keys("Арсен")

    # Введи email
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(generate_email())

    # Введи короткий пароль
    driver.find_element(*PASSWORD_INPUT).send_keys("1234")

    # Нажми кнопку регистрации
    driver.find_element(*REGISTER_BUTTON).click()

    # Дождись появления ошибки
    WebDriverWait(driver, WAIT_SECONDS).until(
        expected_conditions.visibility_of_element_located(PASSWORD_ERROR_TEXT)
    )

    # Проверь, что появилась ошибка под полем пароля
    assert driver.find_element(*PASSWORD_ERROR_TEXT).is_displayed()