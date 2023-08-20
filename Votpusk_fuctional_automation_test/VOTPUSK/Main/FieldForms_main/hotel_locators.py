from selenium.webdriver.common.by import By


class HotelFormLocators:
    OPTION_SWITCHER_HOTEL = (By.XPATH, '/html/body/div[2]/div/div[2]')
    HOTEL_KEYS_INPUT = (By.CSS_SELECTOR, '[class="hotels-search__item search-text"]')
    HOTEL_CHECK_IN = (By.CSS_SELECTOR, '[id="h-checkin"]')
    HOTEL_CHECK_IN_WIDGET = (By.ID, 'ui-datepicker-div')
    # HOTEL_CHECK_OUT = (By.CSS_SELECTOR, '[id="h-checkout"]')
    # HOTEL_CHECK_OUT_WIDGET = (By.CSS_SELECTOR, '[class="ui-datepicker-group ui-datepicker-group-last"]')

    DROPDOWN_ADD_ADULTS = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[1]')
    ADD_ADULTS_OPTION = (By.CSS_SELECTOR, '[class="input-plus"]')
    DROPDOWN_OPEN_KIDS = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]')
    DROPDOWN_GET_ALL_WIDGET = (By.XPATH, '//*[@id="reservation-form"]/div[4]/div[2]/div[2]/div[2]/div/span[3]')

    HOTEL_SEARCH_BUTTON = (By.XPATH, '//*[@id="reservation-form"]/input[4]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
