import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def Instantiate_Common_Pages(self):
        from UI.PageObjectLibrary.LoginPage import LoginPage
        self.login_page = LoginPage(self.driver)
