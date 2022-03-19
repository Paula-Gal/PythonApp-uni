class RepositoryException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors


class ValidationException(Exception):

    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors
