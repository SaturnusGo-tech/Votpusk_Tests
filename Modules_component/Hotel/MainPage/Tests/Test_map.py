from Test_Travel.Modules_component.Hotel.test.TestBase import BaseTest
from Test_Travel.Modules_component.Hotel.MainPage.map import Map


class TestMap(BaseTest):
    def test_map(self, driver):
        driver.get('https://www.votpusk.ru/hotels/russia/moscow')
        close_modal = Map(driver)
        close_modal.close_modal()
        get_map_attribute = Map(driver)
        get_map_attribute.get_map_attribute()

