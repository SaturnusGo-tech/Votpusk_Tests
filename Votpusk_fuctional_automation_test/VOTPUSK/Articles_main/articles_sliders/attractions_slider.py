import time

from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class AttractionLocators(BaseMethods):
    ATTRACTIONS_BLOCK_1 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-active"]')
    ATTRACTIONS_BLOCK_2 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-next"]')
    ATTRACTIONS_BLOCK_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]')
    ATTRACTIONS_BLOCK_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]')
    ATTRACTIONS_BLOCK_5 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-active"]')
    ATTRACTIONS_BLOCK_6 = (By.CSS_SELECTOR, '[class="landmarks__inner-item swiper-slide swiper-slide-next"]')
    ATTRACTIONS_BLOCK_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]')
    ATTRACTIONS_BLOCK_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]')
    NAVIGATION_ARROW_PREV = (By.CSS_SELECTOR, '[class="slider-btn landmarks__prev-btn"]')
    NAVIGATION_ARROW_NEXT = (By.CSS_SELECTOR, '[class="slider-btn landmarks__next-btn"]')
    READ_MORE_LINK_1 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[1]/div[2]/a[2]')
    READ_MORE_LINK_2 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[2]/div[2]/a[2]')
    READ_MORE_LINK_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]/div[2]/a[2]')
    READ_MORE_LINK_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]/div[2]/a[2]')
    READ_MORE_LINK_5 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[3]/div[2]/a[2]')
    READ_MORE_LINK_6 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[4]/div[2]/a[2]')
    READ_MORE_LINK_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]/div[2]/a[2]')
    READ_MORE_LINK_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]/div[2]/a[2]')
    COUNTRY_NAMED_1 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[1]/div[2]/a[3]')
    COUNTRY_NAMED_2 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[2]/div[2]/a[3]')
    COUNTRY_NAMED_3 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[5]/div[2]/a[3]')
    COUNTRY_NAMED_4 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[6]/div[2]/a[3]')
    COUNTRY_NAMED_5 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[3]/div[2]/a[3]')
    COUNTRY_NAMED_6 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[4]/div[2]/a[3]')
    COUNTRY_NAMED_7 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[7]/div[2]/a[3]')
    COUNTRY_NAMED_8 = (By.XPATH, '//*[@id="page-header"]/section[6]/div/div/div[2]/div/div[8]/div[2]/a[3]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_attractions_section(self):
        time.sleep(4)
        self.window_scroll_by(0, 2450)

    def click_to_prev_navigation_arrow(self):
        time.sleep(4)
        self.click_element(AttractionLocators.NAVIGATION_ARROW_PREV)

    def check_the_containers_blocks_first(self):
        self.sleep(3)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_1)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_1)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_1)
        self.sleep(1)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_2)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_2)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_2)
        self.sleep(1)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_3)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_3)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_3)
        self.sleep(1)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_4)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_4)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_4)

    def double_click_to_navigation(self):
        time.sleep(2)
        self.double_click_element(AttractionLocators.NAVIGATION_ARROW_NEXT)

    def check_the_containers_blocks_next(self):
        time.sleep(5)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_5)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_5)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_5)
        self.sleep(1)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_6)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_6)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_6)
        self.sleep(1)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_7)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_7)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_7)
        self.sleep(1)
        self.is_element_present(AttractionLocators.READ_MORE_LINK_8)
        self.is_element_present(AttractionLocators.ATTRACTIONS_BLOCK_8)
        self.is_element_present(AttractionLocators.COUNTRY_NAMED_8)
