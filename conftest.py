#website used -- "https://demo.playwright.dev/todomvc/#/"

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # options = webdriver.ChromeOptions()
    # options.add_argument("--start-maximized")
    driver = webdriver.Edge()
    print("launch the todo url")
    driver.get("https://demo.playwright.dev/todomvc/#/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    print("----------end of test ----------")