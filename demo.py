import efflux
import time
from pprint import pprint
import code

#Put your API key here
api = efflux.EffluxAPI(api_key='')
#Use default scan settings (8.8.8.8)
post = api.post_scan()
#Get job_id
job = post.job_id
print("ID: " + str(job))
#Get Scan object
scan = api.get_scan_job(job=str(job))
print(scan.hosts)

#While loop to wait for scan to complete
status = ''
while(status != 'complete'):
    time.sleep(5)
    status = api.get_scan_status(job=str(job))
    print("Status: " + status)

scans = api.get_scans()
pprint(scans)

#Get scan results
res = api.get_scan_job(job=str(job))
print("RESULTS")
pprint(res.results)

#Test job repeat
post2 = api.post_scan_repeat(job=str(job))

#Get job_id for second job
job2 = post2.job_id
print("Repeated Job")
print (job2)

#We can access results like this. IP's and ports are dictionaries.

print("PORT STATUS")
#Subkeys also work
pprint(res.results["8.8.8.8"].ports["443"].open)
print("AS_ORG")
#Itteration over the dictionary
for ip in res.results:
    print(res.results[ip].metadata.as_org)
#Drop into an interactive session so we can play with res and the other objects.
code.interact(local=locals())


