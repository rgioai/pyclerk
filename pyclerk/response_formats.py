class APIResponse(object):
    def __init__(self, response):
        """
        Parent class of casebody data classes.
        :param response:
        """
        self.response_body = response

    def __str__(self):
        return str(self.response_body)

class TextBody(APIResponse):
    def __init__(self, response):
        """
        Child class that handles body_format=text
        :param response: processed response
        """
        super().__init__(response)
        self.raw_response_body = response
        self.response_body = response['data']

        # FUTURE Implement further special text body handling

class XMLBody(APIResponse):
    def __init__(self, response):
        """
        Child class that handles body_format=xml
        :param response: processed response
        """
        super().__init__(response)
        # FUTURE Implement special xml body handling

class HTMLBody(APIResponse):
    def __init__(self, response):
        """
        Child class that handles body_format=html
        :param response: processed response
        """
        super().__init__(response)
        # FUTURE Implement special html body handling
