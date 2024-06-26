import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--width=1280")
    options.add_argument("--height=960")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
