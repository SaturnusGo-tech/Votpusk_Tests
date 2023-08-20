import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class SliderSection(BaseMethods):
    # Опция выбора типы опций
    BLOCK_VACATION_TYPE_WRAPPER = (By.CSS_SELECTOR, '[class="vacations-type__wrapper"]')

    TOURS_ALL_ITEM_CONTAINER = (By.CSS_SELECTOR, '[class="tours__banner "]')

    FIRST_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="в Адыгею"]')
    SECOND_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="на Байкал"]')
    THIRD_TOUR_BLOCK = (By.CSS_SELECTOR, '[alt="в Дагестан"]')

    FOURTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[1]/picture/img'),
    FIFTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[2]/picture/img'),
    SIXTH_TOUR_BLOCK = (By.XPATH, '//*[@id="swiper-wrapper-0549c746f0e4c691"]/div[3]/a[3]/picture/img'),

    TOURS_SLIDER_NEXT = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[3]')
    TOURS_SLIDER_WORLD_NEXT = (By.XPATH, '/html/body/section[5]/div/div/div/div[2]/div[3]')
    TOURS_SLIDER_PREV = (By.XPATH, '/html/body/section[5]/div/div/div/div[1]/div[2]')
    TOUR_SWITCHER = (By.CSS_SELECTOR, '[class="tours__switcher"]')
    CHECK_THE_ORDER_FUNCTION = (By.CSS_SELECTOR, '[class="tours__order tours__order_active"]')

    # Статьи о путешествиях
    ARTICLE_CONTAINER = (By.CSS_SELECTOR, '[class="articles__banner "]')

    ARTICLE_BLOCK_FIRST = (By.XPATH, '//*[@id="swiper-wrapper-8b5aa897f2573780"]/div[19]/a/picture/img')
    ARTICLE_BLOCK_SECOND = (By.XPATH, '//*[@id="swiper-wrapper-8b5aa897f2573780"]/div[20]/a/picture/img')
    ARTICLE_BLOCK_THIRD = (By.XPATH, '//*[@id="swiper-wrapper-8b5aa897f2573780"]/div[21]/a/picture/img')

    ARTICLES_SLIDERS_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next articles__slider_next"]')
    ARTICLES_SLIDERS_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev articles__slider_prev"]')
    CHECK_ALL_ARTICLES_ITEM = (By.XPATH, '/html/body/section[6]/div/div/div/div[3]/a')
    # Форма поиска статей
    FIELD_FORM_BLOCK = (By.CSS_SELECTOR, '[class="articles__search"]')

    OPEN_CONTAINER_COUNTRY = (By.CSS_SELECTOR, '[id="select2-country-container"]')
    CONTAINER_COUNTRY_CITY_THEMES = (By.CSS_SELECTOR, '[class="select2-results"]')
    OPEN_CONTAINER_CITIES = (By.CSS_SELECTOR, '[id="select2-city-container"]')
    CONTAINER_CITIES = (By.CSS_SELECTOR, '')
    OPEN_CONTAINER_THEMES = (By.CSS_SELECTOR, '[id="select2-theme-container"]')

    SEARCH_ALL_ARTICLES_LINK = (By.CSS_SELECTOR, '[class="articles__order-redirect"]')

    SEARCH_ARTICLES_BUTTON = (By.CSS_SELECTOR, '[class="articles__search-btn"]')

    # Незабываемые достопримечательности
    ATTRACTION_CONTAINER = (By.XPATH, '/html/body/section[7]/div')
    ATTRACTION_CONTAINER_BLOCK = (By.CSS_SELECTOR, '[class="places__slider swiper swiper-initialized '
                                                   'swiper-horizontal swiper-pointer-events"]')
    ATTRACTION_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next places__slider_next"]')
    ATTRACTION_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev places__slider_prev"]')

    ALL_ATTRACTIONS_ITEM = (By.CSS_SELECTOR, '[class="places__order"]')

    # Отели
    HOTEL_CONTAINER = (By.CSS_SELECTOR, '[class="container container_hotels"]')
    HOTEL_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next hotels__slider_next"]')
    HOTEL_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev hotels__slider_prev"]')
    HOTEL_BOOKING_ITEM = (By.CSS_SELECTOR, '[class="hotels__order"]')

    # ЖД билеты
    CONTAINER_TRAINS_LINK = (By.CSS_SELECTOR, '[class="tickets__order-redirect"]')
    CONTAINER_TRAINS_SLIDER_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next tickets__slider_next"]')
    CONTAINER_TRAINS_SLIDER_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev tickets__slider_prev"]')
    TRAIN_BLOCKS_0 = (By.XPATH, '//*[@id="swiper-wrapper-2c0f8045bc3ea09d"]/a[6]/picture/img')
    TRAIN_BLOCKS_1 = (By.XPATH, '//*[@id="swiper-wrapper-2c0f8045bc3ea09d"]/a[5]/picture/img')
    TRAIN_BLOCKS_2 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[7]/picture/img')
    TRAIN_BLOCKS_3 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[8]/picture/img')
    TRAIN_BLOCKS_4 = (By.XPATH, '//*[@id="swiper-wrapper-1085d6bfdf9ce3cb7"]/a[9]/picture/img')
    TRAIN_BLOCKS_5 = (By.XPATH, '//*[@id="swiper-wrapper-99eb585c299ca610d"]/a[10]/picture/img')
    TRAIN_BLOCKS_6 = (By.XPATH, '//*[@id="swiper-wrapper-99eb585c299ca610d"]/a[11]/picture/img')

    # Новости - Фоторепортажи - Калейдоскоп
    CONTAINER_ITEM_NEWS_PHOTO = (By.XPATH, '/html/body/article/div')
    GALLERY_NEWS = (By.CSS_SELECTOR, '[class="gallery__news news"]')
    GALLERY_PHOTOS = (By.CSS_SELECTOR, '[class="gallery__photos photos"]')
    GALLERY_SCOPES = (By.CSS_SELECTOR, '[class="gallery__kaleidoscopes kaleidoscopes"]')
    NEWS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="news__wrapper"]')
    PHOTOS_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="photos__wrapper"]')
    SCOPES_BLOCK_CONTAINER = (By.CSS_SELECTOR, '[class="kaleidoscopes__wrapper"]')

    UNDER_CONTAINER_ITEMS = (By.CSS_SELECTOR, '[class="gallery__order-redirect"]')

    # Другие услуги
    CONTAINER_OTHER_DELAY = (By.CSS_SELECTOR, '[class="other-services__wrapper"]')
    BLOCK_AVIA = (By.XPATH, '/html/body/section[10]/div/div/a[1]')
    BLOCK_EXCURSION = (By.XPATH, '/html/body/section[10]/div/div/a[2]')
    BLOCK_INSURANCE = (By.XPATH, '/html/body/section[10]/div/div/a[3]')
    BLOCK_TRANSFERS = (By.XPATH, '/html/body/section[10]/div/div/a[4]')
    BLOCK_AUTOBUS = (By.XPATH, '/html/body/section[10]/div/div/a[5]')
    BLOCK_AUTO_RENT = (By.XPATH, '/html/body/section[10]/div/div/a[6]')

    # Отзывы о Votpusk.ru
    BLOCK_COMMENT_SECTION = (By.CSS_SELECTOR, '[class="reviews__slider swiper swiper-initialized swiper-horizontal '
                                              'swiper-pointer-events"]')
    WRITE_COMMENT_BUTTON = (By.CSS_SELECTOR, '[class="reviews__btn"]')
    BLOCK_COMMENT_NEXT = (By.CSS_SELECTOR, '[class="swiper-button-next reviews__slider_next"]')
    BLOCK_COMMENT_PREV = (By.CSS_SELECTOR, '[class="swiper-button-prev reviews__slider_prev"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def do_check_block_tours_option(self):
        self.assert_elements_exist(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)
        self.check_container(SliderSection.BLOCK_VACATION_TYPE_WRAPPER)

    def check_tour_container(self):
        self.check_container(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        time.sleep(3)

    def check_each_blocks_to_exist_tours_first(self):
        self.is_element_present(SliderSection.FIRST_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.SECOND_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.THIRD_TOUR_BLOCK)

    def check_each_blocks_to_exist(self):
        self.click_element(SliderSection.TOURS_SLIDER_NEXT)
        time.sleep(2)

    """def check_each_blocks_to_exist_tours_second(self):
        self.is_element_present(SliderSection.FOURTH_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.FIFTH_TOUR_BLOCK)
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.SIXTH_TOUR_BLOCK)"""

    def check_tour_container_again(self):
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.assert_elements_exist(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def switch_tour_section(self):
        self.assert_elements_exist(SliderSection.TOUR_SWITCHER)
        self.click_element(SliderSection.TOUR_SWITCHER)
        WebDriverWait(self.driver, 5)

    def check_the_container_inside(self):
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)
        self.assert_elements_exist(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def slide_to_next_blocks(self):
        self.click_element(SliderSection.TOURS_SLIDER_WORLD_NEXT)
        time.sleep(3)
        self.is_element_present(SliderSection.TOURS_ALL_ITEM_CONTAINER)

    def check_the_tour_order_button(self):
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.CHECK_THE_ORDER_FUNCTION)

    def scroll_to_page_articles(self):
        self.scroll_page_articles()

    def check_the_block_of_articles(self):
        time.sleep(3)
        self.is_element_present(SliderSection.ARTICLE_BLOCK_FIRST)

    def scroll_and_check_the_blocks_container(self):
        self.is_element_present(SliderSection.ARTICLE_BLOCK_SECOND)

    def check_the_blocks_container(self):
        self.is_element_present(SliderSection.ARTICLE_BLOCK_THIRD)

    def check_all_item_container(self):
        self.click_element(SliderSection.ARTICLES_SLIDERS_NEXT)
        time.sleep(3)
        self.is_element_present(SliderSection.ARTICLE_CONTAINER)

    def check_all_article_item(self):
        self.is_element_present(SliderSection.CHECK_ALL_ARTICLES_ITEM)

    # Тест формы поиска статей

    def check_form_block(self):
        time.sleep(2)
        self.is_element_present(SliderSection.FIELD_FORM_BLOCK)

    def do_random_select_country_city_themes(self):
        self.click_element(SliderSection.OPEN_CONTAINER_COUNTRY)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)
        time.sleep(1)
        self.click_element(SliderSection.OPEN_CONTAINER_CITIES)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)
        self.click_element(SliderSection.OPEN_CONTAINER_THEMES)
        self.random_country_selection(SliderSection.CONTAINER_COUNTRY_CITY_THEMES)

    def check_articles_search_hutton(self):
        self.is_element_present(SliderSection.SEARCH_ALL_ARTICLES_LINK)
        self.is_element_present(SliderSection.SEARCH_ARTICLES_BUTTON)

    def scroll_to_attractions_blocks(self):
        self.scroll_page_attractions()

    def check_the_attractions_block(self):
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)

    def check_the_all_container_attraction(self):
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER_BLOCK)
        time.sleep(2)

    def click_next_and_check_container_all_container(self):
        self.click_element(SliderSection.ATTRACTION_SLIDER_NEXT)
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)

    def click_next_again_and_check_container_all_container(self):
        self.click_element(SliderSection.ATTRACTION_SLIDER_NEXT)
        time.sleep(2)
        self.is_element_present(SliderSection.ATTRACTION_CONTAINER)

    def scroll_to_hotel_sliders(self):
        self.scroll_page_hotels()

    def check_the_hotel_container(self):
        time.sleep(3)
        self.is_element_present(SliderSection.HOTEL_CONTAINER)

    def click_next_and_check_the_container_again(self):
        self.click_element(SliderSection.HOTEL_SLIDER_NEXT)
        time.sleep(3)
        self.is_element_present(SliderSection.HOTEL_CONTAINER)

    def check_the_reservation_link(self):
        self.assert_elements_exist(SliderSection.HOTEL_BOOKING_ITEM)

    def scroll_to_train_section(self):
        self.scroll_page_train()
        time.sleep(3)

    def check_the_train_face_blocks(self):
        self.is_element_present(SliderSection.TRAIN_BLOCKS_0)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_1)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_2)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_3)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_4)
        time.sleep(1)
        self.click_element(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_5)
        time.sleep(1)
        self.click_element(SliderSection.CONTAINER_TRAINS_SLIDER_NEXT)
        time.sleep(1)
        self.is_element_present(SliderSection.TRAIN_BLOCKS_6)

    def check_the_reservation_train_link(self):
        self.is_element_present(SliderSection.CONTAINER_TRAINS_LINK)

    def scroll_to_news(self):
        self.scroll_page_news()

    def check_the_all_container_box(self):
        time.sleep(3)
        self.is_element_present(SliderSection.CONTAINER_ITEM_NEWS_PHOTO)

    def check_the_each_blocks_news(self):
        time.sleep(1)
        self.is_element_present(SliderSection.GALLERY_NEWS)
        time.sleep(1)
        self.is_element_present(SliderSection.GALLERY_PHOTOS)
        time.sleep(1)
        self.is_element_present(SliderSection.GALLERY_SCOPES)

    def check_the_each_container(self):
        time.sleep(1)
        self.is_element_present(SliderSection.NEWS_BLOCK_CONTAINER)
        time.sleep(1)
        self.is_element_present(SliderSection.PHOTOS_BLOCK_CONTAINER)
        time.sleep(1)
        self.is_element_present(SliderSection.SCOPES_BLOCK_CONTAINER)

    def check_the_block_links(self):
        WebDriverWait(self.driver, 5)
        self.is_element_present(SliderSection.UNDER_CONTAINER_ITEMS)

    def scroll_to_other_delay(self):
        self.scroll_page_other_delay()

    def check_other_delay_container(self):
        self.is_element_present(SliderSection.CONTAINER_OTHER_DELAY)

    def check_each_blocks(self):
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_AVIA)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AVIA)
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_EXCURSION)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_EXCURSION)
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_INSURANCE)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_INSURANCE)
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_TRANSFERS)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_TRANSFERS)
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_AUTOBUS)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AUTOBUS)
        self.sleep(2)
        self.is_element_present(SliderSection.BLOCK_AUTO_RENT)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_AUTO_RENT)

    def scroll_to_comment(self):
        self.scroll_page_comment()

    def check_the_comment_container(self):
        self.is_element_present(SliderSection.BLOCK_COMMENT_SECTION)

    def check_the_write_comment_button(self):
        self.is_element_present(SliderSection.WRITE_COMMENT_BUTTON)
        self.assert_element_to_be_clickable(SliderSection.WRITE_COMMENT_BUTTON)

    def check_and_click_navigation_arrow(self):
        self.assert_element_to_be_clickable(SliderSection.BLOCK_COMMENT_NEXT)
        self.click_element(SliderSection.BLOCK_COMMENT_NEXT)
        self.sleep(2)
        self.assert_element_to_be_clickable(SliderSection.BLOCK_COMMENT_PREV)
        self.click_element(SliderSection.BLOCK_COMMENT_PREV)
        self.sleep(2)



