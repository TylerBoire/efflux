# PyEffluxAPI
Python Efflux API Wrapper Package
- This package provides a wrapper for using the efflux v2 api.
- The wrapper is not feature complete - Only the `/scans` and `/scans/job_id` endpoints are currently implemented.

## Folder Structure 

    .
    ├── efflux                  # Test files (alternatively `spec` or `tests`)
    │   ├── __init__.py         # Python package initialization
    │   ├── efflux_api.py       # API Main class
    │   ├── exceptions.py       # API Exceptions class
    │   ├── models.py           # API Data models class
    │   └── rest_adapter.py     # RESTful adapter class
    ├── demo.py                 # Small demo that shows how to use the API
    ├── LICENSE
    └── README.md

Todo for feature completion(We don't currently use these afaik):
* /lists/hosts
* /lists/hosts/list_id
* /lists/ports
* /lists/ports/list_id
* /ports/tcp/count
* /ports/udp/count
* /scans/eval
* /schedules
* /schedules/addlists/schedule_id
* /schedules/history/schedule_id
* /schedules/schedule_id
* /search/host
