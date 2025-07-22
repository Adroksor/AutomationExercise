from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    EMAIL_INPUT = By.XPATH, "//input[@data-qa='login-email']"
    PASSWORD_INPUT = By.XPATH, "//input[@data-qa='login-password']"
    LOGIN_BUTTON = By.XPATH, "//button[@data-qa='login-button']"
    SIGNUP_NAME_INPUT = By.XPATH, "//input[@data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = By.XPATH, "//input[@data-qa='signup-email']"
    SIGNUP_BUTTON = By.XPATH, "//button[@data-qa='signup-button']"
    LOGIN_HEADER = By.XPATH, "//h2[text()='Login to your account']"
    REGISTER_HEADER = By.XPATH, "//h2[text()='New User Signup!']"
    ERROR_MESSAGE = By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_login_form_visible(self):
        return self.wait.until(
                EC.visibility_of_element_located(self.LOGIN_HEADER)
            ).is_displayed()

    def is_register_form_visible(self):
        return self.wait.until(
                EC.visibility_of_element_located(self.REGISTER_HEADER)
            ).is_displayed()

    def is_error_message_displayed(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            ).is_displayed()
        except:
            return False

    def login(self, email, password):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        ).send_keys(email)
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def register(self, username, email):
        self.wait.until(
            EC.visibility_of_element_located(self.SIGNUP_NAME_INPUT)
        ).send_keys(username)
        self.wait.until(
            EC.visibility_of_element_located(self.SIGNUP_EMAIL_INPUT)
        ).send_keys(email)
        self.wait.until(
            EC.element_to_be_clickable(self.SIGNUP_BUTTON)
        ).click()
