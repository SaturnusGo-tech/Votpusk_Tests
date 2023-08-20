from selenium.webdriver.common.by import By


class TrainLocators:
    TRAIN_SWITCHER = (By.XPATH, '/html/body/div[2]/div/div[3]')
    CITY_INPUT_FROM = (By.CSS_SELECTOR, '[class="search__item first_tickets"]')
    CITY_INPUT_TO = (By.CSS_SELECTOR, '[class="search__item second_tickets"]')
    TRAIN_CALENDAR_TO = (By.CSS_SELECTOR, '[id="t-datefrom"]')
    TRAIN_CALENDAR_TO_WIDGET = (By.CSS_SELECTOR, '[id="t-datefrom"]')
    TRAIN_SEARCH_BUTTON = (By.XPATH, '//*[@id="search-form_tickets"]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
