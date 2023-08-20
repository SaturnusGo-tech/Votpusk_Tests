from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Routs.Config.config import TestData
from selenium.webdriver.common.by import By


class SecondPageRoutsLocators(BaseMethods):
    BLA_BLOCK = (By.CSS_SELECTOR, '[class="uxie-bbc-widget "]')
    BLA_INPUT_FROM = (By.CSS_SELECTOR, '[class="uxie-bbc-search-place__field uxie-bbc-with-data"]')
    BLA_INPUT_TO = (By.CSS_SELECTOR, '[class="uxie-bbc-search-place2__field uxie-bbc-with-data"]')
    BLA_SUBMIT = (By.CSS_SELECTOR, '[class="uxie-bbc-search-submit__button"]')

    NAVBAR_BLOCK = (By.CSS_SELECTOR, '[class="nav"]')
    CAR_OPTIONS = (By.CSS_SELECTOR, '[class="map-calculator__tab-label map-calculator__tab-label--active '
                                    'button-position"]')
    WALKING_OPTION = (By.XPATH, '/html/body/main/div[2]/div/section[3]/div/div[1]/ul/li[2]')
    BIKE_OPTION = (By.XPATH, '/html/body/main/div[2]/div/section[3]/div/div[1]/ul/li[3]')
    TRACK_OPTION = (By.XPATH, '/html/body/main/div[2]/div/section[3]/div/div[1]/ul/li[4]')
    TRAIN_OPTION = (By.XPATH, '/html/body/main/div[2]/div/section[3]/div/div[1]/ul/li[5]')

    MAP_CALCULATE_ROUTS = (By.XPATH, '//*[@id="car"]/div[2]/div[1]')
    MAP_CALCULATE_COST = (By.XPATH, '//*[@id="car"]/div[2]/div[2]')
    MAP_CALCULATE_COST_GAS = (By.XPATH, '//*[@id="car"]/div[2]/div[3]')

    MAP = (By.XPATH, '//*[@id="mapid"]/div[1]/div[8]/ymaps/ymaps/ymaps/ymaps[1]')

    INPUT_FROM = (By.CSS_SELECTOR, '[class="search__item from-st"]')
    INPUT_TO = (By.CSS_SELECTOR, '[class="search__item to-st"]')

    TRAIN_SUBMIT = (By.XPATH, '//*[@id="search-form_tickets"]/button')

    HOTEL_WRAPPER = (By.CSS_SELECTOR, '[id="router-hotels"]')
    HOTEL_WRAPPER_ARROW_LEFT = (By.CSS_SELECTOR, '[class="swiper-custom-btn swiper-custom-btn--prev"]')
    HOTEL_WRAPPER_ARROW_RIGHT = (By.CSS_SELECTOR, '[class="swiper-custom-btn swiper-custom-btn--next"]')

    EXCURSION_BLOCK = (By.CSS_SELECTOR, '[class="trip_widget"]')
    EXCURSION_IMG = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div[1]/figure[1]/a')
    EXCURSION_RATING = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div[1]/figure[1]/figcaption/div[1]/a')
    EXCURSION_TEXT = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div[1]/figure[1]/figcaption')
    EXCURSION_SUBMIT = (By.XPATH, '/html/body/main/div[2]/div/div[2]/div/div[2]/a')
    EXCURSION_WRITE_RATE = (By.CSS_SELECTOR, '[class="comment-push link-type-one button-position"]')

    RECOMMENDATION_BLOCK = (By.CSS_SELECTOR, '[class="recommendation"]')

    COMMENT_BLOCK = (By.CSS_SELECTOR, '[class="commentary-block__textarea"]')

    COMMENT_INPUT = (By.XPATH, '//*[@id="commentary"]/form/div[2]/input[1]')
    COMMENT_INPUT_EMAIL = (By.XPATH, '//*[@id="commentary"]/form/div[2]/input[2]')
    COMMENT_SUBMIT = (By.CSS_SELECTOR, '[class="commentary-block__submit link-type-one button-position"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_into_view(self, s=2):
        self.window_scroll_by(0, 550)
        self.sleep(s)

    def assert_bla_block(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.BLA_BLOCK)
        self.sleep(s)

    def assert_input_filed(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.BLA_INPUT_FROM)
        self.is_element_present(SecondPageRoutsLocators.BLA_INPUT_TO)
        self.sleep(s)

    def assert_bla_submit(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.BLA_SUBMIT)
        self.sleep(s)

    def navbar(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.NAVBAR_BLOCK)
        self.sleep(s)

    def assert_option_block(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.CAR_OPTIONS)
        self.is_element_present(SecondPageRoutsLocators.WALKING_OPTION)
        self.is_element_present(SecondPageRoutsLocators.BIKE_OPTION)
        self.is_element_present(SecondPageRoutsLocators.TRACK_OPTION)
        self.is_element_present(SecondPageRoutsLocators.TRAIN_OPTION)
        self.sleep(s)

    def assert_clickable_options(self, s=2):
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.CAR_OPTIONS)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.WALKING_OPTION)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.BIKE_OPTION)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.TRACK_OPTION)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.TRAIN_OPTION)
        self.sleep(s)

    def scroll_into_view_map(self, s=2):
        self.window_scroll_by(0, 1150)
        self.sleep(s)

    def assert_map(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.MAP)
        self.sleep(s)

    def scroll_into_view_train(self, s=2):
        self.window_scroll_by(0, 1450)
        self.sleep(s)

    def assert_input_train_field(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.INPUT_FROM)
        self.is_element_present(SecondPageRoutsLocators.INPUT_TO)
        self.sleep(s)

    def assert_input_field_send_keys_from(self, s=2):
        self.send_keys_to_element(SecondPageRoutsLocators.INPUT_FROM, TestData.TRAIN_FROM)
        self.sleep(s)

    def assert_input_field_send_keys_to(self, s=2):
        self.send_keys_to_element(SecondPageRoutsLocators.INPUT_FROM, TestData.TRAIN_TO)
        self.sleep(s)

    def assert_submit(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.TRAIN_SUBMIT)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.TRAIN_SUBMIT)
        self.sleep(s)

    def sroll_into_view_wrapper(self, s=2):
        self.window_scroll_by(0, 1750)
        self.sleep(s)

    def assert_slider_wrapper(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.HOTEL_WRAPPER)
        self.sleep(s)

    def assert_navigation_arrow(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_LEFT)
        self.is_element_present(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_RIGHT)
        self.sleep(s)

    def assert_navigation_links_clickable(self, s=2):
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_LEFT)
        self.click_element(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_RIGHT)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_RIGHT)
        self.click_element(SecondPageRoutsLocators.HOTEL_WRAPPER_ARROW_LEFT)
        self.sleep(s)

    def scroll_into_view_excursion_block(self, s=2):
        self.window_scroll_by(0, 2000)
        self.sleep(s)

    def assert_excursion_block(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_BLOCK)
        self.sleep(s)

    def assert_excursion_item(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_IMG)
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_RATING)
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_TEXT)
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_SUBMIT)
        self.is_element_present(SecondPageRoutsLocators.EXCURSION_WRITE_RATE)
        self.sleep(s)

    def assert_clickable_item(self, s=2):
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.EXCURSION_SUBMIT)
        self.assert_element_to_be_clickable(SecondPageRoutsLocators.EXCURSION_WRITE_RATE)
        self.sleep(s)

    def assert_recommendation_block(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.RECOMMENDATION_BLOCK)
        self.sleep(s)

    def scroll_into_view_comment_sections(self, s=2):
        self.window_scroll_by(0, 2350)
        self.sleep(s)

    def comment_input_filed(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.COMMENT_BLOCK)
        self.send_keys_to_element(SecondPageRoutsLocators.COMMENT_BLOCK, TestData.COMMENT)
        self.sleep(s)

    def assert_name_input(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.COMMENT_INPUT)
        self.send_keys_to_element(SecondPageRoutsLocators.COMMENT_INPUT, TestData.NAME)
        self.sleep(s)

    def assert_email_input(self, s=2):
        self.is_element_present(SecondPageRoutsLocators.COMMENT_INPUT_EMAIL)
        self.send_keys_to_element(SecondPageRoutsLocators.COMMENT_INPUT_EMAIL, TestData.EMAIL)
        self.sleep(s)


