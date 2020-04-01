# Expectations Report Card Security on AWS

### 1. Which of these AWS services includes OS patching under the Shared Responsibility Model as AWS's responsibility?

> S3, Amazon RDS, Lambda, Amazon DynamoDB

* customer's responsibility to focus on patching the OS EC2


### 2.Which of the following are examples of the default alias naming convention for AWS Managed KMS keys?

> aws/rds,  aws/sns

### 3.Which of the following is capable of enabling MFA Delete?

> Root user

### 4.What is the necessary at the end of a Bucket Policy's S3 Bucket ARN to enable access to all objects inside an S3 Bucket?

> S3_Bucket_ARN/*

### 5.What conditions are AWS' WAF (Web Application Firewall ) rules based on?

> SQL injection, IP Address, HTTP header


### 6.Which of these methods can you utilize to install Amazon Inspector on a Linux-based AMI (Amazon Machine Image)?


> wget https://inspector-agent.amazonaws.com/linux/latest/install
sudo bash install, AWS Console, curl -O https://inspector-agent.amazonaws.com/linux/latest/install


### 7.Which IAM feature can grant permissions for an AWS Resource to interact with another AWS Service?

> IAM Role

* Groups > policy > role

### 8.Which NACL (Network Access Control List) will allow the SG (Security Group) to make connections over ports 22/80/443 for inbound traffic?

> NACL 1024-65535

### 9.Which of the following is not an AWS Responsibility based on the Shared Responsibility Model?


> IAM (Identity Access Management)

* DDoS, AWS Regions, Data center Personnel Security

### 10.Which of the following is not a best practice when it comes to AWS Security?

> VPC without workload isolation

### 11.Which selections out of the following is a Customer Responsibility based on the Shared Responsibility Model?

Network device security

> Password and key rotation, IAM (Identity Access Management), Data in transit and at rest

* Fire/power/climate management,DDoS protection

### 12.Which of the following do WAF rules span?

> AWS Region

B
IAM User

### 13.Which of these do Business or Enterprise customers have access to, when using AWS Trusted Advisor, that other customers do not?


> Programmatic access, CloudWatch Automation

### 14When using ACM SSL, which port number should be added to the load-balancer for HTTPS requests?

> 443

Correct Answer: D
Why is this correct?
This is the correct port for listening to the HTTPS connections on a load-balancer using ACM SSL.

Video for reference: AWS Certificate Manager

INCORRECT
15.
What IAM policy grants full administrative actions to an IAM user, but excludes billing access on an AWS account?

> AdministratorAccess

### 16.In regards to Penetration testing in AWS, which of the following statements is true?

> Limited penetration testing is allowed without prior AWS approval.


* All penetration testing is allowed without prior approval, Limited penetration testing is allowed without prior AWS approval, All penetration testing is allowed with prior approval from AWS, No penetration is allowed.

### 17.Which of these is a required prerequisite to enabling MFA Delete on an S3 Bucket?

> Enable Versioning

> 18.Which of the following is a benefit with ACM (AWS Certificate Manager)?


> Native integration with AWS Services, No associated costs for certificates, Certificates auto-renew

### 19.Which of these is used to assign permissions to an IAM Group?

> IAM Policies

### 20.Which port(s) are the ephemeral ports for an AWS VPC (Virtual Private Cloud)?

> 1024-65535

### 21.Which of the following should require MFA (Multi-Factor Authentication)?

> IAM Users with AWS Console access

### 22.Which of these is the scope of use for an AWS KMS key?

> Region

### 23.How many IAM roles can be assigned to an AWS service at a time?

> 1

None of these answers pertain

### 24.What permissions is an IAM user granted at the time of creation by default?


> Implicit denial on all AWS services

25.
For which of the following can we directly attach an IAM Policy?

> IAM Roles, IAM Group, IAM User

D
All of these can have an IAM policy attached directly to them.

### 26.Which of these services is integrated with WAF (Web Application Firewall)?

> ALB, CloudFront, API Gateway

### 27.Which of the following is a benefit of Amazon Inspector?


> Testing network reachability and security state, Assessment of best practice and deviation from those practices, Provides recommendation for resolutions, Analyzing of AWS Resource behavior

### 28.Which of these can be used to mitigate the accidental deletion of an object in an S3 Bucket?

> MFA Delete

29.
Which of these are permitted services for vulnerability and penetration testing without prior approval from AWS?


> Amazon RDS, Amazon EC2 instances, Amazon CloudFront

### 30.Which of the following is taking place when we suspend versioning on an S3 Bucket?


> Temporarily stopping object versioning

D
Deleting the current object versions

### 30. Temporary credentials

> Sts

### Time frame for AWS KMS

> 7-30 days

### 31. Amazon SNS

> Amazon Simple Notification Service

### 32. Aws Resource integrated with an AWS KMS via

> 1 key by default

### 33. Default time for STS Temporary credentials to remain active

> 1 hour

### 34. AGAIN

> Policy > roles > groups

### 35. Administrator access:

> PowerUserAccount - all access
> AdministratorAccess - all access without biling

### 36. ACM SSL validating

> DNS and email validating

### 37. Optional parts of S3 Bucket Policy

> Condition

### 38. How many IAM roles to Services

> Services can have one IAM roles

### 39. Compliance - CloudHSM is built on hardware that is validated at Federal Information Processing Standard (FIPS)

> 140-2 Level 3

### 40 Who can use STS

> Federated User
> IAM users

### 41. Scope for AWS KMS keys

> region

### 42. The best practise for daily work and administration

> IAM with admin access

### 43. Customer responsibility

> Passwords and key
> IAM
> Data in transit and at rest
