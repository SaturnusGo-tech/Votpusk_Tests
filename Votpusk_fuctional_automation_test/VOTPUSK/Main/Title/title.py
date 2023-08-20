from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test import BaseMethods


class TitleLocator(BaseMethods):
    BANNER_TITLE = (By.CSS_SELECTOR, '[class="banner__image __image_pc"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def title_is_exist(self):
        title = self.wait_until_element_visible(TitleLocator.BANNER_TITLE)
        return title




