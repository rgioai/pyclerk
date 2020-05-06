from ._endpoint import Endpoint

class CourtsEndpoint(Endpoint):
    def __init__(self, access_token: str = 'abcd12345', api_version: int = 1, body_format: str = 'text'):
        """
        Class for accessing the courts api endpoint.  Not yet implemented
        :param access_token: Your Caselaw Access Project API token, if you have one.
        :param api_version: API Version, stick with 1 for now
        :param body_format: Desired case content output {text, xml, html}
        """
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'courts'
        raise NotImplementedError('{} not implemented yet, sorry!'.format(type(self)))
    # FUTURE Add the CourtsEndpoint class
