from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Routs.Config.config import TestData
from selenium.webdriver.common.by import By


class RoutsMainPageLocators(BaseMethods):
    HOTEL_BANNER = (By.XPATH, '/html/body/main/div[3]/div/section[1]/div[1]/div[1]/div/a/img')
    LOCAL_ADD = (By.XPATH, '/html/body/main/div[3]/div/section[1]/div[1]/div[2]/a')
    TITLE_SUBTITLE = (By.CSS_SELECTOR, '[class="block-head__subtitle"]')

    BLOCK_CALCULATOR = (By.CSS_SELECTOR, '[class="calculator-route__body  calculator-route__body--test"]')
    FROM_INPUT = (By.CSS_SELECTOR, '[id="w0"]')
    TO_INPUT = (By.CSS_SELECTOR, '[id="w1"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="calculator-route__submit button-position main active"]')
    CITIES_CATALOG = (By.XPATH, '//*[@id="search_form1"]/div[3]/a')
    RADIO_BUTTON_1 = (By.XPATH, '//*[@id="tabenders"]/div[1]/label')
    RADIO_BUTTON_2 = (By.XPATH, '//*[@id="tabenders"]/div[2]/label')

    SWITCH_OPTION = (By.CSS_SELECTOR, '[class="calculator-route__tab button-position"]')
    SEARCH_OBJECT = (By.CSS_SELECTOR, '[id="name_object"]')

    TABLES_ROUTS = (By.CSS_SELECTOR, '[class="table-routes table-routes--first"]')

    EQUIVALENT_TEST_ROUTS_1 = (By.XPATH, '/html/body/main/div[3]/div/section[2]/div/a[1]')
    EQUIVALENT_TEST_ROUTS_2 = (By.XPATH, '/html/body/main/div[3]/div/section[2]/div/a[20]')
    EQUIVALENT_TEST_ROUTS_3 = (By.XPATH, '/html/body/main/div[3]/div/section[2]/div/a[40]')

    DROPDOWN_MENU_1 = (By.XPATH, '//*[@id="ui-id-1"]')
    DROPDOWN_MENU_2 = (By.XPATH, '//*[@id="ui-id-2"]')
    DROPDOWN_MENU_3 = (By.XPATH, '//*[@id="ui-id-3"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_into_view_block(self, s=2):
        self.window_scroll_by(0, 350)
        self.sleep(s)

    def assert_hotel_banner(self, s=2):
        self.is_element_present(RoutsMainPageLocators.HOTEL_BANNER)
        self.sleep(s)

    def assert_local_add(self, s=2):
        self.is_element_present(RoutsMainPageLocators.LOCAL_ADD)
        self.sleep(s)

    def assert_calculate_block(self, s=2):
        self.is_element_present(RoutsMainPageLocators.BLOCK_CALCULATOR)
        self.sleep(s)

    def assert_subtitle(self, s=2):
        self.is_visible(RoutsMainPageLocators.TITLE_SUBTITLE)
        self.sleep(s)

    def scroll_into_view_bla_block(self, s=2):
        self.window_scroll_by(0, 450)
        self.sleep(s)

    def assert_input_filed_from(self, s=2):
        self.is_element_present(RoutsMainPageLocators.FROM_INPUT)
        self.send_keys_to_element(RoutsMainPageLocators.FROM_INPUT, TestData.FROM)
        self.is_dropdown_present(RoutsMainPageLocators.DROPDOWN_MENU_1)
        self.sleep(s)

    def assert_input_filed_to(self, s=2):
        self.is_element_present(RoutsMainPageLocators.TO_INPUT)
        self.send_keys_to_element(RoutsMainPageLocators.TO_INPUT, TestData.TO)
        self.is_dropdown_present(RoutsMainPageLocators.DROPDOWN_MENU_2)
        self.sleep(s)

    def assert_search_button(self, s=2):
        self.is_element_present(RoutsMainPageLocators.SEARCH_BUTTON)
        self.sleep(s)

    def assert_radio_buttons(self, s=2):
        self.is_element_present(RoutsMainPageLocators.RADIO_BUTTON_1)
        self.is_element_present(RoutsMainPageLocators.RADIO_BUTTON_2)
        self.sleep(s)

    def assert_radio_button_clickable(self, s=2):
        self.assert_element_to_be_clickable(RoutsMainPageLocators.RADIO_BUTTON_1)
        self.assert_element_to_be_clickable(RoutsMainPageLocators.RADIO_BUTTON_2)
        self.sleep(s)

    def assert_next_calculate_block(self, s=2):
        self.is_element_present(RoutsMainPageLocators.SWITCH_OPTION)
        self.click_element(RoutsMainPageLocators.SWITCH_OPTION)
        self.sleep(s)

    def assert_object_input(self, s=2):
        self.is_element_present(RoutsMainPageLocators.SEARCH_OBJECT)
        self.send_keys_to_element(RoutsMainPageLocators.SEARCH_OBJECT, TestData.OBJECT)
        self.sleep(s)

    def scroll_into_view(self, s=2):
        self.window_scroll_by(0, 550)
        self.sleep(s)

    def assert_table_routs(self, s=2):
        self.is_element_present(RoutsMainPageLocators.TABLES_ROUTS)
        self.sleep(s)

    def assert_equivalent_test(self, s=2):
        self.is_element_present(RoutsMainPageLocators.EQUIVALENT_TEST_ROUTS_1)
        self.is_element_present(RoutsMainPageLocators.EQUIVALENT_TEST_ROUTS_2)
        self.is_element_present(RoutsMainPageLocators.EQUIVALENT_TEST_ROUTS_3)
        self.sleep(s)



