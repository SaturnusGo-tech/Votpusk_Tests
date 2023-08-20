import time

from selenium.webdriver.common.by import By
from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods


class CommentLocator(BaseMethods):
    COMMENT_CONTAINER = (By.XPATH, '//*[@id="page-header"]/section[9]/div')
    COMMENT_TEXT = (By.XPATH, '//*[@id="page-header"]/section[9]/div/div/div[1]/a[1]/div[2]/div/p')
    SHOW_MORE_LINK = (By.CSS_SELECTOR, '[class="more-comments__item more-comments__item-enabled active"]')
    LIKE_OPTIONS = (By.XPATH, '//*[@id="page-header"]/section[9]/div/div/div[1]/a[1]/div[1]/div[2]/div[2]')
    AD = (By.CSS_SELECTOR, '[class="top-block top-block-desktop"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def scroll_to_comment_sections(self):
        self.window_scroll_by(0, 4250)

    def check_visibility_of_container(self):
        time.sleep(3)
        self.is_element_present(CommentLocator.COMMENT_CONTAINER)

    def check_to_text_area(self):
        self.is_element_present(CommentLocator.COMMENT_TEXT)
        self.is_element_present(CommentLocator.LIKE_OPTIONS)

    def check_show_more_options_and_ad(self):
        self.is_element_present(CommentLocator.SHOW_MORE_LINK)
        self.assert_element_to_be_clickable(CommentLocator.SHOW_MORE_LINK)
        self.is_element_present(CommentLocator.AD)


