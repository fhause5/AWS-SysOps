### <span style="color: black">&#x1F535; Restoring an Amazon RDS Instance Using Snapshots



Restoring an Amazon RDS Instance Using Snapshots
Introduction
A critical part of database management is being able to recover your data after corruption or accidental deletion has occurred.

In this hands-on lab, we'll use the point-in-time restore capability of RDS automated snapshots to restore a database and bring a site back up.

Solution
Please log in to the lab environment with the cloud_user credentials provided. Make sure you are using us-east-1 region throughout the lab.

Make a note of the cloud_user password for connecting to the bastion instance.

NOTE: This environment will take up to 15 minutes to create.

### Open the WordPress Application to Monitor It
```
Navigate to EC2 > Load Balancers.
With the load balancer selected, copy the DNS name listed below, and paste it into a new browser tab.
Keep this tab open to monitor the application later.
```

### Create an RDS Snapshot
```
In the AWS console, navigate to RDS.
Click DB Instances, and select the running instance.

NOTE: Copy the endpoint listed and paste it into a text file, as we'll need it for the next step.

Select Actions > Take snapshot.
Name the snapshot (e.g., "wordpress-YYYYMMDD").
```
### Log in to the Bastion Host and Delete Database Data

Navigate to EC2 > Instances.

With the bastion-host instance selected, copy the public IP listed in the Description section.
Open a terminal session, and log in to the bastion host via SSH as cloud_user using the public IP:

ssh cloud_user@<PUBLIC IP>
Use the password provided on the lab page — it will be different than the one you used to log in to the AWS console.

Install the MySQL command line:

sudo yum install mysql
Connect to MySQL (using the RDS endpoint you copied earlier):

mysql --user=wpuser --password=Password1 --host=<RDS ENDPOINT NAME>
At the MySQL prompt, switch to the WordPress database:

use wordpressdb;
Delete a critical table:

drop table wp_posts;
In the browser, refresh the WordPress site, which should result in an error page.
```

### Restore an RDS Database from a Snapshot

```
In the RDS console, navigate to Snapshots.
Note the snapshot creation time.
Click Databases in the left-hand menu, and select wordpress-database.
Click Actions, and select Restore to point in time.
Select a Custom restore time, and enter the point in time you want to restore from (selecting today's date and a time after the snapshot creation time).
Give it a DB instance identifier of "wordpress-recovery".
Set the Availability zone to us-east-1b.
Click Launch DB Instance. It will take a few minutes for it to become available.
```

### Rename Database Instances
```

Head back to the Databases dashboard, select wordpress-database, and click Modify.

Change the DB instance identifier from "wordpress-database" to "wordpress-corrupt".

Click Continue.
Select Apply Immediately, and click Modify DB Instance. It will take a minute for it to finish renaming.

Now, select wordpress-recovery, and click Modify.

Change the DB instance identifier from "wordpress-recovery" to "wordpress-database".

Under Security group, delete the default security group and select DatabaseSecurityGroup from the dropdown.
Click Continue.

Select Apply Immediately, and click Modify DB Instance.
Refresh the WordPress website, and observe that the last known good configuration is present.
```
