### <span style="color: black">&#x1F535; Troubleshooting Amazon EC2 Network Connectivity bastion and private vpc

Introduction

The goal of this hands-on lab is to fix the connectivity issue in the AWS environment so we can update the yum package installer (from the command line) on the provided EC2 instance (named "web server").

Here, we'll go step-by-step through the scenario and offer detailed instructions on how to solve the connectivity issue.


### add an SSH (port 22) allow rule to the security group associated with the bastion host

Locate the public IP address of the bastion host on the lab page and copy it. Alternately, in the AWS console, navigate to EC2 > Instances and copy it from there.
Open a terminal session, and log in via SSH:
```
ssh cloud_user@<PUBLIC IP ADDRESS>
```
It doesn't seem to connect. Head back to the AWS console to look at the bastion host.
```
Click the listed security group associated with the bastion host.
In the Inbound rules tab, we'll see the only allow rule is port 80, which is for HTTP traffic and not SSH traffic.
Click Edit.
Delete the existing rule.

Click Add Rule, and set the following values:
Type: SSH
Protocol: TCP
Port Range: 22
Source: Anywhere
Click Save.
```
Back in the terminal, we should see the prompt to continue connecting. Enter yes, and then enter the password for the instance (provided on the lab page).

We've now successfully logged in to the bastion host.
Now, we need to log in to the "web server" instance. Copy the private IP address from the lab credentials page (or in the AWS console). In the terminal, enter:

```
ssh cloud_user@<PRIVATE IP ADDRESS>
```

Enter yes at the prompt, and then enter the password provided on the lab page for the web server instance.

Now, run the YUM package installer:
```
sudo yum update
```

Enter the password again.

There seems to be a hangup. Why is the EC2 instance not able to connect to the open internet in order to successfully update the YUM package installer?
```
Fix Egress from Web Server to Internet
The Issue
The NACL protecting the web server only allows return traffic to the public subnet, not the internet.

How to Fix the Issue
Add an outbound "All Traffic" allow rule to 0.0.0.0/0 to the NACL.

In the AWS console, navigate to VPC > Network ACLs.
Click the Private Network NACL listed.
In the Outbound Rules tab, click Edit outbound rules.
Change the Destination to 0.0.0.0/0.
Click Save.
```

Back in the terminal, run:
```
sudo yum update
```

It still won't connect.

Fix Web Server Route to Internet
The Issue
The web server does not have a route to the NAT gateway.

How to Fix the Issue
Add a route to the NAT gateway on the route table associated with the private subnet the web server is located in.
```
In the AWS console, navigate to the VPC > Route Tables.
Select the Private route table, and click the Routes tab. We'll see there isn't a route to the NAT gateway.
Click Edit routes.
Click Add route, and set the following values:
Destination: 0.0.0.0/0
Target: Type "nat", and select the pre-populated NAT gateway listed in the dropdown
Click Save routes.
```
Back in the terminal, run:
```
sudo yum update
```
Note: If you get a lock message, kill -9 PID (replace PID with the process number), then run the yum command again.

It should work this time.

Conclusion
