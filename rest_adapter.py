#!/bin/python3

import requests
import logging
from json import JSONDecodeError

# imports local py files for error handling and data model for http req
from .exceptions import EffluxApiException

Result = tuple[int, str, dict]

class RestAdapter:
    def __init__(self, hostname: str = 'api.effluxio.com/api/', api_key: str = '', ver: str = 'v2', ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for RestAdapter
        :param hostname: Normally, api.effluxio.com/api/
        :param api_key: (optional) string used for authentication when POSTing or DELETEing
        :param ver: v1 or v2
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: (optional) If your app has a logger, pass it in here.
        """

        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/{}".format(hostname, ver)
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _do(self, http_method: str, endpoint: str, ep_params: dict = None, data: dict = None) -> Result:

        # Boiler plate stuff to do HTTP calls and logging.
        # used later in the def GET/POST/DELETE

        full_url = self.url + endpoint
        headers = {'accept': 'application/json',
                   'Authorization': self._api_key, 'Content-Type': 'application/json'}

        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join(
            (log_line_pre, "success={}, status_code={}, message={}"))

        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(
                method=http_method, url=full_url, verify=self._ssl_verify, headers=headers, params=ep_params, json=data)

        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise EffluxApiException("Request Failed") from e

        is_success = 299 >= response.status_code >= 200
        log_line = log_line_post.format(
            is_success, response.status_code, response.reason)

        if is_success:
            self._logger.debug(msg=log_line)
            try:
                data_out = response.json()
            except (ValueError, JSONDecodeError) as e:
                raise EffluxApiException("Bad JSON in response") from e
            return response.status_code, response.reason, data_out
        
        self._logger.error(msg=log_line)
        raise EffluxApiException(response.status_code)

    def GET(self, endpoint: str, ep_params: dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def POST(self, endpoint: str, ep_params: dict = None, data: dict = None) -> Result:
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)

    def PUT(self, endpoint: str, ep_params: dict = None, data: dict = None) -> Result:
        return self._do(http_method='PUT', endpoint=endpoint, ep_params=ep_params, data=data)

    def DELETE(self, endpoint: str, ep_params: dict = None, data: dict = None) -> Result:
        return self._do(http_method='DELETE', endpoint=endpoint, ep_params=ep_params, data=data)
