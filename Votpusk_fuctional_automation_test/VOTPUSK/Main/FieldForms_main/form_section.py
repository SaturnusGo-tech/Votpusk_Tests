import time

from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.Config.TestData import TestData
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.specifide_locators import SpecifiedLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.world_type_locators import WorldTypeLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.Config.TestDataWorld import TestDataWorld
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.hotel_locators import HotelFormLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.Config.TestDataHotels import TestDataHotels
from selenium.webdriver.support.ui import WebDriverWait
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.train_locators import TrainLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.Config.TestDataTrain import TestDataTrain
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.Config.TestDataRouts import TestDataRouts
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.routs_locators import RoutsLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.FieldForms_main.country_and_cities import CountryAndCities


class ToursFormLocators(BaseMethods):
    PINNED_FORM = (By.CSS_SELECTOR, '[class="search"]')
    RTOURS_BUTTON = (By.CSS_SELECTOR, '[class="block-btns__btn block-btns__btn_active"]')
    WTOURS_BUTTON = (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/section[2]/div/div[1]/form[2]/input')
    INPUT_CITY = (By.CSS_SELECTOR, '[id="s-query"]')
    CHOOSE_ATTR = (By.CSS_SELECTOR, '[class="search__item second typelist"]')
    SELECT_DATE_FROM = (By.CSS_SELECTOR, '[id="s-datefrom"]')
    SELECT_DATE_TO = (By.CSS_SELECTOR, '[id="s-dateto"]')
    LOCATORS = [
        (By.XPATH, '/html/body/div[2]/div/div[2]'),
        (By.XPATH, '/html/body/div[2]/div/div[3]'),
        (By.XPATH, '/html/body/div[2]/div/div[4]'),
        (By.XPATH, '/html/body/div[2]/div/div[5]'),
        (By.CSS_SELECTOR, '[class="block-btns__btn block-btns__btn_active"]'),
        (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]'),

    ]
    list_destinations = (By.XPATH, '//*[@id="search-results-rutours"]/ul')
    widget_date = (By.CSS_SELECTOR, '[id="ui-datepicker-div"]')
    CALENDAR_LOCATOR = (By.CSS_SELECTOR, '[class="ui-datepicker-calendar"]')
    CALENDAR_LOCATOR_NEXT = (By.CSS_SELECTOR, '[class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix '
                                              'ui-corner-all hotels-calendar tours-calendar"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
# Главная форма

    def pinned_form(self):
        pinned_form = self.wait_until_element_visible(ToursFormLocators.PINNED_FORM)
        return pinned_form

    def type_section(self):
        global locators
        for locators in self.LOCATORS:
            section = self.assert_element_visibility(locators)
            return section

    def form_keys(self):
        self.scroll_page()
        send_keys = self.send_keys_to_element(ToursFormLocators.INPUT_CITY, TestData.CITY)
        self.assert_elements_exist(ToursFormLocators.list_destinations)
        self.click_element(ToursFormLocators.INPUT_CITY)
        return send_keys

    def type_attraction(self):
        do_click_attraction = self.click_element(ToursFormLocators.CHOOSE_ATTR)
        return do_click_attraction

    def do_random_click(self):
        do_random_click = self.click_random_locator(SpecifiedLocators.ATTRACTION)
        return do_random_click

    def do_double_click_calendar(self):
        flag = self.double_click_element(ToursFormLocators.SELECT_DATE_FROM)
        return flag

    def do_random_choice_date(self):
        time.sleep(2)
        self.click_random_enabled_day_in_calendar(ToursFormLocators.CALENDAR_LOCATOR)

    def do_random_choice_next(self):
        self.click_element(ToursFormLocators.SELECT_DATE_TO)
        self.click_random_enabled_day_in_calendar(ToursFormLocators.CALENDAR_LOCATOR_NEXT)

    def is_exist(self):
        WebDriverWait(self.driver, 7)
        self.wait_until_element_clickable(ToursFormLocators.SEARCH_BUTTON)
# Форма поиска туров (World)

    def world_tour_switcher(self):
        WebDriverWait(self.driver, 7)
        self.click_element(WorldTypeLocators.WORLD_TOUR_SWITCHER)

    def world_tour_input_form(self):
        WebDriverWait(self.driver, 7)
        self.assert_element_visibility(WorldTypeLocators.WORLD_CITY_INPUT)
        self.send_keys_to_element(WorldTypeLocators.WORLD_CITY_INPUT, TestDataWorld.CITY_INPUT)
        self.assert_element_visibility(WorldTypeLocators.WORLD_LEN_LIST)
        self.click_element(WorldTypeLocators.WORLD_CITY_INPUT)
        self.send_keys_to_element(WorldTypeLocators.CITY_DEPARTURE_FIELD, TestDataWorld.DEPARTURE_INPUT)
        self.assert_element_visibility(WorldTypeLocators.WORLD_LEN_LIST_DEPARTURE)
        self.click_element(WorldTypeLocators.CITY_DEPARTURE_FIELD)

    def scroll_to_world_tour(self):
        self.scroll_page_second()

    def do_random_choice_calendar(self):
        time.sleep(3)
        self.assert_element_visibility(WorldTypeLocators.CALENDAR_LOCATOR_WORLD)
        self.click_element(WorldTypeLocators.CALENDAR_LOCATOR_WORLD)
        self.assert_element_visibility(WorldTypeLocators.CALENDAR_LOCATOR_WORLD_WIDGET)
        self.click_random_enabled_day_in_calendar(WorldTypeLocators.CALENDAR_LOCATOR_WORLD_WIDGET)

    def do_random_choice_duration_nights(self):
        time.sleep(3)
        self.assert_element_to_be_clickable(WorldTypeLocators.DURATION_DROPDOWN)
        self.click_element(WorldTypeLocators.DURATION_DROPDOWN)
        self.do_randint_click(WorldTypeLocators.INPUT_FROM)
        self.do_randint_click(WorldTypeLocators.INPUT_TO)

    # БАГ
    def do_random_choice_tourist_quantity(self):
        time.sleep(3)
        self.assert_element_visibility(WorldTypeLocators.TOURIST_QUANTITY)
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY)
        self.do_randint_click(WorldTypeLocators.TOURIST_QUANTITY_SCROLLER)

    def do_random_choice_kids(self):
        time.sleep(2)
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY_KIDS)
        time.sleep(2)
        self.click_element(WorldTypeLocators.TOURIST_QUANTITY_KIDS_RANDOM_CHOICE)

    def check_the_visibility_search_button(self):
        time.sleep(1)
        self.assert_element_to_be_clickable(WorldTypeLocators.CHECK_BUTTON)

    def check_the_blocks_add_buttons(self):
        time.sleep(1)
        self.assert_element_visibility(WorldTypeLocators.TOURS_BLOCKS_TRAVEL_BUTTONS)
# Форма поиска отелей

    def switch_to_hotels(self):
        time.sleep(1)
        self.click_element(HotelFormLocators.OPTION_SWITCHER_HOTEL)

    def do_send_keys_hotel(self):
        time.sleep(1)
        self.assert_element_visibility(HotelFormLocators.HOTEL_KEYS_INPUT)
        self.send_keys_to_element(HotelFormLocators.HOTEL_KEYS_INPUT, TestDataHotels.INPUT_CITY_COUNTRY_HOTEL)

    def do_click_on_check_in_option(self):
        self.wait_for_element(HotelFormLocators.HOTEL_CHECK_IN)
        time.sleep(3)
        self.click_element(HotelFormLocators.HOTEL_CHECK_IN)
        self.scroll_page_second()

    def do_wait_until_element_load_and_randomly_choose_check_in(self):
        time.sleep(3)
        self.click_random_enabled_day_in_calendar(HotelFormLocators.HOTEL_CHECK_IN_WIDGET)

    # def do_wait_until_element_load_and_randomly_choose_check_out(self):
        #  self.wait_for_element(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)
        # self.assert_element_visibility(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)
        # self.click_random_enabled_day_in_calendar(HotelFormLocators.HOTEL_CHECK_OUT_WIDGET)

    def open_dropdown_quantity(self):
        time.sleep(3)
        self.assert_element_visibility(HotelFormLocators.DROPDOWN_ADD_ADULTS)
        self.click_element(HotelFormLocators.DROPDOWN_ADD_ADULTS)
        self.do_randint_click(HotelFormLocators.ADD_ADULTS_OPTION)

    def open_dropdown_kids(self):
        self.click_element(HotelFormLocators.DROPDOWN_OPEN_KIDS)
        time.sleep(3)
        self.click_element(HotelFormLocators.DROPDOWN_GET_ALL_WIDGET)

    def check_visibility_search_button(self):
        self.assert_element_to_be_clickable(HotelFormLocators.HOTEL_SEARCH_BUTTON)

    # Форма поиска Жд билеты

    def switch_to_train_option(self):
        self.click_element(TrainLocators.TRAIN_SWITCHER)

    def do_send_keys_to_input_form_from(self):
        self.assert_element_visibility(TrainLocators.CITY_INPUT_FROM)
        self.send_keys_to_element(TrainLocators.CITY_INPUT_FROM, TestDataTrain.CITY_INPUT_THERE)
        self.click_element(TrainLocators.CITY_INPUT_FROM)

    def do_send_keys_to_input_form_to(self):
        self.assert_element_visibility(TrainLocators.CITY_INPUT_FROM)
        self.send_keys_to_element(TrainLocators.CITY_INPUT_TO, TestDataTrain.CITY_INPUT_BACK)
        self.click_element(TrainLocators.CITY_INPUT_TO)

    def do_click_to_calendar_option(self):
        self.assert_element_visibility(TrainLocators.TRAIN_CALENDAR_TO)
        self.click_element(TrainLocators.TRAIN_CALENDAR_TO)

    def do_random_choice_calendar_date(self):
        self.click_random_enabled_day_in_calendar(TrainLocators.TRAIN_CALENDAR_TO_WIDGET)

    def do_check_search_button_visibility(self):
        self.assert_element_to_be_clickable(TrainLocators.TRAIN_SEARCH_BUTTON)

# Форма маршруты

    def do_switch_to_routs(self):
        self.assert_element_visibility(RoutsLocators.ROUTS_SWITCHER)
        self.click_element(RoutsLocators.ROUTS_SWITCHER)

    def do_send_keys_routs_first(self):
        self.send_keys_to_element(RoutsLocators.FROM_WHERE, TestDataRouts.ROUTS_KEYS_TO)

    def do_send_keys_routs_second(self):
        self.click_element(RoutsLocators.FROM_WHERE)
        self.send_keys_to_element(RoutsLocators.TO_THERE, TestDataRouts.ROUTS_KEYS_FROM)

    def do_check_search_routs_button(self):
        self.assert_element_visibility(RoutsLocators.SEARCH_ROUTS_BUTTON)

# Форма Страны и города
    def switch_to_country_and_cities_option(self):
        self.assert_element_visibility(CountryAndCities.COUNTRY_SWITCHER)
        self.click_element(CountryAndCities.COUNTRY_SWITCHER)

    def check_the_total_form(self):
        self.assert_elements_exist(CountryAndCities.SELECT_COUNTRY)
        self.click_element(CountryAndCities.SELECT_COUNTRY)

    def random_select_country(self):
        self.random_country_selection(CountryAndCities.CITIES_AND_COUNTRY_CONTAINER)
        self.assert_element_to_be_clickable(CountryAndCities.SELECT_CITIES)
        self.click_element(CountryAndCities.SELECT_CITIES)
        self.random_country_selection(CountryAndCities.CITIES_AND_COUNTRY_CONTAINER)

    def random_select_cities_and_check_the_search_button(self):
        self.assert_elements_exist(CountryAndCities.SEARCH_COUNTRY_AND_CITIES_BUTTON)