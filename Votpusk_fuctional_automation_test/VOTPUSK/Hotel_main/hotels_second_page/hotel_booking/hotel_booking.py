from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class HotelBookingOptions(BaseMethods):
    UPPER_LINK_BLOCK = (By.CSS_SELECTOR, '[class="link-underline brd-crmbs"]')
    UPPER_LINK_1 = (By.XPATH, '//*[@id="page-header"]/div[3]/div[2]/ul/li[1]/a')
    UPPER_LINK_2 = (By.XPATH, '//*[@id="page-header"]/div[3]/div[2]/ul/li[2]/a')
    UPPER_LINK_3 = (By.XPATH, '//*[@id="page-header"]/div[3]/div[2]/ul/li[3]/a')

    H1_MAIN = (By.XPATH, '//*[@id="hotels-container"]/h1')
    SEARCH_RESULT = (By.CLASS_NAME, 'h1-def')

    SORT_CONTAINER_1 = (By.CSS_SELECTOR, '[class="hotels-sort"]')
    SORT_CONTAINER_2 = (By.CSS_SELECTOR, '[class="dropdown__content--md"]')
    SORT_POPULARITY = (By.XPATH, '//*[@id="hotels-container"]/div[2]/div/div[2]/div[1]')
    SORT_BY_RATING = (By.XPATH, '//*[@id="hotels-container"]/div[2]/div/div[2]/div[2]')
    SORT_BY_PRICE = (By.XPATH, '//*[@id="hotels-container"]/div[2]/div/div[2]/div[3]')
    SORT_BY_FOR_HOTEL_STAR = (By.XPATH, '//*[@id="hotels-container"]/div[2]/div/div[2]/div[4]')

    HOTEL_CARD_CONTAINER = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]')
    HOTEL_CARD_PHOTO = (By.XPATH, '//*[@id="swiper-wrapper-da87545c3315efb2"]/div[2]/img')
    HOTEL_CARD_NAVIGATION_ARROW_PREV = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[1]/button[1]')
    HOTEL_CARD_NAVIGATION_ARROW_NEXT = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[1]/button[2]')

    HOTEL_DATA_NAME_CONTAINER = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]')
    HOTEL_DATA_NAME_P = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]/header/p')
    HOTEL_MAIN_DATA_NAME_HOTEL = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]/div[1]/a')
    HOTEL_STAR_RATING = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]/div[1]/div')
    DISTANCE_TO_THE_CENTER_TEXT = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]/div[3]')
    HOTEL_OPTION_CARD_BLOCK = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[1]/div[2]/div[4]')

    AVERAGE_PRICE = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[2]')
    AVERAGE_PRICE_TEXT = (By, '//*[@id="hotels-container"]/div[3]/div[1]/div[2]/div[2]/p/text()')
    PROVIDER_OPTIONS = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[2]/div[1]')
    BRONEVIK_LINK = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[2]/div[1]/a/img')
    BOOKING_BUTTON = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[2]/div[2]/a')

    SHOW_MORE_HOTEL_OPTIONS = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[3]/div[1]/div')
    CONTAINER_PROVIDER_OFFER_SECTION = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[3]/div[2]/div')
    STANDARD_ROOM_OFFER = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[3]/div[2]/div/div[2]')
    SHOW_MORE_INFO = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[3]/div[2]/div/div[2]/span')
    HIDE_SHOW_MORE_OPTIONS = (By.XPATH, '//*[@id="hotels-container"]/div[3]/div[1]/div[3]/div[2]/div/div[7]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
