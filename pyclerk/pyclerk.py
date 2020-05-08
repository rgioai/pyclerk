import requests
import json

from .response_formats import *

from .endpoints.bulk import BulkEndpoint
from .endpoints.cases import CasesEndpoint
from .endpoints.citations import CitationsEndpoint
from .endpoints.courts import CourtsEndpoint
from .endpoints.jurisdictions import JurisdictionsEndpoint
from .endpoints.ngrams import NgramsEndpoint
from .endpoints.reporters import ReportersEndpoint
from .endpoints.user_history import UserHistoryEndpoint
from .endpoints.volumes import VolumesEndpoint
from .endpoints._endpoint import Endpoint

# TODO Test packaging and downloading from PyPi test

# TODO Finish the high-level Sphinx file documentation

# TODO Troubleshoot sphinx and RTD for stability
"""
PyClerk package master file contains the master class.  Recommended to invoke all classes and methods through
the PyClerk() class.
"""

class PyClerk(object):
    def __init__(self, access_token: str = 'abcd12345', api_version: int = 1, master_body_format: str = 'text'):
        """
        PyClerk master class. Invoke this first!
        :param access_token: Your Caselaw Access Project API token, if you have one.
        :param api_version: API Version, stick with 1 for now
        :param body_format: Desired case content output {text, xml, html}
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
        self.custom_endpoint = Endpoint(self.access_token, self.api_version, master_body_format)
        # FUTURE Uncomment other endpoints as they are implemented

        self.set_master_body_format(master_body_format)

        print("Pyclerk initiated")

    def set_master_body_format(self, new_format: str):
        """
        Set a new desired case content output
        :param new_format: {text, xml, html}
        :return: None
        """
        if new_format not in ['text', 'xml', 'html']:
            raise ValueError("{} is not a valid data format, must be 'text', 'xml', or 'html'".format(new_format))
        else:
            self.master_body_format = new_format
            self.cases.set_body_format(new_format)
            # FUTURE Add other endpoints
