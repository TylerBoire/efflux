import dataclasses
from typing import Optional
from uuid import UUID
from datetime import datetime

class BaseData:

    @classmethod
    def from_dict(cls, parameters):
        known_parameters = [ field.name for field in dataclasses.fields(cls) ]
        for key in parameters.keys():
            if key not in known_parameters:
                print('Warning: Unrecognized key "{}"'.format(key))
                del(parameters[key])
        return cls(**parameters)

@dataclasses.dataclass
class BacnetCollection(BaseData):
    instance_number: Optional[int] = None
    vendor_id: Optional[int] = None
    vendor_name: Optional[str] = None
    firmware_revision: Optional[str] = None
    software_revision: Optional[str] = None
    object_name: Optional[str] = None
    model_name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None

@dataclasses.dataclass
class FoxCollection(BaseData):
    server_id: Optional[int] = None
    version: Optional[str] = None
    host_name: Optional[str] = None
    host_address: Optional[str] = None
    app_name: Optional[str] = None
    app_version: Optional[str] = None
    vm_name: Optional[str] = None
    vm_version: Optional[str] = None
    os_name: Optional[str] = None
    os_version: Optional[str] = None
    station_name: Optional[str] = None
    language: Optional[str] = None
    time_zone: Optional[str] = None
    host_id: Optional[str] = None
    vm_id: Optional[str] = None
    brand_id: Optional[str] = None
    sys_info: Optional[str] = None
    auth_agent_type: Optional[str] = None

@dataclasses.dataclass
class RDPCollection(BaseData):
    target_name: Optional[str] = None
    proto_rdp: Optional[bool] = None
    proto_ssl: Optional[bool] = None
    proto_hybrid: Optional[bool] = None
    proto_rdstls: Optional[bool] = None
    proto_hybrid_ex: Optional[bool] = None
    cert_signature: Optional[str] = None
    cert_version: Optional[str] = None
    cert_serial_number: Optional[str] = None
    cert_not_before: Optional[str] = None
    cert_not_after: Optional[str] = None
    cert_issuer_country: Optional[str] = None
    cert_issuer_organization: Optional[str] = None
    cert_issuer_organizational_unit: Optional[str] = None
    cert_issuer_locality: Optional[str] = None
    cert_issuer_province: Optional[str] = None
    cert_issuer_street_address: Optional[str] = None
    cert_issuer_postal_code: Optional[str] = None
    cert_issuer_serial_number: Optional[str] = None
    cert_issuer_common_name: Optional[str] = None
    cert_subject_country: Optional[str] = None
    cert_subject_organization: Optional[str] = None
    cert_subject_organizational_unit: Optional[str] = None
    cert_subject_locality: Optional[str] = None
    cert_subject_province: Optional[str] = None
    cert_subject_street_address: Optional[str] = None
    cert_subject_postal_code: Optional[str] = None
    cert_subject_serial_number: Optional[str] = None
    cert_subject_common_name: Optional[str] = None
    net_bios_domain_name: Optional[str] = None
    net_bios_computer_name: Optional[str] = None
    dns_domain_name: Optional[str] = None
    dns_computer_name: Optional[str] = None
    major: Optional[int] = None
    minor: Optional[int] = None
    build: Optional[int] = None
    system_time: Optional[str] = None

@dataclasses.dataclass
class SIPCollection(BaseData):
    response: Optional[str] = None
    accept: Optional[str] = None
    accept_encoding: Optional[str] = None
    accept_language: Optional[str] = None
    allow: Optional[str] = None
    allow_events: Optional[str] = None
    contact: Optional[str] = None
    content_encoding: Optional[str] = None
    content_language: Optional[str] = None
    content_type: Optional[str] = None
    proxy_authenticate: Optional[str] = None
    session_id: Optional[str] = None
    subject: Optional[str] = None
    supported: Optional[str] = None
    user_agent: Optional[str] = None
    via: Optional[str] = None
    warning: Optional[str] = None
    sdp_version: Optional[str] = None
    sdp_owner: Optional[str] = None
    sdp_name: Optional[str] = None
    sdp_information: Optional[str] = None
    sdp_uri: Optional[str] = None
    sdp_email: Optional[str] = None
    sdp_phone: Optional[str] = None
    sdp_connection: Optional[str] = None
    sdp_bandwidth: Optional[str] = None
    sdp_timezone: Optional[str] = None
    sdp_encryption_key: Optional[str] = None
    sdp_attributes: Optional[str] = None
    raw: Optional[str] = None

@dataclasses.dataclass
class S7Collection(BaseData):
    system: Optional[str] = None
    module: Optional[str] = None
    module_id: Optional[str] = None
    module_type: Optional[str] = None
    cpu_profile: Optional[str] = None
    hardware: Optional[str] = None
    firmware: Optional[str] = None
    plant_id: Optional[str] = None
    oem_id: Optional[str] = None
    memory_serial_number: Optional[str] = None
    copyright: Optional[str] = None
    serial_number: Optional[str] = None
    location: Optional[str] = None
    os: Optional[str] = None

@dataclasses.dataclass
class SMBCollection(BaseData):
    major: Optional[int] = None
    minor: Optional[int] = None
    revision: Optional[int] = None
    version_string: Optional[str] = None
    native_os: Optional[str] = None
    has_ntlm: Optional[bool] = False
    ntlm: Optional[str] = None
    group_name: Optional[str] = None
    smbv1_support: Optional[bool] = False
    smb_dfs_support: Optional[bool] = False
    smb_leasing_support: Optional[bool] = False
    smb_multicredit_support: Optional[bool] = False
    smb_multichan_support: Optional[bool] = False
    smb_persistent_handle_support: Optional[bool] = False
    smb_directory_leasing_support: Optional[bool] = False
    smb_encryption_support: Optional[bool] = False
    neg_protocol_id: Optional[str] = None
    neg_status: Optional[int] = None
    neg_command: Optional[int] = None
    neg_credits: Optional[int] = None
    neg_flags: Optional[int] = None
    neg_security_mode: Optional[int] = None
    neg_dialect_revision: Optional[int] = None
    neg_server_guid: Optional[str] = None
    neg_capabilities: Optional[int] = None
    neg_system_time: Optional[int] = None
    neg_server_start_time: Optional[int] = None
    neg_authentication_types: Optional[str] = None
    session_protocol_id: Optional[str] = None
    session_status: Optional[int] = None
    session_command: Optional[int] = None
    session_credits: Optional[int] = None
    session_flags: Optional[int] = None
    session_setup_flags: Optional[int] = None
    session_target_name: Optional[str] = None
    session_negotiate_flags: Optional[int] = None

@dataclasses.dataclass
class SSHCollection(BaseData):
    version: Optional[str]
    software: Optional[str]
    misc: Optional[str]
    pub_key: Optional[str]
    pub_key_type: Optional[str]
    kex_algs: Optional[str]
    ciphers: Optional[str]
    compression: Optional[str]
    macs: Optional[str]
    methods: Optional[str]
    banner: Optional[str]
    raw: Optional[str]

@dataclasses.dataclass
class TelnetCollection(BaseData):
    banner: Optional[str]
    do: Optional[str]
    will: Optional[str]
    wont: Optional[str]
    dont: Optional[str]

@dataclasses.dataclass
class Detection(BaseData):
    name: str
    matches: str

@dataclasses.dataclass
class AppDetection(BaseData):
    url: str
    detections: list[Detection]

    def __post_init__(self):
        if self.detections:
            self.detections = [
                Detection.from_dict(value) for value in self.detections
            ]

@dataclasses.dataclass
class Check(BaseData):
    matched: Optional[str] = None
    check_name: Optional[str] = None
    check_type: Optional[str] = None
    severity: Optional[str] = None
    extract_name: Optional[str] = None
    extractions: Optional [list[str]] = None
    cve_id: Optional [list[str]] = None
    cwe_id: Optional [list[str]] = None
    cvss_metrics: Optional[str] = None
    cvss_score: Optional[int] = None

@dataclasses.dataclass
class Metadata(BaseData):
    asn: int
    as_org: str
    country: str

@dataclasses.dataclass
class Port(BaseData):
    open: Optional[bool] = False
    service: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None
    info: Optional[str] = None
    host_name: Optional[str] = None
    os: Optional[str] = None
    device_type: Optional[str] = None
    cpe: Optional[str] = None
    tls: Optional[bool] = False
    http: Optional[bool] = False
    bacnet_collection: Optional[BacnetCollection] = None
    fox_collection: Optional[FoxCollection] = None
    rdp_collection: Optional[RDPCollection] = None
    sip_collection: Optional[SIPCollection] = None
    s7_collection: Optional[S7Collection] = None
    smb_collection: Optional[SMBCollection] = None
    ssh_collection: Optional[SSHCollection] = None
    telnet_collection: Optional[TelnetCollection] = None
    app_detections: Optional[list[AppDetection]] = None
    checks: Optional[list[Check]] = None
    bytes_rcvd: Optional[int] = None
    raw: Optional[list[str]] = None

    def __post_init__(self):
        if self.bacnet_collection:
            self.bacnet_collection = BacnetCollection.from_dict(self.bacnet_collection)

        if self.fox_collection:
            self.fox_collection = FoxCollection.from_dict(self.fox_collection)

        if self.rdp_collection:
            self.rdp_collection = RDPCollection.from_dict(self.rdp_collection)

        if self.sip_collection:
            self.sip_collection = SIPCollection.from_dict(self.sip_collection)

        if self.s7_collection:
            self.s7_collection = S7Collection.from_dict(self.s7_collection)

        if self.smb_collection:
            self.smb_collection = SMBCollection.from_dict(self.smb_collection)

        if self.ssh_collection:
            self.ssh_collection = SSHCollection.from_dict(self.ssh_collection)

        if self.telnet_collection:
            self.telnet_collection = TelnetCollection.from_dict(self.telnet_collection)

        if self.app_detections:
            self.app_detections = [
                AppDetection.from_dict(value) for value in self.app_detections
            ]

@dataclasses.dataclass
class IP(BaseData):
    metadata: Metadata
    ports: Optional[dict[str, Port]] = None

    def __post_init__(self):
        if self.ports:
            self.ports = {
                port: Port.from_dict(value) for port, value in self.ports.items()
            }
        if self.metadata:
            self.metadata = Metadata.from_dict(self.metadata)

@dataclasses.dataclass
class Scan(BaseData):
    job_id: UUID
    schedule_id: Optional[UUID] = None
    proto: Optional[str] = None
    hosts: Optional[list[str]] = None
    ports: Optional[list[str]] = None
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
    results: Optional[dict[str, IP]] = None

    def __post_init__(self):
        if self.results:
            self.results = {
                host: IP.from_dict(value) for host, value in self.results.items()
            }