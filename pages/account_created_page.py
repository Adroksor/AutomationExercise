from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AccountPage:
    ACCOUNT_CREATED_HEADER = (By.XPATH, "//h2[text()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//button[@data-qa='continue-button']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def is_login_form_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED_HEADER)
        ).is_displayed()

    def continue_click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

