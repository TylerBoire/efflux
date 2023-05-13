class EffluxApiException(Exception):
    ResponseCodes = {
        400: "No valid ports",
        401: "Unauthorized",
        404: "Job not found",
        500: "Failed to create job"
    }

    def __init__(self, resp):
        self.resp = resp

    def __str__(self):
        return 'Error {}: {}\n'.format(self.resp, self.ResponseCodes[self.resp])
