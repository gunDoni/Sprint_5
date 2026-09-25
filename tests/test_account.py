from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import ACCOUNT_BUTTON, LOGOUT_BUTTON
from settings import WAIT_SECONDS


class TestAccount:
    def test_navigate_to_account(self, driver, logged_in_user):
        driver.find_element(*ACCOUNT_BUTTON).click()

        WebDriverWait(driver, WAIT_SECONDS).until(
            expected_conditions.visibility_of_element_located(LOGOUT_BUTTON)
        )

        assert "/account" in driver.current_url