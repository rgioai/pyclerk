from ._endpoint import Endpoint

class CasesEndpoint(Endpoint):
    def __init__(self, access_token='abcd12345', api_version=1, body_format='text'):
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'cases'

    def browse_search(self, parameters):
        valid_parameters = {'name_abbreviation': str,
                            'decision_date_min': str,  # YYYY-MM-DD
                            'decision_date_max': str,  # YYYY-MM-DD
                            'docket_number': str,
                            'cite': str,
                            'reqporter': int,
                            'court': str,  # Future Enforce slug
                            'court_id': int,
                            'jurisdiction': str,  # Future Enforce slug
                            'search': str,
                            'ordering': str  # Must be a field name above
                            }

        # Validate parameters
        # FUTURE May consider elevating this to a function of the Endpoint parent class
        for parameter in parameters.keys():
            if parameter not in valid_parameters.keys():
                raise ValueError('{} is not a valid parameter'.format(parameter))
            if type(parameters[parameter]) != valid_parameters[parameter]:
                raise ValueError('{} must be type {}, found {} instead'.format(parameter,
                                                                               type(parameters[parameter]),
                                                                               valid_parameters[parameter]))
            if '_date_' in parameter:
                self.validate_date(parameters[parameter])

            if parameter == 'ordering' and parameters[parameter] not in valid_parameters.keys():
                raise ValueError('Value to order on must be a valid parameter. {} is not valid.'.
                                 format(parameters[parameter]))

            # FUTURE Add additional parameter validations

        # Create URL
        url = '{}/?'.format(self.endpoint_url)
        for parameter in parameters.keys():
            add_string = '{}={}&'.format(parameter, parameters[parameter])
            url = url + add_string
        url = url[:-1]  # Drop the trailing '&'

        response = self.send_request(url)
        json_response, formatted_response = self.format_response(response.content)
        return json_response, formatted_response

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
