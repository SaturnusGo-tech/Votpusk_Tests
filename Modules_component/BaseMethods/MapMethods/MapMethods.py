import random
import time
import logging
from datetime import datetime
from io import BytesIO
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from functools import wraps
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from PIL import Image, ImageDraw


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

    def log_action(self, message):
        self.logger.debug(message)


class MapBoxesMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def interact_with_map(self, map_element, marker_locator):
        # Проверяем, что карта отображается
        assert map_element.is_displayed(), "Карта не отображается"

        # Взаимодействие с картой (например, клик и увеличение)
        action = ActionChains(self.driver)
        action.click(map_element).perform()

        # Увеличиваем карту
        self.driver.execute_script("arguments[0].setAttribute('style', 'zoom: 1.5; transform: none;')", map_element)

        # Ждем, пока карта полностью загрузится
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, marker_locator)))

        # Проверяем наличие маркеров
        markers = self.driver.find_elements(By.CSS_SELECTOR, marker_locator)
        assert len(markers) > 0, "На карте отсутствуют маркеры"

    def click_element(self, by_locator, timeout=10, error_message="Не удалось кликнуть на элемент"):
        """
        Находит элемент на странице по локатору и кликает на него.
        Если элемент не кликабелен, выводится сообщение об ошибке.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()
            self.logger.info(f"Кликнуто по элементу с локатором: {by_locator}")
        except TimeoutException:
            self.logger.error(f"{error_message}: Превышено время ожидания - Не удалось кликнуть на элемент с локатором: {by_locator}")
            raise
        except ElementNotInteractableException:
            self.logger.error(
                f"{error_message}: Элемент не взаимодействуемый - Не удалось кликнуть на элемент с локатором: {by_locator}")
            raise
        except Exception as e:
            self.logger.error(
                f"{error_message}: Неизвестное исключение - Не удалось кликнуть на элемент с локатором: {by_locator}")
            self.logger.exception(e)
            raise
        except Exception as e:
            self.logger.error(
                f"{error_message}: Unknown exception - Failed to click on element with locator: {by_locator}")
            self.logger.exception(e)
            raise