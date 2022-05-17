""" Conftest module """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """ parser function """
    parser.addoption("--headless", action="store_true",
                     help="turn on headless option if headless arg is added")


@pytest.fixture(scope="class")
def browser(request):
    """ function for driver and connect to project frontend """
    isheadless = request.config.getoption("--headless")
    chrome_options = Options()
    if isheadless:
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://localhost:5010")
    driver.implicitly_wait(5)
    yield driver
    driver.close()
