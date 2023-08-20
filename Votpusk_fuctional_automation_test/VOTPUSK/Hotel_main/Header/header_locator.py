from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class HeaderHotelLocator(BaseMethods):
    HOTEL_HEADER = (By.CSS_SELECTOR, '[class="header header--bordered"]')
    HOTEL_TEXT_VISIBILITY = (By.XPATH, '//*[@id="page-header"]/section[1]/div[2]')
    HOTEL_TEXT_BANNER = (By.CSS_SELECTOR, '[class="hotels-banner__about"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_the_header(self):
        self.is_element_present(HeaderHotelLocator.HOTEL_HEADER)

    def check_the_text_visibility(self):
        self.is_element_present(HeaderHotelLocator.HOTEL_TEXT_VISIBILITY)

    def check_the_hotel_banner(self):
        self.is_element_present(HeaderHotelLocator.HOTEL_TEXT_BANNER)

