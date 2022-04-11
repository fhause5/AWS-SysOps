<span style="color: green">&#x1F535; AWS SYSOPS  
</span>

## Function Reference
PLAN:
* [ComputeQL](#Compute)
* [Network](#Network)
* [Troubleshooting](#Troubleshooting)
* [Cloudwatch](#Cloudwatch)
* [SSM&OpsWOrks](#SSM&OpsWOrks)


### <span style="color: black">&#x1F535; Compute

* change instance type ONLY EBS: stop
* burstable CPU credit- monitor CPU health if unlimited


### types:

* Reserved types: long up 75% 1-3y
upfront, no upfront
* Convertible long with flexible can change type, 54%
* Scheduled friday 12-3
* Dedicated host
* Dedicated instance

### Spot 90% max spot pricem spot block timeframe

* terminate spot request, then instance
* Spot Fleets(lower-price/diversified/optimized) set of spottypes + demand(optional)


### AMI

* Migrate to a new AZ (Create AMI not reboot > migrate)
* Image builder for creation AMI on schedule (test > creation)
* Production: pre-approved by IAM and AWS config

### Placement group

* cluster-single  AZ same hardware 10GBs (BIG DATA, FAST)
* Spread- differant hardware 7 per AZ hight availability
* Partition(Hadoop, Kafka, Cassandra) many AZ, no share hardware 

### <span style="color: black">&#x1F535; Network

### enchanced network SR-IOV

* ENA mod up 100GBs
* Intel 82599 up 10GBs
* EFA only linux

```
modinfo ena
ethtool -i eth0
```

### <span style="color: black">&#x1F535; Troubleshooting

### ec2 Terminates immediately

* EBS limit
* EBS corrupt or decrypt
* AMI is missing


### <span style="color: black">&#x1F535; Cloudwatch


* cloudwatch(procstat) agent for new METRICS: MEM, DIS and LOGS: nginx-error.log
* status check: alarm, restart, scale
* hibirnation(save RAM to DISK) RAM inside EBS volume, will fast starting (RAM loads from VOLUME)

### <span style="color: black">&#x1F535; SSM&OpsWOrks
