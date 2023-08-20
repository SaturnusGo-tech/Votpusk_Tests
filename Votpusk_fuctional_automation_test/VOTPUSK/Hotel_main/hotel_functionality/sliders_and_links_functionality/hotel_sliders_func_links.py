from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.config.configuration import TestData


#  Проверка заголовка
class SlidersHotelLinksLocator(BaseMethods):
    BRAND_HOTELS = (By.CSS_SELECTOR, '[class="hotelsNet-slider__wrapper swiper-container swiper-initialized swiper-horizontal swiper-pointer-events"]')
    NAVIGATE_BRAND_HOTELS_UP = (By.CSS_SELECTOR, '[class="hotelsNet-btn hotelsNet-prev"]')
    NAVIGATE_BRAND_HOTELS_DOWN = (By.CSS_SELECTOR, '[class="hotelsNet-btn hotelsNet-next"]')
    BRAND_NAME_HOTELS_IBIS = (By.XPATH, '//*[@id="swiper-wrapper-66fe31e6bf14d947"]/div[4]/a[1]/img')
    BRAND_NAME_HOTELS_NOVOTEL = (By.XPATH, '//*[@id="swiper-wrapper-66fe31e6bf14d947"]/div[5]/a[1]/img')
    BRAND_NAME_HOTELS_SHERATON = (By.XPATH, '//*[@id="swiper-wrapper-66fe31e6bf14d947"]/div[6]/a[1]/img')
    BRAND_NAME_HOTELS_EUROSTAR_HOTES = (By.XPATH, '//*[@id="swiper-wrapper-e766ef7dadd44a10f"]/div[7]/a[1]/img')
    BRAND_NAME_HOTELS_RAMADA = (By.XPATH, '//*[@id="swiper-wrapper-e766ef7dadd44a10f"]/div[8]/a[1]/img')
    HOTEL_HREF = (By.CSS_SELECTOR, '[class="hotelsNet-link"]')

    POPULAR_DESTINATIONS = (By.CSS_SELECTOR, '[class="swiper swiper-hotels-dir corner-radius-two-50 swiper-initialized swiper-horizontal swiper-pointer-events"]')
    POPULAR_DESTINATIONS_LIST = (By.CSS_SELECTOR, '[class="hotels-popular-dir__grid"]')
    POPULAR_DESTINATIONS_HREF = (By.CSS_SELECTOR, 'class="link-underline"')

    COMMENT_BLOCK = (By.CSS_SELECTOR, '[class="swiper swiper-hotels-comments corner-radius-two swiper-initialized swiper-horizontal swiper-pointer-events"]')
    MODAL_BUTTON = (By.CSS_SELECTOR, '[class="btn-orange"]')
    MODAL_ID = (By.CSS_SELECTOR, '[id="send-comment"]')
    MODAL_INPUT_NAME = (By.CSS_SELECTOR, '[id="hotelsreviews-username"]')
    MODAL_INPUT_COMMENT = (By.CSS_SELECTOR, '[id="hotelsreviews-review"]')
    CLOSE_MODAL = (By.CSS_SELECTOR, '[class="carousel__button is-close"]')
    PUBLIC_BUTTON = (By.CSS_SELECTOR, '[class="btn-orange btn--small"]')
    COMMENT_SHOWN = (By.CSS_SELECTOR, '[class="orange-underline"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_into_view_brand_hotels(self, s=2):
        self.window_scroll_by(0, 350)
        self.sleep(s)

    def assert_brand_hotels_label(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.BRAND_HOTELS)
        self.sleep(s)

    def assert_clickable_brand_hotels_label_ibis(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.BRAND_NAME_HOTELS_IBIS)
        self.sleep(s)

    def assert_clickable_brand_hotels_label_novotel(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.BRAND_NAME_HOTELS_NOVOTEL)
        self.sleep(s)

    def assert_clickable_brand_hotels_label_sheraton(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.BRAND_NAME_HOTELS_SHERATON)
        self.sleep(s)

    def assert_clickable_brand_hotels_label_eurostar_hotel(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.BRAND_NAME_HOTELS_EUROSTAR_HOTES)
        self.sleep(s)

    def assert_clickable_brand_hotels_label_ramada(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.BRAND_NAME_HOTELS_RAMADA)
        self.sleep(s)

    def assert_navigation_brand_hotel_slide_up(self, s=2):
        self.click_in_loop4(SlidersHotelLinksLocator.NAVIGATE_BRAND_HOTELS_UP)
        self.sleep(s)

    def assert_navigation_brand_hotel_slide_down(self, s=2):
        self.click_in_loop4(SlidersHotelLinksLocator.NAVIGATE_BRAND_HOTELS_DOWN)
        self.sleep(s)

    def scroll_into_view_popular_destinations(self, s=2):
        self.window_scroll_by(0, 1100)
        self.sleep(s)

    def assert_popular_destinations_slide(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.POPULAR_DESTINATIONS)
        self.sleep(s)

    def assert_popular_destinations_list(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.POPULAR_DESTINATIONS_LIST)
        self.sleep(s)

    def assert_popular_destination_href(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.HOTEL_HREF)
        self.sleep(s)

    def assert_popular_destination_href_link(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.HOTEL_HREF)
        self.sleep(s)

    def scroll_into_view_comment(self, s=2):
        self.window_scroll_by(0, 2100)
        self.sleep(s)

    def assert_comment_slide(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.COMMENT_BLOCK)
        self.sleep(s)

    def assert_modal_button(self, s=2):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.MODAL_BUTTON)
        self.sleep(s)

    def assert_open_modal(self, s=2):
        self.click_element(SlidersHotelLinksLocator.MODAL_BUTTON)
        self.sleep(s)

    def assert_modal_window(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.MODAL_ID)
        self.sleep(s)

    def fill_the_name_input(self, s=2):
        self.send_keys_to_element(SlidersHotelLinksLocator.MODAL_INPUT_NAME, TestData.USER_NAME)
        self.sleep(s)

    def fill_the_comment_input(self, s=2):
        self.send_keys_to_element(SlidersHotelLinksLocator.MODAL_INPUT_COMMENT, TestData.USER_COMMENT_TEXT)
        self.sleep(s)

    def public_paragraph(self, s=2):
        self.click_element(SlidersHotelLinksLocator.PUBLIC_BUTTON)
        self.sleep(s)

    def close_modal_window(self, s=2):
        self.click_element(SlidersHotelLinksLocator.CLOSE_MODAL)
        self.sleep(s)

    def check_stability_href_link(self, s=2):
        self.is_element_present(SlidersHotelLinksLocator.COMMENT_SHOWN)
        self.sleep(s)

    def assert_clickable_link(self):
        self.assert_element_to_be_clickable(SlidersHotelLinksLocator.COMMENT_SHOWN)







