import time

from Test_Travel.Modules_component.BaseMethods.MapMethods.MapMethods import MapBoxesMethods
from selenium.webdriver.common.by import By


class Map(MapBoxesMethods):
    CLOSE_MODAL = (By.XPATH, '//*[@id="hotels-modal-search"]/button')  # Кнопка закрытия модального окна

    Map = (By.CSS_SELECTOR, '[class="ymaps-2-1-79-events-pane ymaps-2-1-79-user-selection-none"]')
    Map_markers = (By.CSS_SELECTOR, '[class="leaflet-marker-icon leaflet-div-icon leaflet-zoom-animated leaflet-interactive"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_modal(self):
        self.click_element(Map.CLOSE_MODAL)

    def get_map_attribute(self, s=2):
        self.interact_with_map(Map.Map_markers)
        time.sleep(10)
