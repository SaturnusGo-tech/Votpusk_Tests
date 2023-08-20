from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class FiltersLocators(BaseMethods):
    CLOSE_MODAL = (By.XPATH, '//*[@id="hotels-modal-search"]/button')
    PRICE_SLIDER = (By.XPATH, '//*[@id="price-range"]/div/div[1]')
    PRICE_RANGE_HIDDEN = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[2]/button')

    CHECK_BOX_NULL = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[1]/label')
    CHECK_BOX_1_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[2]/label')
    CHECK_BOX_2_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[3]/label')
    CHECK_BOX_3_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[4]/label')
    CHECK_BOX_4_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[5]/label')
    CHECK_BOX_5_STAR = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/div/ul/li[6]/label')
    STAR_RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[3]/button')

    ANY_RATING = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[1]/label/span[2]')
    RATING_6 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[2]/label/span[2]')
    RATING_7 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[3]/label/span[2]')
    RATING_8 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[4]/label/span[2]')
    RATING_9 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/div/ul/li[5]/label/span[2]')
    RATING_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[4]/button')

    DISTANCE_TO_THE_CENTER_SLIDER = (
        By.XPATH, '//*[@id="distance-range"]/div/div[1]/div')

    CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[1]/label/span[1]')
    CHECK_BOX_2 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/ul/li[5]/label/span[1]')
    TYPE_OF_APARTMENTS_HIDDEN_ARROW = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/button')
    TYPE_OF_APARTMENTS_HIDDEN_LINK = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[6]/div/button/span[1]')

    AMENITIES_CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[2]/label/span[1]')
    AMENITIES_CHECK_BOX_4 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/ul/li[5]/label/span[1]')

    AMENITIES_HIDDEN_LINK = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/button')
    AMENITIES_HIDDEN_UPPER_LINK = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[7]/div/button/span[1]')

    AMENITIES_IN_THE_ROOM_CHECK_BOX_1 = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/ul/li[1]/label/span[1]')
    AMENITIES_IN_THE_ROOM_CHECK_BOX_4 = (By.XPATH, '//*[@id="filter_data_short_amenities"]/div[4]/label')

    AMENITIES_IN_THE_ROOM_HIDDEN_LINK = (By.XPATH, '//*[@id="filter_data_short_amenities"]/div[7]/div[2]')
    AMENITIES_IN_THE_ROOM_HIDDEN_UPPER_LINK = (By.XPATH, '//*[@id="filter-hotels"]/fieldset[8]/div/button/span[1]')

    CLEAR_DEFAULT_OPTIONS = (By.CSS_SELECTOR, '[class="filters__apply-btn"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_modal(self, s=2):
        self.click_element(FiltersLocators.CLOSE_MODAL)
        self.sleep(s)

    def scroll_to_average_price_slider(self, offset_x, offset_y, s=2):
        slider_element = self.driver.find_element(*FiltersLocators.PRICE_SLIDER)
        self.move_slider(slider_element, offset_x, offset_y)
        self.sleep(s)

    def load_page(self, s=10):
        self.sleep(s)

    def assert_hidden_arrow(self, s=2):
        self.is_element_present(FiltersLocators.PRICE_RANGE_HIDDEN)
        self.sleep(s)

    def assert_hidden_arrow_clickable(self, s=2):
        self.click_element(FiltersLocators.PRICE_RANGE_HIDDEN)
        self.sleep(s)

    # Звёздность отеля
    def window_scroll_into_view_star_rating(self, s=2):
        self.window_scroll_by(0, 500)
        self.sleep(s)

    def assert_star_rating_check_boxes_0(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_NULL)
        self.sleep(s)

    def assert_star_rating_check_boxes_1(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_1_STAR)
        self.sleep(s)

    def assert_star_rating_check_boxes_2(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_2_STAR)
        self.sleep(s)

    def assert_star_rating_check_boxes_3(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_3_STAR)
        self.sleep(s)

    def assert_star_rating_check_boxes_4(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_4_STAR)
        self.sleep(s)

    def assert_star_rating_check_boxes_5(self, s=2):
        self.is_element_present(FiltersLocators.CHECK_BOX_5_STAR)
        self.sleep(s)

    # Рейтинг
    def assert_active_button_rating_hotel(self, s=2):
        self.is_element_present(FiltersLocators.ANY_RATING)
        self.sleep(s)

    def assert_rating_hotel_6(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.RATING_6)
        self.click_element(FiltersLocators.RATING_6)
        self.sleep(s)

    def assert_rating_hotel_7(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.RATING_7)
        self.click_element(FiltersLocators.RATING_7)
        self.sleep(s)

    def assert_rating_hotel_8(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.RATING_8)
        self.click_element(FiltersLocators.RATING_8)
        self.sleep(s)

    def assert_rating_hotel_9(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.RATING_9)
        self.click_element(FiltersLocators.RATING_9)
        self.sleep(s)

    def scroll_into_view_distance_roller(self, s=2):
        self.window_scroll_by(0, 800)
        self.sleep(s)

    def distance_slider(self, offset_x, offset_y, s=2):
        slider_element = self.driver.find_element(*FiltersLocators.DISTANCE_TO_THE_CENTER_SLIDER)
        self.move_slider(slider_element, offset_x, offset_y)
        self.sleep(s)

    def scroll_into_view_type_of_apart(self, s=2):
        self.window_scroll_by(0, 1000)
        self.sleep(s)

    def assert_clickable_boxes(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_1)
        self.sleep(s)

    def assert_clickable_boxes_2(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.CHECK_BOX_2)
        self.sleep(s)

    def assert_clickable_check_boxes(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.AMENITIES_CHECK_BOX_1)
        self.sleep(s)

    def assert_clickable_check_boxes_4(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.AMENITIES_CHECK_BOX_4)
        self.sleep(s)

    def scroll_into_view_amenities_room(self, s=2):
        self.window_scroll_by(0, 1550)
        self.sleep(s)

    def assert_clickable_checkboxes(self, s=2):
        self.assert_element_to_be_clickable(FiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_1)
        self.click_element(FiltersLocators.AMENITIES_IN_THE_ROOM_CHECK_BOX_1)
        self.sleep(s)

