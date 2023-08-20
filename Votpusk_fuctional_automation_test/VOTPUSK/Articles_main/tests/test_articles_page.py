import time
import pytest
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.comment_section import CommentLocator
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.topic_blocks import TopicBlocks
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.field_articles_forms.articles_form import ArticlesFormLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.test.TestBase import BaseTest
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.article_header.articles_header import ArticleHeaderLocator
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.config.Config import TestData
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.articles_slider import ArticlesSliderLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.photo_sliders import PhotoSection
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.attractions_slider import AttractionLocators
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Articles_main.articles_sliders.what_to_see import WhatToSee


class TestArticlesPage(BaseTest):
    @pytest.mark.smoke()
    def test_articles_header(self, driver):
        driver.get(TestData.URL)
        check_the_article_header_exist = ArticleHeaderLocator(driver)
        check_the_article_header_exist.check_the_article_header_exist()

    @pytest.mark.smoke()
    def test_check_container_articles_forms(self, driver):
        driver.get(TestData.URL)
        scroll_to_locator = ArticlesFormLocators(driver)
        scroll_to_locator.scroll_to_locator()
        click_and_check_the_len_container_country = ArticlesFormLocators(driver)
        click_and_check_the_len_container_country.click_and_check_the_len_container_country()
        click_and_check_len_container_cities = ArticlesFormLocators(driver)
        click_and_check_len_container_cities.click_and_check_len_container_cities()
        click_and_check_len_container_themes = ArticlesFormLocators(driver)
        click_and_check_len_container_themes.click_and_check_len_container_themes()

    @pytest.mark.smoke()
    def test_topics_theme(self, driver):
        driver.get(TestData.URL)
        check_the_pinned_all_topics_button = ArticlesSliderLocators(driver)
        check_the_pinned_all_topics_button.check_the_pinned_all_topics_button()
        check_the_wrapper_container = ArticlesSliderLocators(driver)
        check_the_wrapper_container.check_the_wrapper_container()
        time.sleep(3)

    """def test_slider_container_blocks(self, driver):
        driver.get(TestData.URL)
        time.sleep(3)
        scroll_to_new_articles_page = ArticlesSliderLocators(driver)
        scroll_to_new_articles_page.scroll_to_new_articles_page()
        check_the_each_blocks_in_articles_container_1 = ArticlesSliderLocators(driver)
        check_the_each_blocks_in_articles_container_1.check_the_each_blocks_in_articles_container_1()
        check_the_each_blocks_in_articles_container_2 = ArticlesSliderLocators(driver)
        check_the_each_blocks_in_articles_container_2.check_the_each_blocks_in_articles_container_2()
        check_read_more_links = ArticlesSliderLocators(driver)
        check_read_more_links.check_read_more_links()
        check_the_target_blank = ArticlesSliderLocators(driver)
        check_the_target_blank.check_the_target_blank()
        check_the_all_item_articles_blocks = ArticlesSliderLocators(driver)
        check_the_all_item_articles_blocks.check_the_all_item_articles_blocks()
        check_ead_more_links_next = ArticlesSliderLocators(driver)
        check_ead_more_links_next.check_ead_more_links_next()
        check_the_target_blanks_next = ArticlesSliderLocators(driver)
        check_the_target_blanks_next.check_the_target_blanks_next()
        check_the_each_upper_article_blocks = ArticlesSliderLocators(driver)
        check_the_each_upper_article_blocks.check_the_each_upper_article_blocks()
        check_the_read_more_article_links_upper = ArticlesSliderLocators(driver)
        check_the_read_more_article_links_upper.check_the_read_more_article_links_upper()
        check_the_articles_target_blank_upper = ArticlesSliderLocators(driver)
        check_the_articles_target_blank_upper.check_the_articles_target_blank_upper()"""

    @pytest.mark.smoke()
    def test_hotel_section(self, driver):
        driver.get(TestData.URL)
        scroll_to_popular_articles_section = ArticlesSliderLocators(driver)
        scroll_to_popular_articles_section.scroll_to_popular_articles_section()
        check_each_popular_articles_blocks = ArticlesSliderLocators(driver)
        check_each_popular_articles_blocks.check_each_element_locator_null()
        click_to_next_locator_slider_once = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_once.click_to_next_locator_slider_once()
        check_each_element_locator_once = ArticlesSliderLocators(driver)
        check_each_element_locator_once.check_each_element_locator_once()
        click_to_next_locator_slider_twice = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_twice.click_to_next_locator_slider_twice()
        check_each_element_locator_twice = ArticlesSliderLocators(driver)
        check_each_element_locator_twice.check_each_element_locator_twice()
        click_to_next_locator_slider_thirds = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_thirds.click_to_next_locator_slider_thirds()
        check_each_element_locator_thirds = ArticlesSliderLocators(driver)
        check_each_element_locator_thirds.check_each_element_locator_thirds()
        click_to_next_locator_slider_fourths = ArticlesSliderLocators(driver)
        click_to_next_locator_slider_fourths.click_to_next_locator_slider_fourths()
        check_each_element_locator_fourths = ArticlesSliderLocators(driver)
        check_each_element_locator_fourths.check_each_element_locator_fourths()

    @pytest.mark.smoke()
    def test_photo(self, driver):
        driver.get(TestData.URL)
        scroll_to_photo = PhotoSection(driver)
        scroll_to_photo.scroll_to_photo()
        check_the_full_container = PhotoSection(driver)
        check_the_full_container.check_the_full_container()

    @pytest.mark.smoke()
    def test_new_attractions_sections(self, driver):
        driver.get(TestData.URL)
        scroll_to_attractions_section = AttractionLocators(driver)
        scroll_to_attractions_section.scroll_to_attractions_section()
        click_to_prev_navigation_arrow = AttractionLocators(driver)
        click_to_prev_navigation_arrow.click_to_prev_navigation_arrow()
        check_the_containers_blocks_first = AttractionLocators(driver)
        check_the_containers_blocks_first.check_the_containers_blocks_first()
        double_click_to_navigation = AttractionLocators(driver)
        double_click_to_navigation.double_click_to_navigation()
        check_the_containers_blocks_next = AttractionLocators(driver)
        check_the_containers_blocks_next.check_the_containers_blocks_next()

    @pytest.mark.smoke()
    def test_all_topics(self, driver):
        driver.get(TestData.URL)
        scroll_to_all_topics_section = TopicBlocks(driver)
        scroll_to_all_topics_section.scroll_to_all_topics_section()
        check_the_topics_container = TopicBlocks(driver)
        check_the_topics_container.check_the_topics_container()
        click_to_open_more_button = TopicBlocks(driver)
        click_to_open_more_button.click_to_open_more_button()
        check_the_footer_menu = TopicBlocks(driver)
        check_the_footer_menu.check_the_footer_menu()
        check_each_block_offer = TopicBlocks(driver)
        check_each_block_offer.check_each_block_offer()

    @pytest.mark.smoke()
    def test_what_to_see(self, driver):
        driver.get(TestData.URL)
        scroll_to_desktop_item_blocks = WhatToSee(driver)
        scroll_to_desktop_item_blocks.scroll_to_desktop_item_blocks()
        check_visibility_blocks = WhatToSee(driver)
        check_visibility_blocks.check_visibility_blocks()
        check_visibility_all_news_link = WhatToSee(driver)
        check_visibility_all_news_link.check_visibility_all_news_link()

    @pytest.mark.smoke()
    def test_comment_section(self, driver):
        driver.get(TestData.URL)
        scroll_to_comment_sections = CommentLocator(driver)
        scroll_to_comment_sections.scroll_to_comment_sections()
        check_visibility_of_container = CommentLocator(driver)
        check_visibility_of_container.check_visibility_of_container()
        check_to_text_area = CommentLocator(driver)
        check_to_text_area.check_to_text_area()
        check_show_more_options = CommentLocator(driver)
        check_show_more_options.check_show_more_options_and_ad()









