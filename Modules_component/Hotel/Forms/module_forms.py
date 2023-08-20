from Votpusk_system_automation_test.Methods.Moduls_methods import Methods


class Test(Methods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Status_code_check(self):
        self.check_page("https://www.votpusk.ru/hotels/germany/moos")
