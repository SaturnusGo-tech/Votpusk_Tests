import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    chrome_driver_path = "users/mercuryrucks/ChromeDriver"  # Замените на ваш путь к исполняемому файлу ChromeDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
