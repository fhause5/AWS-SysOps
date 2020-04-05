### <span style="color: black">&#x1F535; Provisioning, Deployment, and Management

### 1. What disaster recovery option keeps all your critical core components running and up to date?

> Pilot Light Method

```
Why is this incorrect?
The Backup and Restore Method is the slowest method of restoration, and it is also the cheapest.

Video for reference: Disaster Recovery

Correct Answer: C
Why is this correct?
The Pilot Light Method keeps all core components running and up to date.

Video for reference: Disaster Recovery
```
### 2. In regards to AWS Systems Manager, where should passwords and secrets be stored?

> Parameter Store

```
The parameter store allows for setting an encrypted value that can only be accessed with the correct IAM privileges.
```
### 3. Which of the following tasks does AWS Elastic Beanstalk automatically perform?

* Health monitoring
* Auto Scaling
* Capacity provisioning
* Load balancing

```
Why is this correct?
Health monitoring is managed automatically with AWS Elastic Beanstalk.

Video for reference: AWS Elastic Beanstalk

Correct Answer: B
Why is this correct?
Auto scaling is managed automatically with AWS Elastic Beanstalk.

Video for reference: AWS Elastic Beanstalk

Correct Answer: C
Why is this correct?
Capacity provisioning is managed automatically with AWS Elastic Beanstalk.

Video for reference: AWS Elastic Beanstalk

Correct Answer: D
Why is this correct?
Load balancing is managed automatically with AWS Elastic Beanstalk.

Video for reference: AWS Elastic Beanstalk
```
### 4. Which of the following is required for an EC2 instance's SSM agent to communicate with AWS Systems manager? Please select the most appropriate answer.

> IAM Role

```
An IAM Role is required for the SSM agent to allow an EC2 instance to communicate with AWS Systems Manager.

Video for reference: AWS Systems Manager
```

### 5. What language is used to create recipes for AWS OpsWorks?

> Ruby

```
Ruby is the language used with AWS OpsWorks to create recipes.

```

### 6. What disaster recovery option has a one-to-one copy of infrastructure and active-active configuration?

> Multi-Site Solution Method

```
The Multi-Site Solution Method is a practice of having a one-to-one active-active copy of infrastructure and configuration.

Video for reference: Disaster Recovery
```

### 7. What disaster recovery option is the slowest restoration method?

> Backup and Restore Method

```
The Backup and Restore Method is the slowest method of restoration, and it is also the cheapest.

Video for reference: Disaster Recovery
```

### 8. What component of the AWS OpsWorks anatomy represents a set of resources we want to manage as a group?

> Stacks

```
Why is this correct?
Stacks represent a set of resources we want to manage as a group.

Video for reference: AWS OpsWorks https://docs.aws.amazon.com/opsworks/latest/userguide/welcome_classic.html#welcome-classic-stacks
```
### 9. What AWS Elastic Beanstalk deployment option allows you to deploy a new version of an application in batches of EC2 instances?

> Rolling

```
Your Answer: A
Why is this incorrect?
Green/Blue deploys a new version of an application to a separate environment.

Video for reference: AWS Elastic Beanstalk

Correct Answer: D
Why is this correct?
Rolling deploys the new version of an application to batches of instances at a time.

Video for reference: AWS Elastic Beanstalk
```

### 10. What deployment software is used to deploy infrastructure as code with AWS OpsWorks?

* Chef
* Puppet  

```
Your Answer: A
Why is this incorrect?
Ansible is a deployment software but is not used with AWS OpsWorks.

Video for reference: AWS OpsWorks

Your Answer: C
Why is this incorrect?
AWS CodeDeploy is a service used to automate code deployments across compute services.

Video for reference: AWS OpsWorks

Correct Answer: B
Why is this correct?
Puppet is a deployment software used with AWS OpsWorks to deploy infrastructure as code.

Video for reference: AWS OpsWorks https://docs.aws.amazon.com/opsworks/latest/userguide/welcome_opspup.html

Correct Answer: D
Why is this correct?
Chef is a deployment software used with AWS OpsWorks to deploy infrastructure as code via recipes.

Video for reference: AWS OpsWorks


```
