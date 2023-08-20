from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Train.config.configuration import TestData


class ObtainFormLocators(BaseMethods):
    FORM_CONTAINER = (By.CSS_SELECTOR, '[class="wg-search__inner"]')
    FROM = (By.CSS_SELECTOR, '[class="wg-search__textinput wg-search__textinput_wide t_depart_place"]')
    TO = (By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div[2]/input')
    DATE_TO = (By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div[1]/div/div/input')
    DATE_RETURN = (By.XPATH, '//*[@id="ufs-railway-app"]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[1]/div/div/input')
    FORM_BUTTON = (By.CSS_SELECTOR, '[class="wg-button wg-button_always-big"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_form_container(self, s=2):
        self.is_element_present(ObtainFormLocators.FORM_CONTAINER)
        self.sleep(s)

    def assert_is_filed_from_present(self, s=3):
        self.is_element_present(ObtainFormLocators.FROM)
        self.send_keys_to_element(ObtainFormLocators.FROM, TestData.OBTAIN_FROM)
        self.sleep(s)

    def assert_is_field_to_present(self, s=2):
        self.is_element_present(ObtainFormLocators.TO)
        self.send_keys_to_element(ObtainFormLocators.TO, TestData.OBTAIN_TO)
        self.sleep(s)

    def assert_scroll_into_view(self, s=2):
        self.window_scroll_by(0, 350)
        self.sleep(s)

    def open_calendar_from(self, s=2):
        self.click_element(ObtainFormLocators.DATE_TO)
        self.sleep(s)

    def assert_select_randomly_date_to(self, s=2):
        self.is_element_present(ObtainFormLocators.DATE_TO)
        self.click_random_enabled_day_in_calendar(ObtainFormLocators.DATE_TO)
        self.sleep(s)

    def open_calendar_to(self, s=2):
        self.click_element(ObtainFormLocators.DATE_RETURN)
        self.sleep(s)

    def assert_select_randomly_date_from(self, s=2):
        self.is_element_present(ObtainFormLocators.DATE_RETURN)
        self.click_random_enabled_day_in_calendar(ObtainFormLocators.DATE_RETURN)
        self.sleep(s)

    def assert_form_button(self, s=2):
        self.assert_element_to_be_clickable(ObtainFormLocators.FORM_BUTTON)
        self.sleep(s)
