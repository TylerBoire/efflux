#!/bin/python3

import json, argparse, requests

baseURL = 'https://api.effluxio.com/api/v1/scans'
AUTH_TOKEN = None
with open(".efflux_apikey", "rt") as apiKey:
    AUTH_TOKEN = apiKey.read().strip()
    
debug = True
if debug: AUTH_TOKEN = "TESTTESTTESTTEST"
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + AUTH_TOKEN }

#TODO: Logic around building query based on args.
def startScan(hosts, ports, finger=0, proto="tcp"):
   
    query = dict(   hosts = [hosts], 
                    ports = [ports], 
                    fingerprint = finger, 
                    proto = proto
                )
    #lazy Debug logic. 
    if not debug:
        r = requests.post(baseURL, headers=header, data=json.dumps(query, separators=(',', ':') ))
        return r
    else:
        print(baseURL, header, json.dumps(query, separators=(',', ':')))

def listJobs():
    r = requests.get(baseURL, headers=header)
    print(r.text())
    return 0

def scanResults(jobID):
    #TODO: error checking around user input. 
    if not debug:
        r = requests.get(baseURL + jobID, headers=header, )
        return r
    else:
        print(baseURL + jobID, header)

if __name__ == "__main__":
    #if host & port specified, do this
    #should probably make a real menu at some point. 
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--hosts', metavar='h', type=str, help='The host(s) you wish to scan: x.x.x.x, x.x.x.x/y, or x.x.x.x-y.y.y.y supported formats')
    parser.add_argument('--ports', metavar='p', type=str, help='The port(s) you wish to probe. Single, top_x or range supported')
    parser.add_argument('--fingerprint', metavar='f', type=int, required=False, default=0, help='0:open, 1:banner, 2:identify services')
    parser.add_argument('--proto', type=str, required=False, default="tcp", choices=['tcp','udp'], help='tcp or udp')
    group.add_argument('--job_id', type=str, help="Check the status of a Job")
    args = parser.parse_args()

    if args.hosts is not None:
        print(startScan(args.hosts, args.ports, args.fingerprint, args.proto ))
    if args.job_id is not None:
        print(scanResults(args.job_id))