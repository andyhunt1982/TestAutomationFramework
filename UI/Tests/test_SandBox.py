import pytest
from UI.Tests.test_base import BaseTest
from Config.config import Config


class TestSandbox(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.Instantiate_Common_Pages()
        url = Config.get_item_from_environment_data("UI", "url")

        self.driver.get(url)

    @pytest.mark.happy_path
    def test_happy_path(self):
        username = Config.get_item_from_environment_data("UI", "username")
        password = Config.get_item_from_environment_data("UI", "password")

        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
