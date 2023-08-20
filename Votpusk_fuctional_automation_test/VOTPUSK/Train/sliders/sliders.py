from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class SlidersTrainLocator(BaseMethods):
    POPULAR_DESTINATION_SLIDER = (By.CSS_SELECTOR, '[class="slider-direct__inner swiper-initialized swiper-horizontal '
                                                   'swiper-pointer-events"]')
    CITY_1 = (By.XPATH, '//*[@id="swiper-wrapper-4ecf625afa79d3b2"]/a[4]')
    CITY_2 = (By.XPATH, '//*[@id="swiper-wrapper-4ecf625afa79d3b2"]/a[5]')
    CITY_3 = (By.XPATH, '//*[@id="swiper-wrapper-4ecf625afa79d3b2"]/a[6]')
    CITY_ARROW_LEFT = (By.CSS_SELECTOR, '[class="slider-direct__btn-prev slider-direct__btn"]')
    CITY_ARROW_RIGHT = (By.CSS_SELECTOR, '[class="slider-direct__btn-next slider-direct__btn"]')
    CITY_SHOW_ALL_DESTINATION = (By.CSS_SELECTOR, '[class="slider-direct__link"]')
    TRAIN_BLOCK = (By.CSS_SELECTOR, '[class="head-info__wrapper"]')
    TRAIN_BLOCK_1 = (By.XPATH, '/html/body/main/section[3]/div/ul/li[1]/div/a/img')
    TRAIN_BLOCK_2 = (By.XPATH, '/html/body/main/section[3]/div/ul/li[2]/div/a/img')
    TRAIN_BLOCK_3 = (By.XPATH, '/html/body/main/section[3]/div/ul/li[3]/div/a/img')
    TRAIN_READ_MORE = (By.CSS_SELECTOR, '[class="head-info__link"]')

    COMMENT_SECTION = (By.CSS_SELECTOR, '[class="slider-reviews__inner swiper-initialized swiper-horizontal '
                                        'swiper-pointer-events"]')
    WRITE_COMMENT_BUTTON = (By.CSS_SELECTOR, '[class="slider-reviews__add"]')
    SHOW_ALL_COMMENT = (By.CSS_SELECTOR, '[class="slider-reviews__link"]')

    FAQ_BLOCK = (By.XPATH, '//*[@id="question"]/div')
    SHOW_ALL_SECTION = (By.CSS_SELECTOR, '[class="question__link"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Популярные направления
    def assert_scroll_into_view_popular_destination(self, s=2):
        self.window_scroll_by(0, 450)
        self.sleep(s)

    def assert_popular_destination_block(self, s=2):
        self.is_element_present(SlidersTrainLocator.POPULAR_DESTINATION_SLIDER)
        self.sleep(s)

    def assert_cities_blocks(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.CITY_1)
        self.assert_element_to_be_clickable(SlidersTrainLocator.CITY_2)
        self.assert_element_to_be_clickable(SlidersTrainLocator.CITY_3)
        self.sleep(s)

    def assert_arrow_links(self, s=2):
        self.click_element(SlidersTrainLocator.CITY_ARROW_LEFT)
        self.click_element(SlidersTrainLocator.CITY_ARROW_RIGHT)
        self.sleep(s)

    def assert_show_all_destination_link(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.CITY_SHOW_ALL_DESTINATION)
        self.sleep(s)

    def assert_scroll_into_view_obtain_tickets(self, s=2):
        self.window_scroll_by(0, 950)
        self.sleep(s)

    def assert_train_blocks(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.TRAIN_BLOCK_1)
        self.assert_element_to_be_clickable(SlidersTrainLocator.TRAIN_BLOCK_2)
        self.assert_element_to_be_clickable(SlidersTrainLocator.TRAIN_BLOCK_3)
        self.sleep(s)

    def assert_read_obtain_tickets_links(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.TRAIN_READ_MORE)
        self.sleep(s)

    # Комментарии

    def assert_scroll_into_view_comment_section(self, s=2):
        self.window_scroll_by(0, 1350)
        self.sleep(s)

    def assert_comment_section(self, s=2):
        self.is_element_present(SlidersTrainLocator.COMMENT_SECTION)
        self.sleep(s)

    def assert_write_comment_button(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.WRITE_COMMENT_BUTTON)
        self.sleep(s)

    def assert_show_all_rate(self, s=2):
        self.assert_element_to_be_clickable(SlidersTrainLocator.SHOW_ALL_COMMENT)
        self.sleep(s)

    # FAQ
    def assert_scroll_into_view_faq(self, s=2):
        self.window_scroll_by(0, 1750)
        self.sleep(s)

    def assert_faq_block(self, s=2):
        self.is_element_present(SlidersTrainLocator.FAQ_BLOCK)
        self.sleep(s)

    def assert_show_all_section(self):
        self.assert_element_to_be_clickable(SlidersTrainLocator.SHOW_ALL_SECTION)



