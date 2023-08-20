from Test_Travel.Votpusk_fuctional_automation_test.VOTPUSK.BaseMethods.object_methods import BaseMethods
from selenium.webdriver.common.by import By


class ArticleHeaderLocator(BaseMethods):
    HEADER_LOCATOR = (By.CSS_SELECTOR, '[alt="promo"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_the_article_header_exist(self):
        self.is_element_present(ArticleHeaderLocator.HEADER_LOCATOR)
