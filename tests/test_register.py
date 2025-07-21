from pathlib import Path
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from conftest import driver

import pytest
import json


file_path = Path(__file__).parent.parent / "data" / "test_user.json"

with file_path.open(encoding="utf-8") as f:
    raw_users = json.load(f)


test_users = [
    (
        user["title"],
        user["name"],
        user["email"],
        user["password"],
        user["dob"]["day"],
        user["dob"]["month"],
        user["dob"]["year"],
        user["first_name"],
        user["last_name"],
        user["company"],
        user["address"],
        user["country"],
        user["state"],
        user["city"],
        user["zipcode"],
        user["mobile"]
    )
    for user in raw_users
]



@pytest.mark.parametrize(
    "title,name,email,password,day,month,year,first_name,last_name,company,address,country,state,city,zipcode,mobile",
    test_users
)
def test_register_user(
    driver, title, name, email, password, day, month, year,
    first_name, last_name, company, address, country,
    state, city, zipcode, mobile
):
    driver.get("http://automationexercise.com")

    home = HomePage(driver)
    home.close_cookie_banner()
    assert home.is_homepage_visible()

    home.click_signup_login()

    login = LoginPage(driver)
    login.register(name, email)

    register = RegisterPage(driver)
    register.register(title, name, email, password, day, month, year,
                  first_name, last_name, company, address, country,
                  state, city, zipcode, mobile)
