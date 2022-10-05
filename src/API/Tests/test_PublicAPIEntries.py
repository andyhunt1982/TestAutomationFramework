import requests
import pytest
from src.Config.config import Config
from src.API.Calls.PublicAPIEntries_Calls import PublicApiEntriesCalls


class TestPublicAPIEntries:
    cookies = None
    base_url = None
    session = None
    public_api_entries_calls = PublicApiEntriesCalls()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        headers = {
            'Content-Type': 'application/json'
        }

        self.base_url = Config().get_item_from_file(product="API", item="url")
        self.session = requests.Session()
        self.session.headers.update(headers)

    def test_public_api_entries_basic_call(self):
        response = self.public_api_entries_calls.basic_call(self.session, self.base_url)

        for i in range(10):
            print(response.entries[i].api)
