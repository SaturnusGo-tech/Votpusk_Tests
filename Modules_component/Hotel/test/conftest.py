import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()
