from ._endpoint import Endpoint

class CasesEndpoint(Endpoint):
    def __init__(self, access_token='abcd12345', api_version=1, body_format='text'):
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'cases'

    def browse_search(self, parameters):
        valid_parameters = {'name_abbreviation': str,
                            'decision_date_min': 'YYYY-MM-DD',
                            'decision_date_max': 'YYYY-MM-DD',
                            'docket_number': str,
                            'cite': str,
                            'reporter': int,
                            'court': str,  # TODO Change to special datatype slug }
                            'court_id': int,
                            'jurisdiction': str,  # TODO Change to special datatype slug }
                            'search': str,
                            'cursor': str,
                            'ordering': str  # TODO Must be a field name above
                            }

        # TODO Validate parameters

        return ''

    def single_case(self, case_id, full_case=True):
        """
        'api.case.law/v1/cases/435800/?full_case=true
        """
        assert(isinstance(full_case, bool))
        assert(int(case_id) > 0)

        full_case_str = 'full_case=' + str(full_case).lower()
        url = '{}/{}/?{}{}'.format(self.endpoint_url, case_id, full_case_str, self.get_body_format())
        response = self.send_request(url)
        json_response, formatted_response = self.format_response(response.content)
        return json_response, formatted_response
