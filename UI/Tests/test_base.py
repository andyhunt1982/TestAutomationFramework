import pytest
from Config.config import Config


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    def Instantiate_Common_Pages(self):
        pass