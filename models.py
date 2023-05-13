from dataclasses import dataclass
from typing import Optional, Dict, List
from uuid import UUID
from datetime import datetime

@dataclass
class Result:
    status_code: int
    message: str
    data: Optional[List[Dict]] = None


@dataclass
class Metadata:
    asn: int
    as_org: str
    country: str


@dataclass
class Port:
    open: str
    service: str
    bytes_rcvd: int
    software: Optional[str] = None
    cpe: Optional[str] = None
    tls: Optional[str] = None
    http: Optional[str] = None


@dataclass
class IP:
    metadata: Metadata
    ports: Dict[str, Port]


@dataclass
class Scan:
    job_id: UUID
    proto: str
    hosts: Optional[List[str]] = None
    ports: Optional[List[str]] = None
    host_count: Optional[int] = None
    port_count: Optional[int] = None
    request_count: Optional[int] = None
    fingerprint: Optional[int] = None
    created_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    accessible_host_count: Optional[int] = None
    accessible_port_count: Optional[int] = None
    status: Optional[str] = None
    results: Optional[Dict[str, IP]] = None