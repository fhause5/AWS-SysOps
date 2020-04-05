### <span style="color: black">&#x1F535; Data Storage

### 1. Which are not replicated by default using S3 CRR?

* Objects that existed before replication
* Lifecycle policies
* Server-side encryption using KMS-managed keys
* Server-side encryption using customer-provided keys

```
Correct Answer: A
Why is this correct?
All objects existing before replication are not replicated across regions.

Video for reference: S3: Cross-Region Replication

Correct Answer: B
Why is this correct?
Lifecycle Policies are not replicated across regions with Cross-Region Replication.

Video for reference: S3: Cross-Region Replication

Correct Answer: C
Why is this correct?
KMS managed keys are not replicated across regions.

Video for reference: S3: Cross-Region Replication

Correct Answer: F
Why is this correct?
Customer provided encryption keys are not replicated across regions.

Video for reference: S3: Cross-Region Replication
```

### 2. What AWS service is used to monitor the performance and availability of Amazon EFS?

> CloudWatch

### 3. Which of these is not a characteristic of a RDS Multi-AZ Failover Deployment?

> Used for failover

```
RDS Multi-AZ Failover Deployments do not serve legitimate traffic.
```

### 4. How long do you have to validate your Vault Lock Policy?

> 24h

```
You have 24 hours to validate your Vault Lock Policy before it becomes immutable.
```

### 5. Which of these are characteristics of a Read Replica?

* Can serve legitimate traffic
* Helpful with disaster recovery
* Receives the offloaded work of master database
* Can be promoted to a stand-alone database instance

```
Correct Answer: A
Why is this correct?
Read Replicas can serve legitimate traffic.

Video for reference: RDS: Scaling for Performance

Correct Answer: C
Why is this correct?
Read Replicas help with disaster recovery because they possess an asynchronous copy of the master database.

Video for reference: RDS: Scaling for Performance

Correct Answer: D
Why is this correct?
Read Replicas receive the offloaded work of the master database to boost performance.

Video for reference: RDS: Scaling for Performance

Correct Answer: G
Why is this correct?
Read Replicas can be promoted to stand-alone database instances.

Video for reference: RDS: Scaling for Performance
```

### 6. Which of these available storage classes have 99.999999999% durability?

> All S3 storage classes

### 7. In terms of EBS and instance-store root volumes, what is the default action upon instance termination?

> Deletion

### 8. Which of these is not a characteristic of Amazon EFS?

> EFS NOT supports the Windows operating system

### 9. What storage classes are integrated with Amazon EFS?

* Standard
* Standard-IA

### 10. Which are not replicated by default using S3 CRR?

* Objects that existed before replication
* Lifecycle policies
* Server-side encryption using KMS-managed keys
* Server-side encryption using customer-provided keys

```
Correct Answer: A
Why is this correct?
All objects existing before replication are not replicated across regions.

Video for reference: S3: Cross-Region Replication

Correct Answer: B
Why is this correct?
Lifecycle Policies are not replicated across regions with Cross-Region Replication.

Video for reference: S3: Cross-Region Replication

Correct Answer: C
Why is this correct?
KMS managed keys are not replicated across regions.

Video for reference: S3: Cross-Region Replication

Correct Answer: F
Why is this correct?
Customer provided encryption keys are not replicated across regions.

Video for reference: S3: Cross-Region Replication
```

### 11. What is the time interval at which EFS metric data gets sent to CloudWatch?

> 1 minute

### 12. What AWS service is used to monitor the performance and availability of Amazon EFS?

> CloudWatch

### 13. What is the difference between Amazon EFS and EBS?

> EFS can be attached to multiple instances

### 14. Which of these is  AWS data transfer services?

* Snowball
* Snowmobile
* Snowball Edge

### 15. Which command expands the filesystem in a resized T2 partition?

> sudo resize2fs /dev/xvda

### 16. How long do you have to validate your Vault Lock Policy?

> 24h

### 17. Which CloudWatch Metric will not be performed on a Provisioned IOPS SSD (io1) volumes?

> BurstBalance

### 18. How often are CloudWatch metrics created for an EBS volume?

> every 5 minutes

### 19. Which CloudWatch metrics are only performed on Provisioned IOPS SSD (io1)?

* VolumeThroughputPercentage
* VolumeConsumedReadWriteOps

```
Correct Answer: A
Why is this correct?
The CloudWatch metric of "VolumeThroughputPercentage" are only performed on Provisioned IOPS SSDs'.

Video for reference: EBS: Metrics

Correct Answer: F
Why is this correct?
The CloudWatch metric of "VolumeConsumedReadWriteOps" are only performed on Provisioned IOPS SSDs'.

Video for reference: EBS: Metrics
```

### 20. What must be enabled on a database to create Read Replicas?

> Enable database backups

### 21. What does CRR stand for?

> Cross-Region Replication

### 22. Which volume type has a maximum baseline performance of 64,000 IOPS?

> Provisioned IOPS SSD Volume

```
Provisioned IOPS SSD volume has a maximum baseline performance of 64,000 IOPS.
```

### 23.Which is true of all Vault Lock policies?

> Vault Lock policies are immutable

```
All Vault Lock policies are immutable, after 24 the Lock ID is permanently deleted.

```
### 24. What does S3 CRR (Cross-Region Replication) do?

> Enables asynchronous copy from source bucket to a destination bucket in a different region.

### 25. How many times can an object be replicated with S3 CRR?

> 1

```
An object can only be replicated across regions to one other bucket. This prevents objects from bucket hopping.


```

### 26. If an EBS volume is encrypted at the time of a snapshot, what will be the status of the snapshot?

> Encrypted

```
The EBS volume snapshot will also be encrypted under the same key(s).
```

### 27. Which of these is not a component of the AWS Storage Gateway?

* Object Gateway
* Archive Gateway

```
Correct Answer: A
Why is this correct?
Object Gateway is not a component of the AWS Storage Gateway.

Video for reference: AWS Storage Gateway

Correct Answer: D
Why is this correct?
Archive Gateway is not a component of the AWS Storage Gateway.
```
### 28. Which of these is not a characteristic of a RDS Multi-AZ Failover Deployment?

> Serves legitimate traffic

```
RDS Multi-AZ Failover Deployments do not serve legitimate traffic.
```

### 29. Which AWS ground transport service has a 100 PB capacity?

> Snowmobile

### 30  Which of these is not a possible transition of storage classes?

> Glacier -> Standard

possible:
```
Standard -> Standard-IA
Standard -> Intelligent-Tiering
Standard-IA -> Glacier
```

### 31. How long is EFS metric data retained within CloudWatch?

> 15 months

### 32 Which of these is not an AWS S3 storage class? Please select the most appropriate answer.

> Archive

AWS S3 storage class:

```
Glacier
Standard-IA
One Zone-IA
Standard
```
