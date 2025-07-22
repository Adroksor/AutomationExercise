import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            name = item.name
            try:
                username = item.callspec.params.get("name", "unknown_user")
                name = username.replace(" ", "_")
            except Exception:
                pass

            time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{name}_{time_str}.png"
            filepath = os.path.join(screenshots_dir, filename)

            driver.save_screenshot(filepath)
            print(f"\n[!] Screenshot saved: {filepath}")