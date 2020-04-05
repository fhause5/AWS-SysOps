### <span style="color: black">&#x1F535; AWS Certified SysOps Administrator - Associate


### <span style="color: black">&#x1F535; Demonstrate the ability to monitor the AWS environment:


### 1. You've been tasked with optimizing costs in your company's AWS environment. After logging in, you discover that there are 3 unused elastic IP addresses, 6 RDS instances that have not had a DB connection for over 7 days, 5 instances that are running at an average CPU utilization of < 5% and one EC2 instance running at 80% utilization. Your company has not purchased any reserved instances but is highly concerned over AWS costs. As a SysOps administrator you know that you can easily help reduce costs and make the company happy again, select all of the statements below that you might do in order to optimize costs quickly.

* Remove all unassigned Elastic IP addresses and create snapshots of all unused EBS volumes and terminate the volumes
* Create a snapshot of RDS instances that have had 0 DB connections after 7 days and terminate the RDS instances
* Reduce instance size for under-utilized instances or combined the instances and terminate the unused

### 2. In order to monitor operating system-level metrics such as disk usage, swap usage, and memory usage, you must install EC2 monitoring scripts. These scripts put custom metric data into Amazon CloudWatch. What do you need to do in order to give the instance permissions to put those custom metrics in CloudWatch?

> Assign a role to the EC2 instance which will be sending custom metrics to CloudWatch

### 3. You currently have Nginx webservers on EC2 instances which receive requests from your ELB. Those Nginx webservers return results from your PHP application. This application connects to an RDS database instance to read and write data. However, a few months ago, you realized that ElastiCache with Redis (cluster mode disabled) could reduce the load on your RDS database by caching some of the popular data. Fast-forward to today, and your ElastiCache Redis (cluster mode disabled) cluster is under a heavy read load and needs to scale. Which of these is the best way to scale your cluster?

> Scale by adding read replicas to your cache cluster.

### 4. One of your instances is not responding. After investigating you see that the system status checks indicate a problem. What would be the best method for attempting to fix a failing system status check?

> Stop and then start the instance so it can be launched on a new host

### 5. What are the two different kinds of status checks involving Amazon EC2 instances?

> System status check and Instance status check

### 6. Which of the following metrics do not get automatically reported to Amazon CloudWatch from Amazon EC2? (Choose 3) BUT Network packets received on all network interfaces INCLUDE IT


* The amount of memory being used
* How much disk space is available
* The amount of swap space used

### 7. You've created a CloudWatch alarm to monitor ElastiCache (memcached) evictions. The CloudWatch alarm begins to alert you that the number of evictions has surpassed your application's requirements. How might you go about resolving the high amount of evictions issue?

* Increasing the size of the ElastiCache instance
* Adding another node to the ElastiCache cluster

### 8. Which of the following are valid alarm statuses in CloudWatch?

* ALARM
* OK
* INSUFFICIENT_DATA

### 9. What best describes burstable performance for t2.micro instances?
> Burstable performance gives you a baseline performance and CPU credits that allow you to burst above this baseline if needed.

### <span style="color: black">&#x1F535; Demonstrate the ability to properly administer to highly available architecture in AWS:


### 10. Your company’s website is hosted on several EC2 instances behind an Elastic Load Balancer. Every time the development team deploys a new upgrade to the web application, the support desk begins receiving calls from customers being disconnected from their sessions. Customers’ session data is very important, as it contains their shopping cart information, and this information is lost when the customers’ sessions are disconnected. Which of the following steps can be taken together to prevent customers’ shopping cart data from being lost without affecting website availability?

* Use ElastiCache to store session state.
* Enable connection draining and remove instances from the Elastic Load Balancer prior to upgrading the application on those instances.

```
Correct Answer: C
Why is this correct?
Storing session state in ElastiCache will allow session data to be shared by all the instances, including the newly added ones.

Correct Answer: D
Why is this correct?
Connection draining will make sure in-flight requests have been completed before the instance is deregistered.
```

### 11. You manage a social media website on EC2 instances in an Auto Scaling group. You have configured your Auto Scaling group to deploy one new EC2 instance when CPU utilization is greater than 90% for 3 consecutive periods of 10 minutes. You notice that between 6:00 pm and 10:00 pm every night, you see a gradual increase in traffic to your website. Although Auto Scaling launches several new instances every night, some users complain they are seeing timeouts when trying to load the index page during those hours. What are cost effective solutions to this problem? (Choose 3).

* Decrease the collection period to five minutes
* Decrease the threshold CPU utilization percentage at which to deploy a new instance
* Decrease the consecutive number of collection periods that must elapse before a new instance is deployed

### 12. You manage a financial application which operates from within a VPC running in us-east-1. The application operates on EC2 instances which are controlled and scaled using an autoscaling group configured to operate over 3 subnets within the VPC. The application needs to talk to an external financial API using HTTPS and the solution must be able to cope with the failure of up to two availability zones. You have been informed the instances cannot be given public IP's.Which solution allows the instances to access the public financial API while meeting the security and high availability (HA) requirements? (choose one)
> Deploy 3 NAT Gateways

```
True HA requires a NAT Gateway to be deployed into each AZ that the VPC uses - a NAT gateway is no HA by design.
Each subnet would have a route table with a default route (0.0.0.0/0)
pointing at the NAT Gateway in the same AZ. With this configuration 1 or 2 AZ's could fail and the ASG and remaining NAT Gateway would continue to function.

```

### 13. You have been asked to maintain a small AWS environment consisting of five on-demand EC2 web server instances. Traffic from the Internet is distributed to these servers via an Elastic Load Balancer. Your supervisor is not pleased with a recent AWS bill. Assuming a consistent, moderately high load on the web servers, what option should you recommend to reduce the cost of this environment without negatively affecting availability?

> You have been asked to maintain a small AWS environment consisting of five on-demand EC2 web server instances. Traffic from the Internet is distributed to these servers via an Elastic Load Balancer. Your supervisor is not pleased with a recent AWS bill. Assuming a consistent, moderately high load on the web servers, what option should you recommend to reduce the cost of this environment without negatively affecting availability?

```
Reserved instances are recommended for instances with a consistently high load.

```

### 14. You are managing a large magazine application inside of Amazon Web Services. Your company posts an article that gets picked up internationally, causing millions of visitors to hit your application. Such a large increase in traffic causes strain on your DB server which is servicing the blog's static content. You use EC2 instances for your web servers. How might you quickly resolve this issue and make the blog post infinitely scalable?

> Create a static HTML page using S3 and use Route 53 to point the DNS to the static S3 bucket.

```
Since the article content is static, it can be saved as an HTML page. S3 buckets can be configured to serve static web pages.


```

### 15. You have an Elastic Load Balancer (ELB) with an Auto Scaling group for your application. You also have 4 running instances, and you have Auto Scaling enabled. Some of those instances are running in one Availability Zone, and others are in a different Availability Zone. Some instances within one of the zones are not available to the ELB. What could be the cause?

> The ELB is not configured for that Availability Zone.

```
When creating an ELB, you specify the subnets/AZs to which it will send traffic.


```
### 16. Your MySQL RDS instance is experiencing high levels of read requests during business hours and performance is being affected. You notice its backups are not being performed. What is the first step you can do to resolve this performance issue?

> Enable automated backups of the database.

```
Enabling backups is required before enabling read replicas. https://aws.amazon.com/rds/faqs/#Read_Replicas

```

### 17. You manage a technology blog website on EC2 instances in an Auto Scaling group behind an Elastic Load Balancer. Traffic volume to the site is consistently low, except during several weeks of the year when major technology conferences are occurring, when traffic increases 300 percent. What is the best way to manage this environment? (Choose 2)

* Use A blend of reserved and on-demand instances to handle the increased load during the technology conference weeks.
* Pre-warm the Elastic Load Balancer prior to technology conference weeks if load testing tools show the need.

```

Correct Answer: B
Why is this correct?
A blend of reserved and on-demand instances would be optimum for this application.

Correct Answer: D
Why is this correct?
Pre-warming the ELB is necessary if there is a sudden very large spike in traffic.
```

### 18. You are running an application that has an IP address assigned to the EC2 instance of the application. How might you apply high availability to the instance running that application in the future?

> Assign an elastic IP address to the EC2 instance, have a backup instance running. In the event of failure, move the Elastic IP from the primary instance to the backup instance.

```
Elastic IPs allow you to mask the failure of an instance by quickly remapping the address to a healthy instance.

```
### <span style="color: black">&#x1F535; Demonstrate the ability to analyze and increase performance in an AWS environment

### 19. You have enabled a CloudWatch metric on your Memcached ElastiCache cluster. Your alarm is triggered due to an increased amount of evictions. How might you go about solving the increased eviction errors from the ElastiCache cluster?

* Add a node to the cluster
* Increase the node size

```
Correct Answer: A
Why is this correct?
A high eviction rate is caused by insufficient memory on the cluster. You can add memory to the cluster by increasing the node size or adding a node to the cluster.

Correct Answer: D
Why is this correct?
A high eviction rate is caused by insufficient memory on the cluster. You can add memory to the cluster by increasing the node size or adding a node to the cluster.
```

### 20. We have a two-tiered application with the following components. We have an ELB, three web and application servers on EC2, and one MySQL RDS database. When our load grows, the database queries take longer and slow down the overall response time for the user request.Which three options would we choose to speed up performance?

* We can cache our database queries with ElastiCache
* We can create an RDS read-replica and redirect half of the database read requests to it
* We can shard the database and distribute the load between shards

```
Correct Answer: B
Why is this correct?
Elasticache is a service that will run an in-memory datastore (Memcached or Redis) on a managed cluster. You can configure your application servers to cache query results from your database in the Elasticache cluster and check the cache for the result set before running the select query on the database.

Correct Answer: C
Why is this correct?
This will free the primary database to just handle the write queries (Insert, Update, Delete), while the read-replica handles the read queries (Select).

Correct Answer: D
Why is this correct?
Sharding the database will double its capacity for both reads and writes.
```

### 21. Your RDS instance is consistently maxed out on its resource utilization. What are multiple ways to solve this issue?

* Fire up an ElastiCache cluster in front of your RDS instance.
* Increase RDS instance size.
* Offload read-only activity to a read replica if the application is read-intensive.

```
Correct Answer: B
Why is this correct?
By caching query results in Elasticache, your RDS instance will have less queries to execute.

Correct Answer: C
Why is this correct?
Increasing the RDS instance size will add more CPU, memory, and network capacity.

Correct Answer: D
Why is this correct?
By offloading Select statements to a ready replica, the primary RDS instance will only have to handle the writes.
```
### 22. You are running an EC2 instance serving a website with an SSL certificate. Your CPU utilization is constantly high. How might you resolve this issue?

> Offload the SSL cert from the EC2 instance and configure it on the Elastic Load Balancer

```
Correct Answer: D
Why is this correct?
A nice feature of the ELB is its ability to terminate SSL. This means that the load balancer will handle the CPU intensive SSL handshake so your instance doesn't have to. You can then send plain HTTP from the ELB to the EC2 instance.
```
### 23. Your supervisor is concerned about losing read access to your RDS database in the unlikely event of an AWS regional failure. You design a plan to create a read replica of the database in another region, but your supervisor sees a problem with this plan. What problem does he see?

> Your RDS database is using an old version of PostgreSQL, which does not support cross-region replication.

```
This feature requires version 9.5.2 or 9.4.7 and higher.
```

### 24. A game server is currently in the process of being migrated to AWS from an on-premises datacenter. One of the server requirements is that the storage it uses needs to be resilient against hardware failure and able to provide 50,000 IOPS. What storage type should you suggest?

> io1 EBS storage

```
Correct Answer: B
Why is this correct?
io1 EBS storage is the best solution, its resilient to hardware failure and can provide up to 64,000 IOPS per volume and 80,000 per instance https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html
```

### 25. In your infrastructure, you are running a corporate application using a T2.Small instance. You are also using a NAT instance so that your private instances can reach out to the internet without being publicly available. What is one thing that we should do to speed up bandwidth and performance?

> Increase your T2.Small instance to a m4.large.

```
Correct Answer: C
Why is this correct?
Instance size has a direct influence on the amount of data your instance can send and receive. Increasing the instance size will increase the available network throughput. You should also check to see if the NAT instance is a bottleneck and consider changing its size or type.

```

### 26. We have a customer with a web application that uses cookie-based sessions to see if users are logged in. This uses the Amazon Elastic Load Balancer and Auto Scaling. When the load on the application increases, Auto Scaling launches new instances so that the load on the other instances does not increase too much. However, all of the existing users still experience slow response time. What could be the cause of this?

> The ELB is continuing to send the request to the web app with the previously established connections in the same backend instances rather than spreading them to the new instances.

```
Correct Answer: D
Why is this correct?
It is likely that the sticky session feature of the ELB is enabled. Disable session stickiness on the ELB to fix this.
```

### 27. Which of the following would you be likely to schedule during a maintenance window (rather than during business hours) when working in a Multi-AZ RDS environment?

> All of these are correct

```
Correct Answer: A
Why is this correct?
While patches and upgrades can be performed with minimal downtime in a Multi-AZ environment, any work that requires a failover of the database or functional changes to the database or underlying OS can still impact connectivity and should be performed during a maintenance window.
```


### <span style="color: black">&#x1F535; Demonstrate the ability to deploy and provision AWS resources


### 28. You are running an application on an EC2 instance that needs access to stored images on Amazon S3. What would be the best practice for allowing API access from the EC2 instance to Amazon S3?

> Launch the EC2 instances using AWS IAM roles that allows API access for the instance

```
When available, it is best practice to use IAM roles for communicating with the AWS API. You should never store API credentials on an AMI.

```

### 29. Your company is setting up an application that is used to share files. Because these files are important to the sales team, the application must be highly available. Which AWS-specific storage option would you set up for low cost, reliability, and security?

> Use Amazon S3, which can be accessed by end users with signed URLs.

```
S3 is designed for 99.999999999% durability and 99.99% availability over a year. Signed URLs can be used to restrict access to the application users.
```

### 30. You can use this to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances.

> NAT Gateway

```
You can use a network address translation (NAT) gateway to enable instances in a private subnet to connect to the internet or other AWS services, but prevent the internet from initiating a connection with those instances.


```

### 31. Your company is ready to start migrating its application over to the cloud, but you cannot afford any downtime. Your manager asks you to come up with a plan of action. She also wants a solution that offers the flexibility to test the application on AWS with only a subset of users, but with the ability to increase the number of users over time. Which of these options are you most likely to recommend?

> Implement a Route53 weighted routing policy that distributes the traffic between your on-premises application and the AWS application depending on weight.

```
This option works great because we can modify the weight of one record set over the other to increase or decrease the amount of traffic. If the application on AWS is behaving properly, we can slowly increase the number of users that get routed to that application and slowly phase out the on-premises application. Otherwise, we can revert back to the on-premises application.

```

### 32. You have been tasked by your manager to build a tiered storage setup for database backups and their logs. These backups must be archived to a durable solution. After 10 days, the backups can then be archived to a lower priced storage tier. The data, however, must be retained for compliance policies. Which tiered storage solution would help you save cost, and still meet this compliance policy?

> Set up an independent EBS volume where we can store daily backups and then copy these files over to S3, where we configure a bucket that has a lifecycle policy to archive files older than 10 days to AWS Glacier

```
AWS Glacier ( ~ $0.004 per GB / Month) is the most cost effective solution for durably storing archives. The archived data can be restored to S3 if ever needed.

```

### 33. What sort of host might you set up in your AWS environment that can be used as a way to “hop” into your environment to gain access to secure servers within a private subnet?

> Bastion host

```
This is also known as a Jump Box. The bastion host is launched into a public subnet and given an Elastic IP. Administrators connect to the bastion, and then from there can connect to the private instances, providing security group rules are created properly.


```

### 34. Which of the following statements are true?
* You can customize your AWS deployments using JSON templates in CloudFormation.
* You can customize your AWS deployments using the Ruby programming language with OpsWorks stacks.

```
Yes. CloudFormation let's you choose JSON or YAML for your templates.

Correct Answer: C
Why is this correct?
Yes. OpsWorks Stacks uses chef recipes written in Rub
```

### 35. What is a logical group of instances within a single AZ, recommended for applications that benefit from a low latency network connection?
> Cluster Placement Group

```
A cluster placement group is a logical grouping of instances within a single Availability Zone.

Cluster placement groups are recommended for applications that benefit from low network latency,
high network throughput, or both,
and if the majority of the network traffic is between the instances in the group.
To provide the lowest latency and the highest packet-per-second network performance for your placement group, choose an instance type that supports enhanced networking.
```

### 36. Your supervisor sends you a list of several processes in your AWS environment that she would like you to automate monitoring via scripts. Which of the following requires a custom script for monitoring?

> None of the provided options require a custom script.

```
The CloudWatch Agent can now monitor memory and disk usage.

```

### 37. A user is using AWS SQS, which operations are NOT supported by AWS SQS?

> ReadMessage

```
Correct - there is NO ReadMessage ... the closest valid operation is receive-message
```

### 38. A successful systems administrator does not need to create a script for:

* Sending CPU Utilization metrics to CloudWatch
* Automating backups of EBS volumes
* Automating backups of RDS databases

```
Correct Answer: A
Why is this correct?
The CPU Utilization metric is sent to CloudWatch automatically.

Correct Answer: B
Why is this correct?
This can now be accomplished without scripting using CloudWatch Events or AWS Backup

Correct Answer: D
Why is this correct?
AWS offers automated backups of RDS, thus it is not a requirement to script this task. AWS Backup can also do this function.
```

### 39. Which of the following is the best procedure for disaster recovery as it relates to RDS?

> Create a read replica in a different region with Multi-AZ enabled. In the event of a failover, promote the read replica to the primary and change the DNS for your application to point to the new primary endpoint.

```
Cross region read replicas are the preferred method to recover from a region failure. Additionally, we can now enable Multi-AZ during read replica creation so the new deployment can be fault tolerant This Cross region replicas for RDS are available for MySQL, MariaDB, Aurora, and PostgreSQL


```
### 41. Assuming you have kept the default settings and have taken manual snapshots, which of the following manual snapshots will be retained?

* A snapshot of an EBS root volume when the EC2 instance is terminated
* A snapshot of an RDS database when the RDS instance is terminated

```
Correct Answer: A
Why is this correct?
Manual snapshots of RDS databases and EBS volumes persist after instance termination.

Correct Answer: D
Why is this correct?
Manual snapshots of RDS databases and EBS volumes persist after instance termination.
```

### 42. A colleague noticed that CloudWatch was reporting that there have not been any connections to one of your RDS MySQL databases for several months. You decided to terminate the database. Two months after the database was terminated, you get a phone call from a very upset user who needs information from that database to run end-of-year reports. What can you do?

> If you took a manual snapshot of the database, you can restore the database from that snapshot.

```
Manual snapshots persist even after a database is terminated. There is not an expiration period for manual snapshots.

```

### 43. Which of the following will cause brief I/O suspension of an AWS RDS instance?

* Creating a Read Replica
* Creating a Snapshot

```
Correct Answer: B
Why is this correct?
Correct - When you initiate the creation of a read replica, Amazon RDS takes a snapshot of your source DB instance and begins replication. As a result, you will experience a brief I/O suspension on your source DB instance as the snapshot occurs. The I/O suspension typically lasts on the order of one minute, and is avoided if the source DB instance is a Multi-AZ deployment (in the case of Multi-AZ deployments, snapshots are taken from the standby).

Correct Answer: C
Why is this correct?
Correct - During the automatic backup window, storage I/O might be briefly suspended while the backup process initializes (typically under a few seconds) and you might experience a brief period of elevated latency. No I/O suspension occurs for Multi-AZ DB deployments, because the backup is taken from the standby. For SQL Server, I/O is suspended briefly for Multi-AZ deployments.
```

### 44. Which of the following events are mitigated by the RDS Multi AZ feature? (Choose all that apply)

* Storage failure on primary
* Loss of availability in primary Availability Zone
* Loss of network connectivity to primary

```
Correct Answer: A
Why is this correct?
Correct. Multi AZ protects against storage failure on the primary database.

Correct Answer: B
Why is this correct?
Correct. Muti AZ uses multiple Availability Zones.

Correct Answer: C
Why is this correct?
Correct. Muti AZ uses multiple Availability Zones, each with separate network connectivity.
```

### 44. Which of the following services have support for automated backups? (Choose all that apply.)
* ElastiCache and Redshift
* RDS
* EBS Volumes

```
Correct Answer: A
Why is this correct?
ElastiCache for Redis supports automatic daily backups. Redshift supports automated and manual snapshots.

Correct Answer: B
Why is this correct?
RDS supports automated and manual snapshots.

Correct Answer: D
Why is this correct?
EBS volumes can be snapshotted on a schedule with your own scripting or with CloudWatch Events. AWS Backup can also be used.
```

### 45. What happens during a failover process in a Multi-AZ deployment with AWS RDS instance?

> The DNS record of the DB instance changes from the primary to the standby DB instance

```
The Multi-AZ failover process does not require any action from the SysOps admin. The DNS on the backend of AWS will change from the primary to the secondary instance. This occurs during time periods such as DB failure and DB updates by AWS.


```
### <span style="color: black">&#x1F535; Demonstrate the ability to use key concepts to secure an AWS environment

### 46. What is the result of the following bucket policy?

```
{
    "Statement": [
        {
            "Sid": "SID1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::mybucket/*",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "50.97.0.0/32"
                }
            }
        }
    ]
}
```

> It will allow all actions to the contents of mybucket for requests coming from IP 50.97.0.0.

```
Requests coming from other IP addresses would be implicitly denied unless allowed by another policy assigned to the entity.


```

### 47. Your company's compliance department mandates that within your multi-national organization, all data for customers in the UK must never leave UK servers and networks. Similarly, US data must never leave US servers and networks without explicit authorization first. What do we have to do to comply with this requirement in our web-based applications running on AWS in EC2? The user has already set up a user profile that states their geographic location. Your company has a requirement to use the user provided location instead of any IP geolocation data.

> We can run EC2 instances in multiple regions, and leverage a third-party data provider to determine whether a user should be redirected to the appropriate region based on that user’s profiles.

```
This is better than relying on geolocation based lookups which are not 100% accurate.

```
### 48. We are preparing for our regularly scheduled security assessment. What two configuration management practices should our organization have implemented?

* Determine that our remote administrative access is performed securely
* Make sure that S3 bucket policies and ACLs correctly implement our security policies

```
Correct Answer: A
Why is this correct?
This includes limiting SSH and RDP to IP address ranges used by the remote administrators.

Correct Answer: B
Why is this correct?
Yes. Limiting access to sensitive data is always at the top of the list.
```

### 49. One of your EC2 instances uses the public IP of 203.0.113.128. You are attempting to only allow connections to the instance using TCP port 22 (SSH) from a single IP address of your on-premises firewall, which uses the ip of 119.18.36.32. Which of the following options will allow connections from your on-premises firewall on port 22, but deny all other public traffic using SSH. (Choose one)

> Configure a NACL on the subnet the EC2 instance is in. Add a rule for traffic from 119.18.36.32/32 to IP 203.0.113.128/32 allowing connections using tcp/22. Add another rule with a higher rule number DENYING all tcp/22 traffic from all sources.

```
This is the best solution because the inbound rule will allow traffic into the EC2 only from 119.18.36.32/32 while the rule with a higher rule number will block SSH traffic from other IPs.


```

### 50. What AWS services give you access to the underlying operating system?
* EC2
* Amazon EMR
* Elastic Beanstalk

```
Correct Answer: A
Why is this correct?
You can SSH (Linux) or RDP (Windows) to EC2 instances if you have access to private part of the key pair associated with the instance creation.

Correct Answer: B
Why is this correct?
You can SSH to the master node of an EMR cluster.

Correct Answer: C
Why is this correct?
You can access the instances created by Elastic Beanstalk the same way you access other EC2s.

```

### 51. A web application you manage is running on a public Elastic IP address within a VPC. You have determined the server is being attacked using a known SQL injection type exploit. Which AWS security entity should you look at using to effectively mitigate the attack.

 >Use WAF and ALB to protect the EC2 instance

```
Correct Answer: A
Why is this correct?
Web Application Firewall (WAF) and an ALB application load balancer could be used to protect the instance from a SQL injection style attack. https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-sql-conditions.html
```

### 52. What two options listed below are you responsible for in the AWS Shared Responsibility Model?

* An application that you have running within AWS EC2
* The operating systems' administrators group

```
Correct Answer: A
Why is this correct?
Application security is handled by you and your developers.

Correct Answer: D
Why is this correct?
Yes, you are fully responsible for OS level security.
```


### 53. We have developed a mobile application that gets downloaded several hundred times a week. What authentication method should we enable for the mobile clients to access images that are stored in an AWS S3 bucket that provides us with the highest flexibility and rotates credentials?

> Identity Federation based on AWS STS using an AWS IAM policy for the respective S3 bucket

```
The application will assume a role via STS and receive temporary credentials for the application to access the S3 bucket.


```

### 54. A deny overrides an allow in which circumstances?

* A NACL associated with subnet A defines two rules. Rule #100 explicitly denies TCP traffic on port 21 from 0.0.0.0/0 and rule #105 explicitly allows TCP traffic on port 21 from 0.0.0.0/0.
* An explicit allow is set in an IAM policy governing S3 access and an explicit deny is set on an S3 bucket via an S3 bucket policy.

```
Correct Answer: A
Why is this correct?
NACL rules are processed in order, so the Allow is never read.

Correct Answer: C
Why is this correct?
IAM and bucket policies are combined in this case.
```
### <span style="color: black">&#x1F535; Demonstrate the ability to properly configure, monitor, and troubleshoot AWS networking resources:

### 55. Your management team have asked for reporting data for one of your core business applications. The app runs inside a VPC and consists of 2 application services, one providing HTTPS access , the other providing API services. Specifically you need to show data for all incoming connections made to both instances, specifically source IP and Port in a format which can be imported into a visualisation app. Which method offers the best solution for this requirement.

> VPC Flow Logs

```
Correct Answer: C
Why is this correct?
VPC flow logs is a good solution, it can be configured on an instance, subnet or VPC basis and provide access to the information needed https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html
```

### 56. You have decided to extend your on-site data center to Amazon Web Services by creating a VPC. You already have multiple DNS servers on-premises. You are using these DNS servers to host DNS records for your internal applications. You have a corporate security network policy that says that a DNS name for an internal application can only be resolved internally and never publicly over the internet. Your existing on-premises data center is already connected to your VPC using IPSec VPN.How can you setup your VPC to use your on-prem DNS servers?

> Create a DHCP option set, add your on-prem DNS servers to it, and replace the option set on your VPC with the newly-created option set.

```
Correct Answer: D
Why is this correct?
This is correct. For details, see: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html
```

### 57. When managing our VPC in an AWS region, we want to give other teams access to create their own instances and modify the security groups inside subnets dedicated to their teams. We have to make sure the development team can NOT do anything in their subnets that could allow their instances to impact production instances in the production subnets. What can we do to separate out our VPC so that instances that the dev team can access can never interfere or interact with the ones within our production?

> We can create NACLs that restrict which subnets can talk to each other

```
Correct Answer: A
Why is this correct?
You create DENY rules in the production subnets for traffic originating from the development subnets.
```

### 58. Your infrastructure does not have an Internet Gateway attached to the VPC. What might you do in order to SSH into your EC2 instances? All other configurations are correct.

> Attach a Virtual Private Gateway and create a VPN connection

```
Correct Answer: D
Why is this correct?
Alternatively, you could attach an Internet Gateway and connect to a public or elastic IP on the instance.
```

### 59. What would be a reason you would upgrade to Direct Connect instead of a traditional VPN connection?

> You gain higher bandwidth and consistent network connectivity


```
Correct Answer: D
Why is this correct?
A private network connection with Direct Connect can reduce costs, increase bandwidth, and provide a more consistent network experience than Internet-based connections.
```

### 60. You configure a VPC with an Internet gateway that has a private and a public subnet, with each subnet in a different Availability Zone. The VPC also has a dual-tunnel VPN between the Virtual Private Gateway and the router in the private data center. You want to make sure you do not have a potential single point of failure in this design. What could you do to make sure we achieve this above environment?

> You set up a secondary router in your private data center to establish another dual-tunnel VPN connection with your Virtual Private Gateway.

```
Yes. The router is a single point of failure.
```
