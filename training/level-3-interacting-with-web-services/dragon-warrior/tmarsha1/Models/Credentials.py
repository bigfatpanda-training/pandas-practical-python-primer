from configuration_panda import ConfigurationPanda

__credentials = ConfigurationPanda(['PROGRAM_CREDENTIALS'])

class Credentials(object):
    """
    'Abstract' class to handle credential tokens

    Class Attributes:

    Attributes:

    Methods:
        tokens:
    """

    def tokens(self):
        raise NotImplementedError(
            "Class %s doesn't implement tokens()" % (self.__class__.__name__))
