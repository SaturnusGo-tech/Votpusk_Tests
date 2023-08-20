import pytest
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.config.configuration import TestData
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.hotel_functionality.form.hotel_func_form import \
    HotelForm
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.hotel_functionality.sliders_and_links_functionality.hotel_sliders_func_links \
    import \
    SlidersHotelLinksLocator
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Main.test.TestBase import BaseTest
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.Hotel_main.hotels_second_page.hotel_filters.hotel_filters import \
    FiltersLocators


class TestHotel(BaseTest):
    @pytest.mark.smoke()
    def test_hotel_form(self, driver):
        driver.get(TestData.URL)
        assert_form_input = HotelForm(driver)
        assert_form_input.assert_form_input()
        assert_put_into_field = HotelForm(driver)
        assert_put_into_field.assert_put_into_field()
        assert_react_calendar_check_in = HotelForm(driver)
        assert_react_calendar_check_in.assert_react_calendar_check_in()
        assert_react_calendar_check_out = HotelForm(driver)
        assert_react_calendar_check_out.assert_react_calendar_check_out()
        assert_room_column = HotelForm(driver)
        assert_room_column.assert_room_column()
        assert_click_room_column = HotelForm(driver)
        assert_click_room_column.assert_click_room_column()
        assert_add_member = HotelForm(driver)
        assert_add_member.assert_add_member()
        assert_remove_member = HotelForm(driver)
        assert_remove_member.assert_remove_member()
        assert_open_list = HotelForm(driver)
        assert_open_list.assert_open_list()
        assert_clickable_button = HotelForm(driver)
        assert_clickable_button.assert_clickable_button()

    @pytest.mark.smoke()
    def test_hotel_brand_hotels(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_brand_hotels = SlidersHotelLinksLocator(driver)
        scroll_into_view_brand_hotels.scroll_into_view_brand_hotels()
        assert_brand_hotels_label = SlidersHotelLinksLocator(driver)
        assert_brand_hotels_label.assert_brand_hotels_label()
        assert_clickable_brand_hotels_label_ibis = SlidersHotelLinksLocator(driver)
        assert_clickable_brand_hotels_label_ibis.assert_clickable_brand_hotels_label_ibis()
        assert_clickable_brand_hotels_label_novotel = SlidersHotelLinksLocator(driver)
        assert_clickable_brand_hotels_label_novotel.assert_clickable_brand_hotels_label_novotel()
        assert_clickable_brand_hotels_label_sheraton = SlidersHotelLinksLocator(driver)
        assert_clickable_brand_hotels_label_sheraton.assert_clickable_brand_hotels_label_sheraton()
        assert_clickable_brand_hotels_label_eurostar_hotel = SlidersHotelLinksLocator(driver)
        assert_clickable_brand_hotels_label_eurostar_hotel.assert_clickable_brand_hotels_label_eurostar_hotel()
        assert_clickable_brand_hotels_label_ramada = SlidersHotelLinksLocator(driver)
        assert_clickable_brand_hotels_label_ramada.assert_clickable_brand_hotels_label_ramada()
        assert_navigation_brand_hotel_slide_up = SlidersHotelLinksLocator(driver)
        assert_navigation_brand_hotel_slide_up.assert_navigation_brand_hotel_slide_up()
        assert_navigation_brand_hotel_slide_down = SlidersHotelLinksLocator(driver)
        assert_navigation_brand_hotel_slide_down.assert_navigation_brand_hotel_slide_down()

    @pytest.mark.smoke()
    def test_popular_destinations(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_popular_destinations = SlidersHotelLinksLocator(driver)
        scroll_into_view_popular_destinations.scroll_into_view_popular_destinations()
        assert_popular_destinations_slide = SlidersHotelLinksLocator(driver)
        assert_popular_destinations_slide.assert_popular_destinations_slide()
        assert_popular_destinations_list = SlidersHotelLinksLocator(driver)
        assert_popular_destinations_list.assert_popular_destinations_list()
        assert_popular_destination_href = SlidersHotelLinksLocator(driver)
        assert_popular_destination_href.assert_popular_destination_href()
        assert_popular_destination_href_link = SlidersHotelLinksLocator(driver)
        assert_popular_destination_href_link.assert_popular_destination_href_link()

    @pytest.mark.smoke()
    def test_comment(self, driver):
        driver.get(TestData.URL)
        scroll_into_view_comment = SlidersHotelLinksLocator(driver)
        scroll_into_view_comment.scroll_into_view_comment()
        assert_comment_slide = SlidersHotelLinksLocator(driver)
        assert_comment_slide.assert_comment_slide()
        assert_modal_button = SlidersHotelLinksLocator(driver)
        assert_modal_button.assert_modal_button()
        assert_open_modal = SlidersHotelLinksLocator(driver)
        assert_open_modal.assert_open_modal()
        assert_modal_window = SlidersHotelLinksLocator(driver)
        assert_modal_window.assert_modal_window()
        fill_the_name_input = SlidersHotelLinksLocator(driver)
        fill_the_name_input.fill_the_name_input()
        fill_the_comment_input = SlidersHotelLinksLocator(driver)
        fill_the_comment_input.fill_the_comment_input()
        public_paragraph = SlidersHotelLinksLocator(driver)
        public_paragraph.public_paragraph()
        close_modal_window = SlidersHotelLinksLocator(driver)
        close_modal_window.close_modal_window()
        check_stability_href_link = SlidersHotelLinksLocator(driver)
        check_stability_href_link.check_stability_href_link()
        assert_clickable_link = SlidersHotelLinksLocator(driver)
        assert_clickable_link.assert_clickable_link()

