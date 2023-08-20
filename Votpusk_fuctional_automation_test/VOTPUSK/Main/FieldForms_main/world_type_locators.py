import random
from selenium.webdriver.common.by import By


class WorldTypeLocators:
    WORLD_TOUR_SWITCHER = (By.CSS_SELECTOR, '[class="block-btns__btn world-tours"]')
    WORLD_CITY_INPUT = (By.CSS_SELECTOR, '[id="toursearchapi-destinations"]')
    CITY_DEPARTURE_FIELD = (By.CSS_SELECTOR, '[id="toursearchapi-departurecityname"]')
    CALENDAR_LOCATOR_WORLD = (By.CSS_SELECTOR, '[id="toursearchapi-checkindaterangefrom"]')
    CALENDAR_LOCATOR_WORLD_WIDGET = (By.CSS_SELECTOR, '[class="ui-datepicker-calendar"]')
    DURATION_DROPDOWN = (By.CSS_SELECTOR, '[class="set-nights__number"]')
    INPUT_FROM = (By.CSS_SELECTOR, '[class="input-plus-t input-change input-plus-first"]')
    INPUT_TO = (By.CSS_SELECTOR, '[class="input-plus-t input-change input-plus-second"]')
    TOURIST_QUANTITY = (By.CSS_SELECTOR, '[class="dropdown__btn hotels-search__item  br-left"]')
    TOURIST_QUANTITY_SCROLLER = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[1]/div/span[2]')
    TOURIST_QUANTITY_KIDS = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]')
    TOURIST_QUANTITY_KIDS_RANDOM_CHOICE = (By.XPATH, '//*[@id="tours-search-form"]/div[5]/div[2]/div[2]/div[2]/div/span[3]')

    CHECK_BUTTON = (By.XPATH, '//*[@id="tours-search-form"]/button')

    TOURS_BLOCKS_TRAVEL_BUTTONS = (By.CSS_SELECTOR, '[class="block-btns__travel"]')

    WORLD_LEN_LIST = (By.CSS_SELECTOR, '[class="list destinations__list dropdown open"]')
    WORLD_LEN_LIST_DEPARTURE = (By.CSS_SELECTOR, 'class="item departure-cities__item"')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @classmethod
    def get_random_locator(cls):
        return random.choice(cls.DURATION_RANDOM_LIST)
