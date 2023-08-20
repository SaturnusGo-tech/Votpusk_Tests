import pytest
from Test_Travel.Modules_component.Articles.test.TestBase import BaseTest
from Test_Travel.Modules_component.Articles.module_form.form_module import ModuleFormAsserting
from Test_Travel.Modules_component.Articles.Config.Configuration import Config


class TestArt(BaseTest):
    @pytest.mark.smoke()
    def test_module_form(self, driver):
        driver.get(Config.MODULE_1_URL)
        check_dropdown_links = ModuleFormAsserting(driver)
        check_dropdown_links.check_dropdown_links()
