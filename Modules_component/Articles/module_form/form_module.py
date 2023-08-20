from selenium.webdriver.common.by import By
from Test_Travel.Modules_component.BaseMethods.Custom_methods import BaseMethods


class ModuleFormAsserting(BaseMethods):
    COUNTRY = (By.CSS_SELECTOR, '[id="select2-countries_list-container"]')
    CITIES = (By.CSS_SELECTOR, '[id="select2-cities_list-container"]')
    THEMES = (By.CSS_SELECTOR, '[id="select2-subjects_list-container"]')
    LIST_CONTAINER_COUNTRY_CITIES_THEMES = (By.CSS_SELECTOR, '[class="select2-results"]')
    SEARCH_ARTICLES_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_dropdown_links(self, x=2):
        self.random_country_selection(ModuleFormAsserting.COUNTRY)
        self.sleep(x)
        self.verify_dropdown_list(ModuleFormAsserting.LIST_CONTAINER_COUNTRY_CITIES_THEMES)
        self.random_country_selection(ModuleFormAsserting.CITIES)
        self.sleep(x)
        self.verify_dropdown_list(ModuleFormAsserting.CITIES)
        self.random_country_selection(ModuleFormAsserting.THEMES)
        self.verify_dropdown_list(ModuleFormAsserting.THEMES)

