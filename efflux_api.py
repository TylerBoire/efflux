import logging
from .rest_adapter import RestAdapter
from .exceptions import EffluxApiException
from .models import *


class EffluxAPI:
    def __init__(self, hostname: str = 'api.effluxio.com/api', api_key: str = '', ver: str = 'v2', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(
            hostname, api_key, ver, ssl_verify, logger)

    def post_scan(self, hosts: dict = ['8.8.8.8'], ports: dict = ["top_10", "23", "135", "139", "5900"], fingerprint: int = 1, protocol: str = "tcp") -> Result:
        scan_data = {
            "hosts": hosts,
            "ports": ports,
            "proto": protocol,
            "fingerprint": fingerprint
        }
        result = self._rest_adapter.POST(endpoint='/scans', data=scan_data)
        return result.data['job_id']
