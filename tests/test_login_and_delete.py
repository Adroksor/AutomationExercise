from pathlib import Path
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_deleted_page import DeletedPage
from conftest import driver

import pytest
import json


file_path = Path(__file__).parent.parent / "data" / "test_user.json"

with file_path.open(encoding="utf-8") as f:
    raw_users = json.load(f)

test_users = [
    (user["email"], user["name"], user["password"])
    for user in raw_users
]

@pytest.mark.parametrize("email,username,password", test_users)
def test_login_and_delete_user(driver, email, username, password):
    driver.get("http://automationexercise.com")

    home = HomePage(driver)
    home.close_cookie_banner()
    assert home.is_homepage_visible()

    home.click_signup_login()

    login = LoginPage(driver)
    assert login.is_login_form_visible()
    login.login(email, password)

    assert home.is_logged_in_as(username)

    home.click_delete_account()

    deleted = DeletedPage(driver)
    assert deleted.is_deleted_visible()

    deleted.continue_click()
