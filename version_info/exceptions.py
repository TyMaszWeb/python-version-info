class VCSNotSupported(Exception):

    def __init__(self, vcs_type):
        self.message = '{0!s} is not supported'.format(vcs_type)
