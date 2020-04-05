### <span style="color: black">&#x1F535; Deploying an Amazon RDS Multi-AZ and Read Replica

Deploying an Amazon RDS Multi-AZ and Read Replica
Introduction

Welcome to this live hands-on AWS lab, where we will be working with the Relational Database Service (RDS).

### This lab will provide you with hands-on experience with:

* Enabling Multi-AZ and Backups
* Creating a read replica
* Promoting a read replica
* Updating the RDS endpoint in Route53
* Solution


### Enable Multi-AZ Deployment

```
Navigate to EC2 > Load Balancers.
Copy the DNS name of the load balancer.

Open a new browser tab, and enter the DNS name. We will use this web page to test failovers and promotions in this lab.

Back in the AWS console, navigate to RDS > Databases.
Click on our database instance.
Click Modify.

Under Multi-AZ deployment, click Yes.
Change Backup Retention to 1 day, needed later for read replicas.

Click Continue.
Under Scheduling of modifications, select Apply immediately, and then click Modify DB Instance.

Once the instance shows Multi-AZ is enabled (it could take about 10 minutes), select the database instance.
Click Actions, and select Reboot.
On the reboot page, select Reboot With Failover?, and click Reboot.

Use the web page to monitor the outage (normally about 30 seconds).
The Multi-AZ standby is now the primary.
```
### Create a Read Replica
```

With the database instance still selected, click Actions, and select Create read replica.

For Destination region, select US East (N. Virginia).
Enter a name under DB instance identifier (e.g., "wordpress-rr").

Leave the other defaults, and click Create read replica. It will take a few minutes for it to become available.
```
### Promote the Read Replica and Change the CNAME Records Set in Route 53 to the New Endpoint

```
Once the read replica is available, check the circle next to it.

Click Actions, and select Promote.

Leave the defaults, and click Continue, and then click Promote Read Replica.

Use the web page to monitor for downtime.

Once the read replica is available, click to open it.
In the Connectivity & security section, copy the endpoint under Endpoint & port.

Open Route 53 in a new tab.
Click Hosted zones, and select the sysopsdatabase hosted zone.
Click Go to Record Sets.
Click the CNAME row.
Replace what's currently in the Value box with the endpoint you copied.
Click Save Record Set.
Monitor using the web page for downtime.
```
