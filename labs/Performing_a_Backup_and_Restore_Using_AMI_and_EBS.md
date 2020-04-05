### <span style="color: black">&#x1F535; Performing a Backup and Restore Using AMI and EBS

Performing a Backup and Restore Using AMI and EBS
Introduction

In this hands-on lab, we will perform a backup and restore using AMIs and EBS. This activity will explore several common backup and restore methods for the Amazon EC2 service.

Solution
Log in to the live AWS environment using the credentials provided. Make sure you're in the N. Virginia (us-east-1) region throughout the lab.

### Create an EBS Snapshot

```
Navigate to EC2 > Instances.
Check the box beside one of the "webserver-instance" instances.
Click the Root device link in the Description section below, and then click the EBS ID link.
On the Volumes page, make sure the listed volume is selected, and then click Actions and select Create Snapshot.
Enter a description (e.g., "WordPressSnap").
Click Create Snapshot.
```

### Create a New EBS Volume from a Snapshot

```
Navigate to Snapshots.
Check the box beside the snapshot you just created.
Click Actions, and select Create Volume.
Change the volume size to 10 GiB.
Click Create Volume.
Click Close.
Select the newly created volume, and then click Actions and select Attach Volume.
In the Instance dropdown, select the webserver-instance and click Attach.
```

### Create Two EC2 AMIs
# Method 1

```
Navigate to Instances.
Check the box beside one of the "webserver-instance" instances.

Click Actions, then Image, and then Create Image.
Add a name and description (e.g., both could be "AMI1").
Click Create Image, and then Close.
Choose AMIs from the left menu to see the image you created.
Once the image is available, navigate to the instances page.

Click Launch Instance.
Choose My AMIs in the left column.
Click Select.

Leave t2.micro selected, and click Next: Configure Instance Details.

On the Configure Instance Details page:
Network: Leave default
Subnet: AppLayer1private
Auto-assign Public IP: Disable
Click Next: Add Storage, then Next: Add Tags, and then Next: Configure Security Group.
Click to Select an existing security group.
Select the WebServerSecurityGroup one from the table.

Click Review and Launch, and then Launch.
In the key pair dialog, select Proceed without a key pair.
Click Launch Instances, and then View Instances.
```

# Method 2
```
Navigate to Snapshots.
Check the box beside the snapshot you made earlier.
Click Actions, and select Create Image.
Enter a name and description (e.g., both could be "AMI2").

Change Virtualization type to Hardware-assisted virtualization.

Click Create, and then Close.
Choose AMIs from the left menu to see the image you created.
```
