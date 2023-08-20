from selenium.webdriver.common.by import By


class CountryAndCities:
    COUNTRY_SWITCHER = (By.XPATH, '/html/body/div[2]/div/div[5]')
    SELECT_COUNTRY = (By.CSS_SELECTOR, '[id="select2-search-country-container"]')
    CITIES_AND_COUNTRY_CONTAINER = (By.CSS_SELECTOR, '[class="select2-results"]')

    SELECT_CITIES = (By.CSS_SELECTOR, '[id="select2-search-city-container"]')

    SEARCH_COUNTRY_AND_CITIES_BUTTON = (By.XPATH, '/html/body/section[2]/div/div[5]/form/button')

