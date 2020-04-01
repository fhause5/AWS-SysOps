### Auditing Resource Compliance with AWS Config

> In this hands-on lab, we'll implement AWS Config rules and use Config for compliance auditing and remediation. We will configure compliance rules for evaluating EC2 instance type, if S3 versioning is enabled, EC2 instances in a VPC, and if CloudTrail is enabled.

> These rules will give you firsthand knowledge about how the AWS Config service works. We will then explore the configuration management aspect of Config.

* Solution
Log in to the live AWS environment with the cloud_user credentials provided.

* Make sure you are using the N. Virginia (or us-east-1) AWS region throughout the lab.

### Enable Config in the Account
 * Navigate to the Config service.
 * Click Get started.
 * On the Settings page, check Record all resources supported in this region.
 * Choose Create a bucket, and leave the default name.
 * Do not check to create an SNS topic at this time.
 * Check Use an existing AWS Config service-linked role.
 * Click Next.
 * On the AWS Config rules page, click Skip.
 * On the Review page, click Confirm.

### Configure Rules for Resources
* In the left-hand menu, click Rules.
* Click Add rule.
* Search for "cloudtrail".
* Select the cloudtrail-enabled card.
* Leave the default parameters, and click Save.
* Click Add rule.
* Search for "desired".
* Select the desired-instance-type card.
* In the Rule parameters section, enter a value of "t2.micro".
* ick Save.
* Click Add rule.
* Search for "ec2-instances".
* Select the ec2-instances-in-vpc card.
* In a new browser tab, navigate to VPC > Your VPCs.
* Copy the VPC ID of the listed VPC.
* Back in the Config browser tab, enter the VPC ID as the value under
* Rule parameters.
* Click Save.
* Click Add rule.
* Search for "s3-bucket".
* Select the s3-bucket-versioning-enabled card.
* Click Save.

### Configure the Non-Compliant Resources to Comply
* Open S3 in another browser tab.
* Select the bucket listed to open it.
* Go to the Properties tab.
* Select the Versioning card.
* Click to Enable versioning.
* Click Save.
* Navigate to CloudTrail.
* Click Create trail.
* Name the trail (e.g., "MyTrail").
* Under Storage location, choose Create a new S3 bucket, and give it a unique name (e.g., "cloudtrail-" with a series of random numbers at the end).
* Click Create.
* Re-Evaluate the Non-Compliant Rules in Config
* Navigate back to the Config tab.
* On the Rules page, click the S3 bucket rule.
* Choose Re-evaluate.
* Back on the Rules page, wait for the S3 rule to become compliant. (It could take about 10 minutes.)
* Now, select the CloudTrail rule.
* Choose Re-evaluate.
* Back on the Rules page, wait for the CloudTrail rule to become compliant.
* Conclusion
* Congratulations on completing this hands-on lab!
