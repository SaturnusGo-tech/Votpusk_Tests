import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_pagination(driver):
    # Открытие страницы
    driver.get("https://www.votpusk.ru/hotels/russia/moscow")

    # Ожидание загрузки элементов
    wait = WebDriverWait(driver, 10)
    pagination = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".pagination")))

    # Проверка наличия пагинации
    assert pagination.is_displayed(), "Пагинация не отображается"

    # Получение списка страниц пагинации
    pages = pagination.find_elements(By.TAG_NAME, "a")

    # Перебор страниц пагинации и проверка их доступности
    for page in pages:
        page.click()
        time.sleep(2)  # Пауза для ожидания загрузки новой страницы

        # Проверка активности текущей страницы пагинации
        current_page = pagination.find_element(By.CSS_SELECTOR, ".current")
        assert current_page == page, f"Текущая страница не соответствует ожидаемой: {current_page.text}"

        # Проверка отображения результатов на текущей странице
        hotel_list = driver.find_element(By.CSS_SELECTOR, ".hotel-list")
        assert hotel_list.is_displayed(), "Результаты отображаются некорректно на текущей странице"

