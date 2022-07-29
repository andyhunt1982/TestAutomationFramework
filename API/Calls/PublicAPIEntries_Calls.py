from API.Contracts.PublicAPIEntries_Response import PublicAPIEntriesResponse
from CustomTools.UniversalLogger import logger


class PublicApiEntriesCalls:
    @staticmethod
    def basic_call(session, base_url):
        logger.info("PublicAPIEntries_Calls.basic_call()")
        url = base_url + "/entries"

        # make api call
        response = session.get(url)

        # assert response.status_code == 200
        assert response.status_code == 200, f"PublicAPIEntries_Calls.basic_call() failed." \
                                            f" Response code: {str(response.status_code)}"

        # assert response is type of json string
        assert response.text.startswith("{"), "PublicAPIEntries_Calls.basic_call() - response is not json string"

        # convert json string to PublicAPIEntriesResponse
        public_api_entries_response = PublicAPIEntriesResponse.from_dict(response.json())

        return public_api_entries_response
