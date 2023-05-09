from typing import List, Dict

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class APIkeyAuth:
    def __init__(self, Apikey: str) -> str: 
        return f"Authorization: Bearer {self.Apikey}"

class consumes:
    def __init__(self, consumes: str):
        self.consumes = consumes

class HTTPResponse:
    def __init__(self, status_code):
        """
        Constructor for HTTPResponse class.
        Parameters:
        - status_code (int): The HTTP response status code.
        """
        self.status_code = status_code
        
    def get_status_code(self):
        """
        Returns the HTTP response status code.
        Returns:
        - (int): The HTTP response status code.
        """
        return self.status_code
    
    def is_successful(self):
        """
        Returns True if the HTTP response status code indicates a successful response (2xx).
        Returns:
        - (bool): True if the response is successful, False otherwise.
        """
        return 200 <= self.status_code < 300
    
    def is_redirect(self):
        """
        Returns True if the HTTP response status code indicates a redirect response (3xx).
        Returns:
        - (bool): True if the response is a redirect, False otherwise.
        """
        return 300 <= self.status_code < 400
    
    def is_client_error(self):
        """
        Returns True if the HTTP response status code indicates a client error response (4xx).
        Returns:
        - (bool): True if the response is a client error, False otherwise.
        """
        return 400 <= self.status_code < 500
    
    def is_server_error(self):
        """
        Returns True if the HTTP response status code indicates a server error response (5xx).
        Returns:
        - (bool): True if the response is a server error, False otherwise.
        """
        return 500 <= self.status_code < 600
