import requests
import pytest
from Config.config import Config
from API.Tests.test_ConfigStartUp import ENVIRONMENT, PRODUCT
from API.Calls.PublicAPIEntries_Calls import PublicApiEntries_Calls


class Test_PublicAPIEntries():
    ENVIRONMENT = ENVIRONMENT
    cookies = None
    base_url = None
    session = None
    public_api_entries_calls = PublicApiEntries_Calls()

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self):
        headers = {
            'Content-Type': 'application/json'
        }

        self.base_url = Config().get_url(environment=self.ENVIRONMENT, product=PRODUCT)
        self.session = requests.Session()
        self.session.headers.update(headers)

    def test_public_api_entries_basic_call(self):
        response = self.public_api_entries_calls.basic_call(self.session, self.base_url)

        for i in range(10):
            print(response.entries[i].api)
