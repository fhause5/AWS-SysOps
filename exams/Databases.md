### <span style="color: black">&#x1F535; Databases

### 1. Which of these can we use to know when an RDS Multi-AZ failover event occurs?

* Email
* Amazon RDS Dashboard
* SMS

```
Correct Answer: A
Why is this correct?
Email is a method of receiving notification about the occurrence of a Multi-AZ failover event.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments

Correct Answer: B
Why is this correct?
The Amazon RDS Dashboard Events tab is a method of manually checking notifications on the occurrence of a Multi-AZ failover event.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments

Correct Answer: E
Why is this correct?
SMS is a method of receiving a text message notification about the occurrence of a Multi-AZ failover event.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments
```

### 2. Which of the following are data type(s) of DynamoDB? Please select the appropriate answer.

> Scalar, document, and set

### 3. What are two of the available node types for Amazon ElastiCache of the current generation? (Choose 2)

* General Purpose
* Memory Optimized

### 4. Which of the following database engines is not supported by Amazon RDS?

> MongoDB

### 5. Commonly, Solutions Architects will use Multi-AZ deployments for the intent of failover operations. Which of the following describes the design of Multi-AZ deployments used in failover operations?

* Highly Available
* Fault-Tolerant

```
Correct Answer: B
Why is this correct?
The design of a Multi-AZ Deployments is described as Highly Available because access to your databases can be maintained during maintenance, DB failure, or AZ problems.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments

Correct Answer: D
Why is this correct?
The design of a Multi-AZ Deployment can be described as Fault Tolerant. This fault tolerance is achieved by having standby failover replications of the RDS Master instance.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments
```
### 6. Which of the following is the most accurate in regards to Multi-AZ Deployments?

> Multi-AZ Deployments automate RDS failover, consist of RDS master and Multi-AZ DB instance, and perform synchronous replication of RDS Master to Multi-AZ DB instance.

```
Correct Answer: F
Why is this correct?
Multi-AZ Deployments are intended to automate RDS failover, consist of RDS master and Multi-AZ DB instance while performing synchronous replication from RDS Master to Multi-AZ DB instance.

Video for reference: Amazon RDS: Understanding Multi-AZ Deployments
```

### 7. Which of these must be manually setup after restoring a DynamoDB table?

* Auto-scaling policies
* Amazon CloudWatch metrics and alarms
* Tags
* Only Tags and AWS IAM policies
* All of these are automatically restored when restoring a DynamoDB table
AWS IAM policies

### 8. What is Amazon Redshift used for?

> Data warehousing solution

### 9. Which one of the following best describes means for monitoring Amazon RDS?

* CloudWatch metrics
* Enhanced monitoring
* RDS events

```
Amazon RDS may be monitored by CloudWatch, RDS events, and enhanced monitoring.

Video for reference: RDS: Monitoring for Performance and Availability

```

### 10. Which of the following are characteristics of the Amazon Redshift Leader node?

* Receives queries from client applications
* Creates execution plans
* Parses queries
* Coordinates parallel execution

```
Correct Answer: A
Why is this correct?
The leader node receives queries from client applications.

Correct Answer: B
Why is this correct?
The leader node creates execution plans for the compute nodes.

Correct Answer: C
Why is this correct?
The leader node parses queries.

Correct Answer: D
Why is this correct?
The leader node coordinates the parallel execution of the compute nodes.
```
### 11. What is the maximum number of data copies that Amazon Aurora can lose without affecting writes?

> 2

### 12. What CloudWatch metric keeps track of items removed to free up space?

> Evictions

```
Evictions are a CloudWatch metric that keeps a record of removal events for freeing up space.

Video for reference: Amazon ElastiCache: Monitoring for Performance and Availability
```
