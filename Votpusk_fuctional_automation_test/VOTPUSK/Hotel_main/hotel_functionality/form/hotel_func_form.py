from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.config.configuration import TestData


class HotelForm(BaseMethods):
    MIAN_INPUT = (By.CSS_SELECTOR, '[class="hotels-search__item search-text"]')
    NO_DOM_CALENDAR_CHECK_IN = (By.ID, 'travel-in-hotels')
    NO_DOM_CALENDAR_CHECKOUT = (By.ID, 'travel-out-hotels')
    ROOM_COLUMN = (By.CSS_SELECTOR, '[class="dropdown__btn hotels-search__item"]')
    INPUT_PLUS = (By.CLASS_NAME, 'input-plus')
    INPUT_MINUS = (By.CLASS_NAME, 'input-minus')
    ADD_COLUMN = (By.CLASS_NAME, 'collapse__btn')
    FORM_HEADER_BUTTON = (By.XPATH, '//*[@id="reservation-form"]/input[4]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_form_input(self, s=2):
        self.is_element_present(HotelForm.MIAN_INPUT)
        self.sleep(s)

    def assert_put_into_field(self, s=2):
        self.send_keys_to_element(HotelForm.MIAN_INPUT, TestData.CITY_INPUT_DATA)
        self.sleep(s)

    def assert_react_calendar_check_in(self, s=2):
        self.is_element_present(HotelForm.NO_DOM_CALENDAR_CHECK_IN)
        self.sleep(s)

    def assert_react_calendar_check_out(self, s=2):
        self.is_element_present(HotelForm.NO_DOM_CALENDAR_CHECKOUT)
        self.sleep(s)

    def assert_room_column(self, s=2):
        self.is_element_present(HotelForm.ROOM_COLUMN)
        self.sleep(s)

    def assert_click_room_column(self, s=2):
        self.click_element(HotelForm.ROOM_COLUMN)
        self.sleep(s)

    def assert_add_member(self, s=2):
        self.click_in_loop4(HotelForm.INPUT_PLUS)
        self.sleep(s)

    def assert_remove_member(self, s=2):
        self.click_in_loop4(HotelForm.INPUT_MINUS)
        self.sleep(s)

    def assert_open_list(self, s=2):
        self.click_element(HotelForm.ADD_COLUMN)
        self.sleep(s)

    def assert_clickable_button(self, s=2):
        self.is_element_present(HotelForm.FORM_HEADER_BUTTON)
        self.assert_element_to_be_clickable(HotelForm.FORM_HEADER_BUTTON)
        self.sleep(s)








