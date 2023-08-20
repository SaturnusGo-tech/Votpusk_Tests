from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class PhotoSection(BaseMethods):
    FULL_CONTAINER = (By.CSS_SELECTOR, '[class="photo__slider"]')
    FULL_CONTAINER_BLOCKS = (By.CSS_SELECTOR, '[class="photo__slider-wrapper_four swiper-container swiper-initialized '
                                              'swiper-horizontal swiper-pointer-events"]')
    NAVIGATION_ARROW = (By.CSS_SELECTOR, '[id="sub-next"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_photo(self):
        self.window_scroll_by(0, 1750)

    def check_the_full_container(self):
        self.is_element_present(PhotoSection.FULL_CONTAINER)
        self.is_dropdown_present(PhotoSection.FULL_CONTAINER_BLOCKS)

