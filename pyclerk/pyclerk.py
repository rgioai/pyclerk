import requests
import json
from .response_formats import *
from .endpoint_types.cases import CasesEndpoint

# TODO Test packaging and downloading from PyPi test

# TODO Add documentation

# TODO Finish CasesEndpoint

"""

"""

class PyClerk(object):
    """PyClerk is the base class to use all the other methods and functions available in the module."""
    def __init__(self, access_token='abcd12345', api_version=1, master_body_format='text'):
        self.access_token = access_token
        self.api_version = api_version
        self.master_body_format = ''


        self.cases = CasesEndpoint(access_token=self.access_token,
                                   api_version=self.api_version,
                                   body_format=master_body_format)
        # FUTURE Add other endpoints

        self.set_master_body_format(master_body_format)

        print("Pyclerk initiated")

    def hello_world(self, name=None):
        """
        Prints a welcome statement
        :param name: optional string of someone to say hello to
        :return: None
        """
        if name is None:
            print("Hello world!")
        else:
            print("Hello %s!" % str(name))

    def set_master_body_format(self, new_format):
        if new_format not in ['text', 'xml', 'html']:
            raise ValueError("{} is not a valid data format, must be 'text', 'xml', or 'html'".format(new_format))
        else:
            self.master_body_format = new_format
            self.cases.set_body_format(new_format)
            # FUTURE Add other endpoints
