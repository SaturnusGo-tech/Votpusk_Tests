from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class TrainCheckingTrainLocators(BaseMethods):
    SCHEDULE_BUTTON = (By.CSS_SELECTOR, '[class="head__btn-table head__btn-table--active"]')

    BY_ROUTS = (By.CSS_SELECTOR, '[class="search__item-link search__item-link--one"]')
    FROM = (By.CSS_SELECTOR, '[class="search__content-input  search__content-input--one"]')
    TO = (By.CSS_SELECTOR, '[class="search__content-input  search__content-input--where"]')
    DAY = (By.CSS_SELECTOR, '[class="form-group field-routesearch-day"]')
    MONTH = (By.CSS_SELECTOR, '[class="form-group field-routesearch-month"]')
    YEAR = (By.CSS_SELECTOR, '[class="form-group field-routesearch-year"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search-by-route"]/button')

    BY_STATION = (By.XPATH, '/html/body/main/section[1]/div[4]/div[1]/a[2]')
    STATION = (By.CSS_SELECTOR, '[class="search__content-input search__content-input--station"]')
    STATION_DAY = (By.XPATH, '//*[@id="stationsearch-day-styler"]/div[1]')
    STATION_MONTH = (By.XPATH, '//*[@id="stationsearch-month-styler"]/div[1]')
    STATION_YEAR = (By.XPATH, '//*[@id="stationsearch-year-styler"]/div[1]')
    STATION_SEARCH_BUTTON = (By.XPATH, '//*[@id="search-by-station"]/button')

    BY_NUMBER = (By.XPATH, '[class="search__item-link"]')
    BY_NUMBER_FORM = (By.CSS_SELECTOR, '[id="trainsearch-trainnumber"]')

    OBTAIN_TICKETS = (By.CSS_SELECTOR, '[class="head__btn-booking"]')
    OBTAIN_FROM = (By.CSS_SELECTOR, '[class="search__booking-input search__content-input--one"]')
    OBTAIN_TO = (By.CSS_SELECTOR, '[class="search__booking-input search__booking-input--where '
                                  'search__content-input--where"]')
    OBTAIN_DATE_FROM = (By.CSS_SELECTOR, '[class="travel-div travel-div-in"]')
    OBTAIN_SELECT_DATE_TO = (By.CSS_SELECTOR, '[class="search__booking-box_two-ways"]')
    OBTAIN_DATE_TO = (By.CSS_SELECTOR, '[class="travel-div travel-div-out"]')
    OBTAIN_SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="search__booking-btn"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_schedule_button(self, s=2):
        self.assert_element_to_be_clickable(TrainCheckingTrainLocators.SCHEDULE_BUTTON)
        self.sleep(s)

    def assert_by_routs_form(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.FROM)
        self.sleep(s)

    def assert_by_routs_form_to(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.TO)
        self.sleep(s)

    def assert_select_random_date_day(self, s=2):
        self.click_element(TrainCheckingTrainLocators.DAY)
        self.random_country_selection(TrainCheckingTrainLocators.DAY)
        self.sleep(s)

    def assert_select_random_date_month(self, s=2):
        self.click_element(TrainCheckingTrainLocators.MONTH)
        self.random_country_selection(TrainCheckingTrainLocators.MONTH)
        self.sleep(s)

    def assert_select_random_date_year(self, s=2):
        self.click_element(TrainCheckingTrainLocators.YEAR)
        self.random_country_selection(TrainCheckingTrainLocators.YEAR)
        self.sleep(s)

    def assert_search_by_routs_button(self, s=2):
        self.assert_element_to_be_clickable(TrainCheckingTrainLocators.SEARCH_BUTTON)

    # По станции

    def assert_click_by_station_button(self, s=2):
        self.click_element(TrainCheckingTrainLocators.BY_STATION)
        self.sleep(s)

    def assert_by_station_input(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.STATION)
        self.sleep(s)

    def assert_select_random_date_station_day(self, s=2):
        self.click_element(TrainCheckingTrainLocators.STATION_DAY)
        self.random_country_selection(TrainCheckingTrainLocators.STATION_DAY)
        self.sleep(s)

    def assert_select_random_date_station_month(self, s=2):
        self.click_element(TrainCheckingTrainLocators.STATION_MONTH)
        self.random_country_selection(TrainCheckingTrainLocators.STATION_MONTH)
        self.sleep(s)

    def assert_select_random_date_station_year(self, s=2):
        self.click_element(TrainCheckingTrainLocators.STATION_YEAR)
        self.random_country_selection(TrainCheckingTrainLocators.STATION_YEAR)
        self.sleep(s)

    def assert_station_search_button(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.STATION_SEARCH_BUTTON)
        self.sleep(s)

    # По номеру поезда

    def assert_by_train_number(self, s=2):
        self.assert_element_to_be_clickable(TrainCheckingTrainLocators.BY_NUMBER)
        self.click_element(TrainCheckingTrainLocators.BY_NUMBER)
        self.sleep(s)

    def assert_search_by_number_form(self):
        self.is_element_present(TrainCheckingTrainLocators.BY_NUMBER_FORM)

    # Покупка билетов

    def assert_obtain_button(self, s=2):
        self.assert_element_to_be_clickable(TrainCheckingTrainLocators.OBTAIN_TICKETS)
        self.sleep(s)

    def assert_click_obtain_tickets(self, s=2):
        self.click_element(TrainCheckingTrainLocators.OBTAIN_TICKETS)
        self.sleep(s)

    def assert_obtain_form(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.OBTAIN_FROM)
        self.sleep(s)

    def assert_obtain_to(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.OBTAIN_TO)
        self.sleep(s)

    def assert_select_randomly_date_from(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.OBTAIN_DATE_FROM)
        self.sleep(s)

    def assert_obtain_next_date(self, s=2):
        self.click_element(TrainCheckingTrainLocators.OBTAIN_SELECT_DATE_TO)
        self.sleep(s)

    def assert_select_randomly_date_to(self, s=2):
        self.is_element_present(TrainCheckingTrainLocators.OBTAIN_DATE_TO)
        self.sleep(s)

    def assert_obtain_search_button(self):
        self.assert_element_to_be_clickable(TrainCheckingTrainLocators.OBTAIN_SEARCH_BUTTON)

