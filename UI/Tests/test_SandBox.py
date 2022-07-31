import pytest
from UI.Tests.test_base import BaseTest


class TestSandbox(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.Instantiate_Common_Pages()
        self.driver.get("https://www.saucedemo.com/")


    @pytest.mark.happy_path
    def test_happy_path(self):
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login_button()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
