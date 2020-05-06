import requests
import json

from .response_formats import *

from .endpoint_types.bulk import BulkEndpoint
from .endpoint_types.cases import CasesEndpoint
from .endpoint_types.citations import CitationsEndpoint
from .endpoint_types.courts import CourtsEndpoint
from .endpoint_types.jurisdictions import JurisdictionsEndpoint
from .endpoint_types.ngrams import NgramsEndpoint
from .endpoint_types.reporters import ReportersEndpoint
from .endpoint_types.user_history import UserHistoryEndpoint
from .endpoint_types.volumes import VolumesEndpoint

# TODO Test packaging and downloading from PyPi test

# TODO Add documentation

"""

"""

class PyClerk(object):
    """PyClerk is the base class to use all the other methods and functions available in the module."""
    def __init__(self, access_token='abcd12345', api_version=1, master_body_format='text'):
        """

        :param access_token:
        :param api_version:
        :param master_body_format:
        """
        self.access_token = access_token
        self.api_version = api_version
        self.master_body_format = ''


        self.cases = CasesEndpoint(self.access_token, self.api_version, master_body_format)
        # self.bulk = BulkEndpoint(self.access_token, self.api_version, master_body_format)
        # self.citations = CitationsEndpoint(self.access_token, self.api_version, master_body_format)
        # self.courts = CourtsEndpoint(self.access_token, self.api_version, master_body_format)
        # self.jurisdictions = JurisdictionsEndpoint(self.access_token, self.api_version, master_body_format)
        # self.ngrams = NgramsEndpoint(self.access_token, self.api_version, master_body_format)
        # self.reporters = ReportersEndpoint(self.access_token, self.api_version, master_body_format)
        # self.user_history = UserHistoryEndpoint(self.access_token, self.api_version, master_body_format)
        # self.volumes = VolumesEndpoint(self.access_token, self.api_version, master_body_format)
        # FUTURE Uncomment other endpoints as they are implemented

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
