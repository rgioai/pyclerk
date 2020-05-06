from ._endpoint import Endpoint

class VolumesEndpoint(Endpoint):
    def __init__(self, access_token='abcd12345', api_version=1, body_format='text'):
        super().__init__(access_token, api_version, body_format)
        self.endpoint_url = self.base_url + 'volumes'
        raise NotImplementedError('{} not implemented yet, sorry!'.format(type(self)))
    # FUTURE Add the VolumesEndpoint class
