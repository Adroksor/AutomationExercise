from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HomePage:
    SIGNUP_LOGIN = By.LINK_TEXT, "Signup / Login"
    DELETED_HEADER = By.LINK_TEXT, "Delete Account"
    COOKIE_CONSENT = By.XPATH, "//button[.//p[text()='Consent']]"
    LOGGED_IN_AS = (By.XPATH, "//li/a[contains(., 'Logged in as')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_homepage_visible(self):
        return "Automation Exercise" in self.driver.title

    def click_signup_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_LOGIN)
        ).click()

    def click_delete_account(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DELETED_HEADER)
        ).click()

    def close_cookie_banner(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable(self.COOKIE_CONSENT)
            )
            cookie_button.click()
        except Exception as e:
            print("Cookie popup not found or not clickable:", e)

    def is_logged_in_as(self, expected_username):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.LOGGED_IN_AS)
            )
            actual_username = element.text.replace("Logged in as ", "").strip()
            print("actual_username", actual_username)
            return actual_username == expected_username
        except Exception as e:
            print(f"[ERROR] Could not verify logged in user: {e}")
            return False