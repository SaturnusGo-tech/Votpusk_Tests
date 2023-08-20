from abc import ABC

from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ArticlesFormLocators(BaseMethods, ABC):
    FORM_CONTAINER = (By.CSS_SELECTOR, '[class="form__block-wrapper"]')
    FORM_LIST_CONTAINER_COUNTRY = (By.CSS_SELECTOR, '[id="select2-countries_list-container"]')
    FORM_LIST_CONTAINER_CITIES = (By.CSS_SELECTOR, '[id="select2-cities_list-container"]')
    FORM_LIST_CONTAINER_THEMES = (By.CSS_SELECTOR, '[id="select2-subjects_list-container"]')
    LIST_CONTAINER_COUNTRY_CITIES_THEMES = (By.CSS_SELECTOR, '[class="select2-results"]')

    SEARCH_ARTICLES_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_locator(self, s=2):
        self.window_scroll_by(0, 450)
        self.sleep(s)

    def click_and_check_the_len_container_country(self, s=2):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_COUNTRY)
        self.random_country_selection(ArticlesFormLocators.FORM_LIST_CONTAINER_COUNTRY)
        self.sleep(2)

    def click_and_check_len_container_cities(self, s=2):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_CITIES)
        self.random_country_selection(ArticlesFormLocators.LIST_CONTAINER_COUNTRY_CITIES_THEMES)
        self.sleep(2)

    def click_and_check_len_container_themes(self, s=2):
        self.click_element(ArticlesFormLocators.FORM_LIST_CONTAINER_THEMES)
        self.random_country_selection(ArticlesFormLocators.LIST_CONTAINER_COUNTRY_CITIES_THEMES)
        self.sleep(2)
