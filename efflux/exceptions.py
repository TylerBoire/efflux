class EffluxApiException(Exception):
    """EffluxApiException Exception handling class

    Args:
        Exception (_type_): Takes exception

    Returns:
        _type_: returns Error response string based on API code
    """
    ResponseCodes = {
        400: "No valid ports or hosts",
        401: "Unauthorized",
        404: "Job not found",
        500: "Failed to create job"
    }

    def __init__(self, resp):
        self.resp = resp

    def __str__(self):
        return 'Error {}: {}\n'.format(self.resp, self.ResponseCodes[self.resp])
