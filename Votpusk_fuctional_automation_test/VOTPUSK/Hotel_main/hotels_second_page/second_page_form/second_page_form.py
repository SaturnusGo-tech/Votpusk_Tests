import time

from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.hotels_second_page.config.configuration import TestDataSecondPage


class SecondFormLocators(BaseMethods):
    FROM_FIELD_BLOCK = (By.CSS_SELECTOR, '[class="hotels-search corner-radius-two"]')
    DEFAULT_INPUT_FIELD = (By.CSS_SELECTOR, '[class="hotels-search__item search-text"]')
    FORM_INPUT_CITY = (By.CSS_SELECTOR, '[class="hotels-search__item search-text"]')
    FORM_LEN = (By.XPATH, '//*[@id="search-results"]/ul')
    CHECK_IN = (By.ID, 'h-checkin')
    CHECK_OUT = (By.ID, 'h-checkout')
    DROPDOWN_QUANTITY = (By.CSS_SELECTOR, '[class="dropdown__btn hotels-search__item"]')
    INPUT_PLUS = (By.CLASS_NAME, 'input-plus')
    INPUT_MINUS = (By.CLASS_NAME, 'input-minus dis')
    DROPDOWN_KIDS = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[1]')
    DROPDOWN_KIDS_COLUM = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[2]/div')
    SEARCH_TYPE_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Проверка работоспособности функционала внутренней формы поиска отелей
    def check_the_form_visibility(self):
        self.page_loaded(SecondFormLocators.FROM_FIELD_BLOCK)
        self.is_element_present(SecondFormLocators.FROM_FIELD_BLOCK)

    def clear_default_value_and_assert_the_len(self):
        self.send_keys_to_element(SecondFormLocators.DEFAULT_INPUT_FIELD, TestDataSecondPage.CITY)
        time.sleep(1)
        self.is_dropdown_present(SecondFormLocators.FORM_LEN)

    def select_check_in(self):
        self.is_element_present(SecondFormLocators.CHECK_IN)
        self.click_random_enabled_day_in_calendar(SecondFormLocators.CHECK_IN)
        time.sleep(2)

    def select_check_out(self):
        self.page_loaded(SecondFormLocators.CHECK_OUT)
        self.is_element_present(SecondFormLocators.CHECK_OUT)
        self.click_random_enabled_day_in_calendar(SecondFormLocators.CHECK_OUT)

    def select_dropdown_quantity(self):
        self.page_loaded(SecondFormLocators.DROPDOWN_QUANTITY)
        self.is_element_present(SecondFormLocators.DROPDOWN_QUANTITY)
        self.click_element(SecondFormLocators.DROPDOWN_QUANTITY)

    def check_input_sign(self):
        self.page_loaded(SecondFormLocators.INPUT_PLUS)
        self.is_visible(SecondFormLocators.INPUT_PLUS)
        self.is_visible(SecondFormLocators.INPUT_MINUS)

    def randint_click(self):
        self.do_randint_click(SecondFormLocators.INPUT_PLUS)
        self.do_randint_click(SecondFormLocators.INPUT_MINUS)

    def check_dropdown_quantity_kids(self):
        self.is_element_present(SecondFormLocators.DROPDOWN_KIDS)
        self.sleep(2)

    def click_to_dropdown_kids(self):
        self.click_element(SecondFormLocators.DROPDOWN_KIDS)

    def check_visibility_dropdown_len(self):
        self.is_dropdown_present(SecondFormLocators.DROPDOWN_KIDS_COLUM)

    def assert_clickable_search_button(self):
        self.is_element_present(SecondFormLocators.SEARCH_TYPE_BUTTON)
        self.assert_element_to_be_clickable(SecondFormLocators.SEARCH_TYPE_BUTTON)














