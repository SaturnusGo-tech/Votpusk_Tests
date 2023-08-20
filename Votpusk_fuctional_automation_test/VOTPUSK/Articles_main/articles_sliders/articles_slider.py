import time

from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class ArticlesSliderLocators(BaseMethods):
    ALL_TOPICS_BUTTON = (By.CSS_SELECTOR, '[class="news-topic__wrapper_fixed"]')
    TOPICS_SLIDER = (By.CSS_SELECTOR, '[class="news-topic__wrapper_dynamic"]')

    PREV_FIRST_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[1]')
    PREV_READ_MORE_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[1]/div[2]/a[3]')
    PREV_TARGET_BLANK_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[1]/div[1]/a[2]')
    PREV_SECOND_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[2]')
    PREV_READ_MORE_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[2]/div[2]/a[3]')
    PREV_TARGET_BLANK_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[2]/div[1]/a[2]')
    PREV_THIRD_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[8]')
    PREV_READ_MORE_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[7]/div[2]/a[3]')
    PREV_TARGET_BLANK_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[7]/div[1]/a[2]')
    PREV_FOURTH_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[8]')
    PREV_READ_MORE_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[8]/div[2]/a[3]')
    PREV_TARGET_BLANK_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[8]/div[1]/a[2]')


    NEXT_FIRST_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[3]')
    NEXT_READ_MORE_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[3]/div[1]/a[2]')
    NEXT_TARGET_BLANK_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[3]/div[1]/a[2]')
    NEXT_SECOND_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[4]')
    NEXT_READ_MORE_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[4]/div[2]/a[3]')
    NEXT_TARGET_BLANK_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[4]/div[1]/a[2]')
    NEXT_THIRD_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[3]')
    NEXT_READ_MORE_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[9]/div[2]/a[3]')
    NEXT_TARGET_BLANK_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[9]/div[1]/a[2]')
    NEXT_FOURTH_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[10]')
    NEXT_READ_MORE_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[10]/div[2]/a[3]')
    NEXT_TARGET_BLANK_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[10]/div[1]/a[2]')

    UPPER_FIRST_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[5]')
    UPPER_READ_MORE_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[5]/div[2]/a[3]')
    UPPER_TARGET_BLANK_1 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[5]/div[1]/a[2]')
    UPPER_SECOND_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[6]')
    UPPER_READ_MORE_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[6]/div[2]/a[3]')
    UPPER_TARGET_BLANK_2 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[6]/div[1]/a[2]')
    UPPER_THIRD_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[11]')
    UPPER_READ_MORE_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[11]/div[2]/a[3]')
    UPPER_TARGET_BLANK_3 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[11]/div[1]/a[2]')
    UPPER_FOURTH_BLOCK = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[12]/div[1]/a[1]/img')
    UPPER_READ_MORE_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[12]/div[2]/a[3]')
    UPPER_TARGET_BLANK_4 = (By.XPATH, '//*[@id="page-header"]/section[3]/div/div/div[3]/div/div[12]/div[1]/a[2]')

    POPULAR_ARTICLES_SECTION_1 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div['
                                            '1]/div')
    POPULAR_ARTICLES_SECTION_2 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div['
                                            '2]/div[1]')
    POPULAR_ARTICLES_SECTION_3 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div['
                                            '2]/div[2]')
    POPULAR_ARTICLES_NAVIGATION_ARROW = (By.CSS_SELECTOR, '[class="slider-btn popularity__next-btn"]')

    POPULAR_ARTICLES_SECTION_4 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div['
                                            '1]/div')
    POPULAR_ARTICLES_SECTION_5 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div['
                                            '2]/div[1]')
    POPULAR_ARTICLES_SECTION_6 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div['
                                            '2]/div[2]')
    POPULAR_ARTICLES_SECTION_7 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div['
                                            '1]/div')
    POPULAR_ARTICLES_SECTION_8 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div['
                                            '2]/div[1]')
    POPULAR_ARTICLES_SECTION_9 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div['
                                            '2]/div[2]')
    POPULAR_ARTICLES_SECTION_10 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div['
                                             '1]/div')
    POPULAR_ARTICLES_SECTION_11 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div['
                                             '2]/div[1]')
    POPULAR_ARTICLES_SECTION_12 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div['
                                             '2]/div[2]')
    POPULAR_ARTICLES_SECTION_13 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[5]/div['
                                             '1]/div')
    POPULAR_ARTICLES_SECTION_14 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[5]/div['
                                             '2]/div[1]')
    POPULAR_ARTICLES_SECTION_15 = (By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[5]/div['
                                             '2]/div[2]')
    POPULAR_ARTICLES_CARD_FOOTER_ICON = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[2]')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_1 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_2 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_3 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_4 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_5 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_6 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_7 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div[1]/div/div[2]/div[2]')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_8 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div[2]/div[1]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_9 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_10 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div[1]/div/div[2]/div[2]')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_11 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div[2]/div[1]/div[2]/div')
    POPULAR_ARTICLES_CARD_FOOTER_ICON_12 = (
        By.XPATH, '//*[@id="page-header"]/section[4]/div/div/div/div/div/div/div[4]/div[2]/div[2]/div[2]/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_into_view(self, s=2):
        self.window_scroll_by(0, 450)
        self.sleep(s)

    def check_the_pinned_all_topics_button(self, s=2):
        self.is_element_present(ArticlesSliderLocators.ALL_TOPICS_BUTTON)
        self.sleep(s)

    def check_the_wrapper_container(self, s=2):
        self.is_element_present(ArticlesSliderLocators.TOPICS_SLIDER)
        self.sleep(s)

    def scroll_to_new_articles_page(self):
        self.window_scroll_by(0, 650)

    def check_the_each_blocks_in_articles_container_1(self, s=2):
        self.is_element_present(ArticlesSliderLocators.PREV_FIRST_BLOCK)
        self.sleep(s)

    def check_the_each_blocks_in_articles_container_2(self, s=2):
        self.is_element_present(ArticlesSliderLocators.PREV_FOURTH_BLOCK)
        self.sleep(s)

    def check_read_more_links(self, s=2):
        self.is_element_present(ArticlesSliderLocators.PREV_READ_MORE_1)
        self.is_element_present(ArticlesSliderLocators.PREV_READ_MORE_4)
        self.sleep(s)

    def check_the_target_blank(self, s=2):
        self.is_element_present(ArticlesSliderLocators.PREV_TARGET_BLANK_1)
        self.is_element_present(ArticlesSliderLocators.PREV_TARGET_BLANK_4)
        self.sleep(s)

    def check_the_all_item_articles_blocks(self, s=2):
        self.is_element_present(ArticlesSliderLocators.NEXT_FIRST_BLOCK)
        self.is_element_present(ArticlesSliderLocators.NEXT_FOURTH_BLOCK)
        self.sleep(s)

    def check_ead_more_links_next(self, s=2):
        self.is_element_present(ArticlesSliderLocators.NEXT_READ_MORE_1)
        self.is_element_present(ArticlesSliderLocators.NEXT_READ_MORE_4)
        self.sleep(s)

    def check_the_target_blanks_next(self, s=2):
        self.is_element_present(ArticlesSliderLocators.NEXT_TARGET_BLANK_1)
        self.is_element_present(ArticlesSliderLocators.NEXT_TARGET_BLANK_4)
        self.sleep(s)

    def check_the_each_upper_article_blocks(self, s=2):
        self.is_visible(ArticlesSliderLocators.UPPER_FIRST_BLOCK)
        self.is_visible(ArticlesSliderLocators.UPPER_FOURTH_BLOCK)
        self.sleep(s)

    def check_the_read_more_article_links_upper(self, s=2):
        self.is_element_present(ArticlesSliderLocators.UPPER_READ_MORE_1)
        self.is_element_present(ArticlesSliderLocators.UPPER_READ_MORE_4)
        self.sleep(s)

    def check_the_articles_target_blank_upper(self, s=2):
        self.is_element_present(ArticlesSliderLocators.UPPER_TARGET_BLANK_1)
        self.is_element_present(ArticlesSliderLocators.UPPER_TARGET_BLANK_4)
        self.sleep(s)

    def scroll_to_popular_articles_section(self):
        self.window_scroll_by(0, 1750)

    def check_each_element_locator_null(self, s=2):
        self.is_element_present(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_1)
        self.is_element_present(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_3)
        self.sleep(s)

    def click_to_next_locator_slider_once(self, s=2):
        self.click_element(ArticlesSliderLocators.POPULAR_ARTICLES_NAVIGATION_ARROW)
        self.sleep(s)

    def check_each_element_locator_once(self, s=2):
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_4)
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_6)
        self.sleep(s)

    def click_to_next_locator_slider_twice(self, s=2):
        self.click_element(ArticlesSliderLocators.POPULAR_ARTICLES_NAVIGATION_ARROW)
        self.sleep(s)

    def check_each_element_locator_twice(self, s=2):
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_7)
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_9)
        self.sleep(s)

    def click_to_next_locator_slider_thirds(self, s=2):
        self.click_element(ArticlesSliderLocators.POPULAR_ARTICLES_NAVIGATION_ARROW)
        self.sleep(s)

    def check_each_element_locator_thirds(self, s=2):
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_10)
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_12)
        self.sleep(s)

    def click_to_next_locator_slider_fourths(self, s=2):
        self.click_element(ArticlesSliderLocators.POPULAR_ARTICLES_NAVIGATION_ARROW)
        self.sleep(s)

    def check_each_element_locator_fourths(self, s=2):
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_13)
        self.is_visible(ArticlesSliderLocators.POPULAR_ARTICLES_SECTION_15)
        self.sleep(s)
