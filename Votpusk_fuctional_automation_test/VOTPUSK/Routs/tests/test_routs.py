from VOTPUSK.Routs.Main_Routa_Page.routs_main_page import RoutsMainPageLocators
from VOTPUSK.Routs.Second_Page_Routs.second_page_routs import SecondPageRoutsLocators
from VOTPUSK.Routs.tests.TestBase import BaseTest
from VOTPUSK.Routs.Config.config import TestData


class TestMainRoutsPage(BaseTest):
    def test_banner(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_block = RoutsMainPageLocators(driver)
        scroll_into_view_block.scroll_into_view_block()
        assert_hotel_banner = RoutsMainPageLocators(driver)
        assert_hotel_banner.assert_hotel_banner()
        assert_local_add = RoutsMainPageLocators(driver)
        assert_local_add.assert_local_add()
        assert_subtitle = RoutsMainPageLocators(driver)
        assert_subtitle.assert_subtitle()

    def test_calculate_block(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_bla_block = RoutsMainPageLocators(driver)
        scroll_into_view_bla_block.scroll_into_view_bla_block()
        assert_calculate_block = RoutsMainPageLocators(driver)
        assert_calculate_block.assert_calculate_block()
        assert_input_filed_from = RoutsMainPageLocators(driver)
        assert_input_filed_from.assert_input_filed_from()
        assert_input_filed_to = RoutsMainPageLocators(driver)
        assert_input_filed_to.assert_input_filed_to()
        assert_search_button = RoutsMainPageLocators(driver)
        assert_search_button.assert_search_button()
        assert_radio_buttons = RoutsMainPageLocators(driver)
        assert_radio_buttons.assert_radio_buttons()
        assert_radio_button_clickable = RoutsMainPageLocators(driver)
        assert_radio_button_clickable.assert_radio_button_clickable()

    def test_search_by_name(self, driver):
        driver.get(TestData.URL)
        assert_next_calculate_block = RoutsMainPageLocators(driver)
        assert_next_calculate_block.assert_next_calculate_block()
        assert_object_input = RoutsMainPageLocators(driver)
        assert_object_input.assert_object_input()

    def test_tables_column(self, driver):
        scroll_into_view = RoutsMainPageLocators(driver)
        scroll_into_view.scroll_into_view()
        assert_table_routs = RoutsMainPageLocators(driver)
        assert_table_routs.assert_table_routs()
        assert_equivalent_test = RoutsMainPageLocators(driver)
        assert_equivalent_test.assert_equivalent_test()

    # Second Page

    def test_bla_bla_car_section(self, driver):
        driver.get(TestData.SECOND_URL)
        scroll_into_view = SecondPageRoutsLocators(driver)
        scroll_into_view.scroll_into_view()
        assert_bla_block = SecondPageRoutsLocators(driver)
        assert_bla_block.assert_bla_block()
        assert_input_filed = SecondPageRoutsLocators(driver)
        assert_input_filed.assert_input_filed()
        assert_bla_submit = SecondPageRoutsLocators(driver)
        assert_bla_submit.assert_bla_submit()

    def test_navbar(self, driver):
        driver.get(TestData.SECOND_URL)
        scroll_into_view = SecondPageRoutsLocators(driver)
        scroll_into_view.scroll_into_view()
        navbar = SecondPageRoutsLocators(driver)
        navbar.navbar()
        assert_option_block = SecondPageRoutsLocators(driver)
        assert_option_block.assert_option_block()
        assert_clickable_options = SecondPageRoutsLocators(driver)
        assert_clickable_options.assert_clickable_options()

    def test_map(self, driver):
        driver.get(TestData.SECOND_URL)
        scroll_into_view_map = SecondPageRoutsLocators(driver)
        scroll_into_view_map.scroll_into_view_map()
        assert_map = SecondPageRoutsLocators(driver)
        assert_map.assert_map()

    def test_train_filed(self, driver):
        driver.get(TestData.SECOND_URL)
        scroll_into_view_train = SecondPageRoutsLocators(driver)
        scroll_into_view_train.scroll_into_view_train()
        assert_input_train_field = SecondPageRoutsLocators(driver)
        assert_input_train_field.assert_input_train_field()
        assert_input_field_send_keys = SecondPageRoutsLocators(driver)
        assert_input_field_send_keys.assert_input_field_send_keys_from()
        assert_input_field_send_keys_to = SecondPageRoutsLocators(driver)
        assert_input_field_send_keys_to.assert_input_field_send_keys_to()
        assert_submit = SecondPageRoutsLocators(driver)
        assert_submit.assert_submit()

    def test_hotel_wrapper(self, driver):
        sroll_into_view_wrapper = SecondPageRoutsLocators(driver)
        sroll_into_view_wrapper.sroll_into_view_wrapper()
        assert_slider_wrapper = SecondPageRoutsLocators(driver)
        assert_slider_wrapper.assert_slider_wrapper()
        assert_navigation_arrow = SecondPageRoutsLocators(driver)
        assert_navigation_arrow.assert_navigation_arrow()
        assert_navigation_links_clickable = SecondPageRoutsLocators(driver)
        assert_navigation_links_clickable.assert_navigation_links_clickable()

    def test_excursion_block(self, driver):
        scroll_into_view_excursion_block = SecondPageRoutsLocators(driver)
        scroll_into_view_excursion_block.scroll_into_view_excursion_block()
        assert_excursion_block = SecondPageRoutsLocators(driver)
        assert_excursion_block.assert_excursion_block()
        assert_excursion_item = SecondPageRoutsLocators(driver)
        assert_excursion_item.assert_excursion_item()
        assert_clickable_item = SecondPageRoutsLocators(driver)
        assert_clickable_item.assert_clickable_item()
        assert_recommendation_block = SecondPageRoutsLocators(driver)
        assert_recommendation_block.assert_recommendation_block()

    def test_comment_section(self, driver):
        driver.get(TestData.SECOND_URL)
        scroll_into_view_comment_sections = SecondPageRoutsLocators(driver)
        scroll_into_view_comment_sections.scroll_into_view_comment_sections()
        comment_input_filed = SecondPageRoutsLocators(driver)
        comment_input_filed.comment_input_filed()
        assert_name_input = SecondPageRoutsLocators(driver)
        assert_name_input.assert_name_input()
        assert_email_input = SecondPageRoutsLocators(driver)
        assert_email_input.assert_email_input()
        assert_submit_comment = SecondPageRoutsLocators(driver)
        assert_submit_comment.assert_submit_comment()
        assert_submit_comment_1 = SecondPageRoutsLocators(driver)
        assert_submit_comment_1.assert_submit_comment_1()





