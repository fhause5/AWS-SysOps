<span style="color: green">&#x1F535; AWS SYSOPS  
</span>

## Function Reference
PLAN:
* [Compute](#Compute)
* [Cloudwatch](#Cloudwatch)
* [SSM&OpsWOrks](#SSM&OpsWOrks)
* [HA](#HA)
* [ElasticBeanstalk](#ElasticBeanstalk)
* [CloudFormation](#CloudFormation)
* [Storage](#Storage)
* [S3](#S3)
* [Snow-Family](#Snow-Family)
* [Cloudfront](#Cloudfront)
* [RDS](#RDS)
* [ElastiCache](#ElastiCache)
* [CloudTrail](#CloudTrail)
* [AWS-Config](#AWS-Config)
* [Account-Managment](#Account-Managment)
* [Disaster-recovery](#Disaster-recovery)
* [Security/Shared](#Security/Shared)
* [IAM](#IAM)
* [Cognito](#Cognito)
* [SSO](#SSO)
* [Route53](#Route53)
* [Network](#Network)
* [VPN](#VPN)
* [SQS](#SQS)
* [aws-cli](#aws-cli)
* [Athena](#Athena)
* [Gateways](#Gateways)

<span style="color: black">&#x1F535; 
# Compute
</span>

###  Placement group accross EC2

* Cluster Placement Group is the way to go in order to reduce latency
* In one Hardware for Clustering

### types:

* Reserved types: long up 75% 1-3y
upfront, no upfront
* Convertible long with flexible can change type, 54%
* Scheduled friday 12-3
* Dedicated host
* Dedicated instance
* change instance type ONLY EBS: stop
* burstable CPU credit- monitor CPU health if unlimited (T-type)

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

### enchanced network SR-IOV

* ENA mod up 100GBs
* Intel 82599 up 10GBs
* EFA only linux

```
modinfo ena
ethtool -i eth0
```

<span style="color: black">&#x1F535; 
# Troubleshooting
</span>

### ec2 Terminates immediately

* EBS limit
* EBS corrupt or decrypt
* AMI is missing

### Compute Optimizer

Reduce cost and improve performance


<span style="color: black">&#x1F535; 
# Cloudwatch
</span>

* Create alarm on Service Quotas
* EC2 5 min metrics
* Custom metric use put-metric-date AWSCLI 
* Cloudwatch logs send to: S3, Lambda, Kinesis, ElasticSearch
* Metric Filter to find specific IP in logs and create a new Metric
* Create alarm depends on LOG filter
* Events > Choose event type JSON > Target (Lambda, Snapshoot, SNS)

### Logging in AWS

* CloudTrail: all API call
* ConfigRule: config & compliance
* CloudWatch full data retention
* VCP Flow Logs: IP traffic
* ELB Access Logs: metadata for LB
* CloudFront: web distribution access logs
* WAF

LOGS can be stored in S3 and filter by Athena

### EventBridge 

updated AWS events

* Send data beetween accounts
* Default Event Bus my account
* Download code bindings: Java, Python
* Custom Event Bus for your applications, Partner Bus for DataDog
* Can share with others AWS accounts
* Can analyze data
* Schema Registry allows to generate code for your APP
* Создает Рулы на основание ивента
* event to logs, lambda, SNS

### Alarm

* Metric alarm - один метрик
* Composite alarm - больше одного метрика
* OK, ALARM, UNSUFICIENT_DATA
* Alarm history 2 week

* By default CLoudwatch keep: 1 min-15 days, 5 min-63 days,  1 hour 455 days
* 5 min period: alarm 4 min, evaluation period 1 min
* agent > AWS metric > Alarm > SNS topic
* cloudwatch(procstat) agent for new METRICS: MEM, DIS and LOGS: nginx-error.log
* status check: alarm, restart, scale
* hibirnation(save RAM to DISK) RAM inside EBS volume, will fast starting (RAM loads from VOLUME)
* Custom metrics

```
aws cloudwatch put-metric-data --metric-name Custom-test --namespace MyNameSpace --unit Bytes --value 116 --dimensions InstanceId=i-0892712e6a374cbc2,InstanceType=m1.small --region eu-central-1
```

* Log groups
https://medium.com/tensult/to-send-linux-logs-to-aws-cloudwatch-17b3ea5f4863

```
sudo yum -y install polkit.x86_64

```


<span style="color: black">&#x1F535; 
# SSM&OpsWOrks
</span>

* Create role with policy AmazonEC2RoleForSSM
* Resource group tag base
* SSM document like CloudFormation allow run sh
* SSM command like ansible to run commands without ssh
* SSM store credentials

```
aws ssm get-parameters --name /app/dev /app/prod --with-decryption
```
* SSM inventory: metadata, software, store data in s3
* SSM State Manager monitor instance state, application and versions, at time
* SSM Session manager ssh thougth aws cli, console, SSM SDK without keys
* all works from SSM agent
* Patch manager to patching onstances
* OPSWorks for CHEF and puppet

### AWS System Manager

* Parameters store

AWS System Managmer > Parameters store > key/values

```
DB_ENV=`aws ssm get-parameters --name DB_ENV --region us-east-1 --with-decription --output text --query Parameters[].Value`
```

* AWS System Managmer, run command

```
AWS System Managmer > managed instances with role/SSM agent > run command
```

* Inventory

Statistics/OS/Network about Managed Instances

* Hybrid Infastracture

```
Create Activation > Install SSM on Hybrid Infastracture
```

* Maintenance Windows

* Add instances to managed instances

<span style="color: black">&#x1F535; 
# HA
</span>

### Stresstest

```
sudo stress --cpu 8 -v
```

### Unlimited ASG CPU

* Unlimited mode for burstable performance instances can use MORE than actual CPU usage

* HA many AZ

### LB https > LB > http > target

* LB internal, external: Gateway, Clasic, Application, Network
* Outofservice if port not opened SG
* Allow trafic only from LB
* Application: /admin /home, query id=123&order=false
* LB secure, don't have IP
* LB Gateway(GENEVE 6081) packet inspect, firewall, analyzer 
* Sticky Sessions(Affininy-target group enable) client to the same instance, for session data, cookie generated by LB
* NLB pay for AZ data
* SNI multiple SSL certificates
* Connection draining - stop sending a new requests, de-registration
* APPUSERC application-based cookie

### ERROR CODE

* 4XX client side
* 5XX servir side

### Metrics

* backendConnectionError
* request number
* Latency
* Access log to AWS S3, pay for only S3
* SpilloverCount  total number of request
* RAM > Request Per instance

### Target group

* deregistration time
* slow_start.duration_seconds
* stickiness.enabled
* LB.algorithm.type (Round Robin, Least, flow hash based IP,port)
* weight
* warm up configure slow start in target group

### Autoscaling ASG

* spread placement  regionally to specific hardware
* Can be based on Cloudwatch alarms and custom metrics
* Cloudwatch, Time, Predictable scaling
* Advice use ready-to-use AMI for quickly
* use script in progress/terminated state
* Target Group on lambda
* Troubleshoot ASG hook to pause the instance in the termination state

# ElasticBeanstalk

LB/Elastic IP > ASG > instance

* Use pre-pared AMI golden for faster deploy

# CloudFormation

* StackSets deploy to many AWS accounts, multiple regions
* ChangeSets rollback to work version when updating
* 200 stack limit
* Changes set preview
* CloudFormation knows what to create firstly
* Not supported resource use AWS Lambda Custom Resources
* cfn-init.yaml like ansible for AWS CloudFormation
var/logcfn-init.log
* we can tell CloudFormation cfn-init status
cfn-signal -e $? --stack $P{AWS::StackId} --resource SampleWaitCondition exit1
* Nested stack TemplateURL like Terraform module import
* Detect drift to view changes
* Deletion policy: Retain-keep; Snapshot-volume; Delete-default-delete
* Creation policy signal count for creation
* Update policy: Replacing, Rolling, Scheduled
* Prevent Update stack-policy.yaml add to Stack policy 
* Change set like terraform plan

```
Conditions:
  CreateProdResources: !Equals [ !Ref]
AvailabilityZone:
  !GetAtt EC2Instance.AvailabilityZone

```

<span style="color: black">&#x1F535; 
# Storage
</span>

### EBS

* Instance Store for the better performance IOPS, special types
* GP3 5334 GB max 16000 IOPS
* io1/io2 for database workloads, can be attached to multiple instances, must use cluster-aware (not EX4,XFS)
* EBS migration > snapshot AZ > create a new volume

### EFS

* EFS-NFSv4 POSIX: types: General-web, MAX I/O-big-date,media
*  Stadart-frequental, infrequent access, no-access for 60 days up 90% in cost savings
* Access Points restrict access using IAM, access to specific directory, +  POSIX

### FsX like EFS for windows

* Fully managed Windows file system
* Microsoft Active Directory instegration
* FsX Lustre-linux and cluster
* FsX Lustre integration with S3
* FsX short-term processing wihtout data replication

> https://aws.amazon.com/ebs/volume-types/


<span style="color: black">&#x1F535; 
# S3
</span>

*  S3 Batch Operations job to copy each object in place with encryption enabled

* SSE-S3 maanged by AWS, server side AES-256 HEADER x-ams
* SSE-KMS managed by KMS, user control server side AES-256 HEADER:aws:kms
* SSE-C custom key, client-side AWS not store key you provided, the key need to be provided in HTTP header for every HTTP request. Encrypted before upload to S3
* SSL/TSL S3 endpoint
* S3 index > create public > policy to get object
* Policy for force encryption by HEADER
* Log bucket: Bucket > server access logging
* S3 Inventory (For bucket analytics): Identify the total storage, object number, replication reports
* S3 Inventory: Managments > Inventory configuration > Destination
* S3 has automaticaly scales 3500 PUT/DELETE 5500 GET per second
* SSW-KMS limits 5550, 10000 req/sec
* multi-part upload for > 100MB
* Transfer Acceleration upload increase by creating Edge location beetwen regions
* S3 Byte-Range Fetches speed up download
* S3 Glacier select for filtering
* S3 Analytics > Analytics > add filter How many days to send to another storage class 
* S3 Glacier vaults policy denny delete archive forever for 365 days LOCK POLICY
* Each Access Points have own DNS and access limits policy, can be INTERNET OR VPC
* Allow access from source VPC policy: aws:SourceVpce

### Make public

* Create webhost

```
{
  "Id": "Policy1662452043342",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1662452020967",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::front-089-cors/*",
      "Principal": "*"
    }
  ]
}
```

### CORS: browser based security

```
Access-Control-Allow-Origin: https://www.example.com
Access-Control-Allow-Methods: GET,PUT,DELETE
```

```
Access to fetch at 'http://front-089-cors.s3-website.eu-central-1.amazonaws.com/extra-page.html' from origin 'http://front-089.s3-website.eu-central-1.amazonaws.com' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

### Allow cors


```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "http://front-089.s3-website.eu-central-1.amazonaws.com"
        ],
        "ExposeHeaders": [],
        "MaxAgeSeconds": 3000
    }
]

```

### MFA

* delete/disable version using the CLI

### S3 Replication

* Can be in diffrent accounts
* Copying in asynchronoues
* Must be enable version
* The only new object will be replicated or using S3 Batch Replication
* Deletion can be replicated

### S3 pre-signed

* default expiration of 3600 seconds
* Users inherit permisions from IAM
* Temprery users

* Bucket, open private file, it will give pre-signed access
* Object action > share with a pre-sign url

### Storage classes

* Standart-Frequental: content, big-data, gaming
* Standart-Infrequent rapid access when needed
* One zone infrequent: buckup,*  store the second buckup
* Glacier instant retrieval once a quater minimyn 90 days
* Glacier flexible expedited 1-5 min, standart 3-5 hours, build 5 -12 hours is free
* Glacier Deep arhive 12 hours, build 48 hours
* Intelligent-tier automatically

# Snow-Family

* offline migration device
* Snowcone small device 8TB
* Snowball Edge Storage Optomized 80 TB
* Snowball Edge Compute Optimized 42 TB
* Snowmobile 100 PB




<span style="color: black">&#x1F535; 
# Cloudfront 
</span>

Amazon CloudFront globally
CDN content delivery content

Create Distribution > WEB >bucket > restrict access > Redirect HTTP to HTTPS

* automatically create S3 bucket policy
* By origin access ID
* Reports: cache, popular object, top, usage, viewer from access log
* enable standart logging FIND in S3 bucket
* Caching TTL max age header
* Cookie key-value: username:Jon
* CloudFront with ALB sticky sessions need to use whitelist
* CloudFront invalidation to appy imidiatelly


Cloudfront Header value for all request
vs Cache Behavior (Accept, Accept-datetime)

<span style="color: black">&#x1F535; 
# RDS
</span>


* Force SSL connections rds.force_ssl-1 
```
GRANT USAGE ON *.* to 'mysql'@'%' REQUIRE SSL;
```

* Can't create an instance from DB snapshoot
(create clone of snapshot, then create an instance)
* restore point time 5 minutes
* db snapshots manually by user
* storage autoscaling increase storage on RDS DB all DB
[less than 10%, low-storage lasts at least 5 minutes, 6 hours passed]

* Read relicas for scalability more RDS, need update connection string read relicas only SELECT statement
* Free if replica in the same region
* DNS name automaticaly failover if master will fail

### Encryption

* Server Side: request Amazon for encryption, decrypt after downloading (AWS SSE-KMS)
* Client side: encrypt, upload data to s3
* At rest encryption master with AWS KMS AES 256
* In-flight encryption SSL in flight, enforce using SSL
* encrypt an un-encrypted
[create a snapshot, copy snapshot and enable encryption, restore database from encrypted snapshot]
* IAM-based autherntecation can used to login into RDS with authentication token

### Responsibility

AWS

* no SSH, manul DB/OS patching, audit instance

### RDS proxy

* AWS Lambda can connect in the same VPC though Elastic Network Interface (ENI)
* Use RDS proxy, deploy RDS Proxy to public subnet > then connect to RDS DB instance

### Parameter groups

* Assign paramaters to database
* set value 1 to enable
* CLick to Database to find parameters

### backups vs snapshoot

* snapshoot stop database
* snapshoot copy/share
* full snapshoot when you deleting
* backup to specific time

### Events/Cloud watch

* DB instance (State/Pending)
* Snapshoot/backup created

Metrics:

* Connections
* SwapUsage
* ReadIOPS/WriteIOPS
* DiskQuequeDepth
* FreeStorageSpace
* Enchanced monitor to see diffrent process/threads use the CPU

### Performance Insight

* Finding botlenack in tables, process, iops, hosts, SQL queries
* not supported for db.t2.micro

### AWS Aurora

* Postgresql/Mysql
* Optimized/Performance improvment
* Automatically grows 10G to 64 TB
* Cost more than RDS
* 6 copies of your data
* Self healing data
* AUtora master if fail automatic failover less then 30 seconds and redirected automatically
* Advanced monitoring/maintenance/backtrack/push-button scaling

<span style="color: black">&#x1F535; 
# ElastiCache
</span>

> get queries from ElastiCache, if not present > get from RDS > save to ElastiCache missed cache

* METRICS REDIS: Eviction- number non expired items, CPU, SwapUsage, CurrentConnections, DatabaseMemoryUsage, networkIN/OUT, Replication
* METRICS MEMCACHE: CPU, SwapUsage, Conneciton, FreeMemory

* in-memory database
* reduce loads
* Redis like RDS with backup and restore and high availability
* Memcached no backup, no HA, no persistent
* Disabled cluster 0-5 nodes

* Enabled cluster: data shared partitioned
* Online scaling no downtime
* Offline with downtime
* Horizontal support BOTH
* Vertical Support Online


<span style="color: black">&#x1F535; 
# CloudTrail
</span>

* Check events limit/resources breach
* integrity detect whether cloudtrain logs: deleted, changed
* Default 90days next to S3 and Use Athena to analize
* Console, awscli, sdk events to S3
* Managment event: AttachRole
* Data event: GetObject, DeleteVolume, Lambda
* Insights Events: User activity
* Can trigger event bridge
* To check cloudtrail logs in s3, use Log File Integrity Validation

<span style="color: black">&#x1F535; 
# AWS-Config
</span>

* AWS Config with the required-tags managed rule to evaluate all resources for the specified tags.
* keep configuration evaliate compliance

* Remediation actions
* unrestricted SSH
* public buckets
* ALB changes
* receive alert if smth change

* auditing and recording compliance
* Security groups check
* SNS Alert
* Evaluate disk types, instance types

Aggregator
* One central AWS Account Aggregator
* Aggregator rules
* Collect data to central AWS Account Aggregator


<span style="color: black">&#x1F535; 
# Account-Managment
</span>

### AWS Personal Health

* https://status.aws.amazon.com <--- Region health
* AWS Personal Health Dashboard <--- Global service, shows impact services, maintenance events, API access create event bribge with notification
* Lambda to sent to Slack

### AWS Organization

* Consolidated for centrelized biling
* The main account
* Member account part of AWS Organization
* Single payment
* Discaount for ec2, s3
* Automate AWS account creation
* MIGRATE account: remove account from old Organization, except from new one, go to invitation
* Use Organization Utits
* Can share reserved instances
* Create TAG, prevent creation without tag
* Biling only in US-EAST-1

### SCP Service Control List

Resctict access to certain services

* Account level
* SCP applied to all Users including root

###  SCP Service Control List Hierarchy

ROOT OU (full access) > PROD OU (RedshiftDeny) > HR OU can not use Redshift

### AWS Control Tower

Multiaccount the best practise

### AWS Service Catalog

* Pre-defined services by Admin for users: database, storage via CloudFormaition, for users with lack of knowledge in AWS
* Portfolio with collection of products
* Can be shared in Organization

### Cost Explorer

* manage AWS account costs
* report/analyze
* saving plan
* Forecast

### AWS Budget

Send Alarm when cost exceeds

* 2 Budget are free
* Cost, Usage, Reservation, Saving Plan

### Allocation Tags 

Track cost details by your Tags

* User tags and AWS generated tags
* Create report, use Athena, S3

### AWS Service Health Dashboard

find outages  services like ElastiCache

### AWS Trusted Advisor

* Analyze: Cost, Performance, Security, Fault Tolerance, Service LIMITS
* Recomendation
* Check storage quota limit on RDS

<span style="color: black">&#x1F535; 
# Disaster-recovery
</span>

### AWS DataSync

* SYNC: S3, EFS, Glacier, FSx via NFS or SMB
* NFS with DataSync agent > REGION AWS DataSync > S3, EFS, FSx
* EFS > Datasycn endpoint with another EFS

### AWS Buckup

* PITR backup
* database, S3, EFS, EC2, EBS
* Template with retation, build a new plan, Define JSON
* Daily, Mounthly
* Working with Tags and Jobs

<span style="color: black">&#x1F535; 
# Security/Shared
</span>

### Encryption

* SSE-C
If you want to manage the encryption key yourself, you need to include that encryption key as part of every request to S3. If you lose the encryption key, you lose all the objects that are encrypted by this key.
* SSE-KMS
If you store it in KMS, you don't need to include it in the requests to S3. Instead, just upload/download your files normally and KMS will talk to S3 and handle that for you.
* SSE-S3
Server-side encryption protects data at rest. Amazon S3 encrypts each object with a unique key.

### AWS Shared moded

Customer
* Security in Cloud: EC2, IAL
* Port, IP, SG
* User Permisions
* Bucket policy/enabling encryption
AWS
* S3 encrypt
* Not allow AWS employees access to S3
* Security in Cloud: S3, DynamoDB, RDS
* patching: OS, DB. EC2, disck
Shared:
Configuratiom, Training, Patching

### AWS Shield

Free standart

DDOS Protection

Route 53 AWS Shield > CloudFront AWS Shield with AWS WAF > LB AWS Shield > Autoscaling

### AWS WAF

* Filter specific requests
* Protect application from common web expoits

WEB ACL Web Access Control List
* SQL injection
* Cross-Site Scripting XSS
* geo-match
* based DDOS rules

### Penetration Testing

* Allow EC2, Nat Gateway, LB, RDS, Api Gateway, Lambda, Elasticbean
* Deny: DNZ zone walking, Port/Protocol/Requests flooding,

### AWS Inspector

Security Assesment

* SSM agent running OS, push to ECR
* Reporting with AWS Security Hub
* Send findings to AWS Event bridge
* SSM pre-installed on AWS Linux

### AWS GuardDuty

* Analyze AWS Account 30 days trial
* DNS logs
* K8S logs
* VPC logs
* Cloud trail
* Push keys to repository deny
* Suspicious activity

### AWS Macie

* My own PATERN in S3 bucket
* Protect sensitive data like PII personal identifiable information
* Identify private sensetive information for AWS S3 bucket: creditcard/passport/human names
* Find sensetive data in S3 bucket

### AWS KMS

* KMS FIPS 140-2 level 2
* Symetric AES-256 one key
* Asymmetric RSA & ECC two key
* Create/Imported $1/month, $0.03 10000 APIcall
* Share password with KMS
* 1year rotation ONLY
* Share key then snaphoot
* FIPS 140-2 level 3 STOP/BLOCK
* KMS Key Policies

```
aws kms encrypt --key-id alias/lynx --plaintext fileb://Valaxy.txt --output text --query CiphertextBlob  > Valaxy.base64
cat Valaxy.base64 | base64 --decode > ValaxyEncrypted
aws kms decrypt --ciphertext-blob fileb://ValaxyEncrypted   --output text --query Plaintext
echo SGVsbG8gV29ybGQgIQo= | base64 --decode
```


```
# 1) encryption
aws kms encrypt --key-id alias/tutorial --plaintext fileb://ExampleSecretFile.txt --output text --query CiphertextBlob  --region eu-west-2 > ExampleSecretFileEncrypted.base64
```

### AWS CloudHSM

* dedicated hardware module

```
Что такое облачный HSM?
Cloud HSM — это служба аппаратного модуля безопасности (HSM), размещенная в облаке, которая позволяет размещать ключи шифрования и выполнять криптографические операции в кластере модулей HSM, сертифицированных по стандарту FIPS 140-2 уровня 3
```

### AWS Artifact

* Download compliance reports
* Artifact agreements: review status of AWS agreements such as BAA or HIPAA for individual accounts

### AWS ACM certificate manager

* Secrets for: RDS, Redshift, other credentials
* METRICS: Conceled, End Secret, Rotation

<span style="color: black">&#x1F535; 
# IAM
</span>

##### Policy
* Customer managed by account
* AWS managed
* Inline policy directly to user
* The only one IAM princepal Inline policy (applies to that principal)


* IAM Credentials Report
Report list of account to get not MFA users
* IAM Access Advisor
Service permissions
* IAM Acces Analyzer to check permissions, check users outside AWS

### Indentity Federations

* Allow users outside of AWS to assume temprory role accessing AWS resources
* LDAP, SSO, OPENID, COGNITO
* identity broker must has IAM policy
* SAML 2.0 LDAP

GCP:
```
Service account > Pool + AWS provider > arn:aws:iam::286875803438:assumed-role/test > Config
```

### AWS STS Security Token Service

* Limited or Temprery access to AWS valid up 1 hour
* Assume Role
* AssumeRoleWithSAML Indentity Federations
* AssumeRole with Webidentity
* GetSession Token

<span style="color: black">&#x1F535; 
# Cognito
</span>


Create serveless database Conginto User Pools(CUP) of users for you web/mobile users

> https://www.youtube.com/watch?v=8a0vtkWJIA4
```
create user pool
create App clients
App Setings:
Callback: http://localhost:8000/login-page.html
Sign OUT: http://localhost:8000/logged_out.html

Hosted UI
Add DOMAIN to HTML, 
REMOVE: for logout change URl from login > logout
REMOVE:  response_type=code&scope=email+openid&
```

* Usename/Password
* Password reset
* Email/Phome number verificatio
* MFA
* Federated identities: Google, SAML, Facebook
* JSON JWT token
* Defined Roles for access User
* Cognito Identity pool obtain credentials for users in Cognito User Pools

<span style="color: black">&#x1F535; 
# SSO
</span>

Free

> https://www.youtube.com/watch?v=9hZWPkIZxPw

* AWS Organization > Users out from AWS IAM
* Active directory connection
* FIFO

<span style="color: black">&#x1F535; 
# Route53
</span>

### Record

* A, AAAA-ipv6, CHAME a host with A, NS
* Public hosted zone internet
* Private Hosted zone app1.company.internal $0.50 per zone
* TTL cache seconds for updatin 120 sec
* CNAME only for non root, redirect to app.example.com, ALIAS to AWS services root example.com (LB, CloudFront, Beanstock, S3, Gateway, VPC andpoing)

### Routing Policy

Many IP in one record

* Simple routing policy – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website. You can use simple routing to create records in a private hosted zone.
* Failover routing policy – Use when you want to configure active-passive failover. You can use failover routing to create records in a private hosted zone.
* Geolocation Policy where User located, need to create default route, can be deny by country. Use when you want to route traffic based on the location of your users. You can use geolocation routing to create records in a private hosted zone.
* Geoproximity routing policy  by AZ, us-west-1, us-east-1, devided by bios: 0, bios: 50 Near, increaase Bios will increase DNS MAP. Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.
* Latency Policy redirect to the near service, IP to regions, to minimize the time.  Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency. You can use latency routing to create records in a private hosted zone.
* IP-based routing policy – Use when you want to route traffic based on the location of your users, and have the IP addresses that the traffic originates from.
* Multi-Value to multiple resources assosiated with Health checks use valie only HEALTH, doesn't work with ELB. Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random. You can use multivalue answer routing to create records in a private hosted zone.
* Weight Policy by percentage, health check, 0% weight to stop sending. Use to route traffic to multiple resources in proportions that you specify. You can use weighted routing to create records in a private hosted zone.

### Resolver Inbound Endpoints

* works with Private Hosted Zone in deferant VPC
* by default resolver works with instance domain
* use VPN or DX connections 


### Health check

* 15 global health
* 30 sec interval
* Check endpoint
* need to allow Route 53 connect to resource
* Calculated Health

### Traffic flow

* To view how it connected, by Route 53

<span style="color: black">&#x1F535; 
# Network
</span>

* 23.44.22.11/32 one IP

### VPC

* AWS VPC reserve 5 IP adress: первые 4 и последний
* Default VPC has internet connectivity and public IP for all instances
* Min.size /28 (16 IP)
* Max.size /16 (65536)
* 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
* 172.16.0.0 - 172.31.255.255 (/12)
* 192.168.0.0 - 192.168.255.255 (/16)
* Tenancy default/dedicated (expensive)
* AWS reserved the first 4 and last 1 IP (10.0.0.0 network, 10.0.0.1 router, 10.0.0.2 mapping for DNS provider, 10.0.0.3 for the future, 10.0.0.255 broadcast )

### Public VPC

* Assign IP by default > Modify subnets > enable auto-assign
* Create a new Internet gateway and attach to VPC
* Create a new route table
* Edit assosiations VPC to Internet gateway

### Nat instance with EIP network address translation

* from private subnet to public
* find specific AMI
* stop source/destination check
* add nat instance to Private Route table
* 0.0.0./0 > i-0211s4534ddfd
* add security commands

### VPC Endpoint

```
aws s3api list-objects --region ap-south-1 --bucket terraform-state-lynx
```

### Nat Gateway

* Create Nat Gateway > Connectivity Public > alocate EIP
* Edit Route to Nat Gateway

### DNS Resolution

* enable DnsSupport is DNS service to get IP
* enable DNSHostnames if true by default create private dns for a instace
* EDIT VPC
* Create Private hosted zone ana assosiate


### Security Group

* The first requests goes to the NACL
* SG request to  Inbound will will go through outbound automatically
* instance level
* support allow
* eveluated before
* ACCEPT/REJECT OK 

### AWS Network Access Control List (NACL)

* subnet level
* Default NACL eccepts everything inboud/outboud
* support allow/deny
* eveluated lower to highest
* apply to all instances

> NACL and SG work together


### Ephemeral Ports 

Request: 192.168.0.21:50105 to 8.8.8.8:443

* Windows uses 49|52 - 65535
* Linux uses 32768 - 60999

### VPC Reachability Analyzer

* check connectivity not sending packages
* $0.10 per a analyzer
* create analyzer path
* veiw full network path

### VPC endpoints

* Connect to AWS resource though internet > Private Subnet > Nat > Public > IG expensive
* Create VPC endpont to direct connection to a VPC cost savings

Types:

* interface provision an ENI support many services, must attach a security group
* gateway endpoint only S3 and DynamoDB

### VPC Flow Logs

* send to S3 > Athena

### Direct connect DX

* private connection from remote to your VPC
* setup Virtual Private Gateway on your VPC
* to connect to one or more VPC use Direct Connection Gateway
* Dedicated connection 1-10GB:  physical ethernet port more then mounth to establish, not encrypted
* Hosted connection50, 500,10 GB:
AWS direct  connect partner

VPN CloudHub
* multiple networks


### AWS PrivateLink (VPC Endpoint Services)

* Doesn't require peering, internet gateway, NAT, route tables
* most scalable
* need network LB and ENI or GWLB

### EC2-Clasic && ClassicLink

* EC2-Clasic: run in a single shared network
* ClassicLink allows you to link EC2-Clasic

### Transit Gateway

* Peering for thousands of VPC
* Works with Direct Connect gateway, VPN
* VPN ECMP equal-cost multi-path routing for multiple VPN 

### VPC Traffic Mirroring

* Capture and inspect traffic
* Source and Target can be everywhere

### ipv6

* can has both ipv4 and ipv6

### Egress-only Internet Gateway

* For ipv6

kubectl -n cgbu-analytics--* exec -ut 

<span style="color: black">&#x1F535; 
# VPN
</span>


customer gateway CGW
* need datacent and devoc

* virtual private gateway
need enable route propogation

when you have customer gateway CGW and virtual private gateway create site-to-site VPN

* VPN concentrator on the AWS side
* VGW attached to the VPC

<span style="color: black">&#x1F535; 
# SQS
</span>


* DECOUPLE/разделить component
* 256KB
* FIFO/HA
* multiple writes/readers
* Retantions period: from 1min-14d
* Long polling reduce time for empty response, 20sec/max
* Visibility timeout period: 30sec-12h, scale if app need more time
* InFLign Messages in Standart: 120k
* InFLign Messages in FIFO Queue: 20k
* Dead-Letter Queue: не получаеться обработать 

<span style="color: black">&#x1F535; 
# aws-cli
</span>

* aws cloudwatch list-metrics--namespaces AWS/EC2

<span style="color: black">&#x1F535; 
# Athena
</span>

* Create two bucket with folders (input/output)
* Upload CSV
* Create workspace from output bucket
* Create table with collums

### Amazon Red shift


### LOAP for authentication


<span style="color: black">&#x1F535; 
# Gateways
</span>

## AWS API Gateway

* FrontDoor
* Create URL with GET/POST to LABMDA

AWS API Gateway service to use as an HTTP frontend. You can use it for proxying HTTP requests directly to other AWS services.

![](https://user-images.githubusercontent.com/6509926/55251995-c4c1a680-521f-11e9-8e1c-f01ad5622f1e.png)

## AWS Transit Gateway

AWS Transit Gateway connects your Amazon Virtual Private Clouds (VPCs) and on-premises networks through a central hub

## AWS Storage Gateway
```
AWS Storage Gateway is a hybrid cloud storage solution that is deployed on premise, and allows your applications to utilize AWS cloud storage services like S3, Glacier, EBS, etc. It is deployed as a virtual machine or a hardware gateway appliance, and by using storage protocols like NFS, iSCSI, and SMB it provides a very optimized data transfer capabilities, along with various other features.
```

## AWS SMTP Gateway

* Amazon WorkMail Serverless Mail service
* Outbound email flow rules let you route email messages sent from your Amazon WorkMail organization through an SMTP gateway
* handles email by rules in the Gateway

# AWS Backup Gateway

Backup gateway connects Backup to your hypervisor, so you can create, store, and restore backups of your virtual machines (VMs) anywhere, whether on-premises or in the VMware Cloud (VMC) on Amazon Web Services. Download software

### AWS Customer Gateway

A customer gateway is a resource that you create in AWS that represents the customer gateway device in your on-premises network Site-to-Site VPN

AWS Virtual private gateway from AWS  >>>>>> AWS Customer Gateway from PREMISE
### AWS Virtual private gateway

A virtual private gateway is the VPN endpoint on the Amazon side of your Site-to-Site VPN connection that can be attached to a single VPC.