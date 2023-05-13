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


class Scan:
    def __init__(self, job_id: str, hosts: list,  ports: list, proto: str, fingerprint: int, status: str, **kwargs):
        self.job_id = job_id
        self.hosts = hosts
        self.ports = ports
        self.proto = proto
        self.fingerprint = fingerprint
        self.status = status
        # scoop up any other extra json
        self.__dict__.update(kwargs)
        # Someone else can impliment this if they want it, we dont use it
        # if collect is not None:
        #    self.collect = collect
