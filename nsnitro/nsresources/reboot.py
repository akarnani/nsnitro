from nsbaseresource import NSBaseResource
from httplib import BadStatusLine

__author__ = 'ndenev'


class Reboot(NSBaseResource):

    # General Netscaler configuration object

    def __init__(self, json_data=None):
        """
        Supplied with json_data the object can be pre-filled
        """

        super(Reboot, self).__init__()

        self.options = {'warm': False}

        if not (json_data is None):
            for key in json_data.keys():
                if key in self.options.keys():
                    self.options[key] = json_data[key]

        self.resourcetype = Reboot.get_resourcetype()

    @staticmethod
    def get_resourcetype():
        return "reboot"

    def set_warm(self, warm):
        self.options['warm'] = warm

    def get_warm(self):
        return self.options['warm']



    @staticmethod
    def reboot(nitro, reboot):
        __reboot = Reboot()
        __reboot.set_warm(reboot.get_warm())
        try:
            return __reboot.perform_operation(nitro, "")
        except BadStatusLine:
            pass
