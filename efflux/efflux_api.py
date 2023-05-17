import logging
from .rest_adapter import RestAdapter
from .models import *


class EffluxAPI:
    """ Main API Class
    """
    def __init__(self, hostname: str = 'api.effluxio.com/api', api_key: str = '', ver: str = 'v2', ssl_verify: bool = True, logger: logging.Logger = None):
        """__init__ 

        Args:
            hostname (str, optional): API hostname. Defaults to 'api.effluxio.com/api'.
            api_key (str, optional): API Key. Defaults to ''.
            ver (str, optional): API Version. Defaults to 'v2'.
            ssl_verify (bool, optional): Verify SSL. Defaults to True.
            logger (logging.Logger, optional): Debug logging. Defaults to None.
        """
        self._rest_adapter = RestAdapter(
            hostname, api_key, ver, ssl_verify, logger)

    def post_scan(self, hosts: list = ['8.8.8.8'], ports: list = ["top_10", "23", "135", "139", "5900"], fingerprint: int = 1, protocol: str = "tcp") -> Scan:
        """post_scan POST request to scan endpoint

        Args:
            hosts (list, optional): Hosts to scan. Defaults to ['8.8.8.8'].
            ports (list, optional): Ports to scan. Defaults to ["top_10", "23", "135", "139", "5900"].
            fingerprint (int, optional): Fingerprinting level - 0:open, 1:banner, 2:identify services. Defaults to 1.
            protocol (str, optional): Scan protocol - tcp/udp. Defaults to "tcp".

        Returns:
            Scan: Scan object
        """
        scan_data = {
            "hosts": hosts,
            "ports": ports,
            "proto": protocol,
            "fingerprint": fingerprint
        }
        _, _, data = self._rest_adapter.POST(endpoint='/scans', data=scan_data)
        return Scan.from_dict(data)
    
    def post_scan_repeat(self, job: str) -> Scan:
        """post_scan_repeat Repeats scan based on jobid

        Args:
            job (str): previously run job_id you want to run

        Returns:
            Scan: Scan Object
        """
        endpoint = "/scans/repeat/" + job
        _, _, data = self._rest_adapter.POST(endpoint=endpoint)
        return Scan.from_dict(data)
    
    def get_scans(self, count: int = 10) -> list[Scan]:
        """get_scans Get list of n historical user scans

        Args:
            count (int): Number of scans to return. Defaults to 10.

        Returns:
            scans: Returns list of previous n scans in list[Scan] format
        """
        endpoint = "/scans?count=" + str(count)
        _, _, data = self._rest_adapter.GET(endpoint=endpoint)
        scans: list[Scan] = []
        for scan in data:
            scans.append(Scan.from_dict(scan))
        return scans
    
    def get_scan_job(self, job: str, details: bool = True) -> Scan:
        """get_scan_job GET request to scan endpoint to get details about a scan.

        Args:
            job (str): Job ID
            details (bool, optional): Whether to return the scan result details. Defaults to True.

        Returns:
            Scan: Scan Object
        """
        endpoint = "/scans/" + job + "?details=" + str(details)
        _, _, data = self._rest_adapter.GET(endpoint=endpoint)
        return Scan.from_dict(data)
    
    def get_scan_status(self, job: str) -> str:
        """get_scan_status _summary_

        Args:
            job (str): Job ID

        Returns:
            str: Returns scan status as a string - "pending","in progress", "complete"
        """
        scan = self.get_scan_job(job=job,details=False)
        return str(scan.status)
    
    def get_scan_results(self, job: str, details: bool = True):
        """get_scan_results _summary_

        Args:
            job (str): Job ID
            details (bool, optional): Whether to return the scan result details. Defaults to True.

        Returns:
            _type_: Returns result variable - [dict[str, IP]]
        """
        scan = self.get_scan_job(job=job,details=details)
        return scan.results
