### <span style="color: black">&#x1F535; Deploying a Highly Available Web Application and a Bastion Host in AWS

Solution

wordpress-database.chuqxfqdgv7u.us-east-1.rds.amazonaws.com


Launch an RDS Database

### Create a Subnet Group for the Database
```
Navigate to the RDS console.
Click Subnet groups in the left-hand menu.
Click Create DB Subnet Group.
For the Subnet group details, set the following values:
Name: sng1
Description: sng1
Under Add subnets, set the following values for the first subnet:
Availability zone: us-east-1a
Subnet: 10.99.21.0/24
Click Add subnet.
Now, set the following values for the second subnet:
Availability zone: us-east-1b
Subnet: 10.99.22.0/24
Click Add subnet.
Click Create.
```
### Restore the Database from a Public Snapshot

```
Click Snapshots in the left-hand menu.
In the filter box, paste in the following snapshot ARN:
arn:aws:rds:us-east-1:892710030684:snapshot:sysops-certification-la-course

Change the dropdown to All Public Snapshots.
Check the box next to the snapshot, and in the Actions dropdown, select Restore Snapshot.
Under Instance specifications, set the following values:

DB Engine: MySQL Community Edition
License Model: general-public-license
DB Instance Class: db.t2.micro
Multi-AZ Deployment: Yes
Under Settings, use the following:
DB Instance identifier: wordpress-database
Under Network & Security, the VPC and subnet group should auto-populate to what we need.
Click Restore DB Instance. It will take about 10-15 minutes to complete.
```

### Create Security Groups

Navigate to VPC > Security Groups.
### BastionSG
```
Click Create security group, and set the following values:
Security group name: BastionSG
Description: Bastion security group
VPC: SysOpsVPC
Click Create.
Check the box next to BastionSG.
Click the Inbound Rules tab.
Click Edit rules, and set the following values:
Type: SSH
Source: Anywhere
Description: SSH from anywhere
Click Save rules.
```
### LoadBalancerSG
```
Click Create security group, and set the following values:

Security group name: LoadBalancerSG
Description: Load balancer security group
VPC: SysOpsVPC
Click Create.

Check the box next to LoadBalancerSG.
For its inbound rules, click Edit rules, and set the following values:

Type: HTTP
Source: Anywhere
Description: HTTP from anywhere
Click Add Rule, and use these settings:
Type: HTTPS
Source: Anywhere
Description: HTTPS from anywhere
Click Save rules.
```

### WebServerSG
```
Click Create security group, and set the following values:
Security group name: WebServerSG
Description: Web server security group
VPC: SysOpsVPC
Click Create.
Check the box next to WebServerSG.
For its inbound rules, click Edit rules, and set the following values:
Type: SSH
Source: Custom, BastionSG
Description: SSH from bastion
Click Add Rule, set the following values:
Type: HTTP
Source: Custom, LoadBalancerSG
Description: HTTP from ALB
Click Add Rule, set the following values:
Type: HTTPS
Source: Custom, LoadBalancerSG
Description: HTTPS from ALB
Click Save rules.

```

### Database
Click create security group, and set the following values:
```
Security group name: DatabaseSG
Description: Database security group
VPC: SysOpsVPC
Click Create.
Check the box next to DatabaseSG.
For its inbound rules, click Edit rules, and set the following values:
Type: MySQL
Source: Custom, WebServerSG
Description: MySQL from WebServerSG
Click Save rules.
Create Launch Configurations and Auto Scaling Groups
Create Launch Figuration for First Auto Scaling Group
Navigate to EC2 > Auto Scaling Groups.
Click Create Auto Scaling group.
Select Launch Configuration, and click Next Step.
Click Select beside Amazon Linux 2 AMI.
Leave t2.micro chosen, and click Next: Configure details.
Give it a Name of "BastionLC".
For IP Address Type, select Assign a public IP address to every instance.
Click Next: Add Storage.
Leave the defaults, and click Next: Configure Security Group.
For Assign a security group, choose Select an existing security group.
Select BastionSG.
Click Review, and then Create launch configuration.
Create a new key pair (example name: "bastion"), and download it.
```

### Click Create launch configuration.


### Create First Auto Scaling Group
```
On the Create Auto Scaling Group page, set the following values:
Group name: BastionASG
Group size: 1 instances
Network: SysOpsVPC
Subnet: DMZ1public and DMZ2public
Click Next: Configure scaling policies.
Select Keep group at its initial size, and click Review.
Click Create Auto Scaling group, and then Close.
```

### Create Launch Configuration for Second Auto Scaling Group
```
Click Create Auto Scaling group.
Select Launch Configuration, Create a new launch configuration, and click Next Step.
Click Select beside Amazon Linux 2 AMI.
Leave t2.micro chosen, and click Next: Configure details.

Give it a Name of "WebServerLC".
Click Advanced Details, and paste the script from GitHub into the User data box.
Click Next: Add storage.
Leave the defaults, and click Next: Configure Security Group.

For Assign a security group, choose Select an existing security group.
Select WebServerSG.
Click Review, and then Create launch configuration.
Choose the existing key pair we just created.
Click Create launch configuration, and Close.
```
### Create Second Auto Scaling Group
```
On the Create Auto Scaling Group page, use the following settings:
Group name: WebServerASG
Group size: 2 instances
Network: SysOpsVPC
Subnet: AppLayer1private and AppLayer2private
Click Next: Configure scaling policies.
Select Keep group at its initial size, and click Review.
Click Create Auto Scaling group, and then Close.
Modify Database Security Groups and Create an Application Load Balancer
```
### Modify the Database Security Group
```
Navigate to RDS.
Click Databases in the left-hand menu.
Select our listed database.

Note: Before we modify anything, in the Connectivity & security section, copy the Endpoint listed (e.g., wordpress-database.clei7j95opir.us-east-1.rds.amazonaws.com) and paste it into a note or text file — we're going to need it in a few minutes for the last part of the lab.

Click Modify at the top.


### In the Network & Security section, delete the default security group listed.
Choose our DatabaseSG from the Security group dropdown.
Click Continue.
Select Apply Immediately, and then Modify DB Instance.
```

### Create an Application Load Balancer
```
Navigate to EC2, and then click Load Balancers in the left-hand menu.
Click Create Load Balancer.

In the Application Load Balancer box, click Create.
Use the following configuration settings:
Under Basic Configuration, give it a Name of "ALB1".
Under Availability Zones, select the default SysOpsVPC and check both availability zones.

Click Next: Configure Security Settings.
Click Next: Configure Security Groups.

Un-check the default security group, and select LoadBalancerSG.

Click Next: Configure Routing.
In the Target group section, give it a Name of "TG1".
In the Health checks section, enter a Path of "/readme.html".

Click Next: Register Targets.
Click Next: Review, and then Create.
```
### Modify Auto Scaling Group
```
Click Auto Scaling Groups in the left-hand menu.
Select WebServerASG.

In the Details section below, click Edit.
Click into Target Groups box, and select TG1.
Click Save.
```
### Browse Web Application
```
Navigate to Load Balancers.
Copy the DNS name, and paste it into a new browser tab.
Click Let's go!, and configure WordPress:
Database Name: wordpressdb
Username: wpuser
Password: Password1
Database Host: Enter the RDS endpoint name
Table prefix: wp_
Click Submit, and Run the installation.
Click Log in, but then navigate back to the Load Balancer DNS name.
```
Conclusion
