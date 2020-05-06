from ._endpoint import Endpoint

class CasesEndpoint(Endpoint):
    def __init__(self, access_token: str = 'abcd12345', api_version: int = 1, body_format: str = 'text'):
        """
        Class for accessing the cases api endpoint.
        :param access_token: Your Caselaw Access Project API token, if you have one.
        :param api_version: API Version, stick with 1 for now
        :param body_format: Desired case content output {text, xml, html}
        """
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'cases'

    def browse_or_search_cases(self, parameters: dict) -> tuple:
        """
        API call to browse or search all available cases
        :param parameters: dict of parameters to include in the API call
        :return: tuple of (dict, APIResponse), or (dict, None) if no casebody data
        """
        valid_parameters = {'name_abbreviation': str,
                            'decision_date_min': str,  # YYYY-MM-DD
                            'decision_date_max': str,  # YYYY-MM-DD
                            'docket_number': str,
                            'cite': str,
                            'reporter': int,
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

    def single_case(self, case_id: int, full_case: bool = True) -> tuple:
        """
        API Call to return a single case.
        :param case_id: Caselaw Access Project ID of the desired case
        :param full_case: True to return the case body, False to return only metadata
        :return: tuple of (dict, APIResponse), or (dict, None) if no casebody data
        """
        assert(isinstance(full_case, bool))
        assert(int(case_id) > 0)

        full_case_str = 'full_case=' + str(full_case).lower()
        url = '{}/{}/?{}{}'.format(self.endpoint_url, case_id, full_case_str, self.get_body_format())
        response = self.send_request(url)
        json_response, formatted_response = self.format_response(response.content)
        return json_response, formatted_response
