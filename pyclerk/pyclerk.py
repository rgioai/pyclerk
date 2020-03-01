class PyClerk(object):
    """PyClerk is the base class to use all the other methods and functions available in the module."""
    def __init__(self):
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