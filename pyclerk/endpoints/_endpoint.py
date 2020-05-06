import requests
import json

from pyclerk.response_formats import *


class Endpoint(object):
    def __init__(self, access_token: str = 'abcd12345', api_version: int = 1, body_format: str = 'text'):
        """
        Parent class of the various API endpoints.
        :param access_token: Your Caselaw Access Project API token, if you have one.
        :param api_version: API Version, stick with 1 for now
        :param body_format: Desired case content output {text, xml, html}
        """
        self.access_token = access_token
        self.api_version = api_version
        self.body_format = ''
        self.set_body_format(body_format)
        self.base_url = 'https://api.case.law/v{}/'.format(self.api_version)

    def set_body_format(self, new_format: str):
        """
        Set a new desired case content output
        :param new_format: {text, xml, html}
        :return: None
        """
        if new_format not in ['text', 'xml', 'html']:
            raise ValueError("{} is not a valid data format, must be 'text', 'xml', or 'html'".format(new_format))
        else:
            self.body_format = new_format

    def get_body_format(self) -> str:
        """
        Returns the desired case content output format, in the proper format for including in an API request
        :return:
        """
        if self.body_format == 'text':
            body_format = '&body_format=text'
        elif self.body_format == 'xml':
            body_format = '&body_format=xml'
        elif self.body_format == 'html':
            body_format = '&body_format=html'
        else:
            raise ValueError("{} is not a valid data format, must be 'text', 'xml', or 'html'".format(self.body_format))
        return body_format

    def make_valid_url(self, string: str) -> str:
        """
        Slugify a string to make it a valid url
        :param string: input string
        :return: valid url
        """
        string = string.replace(' ', '%20')
        # FUTURE Add corrections for all incompatible characters
        # Could consider a library like python-slugify
        return string

    def validate_date(self, string: str):
        """
        Validates a date parameter string
        :param string: YYYY-MM-DD
        """
        try:
            assert(len(string) == 10)
            assert(1000 < int(string[:4]) < 2100)
            assert(string[4] == '-')
            assert(string[7] == '-')
            assert(0 < int(string[5:7]) < 12)
            assert (0 < int(string[8:]) < 32)
        except Exception:
            raise ValueError('Invalid date {} must conform to YYYY-MM-DD'.format(string))


    def send_request(self, url: str) -> requests.Response:
        """
        Sends a url to the API and packages the response.  Adds API token if you set one.
        :raises ValueError if response status code != 200
        :param url: url for the API call
        :return: requests.Response containing the response.
        """
        url = self.make_valid_url(url)
        if self.access_token is None or self.access_token == 'abcd12345':
            response = requests.get(url)
        else:
            response = requests.get(url, headers={'Authorization': 'Token {}}'.format(self.access_token)})
        if response.status_code == 200:
            return response
        else:
            raise ValueError('Invalid response status code {}'.format(response.status_code))

    def format_response(self, response: requests.Response) -> tuple:
        """
        Formats an API response for ease of use.  First extracts JSON data and stores as python dict.
        Then extracts casebody data and formats according to format specified in PyClerk.Endpoint.body_format.
        :param response: API response
        :return: tuple of (dict, APIResponse), or (dict, None) if no casebody data
        """
        json_response = json.loads(response)

        try:
            casebody = json_response['casebody']

            if self.body_format == 'text':
                formatted_casebody = TextBody(casebody)
            elif self.body_format == 'xml':
                formatted_casebody = XMLBody(casebody)
            elif self.body_format == 'html':
                formatted_casebody = HTMLBody(casebody)
            else:
                raise ValueError("{} is not a valid data format, must be 'text', 'xml', or 'html'".format(self.body_format))
        except Exception:
            formatted_casebody = None

        return json_response, formatted_casebody

    def get_next_page(self, json_response: dict) -> tuple:
        """
        When the API returns a paginated result, use this method to get the next page of data.
        :param json_response: formatted json response converted to python dict
        :return: tuple of (dict, APIResponse), or (dict, None) if no casebody data
        """
        url = json_response['next']
        response = self.send_request(url)
        return self.format_response(response)

    def get_prev_page(self, json_response: dict) -> tuple:
        """
        When the API returns a paginated result, use this method to get the previous page of data.
        :param json_response: json_response: formatted json response converted to python dict
        :return: tuple of (dict, APIResponse), or (dict, None) if no casebody data
        """
        url = json_response['previous']
        response = self.send_request(url)
        return self.format_response(response)
