from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeletedPage:
    ACCOUNT_DELETED_HEADER = (By.XPATH, "//h2[@data-qa='account-deleted']/b[text()='Account Deleted!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[@data-qa='continue-button']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def is_deleted_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_DELETED_HEADER)
        ).is_displayed()

    def continue_click(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()
