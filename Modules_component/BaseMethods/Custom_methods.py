import logging
import re
import os
import time
import random
from colorlog import ColoredFormatter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import requests

logging.basicConfig(level=logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

        # Настройка логирования с использованием colorlog
        formatter = ColoredFormatter(
            "%(log_color)s%(message)s%(reset)s",
            log_colors={
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )

        # Создание объекта логгера
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Создание обработчика для вывода логов в консоль
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # Добавление обработчика к логгеру
        logger.addHandler(handler)

        # Пример использования логирования
        logger.debug("Отладочное сообщение")
        logger.info("Информационное сообщение")
        logger.warning("Предупреждение")
        logger.error("Ошибка")
        logger.critical("Критическая ошибка")


def is_special_characters_allowed(input_field):
    # Проверка, разрешены ли специальные символы в поле ввода
    # Можно добавить соответствующую логику здесь
    return True


def has_negative_number(text):
    # Проверка наличия отрицательного числа в тексте
    return '-' in text


def has_sql_injection(text):
    # Проверка наличия SQL-инъекций в тексте
    sql_injection_pattern = re.compile(
        r"(?:')|(?:--)|(/\\*(?:.|[\\n\\r])*?\\*/)|"
        r"(\\b(select|update|union|and|or|delete|insert|truncate|drop|"
        r"create|alter|exec|execute|declare|shutdown|xp_cmdshell|"
        r"createuser|grant|revoke)\\b)", re.IGNORECASE)
    return sql_injection_pattern.search(text) is not None


class BaseMethods(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def refresh_page(self):
        """
        Обновляет страницу с помощью метода `driver.refresh()`.
        Если обновление страницы не удалось после нескольких попыток, выводится сообщение об ошибке.
        """
        max_attempts = 3
        attempt = 1

        while attempt <= max_attempts:
            try:
                self.driver.refresh()
                break
            except WebDriverException as e:
                self.logger.error(f"Ошибка при обновлении страницы: {e}")
                # Дополнительные действия при ошибке сети

            time.sleep(1)  # Задержка перед повторной попыткой
            attempt += 1

        if attempt > max_attempts:
            self.logger.error("Не удалось обновить страницу после нескольких попыток.")
            # Дополнительные действия при неудаче

    def verify_dropdown_list(self, dropdown_locator):
        """
        Проверяет выпадающий список на странице.
        Выводит список опций, проверяет значения по умолчанию и другие ожидаемые значения.
        """
        wait = WebDriverWait(self.driver, 100)
        dropdown = wait.until(EC.visibility_of_element_located(dropdown_locator))

        options = dropdown.options
        assert 0 < len(options), "Список в выпадающем меню пуст"

        # Вывод списка опций (для отладки или информации)
        self.logger.info("Опции выпадающего списка:")
        for option in options:
            self.logger.info(option.text)

        # Дополнительные проверки или утверждения, если требуется
        first_option = options[0]
        assert first_option.text != "Пожалуйста, выберите опцию", "Неверная опция по умолчанию"

        selected_option = dropdown.first_selected_option
        assert selected_option.text == "Выбор по умолчанию", "Неверный выбор по умолчанию"

        expected_options = ["Опция 1", "Опция 2", "Опция 3"]
        actual_options = [option.text for option in options]
        assert actual_options == expected_options, "Опции выпадающего списка не соответствуют ожидаемым значениям"

        # Другие проверки или утверждения, по необходимости
        assert len(options) <= 100, "Слишком много опций в выпадающем списке"
        assert options[-1].text == "Последняя опция", "Неверная последняя опция"
        assert dropdown.is_multiple == False, "Выпадающее меню позволяет выбирать несколько опций"

        # Проверка отсутствия определенной опции
        assert not any(option.text == "Опция X" for option in options), "Опция X не должна присутствовать"

    def click_and_verify(self, element_locator, expected_url):
        """
        Находит элемент на странице по локатору, кликает на него и проверяет URL после клика.
        """
        element = self.driver.find_element(*element_locator)
        element.click()

        # Дополнительные проверки или утверждения, если требуется
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL после клика не соответствует ожидаемому URL: {expected_url}"

    def click_and_check_response(self, element_locator, screenshot_dir):
        """
        Находит элемент на странице по локатору, кликает на него и проверяет ответ сервера.
        При ошибке создает скриншот страницы и сохраняет содержимое страницы.
        """
        element = self.driver.find_element(*element_locator)
        element.click()

        response = requests.get(self.driver.current_url)
        status_code = response.status_code

        if status_code == 200:
            # Дополнительные проверки или утверждения, если требуется
            assert response.headers["Content-Type"] == "application/json", "Неверный тип содержимого"

            data = response.json()
            assert "key" in data, "Ключ не найден в ответе"
            return True
        elif 201 <= status_code <= 599:
            # Создание скриншота страницы при ошибке
            screenshot_path = os.path.join(screenshot_dir, "error_page.png")
            self.driver.save_screenshot(screenshot_path)

            # Сохранение содержимого страницы при ошибке
            page_source_path = os.path.join(screenshot_dir, "error_page.html")
            with open(page_source_path, "w", encoding="utf-8") as file:
                file.write(self.driver.page_source)

            # Другие проверки или утверждения, если требуется
            assert False, f"Неожиданный код ответа сервера: {status_code}"
        return False

    def get_page_title(self):
        """Возвращает заголовок текущей страницы."""
        return self.driver.title

    def get_element_text(self, element_locator):
        """
        Возвращает текст определенного элемента на странице.
        """
        element = self.driver.find_element(*element_locator)
        return element.text

    def is_element_visible(self, element_locator):
        """
        Проверяет, видим ли элемент на странице.
        Возвращает True, если элемент видим, иначе False.
        """
        element = self.driver.find_element(*element_locator)
        return element.is_displayed()

    def is_element_present(self, element_locator, screenshot_dir):
        """
        Проверяет наличие элемента на странице.
        Возвращает True, если элемент присутствует, иначе False.
        Создает скриншот ошибки при отсутствии элемента и сохраняет его в указанной директории.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(element_locator))
            assert element.is_displayed(), "Элемент не отображается"
            assert element.is_enabled(), "Элемент неактивен"
            # Другие проверки или утверждения, по необходимости
            return True
        except Exception as e:
            # Создание скриншота при ошибке
            screenshot_path = os.path.join(screenshot_dir, "element_not_present.png")
            self.driver.save_screenshot(screenshot_path)

            # Вывод сообщения об ошибке
            error_message = f"Элемент отсутствует или не в ожидаемом состоянии: {element_locator}\nОшибка: {str(e)}"
            self.logger.error(error_message)

            # Выбрасывание исключения AssertionError
            raise AssertionError(error_message)

    def random_country_selection(self, dropdown_country):
        """
        Выбирает случайную опцию в выпадающем списке стран.
        """
        driver = self.driver
        action = ActionChains(driver)
        dropdown = driver.find_element(*dropdown_country)  # Ищем элемент по локатору

        while dropdown.is_displayed():
            action.send_keys(Keys.DOWN).perform()
            WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable(dropdown_country))
            if random.randint(1, 10) == 3:
                action.send_keys(Keys.ENTER).perform()
                break

    def scroll_into_element_view(self, x, y):
        """
        Прокручивает окно до указанных координат x и y.
        """
        try:
            # Ожидание полной загрузки страницы
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'body')))

            # Прокрутка окна до указанной позиции
            self.driver.execute_script("window.scrollTo(arguments[0], arguments[1]);", x, y)
        except Exception as e:
            self.logger.error("Ошибка при прокрутке окна:", e)

    def sleep(self, seconds=5, randomize=False, min_seconds=None, max_seconds=None):
        """
        Выполняет паузу в выполнении кода на указанное количество секунд.
        Можно задать случайную паузу в заданном диапазоне времени.
        """
        if randomize:
            if min_seconds is None:
                min_seconds = 1
            if max_seconds is None:
                max_seconds = seconds * 2
            sleep_time = random.uniform(min_seconds, max_seconds)
        else:
            sleep_time = seconds
        time.sleep(sleep_time)

    def move_slider(self, slider, offset_x, offset_y):
        initial_prices = self._get_prices()

        action = ActionChains(self.driver)
        action.click_and_hold(slider)
        action.move_by_offset(offset_x, offset_y)
        action.release()
        action.perform()

        # Ждем, пока прогрузится вся страница
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loader')))

        # Получаем обновленные цены
        updated_prices = self._get_prices()

        # Проверяем, что количество начальных и обновленных цен одинаковое
        assert len(initial_prices) == len(updated_prices), "Количество начальных и обновленных цен не совпадает"

        # Настройка логирования с использованием colorlog
        formatter = ColoredFormatter(
            "%(log_color)s%(message)s%(reset)s",
            log_colors={
                'INFO': 'green'
            }
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        # Сравниваем начальные и обновленные цены
        for initial_price, updated_price in zip(initial_prices, updated_prices):
            assert initial_price != updated_price, f"Цена не изменилась: {initial_price}"
            self.logger.info(f"Цена изменилась: {initial_price} -> {updated_price}")

    def _get_prices(self):
        """
        Возвращает список цен, найденных на странице.
        """
        # Находим все элементы с классом 'price' и сохраняем их текст (цены)
        prices_elements = self.driver.find_elements(By.CLASS_NAME, 'price')
        return [price.text for price in prices_elements]

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
            self.logger.error(
                f"{error_message}: Превышено время ожидания - Не удалось кликнуть на элемент с локатором: {by_locator}")
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

    def input_text(self, field_locator, text):
        input_field = self.driver.find_element(*field_locator)
        input_field.clear()
        input_field.send_keys(text)

        # Проверка доступности ввода специальных символов
        if not is_special_characters_allowed(input_field):
            raise AssertionError("В поле ввода недопустимы специальные символы")

        # Проверка отрицательных чисел
        if text.startswith("-"):
            raise AssertionError("В поле ввода недопустимы отрицательные числа")

        # Проверка ограничения на количество символов (64 символа)
        if len(text) > 64:
            raise AssertionError("Превышено ограничение на количество символов")

    def send_keys_to_element(self, by_locator, keys):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(by_locator)
            )
            element.clear()

            # Проверка отрицательных чисел
            assert not has_negative_number(keys), "Недопустимое значение: отрицательные числа"

            # Проверка ограничения на количество символов (32 символа)
            assert len(keys) <= 32, "Недопустимое значение: превышено ограничение на количество символов"

            # Проверка наличия SQL-инъекций
            assert not has_sql_injection(keys), "Недопустимое значение: SQL-инъекции обнаружены"

            element.send_keys(keys)
        except Exception as e:
            self.logger.error("Can't find an element")
            self.logger.error(e)
