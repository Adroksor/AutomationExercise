from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class RegisterPage:
    INFORMATION_HEADER = By.XPATH, "//b[text()='Enter Account Information']"
    NAME = (By.ID, "name")
    TITLE_MR = (By.XPATH, "//input[@value='Mr']")
    TITLE_MRS = (By.XPATH, "//input[@value='Mrs']")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_SELECT = (By.ID, "days")
    MONTH_SELECT = (By.ID, "months")
    YEAR_SELECT = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    COMPANY = (By.ID, "company")
    CREATE_ACCOUNT = (By.XPATH, "//button[@data-qa='create-account']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_information_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.INFORMATION_HEADER)
        ).is_displayed()


    def register(self, title, name, email, password, day, month, year,
                  first_name, last_name, company, address, country,
                  state, city, zipcode, mobile):

        check = self.TITLE_MRS if "Mrs" in title else self.TITLE_MR
        self.wait.until(
            EC.presence_of_element_located(check)
        ).click()
        self.enter_information(self.PASSWORD_INPUT, password)

        Select(self.driver.find_element(*self.DAYS_SELECT)).select_by_value(day)
        Select(self.driver.find_element(*self.MONTH_SELECT)).select_by_value(month)
        Select(self.driver.find_element(*self.YEAR_SELECT)).select_by_value(year)

        self.enter_information(self.FIRST_NAME, first_name)
        self.enter_information(self.LAST_NAME, last_name)
        self.enter_information(self.ADDRESS, address)
        self.enter_information(self.STATE, state)
        self.enter_information(self.CITY, city)
        self.enter_information(self.ZIPCODE, zipcode)
        self.enter_information(self.MOBILE_NUMBER, mobile)
        self.enter_information(self.COMPANY, company)

        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_ACCOUNT)
        ).click()

    def enter_information(self, where, what):
        self.wait.until(
            EC.presence_of_element_located(where)
        ).send_keys(what)

