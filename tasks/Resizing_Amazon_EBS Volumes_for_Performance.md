### <span style="color: black">&#x1F535; Resizing Amazon EBS Volumes for Performance


### user data
```
#!/bin/bash -xe
yum update -y
yum install -y httpd24 php70 mysql56-server php70-mysqlnd git
cd /var/www/html
git clone https://github.com/linuxacademy/content-aws-soa-c01.git
cd content-aws-soa-c01/wp-site/
mv * /var/www/html
groupadd www
usermod -a -G www cloud_user
chown -R root:www /var/www
chmod -R 2775 /var/www
echo '<?php phpinfo(); ?>' > /var/www/html/phpinfo.php
service httpd start
chkconfig httpd on
service mysqld start
chkconfig mysqld on

```

Introduction

Welcome to this live AWS hands-on lab where you will be changing the size of root EBS volumes on EC2 instances.

This activity provides hands-on experience resizing volumes in:

Standalone instances (a bastion host)
Auto scaling groups (two web server instances)
There are different reasons for a system administrator to have to resize a root volume. Needing larger storage capacity is the most obvious, but resizing is also necessary to increase the base IOPS of a volume. In this case, the volume may not be running low on storage space.


### Solution:
```
Create an EBS Snapshot

Create an EBS snapshot from one of the existing EC2 instance volumes.

Navigate to the EC2 service and click Instances
Find the root volume of the bastion host

Select the checkbox next to the bastion-host instance and scroll down in the details window to find the Root device information

Click /dev/xvda and then click the EBS ID to navigate directly to this attached volume

Check the box beside it on the Volumes page
Click Actions
Choose Create Snapshot

Add a description of "BastionSnap" and click Create Snapshot
Click Close

Create a New (Larger) EBS Volume

Using the snapshot you just created, provision a new EBS volume from the snapshot that provides a higher amount of IOPS.

Click Snapshots in the menu on the left of the page
Check the box beside your new snapshot
Click Actions
Choose Create Volume
Change size to 40 GB
Click Create Volume
Click Close

Attach the (Larger) EBS Volume to an EC2 Instance
Replace an existing (root) EBS volume that is attached to an EC2 instance with the new (larger) EBS volume that you just created. The new volume needs to replace the old volume as the root volume.
```
```
Click Instances in the menu on the left of the page
Stop the Bastion host
With the bastion-host instance selected, click Actions, Instance State, Stop
In the details window for the bastion-host instance, click the /dev/xvda root device and click the EBS ID to navigate to the attached volume
Click Actions, choose Detach Volume
Check the box next to the new larger volume
Clear the filter to view the other volumes
Click Actions, choose Attach Volume
Choose the stopped Bastion host for "instance"
Device should be /dev/xvda
Click Attach
```

### Create a New Auto Scaling Launch Configuration and Update the Existing Auto Scaling Group
```
Create a new Auto Scaling launch configuration that uses the new (larger) EBS volume for created instances. Then update the existing Auto Scaling group to use the new launch configuration.

Click Launch Configurations in the menu on the left of the page
Copy the user-data from the existing launch configuration
In the details window for the launch configuration, click View User data
Click Create a Launch Configuration
Click Select beside Amazon Linux to select the AMI
Leave t2.micro chosen, click Next: Configure details
Add a name of "WebServerLC2"
Click Advanced Details, paste in the user-data from the original launch configuration
Change IP Address Type to Do not assign...
Click Next: Add storage
Change the volume size to 40 GB, click Next: Configure Security Group
Choose the existing WebServerSecurityGroup
Click Review, click Create launch configuration
Choose to Proceed without a key pair
Click Close
Navigate to the Auto Scaling Groups page
Edit the existing Auto Scaling group to use the new launch configuration
Actions, Edit, and change Launch Configuration to WebServerLC2
Click Save
Terminate the webserver instances one at a time to update the volume size
Navigate to Instances in the menu on the left of the page
One at a time, select an instance, click Actions, Instance State, Terminate, Yes, Terminate
```
