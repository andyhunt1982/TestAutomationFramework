import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def Instantiate_Common_Pages(self):
        pass
