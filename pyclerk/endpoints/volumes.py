from ._endpoint import Endpoint

class VolumesEndpoint(Endpoint):
    def __init__(self, access_token: str = 'abcd12345', api_version: int = 1, body_format: str = 'text'):
        """
        Class for accessing the volumes api endpoint.  Not yet implemented
        :param access_token: Your Caselaw Access Project API token, if you have one.
        :param api_version: API Version, stick with 1 for now
        :param body_format: Desired case content output {text, xml, html}
        """
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'volumes'
        raise NotImplementedError('{} not implemented yet, sorry!'.format(type(self)))
    # FUTURE Add the VolumesEndpoint class
