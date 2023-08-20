import time

from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class WhatToSee(BaseMethods):
    ITEM_DESKTOP = (By.CSS_SELECTOR, '[class="else__wrapper-item else__wrapper-item-desktop"]')
    ITEM_NEWS = (By.CSS_SELECTOR, '[class="else__wrapper-item"]')
    ALL_NEWS_LINK = (By.XPATH, '//*[@id="page-header"]/section[8]/div/div/div/div[1]/div[2]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_desktop_item_blocks(self):
        self.window_scroll_by(0, 3650)

    def check_visibility_blocks(self):
        time.sleep(2)
        self.is_element_present(WhatToSee.ITEM_DESKTOP)
        time.sleep(2)
        self.is_element_present(WhatToSee.ITEM_NEWS)

    def check_visibility_all_news_link(self):
        self.is_element_present(WhatToSee.ALL_NEWS_LINK)
        self.assert_element_to_be_clickable(WhatToSee.ALL_NEWS_LINK)


