### <span style="color: black">&#x1F535; Using CloudWatch for Resource Monitoring


### Introduction

Welcome to this AWS hands-on lab for Using CloudWatch for Resource Monitoring!

This lab provides practical experience with creating and configuring multiple custom AWS CloudWatch dashboards and widgets.

The primary focus will be on the following features within CloudWatch:

CloudWatch Dashboards
Dashboard Widgets
CloudWatch Metrics
Solution

Log in to the AWS Management Console using the credentials provided on the lab instructions page. Make sure you're using the us-east-1 region.
Create a CloudWatch Dashboard for the DMZ Layer

### In the AWS Management Console, start typing "CloudWatch" into the search box and click on CloudWatch when it appears in the list.
```
Click on Dashboards from the left-hand menu.

Click Create dashboard.

Under Dashboard name:, enter "DMZLayer".

Click Create dashboard.

Select the Line option and click Configure.

Click EC2.

Click Per-Instance Metrics.

In the filter box, enter "CPUUtilization".

Select the box next to bastion-host.

Click on custom at the top of the window and select 15 Minutes.

Click Create widget.

Expand the graph for readability and then click Save dashboard.
```

### Create a CloudWatch Dashboard for the Application Layer
```
Click on Metrics from the left-hand menu.

Click EC2.

Click Per-Instance Metrics.

Find CPUUtilization under Metric Name and click the down arrow next to the name. Select Search for this only from the menu.

Select the database instance and both instance-wordpress instances by clicking the boxes next to their names.

Click the dropdown at the top with the word Line displayed. Select Stacked area from the list of options.

Click on custom at the top of the window and select 15 Minutes.

Click Actions at the top of the window and select Add to dashboard.

Click Create new under Select a dashboard. Enter "AppLayer" in the box that appears and then click the checkmark next to the box.
```
### Click Add to dashboard.
```
Expand the graph for readability and then click Save dashboard.

Add Custom Widgets for the Application Layer
Click Add widget.

Select Number.

Click Configure.

Click ApplicationELB.

Click Per AppELB Metrics.

Find RequestCount under Metric Name and select it.

Click Create widget.

Click Save dashboard.

Click Add widget.

Select Line.

Click Configure.

Click EC2.

Click Per-Instance Metrics.

Find NetworkIn under Metric Name and click the down arrow next to the name.

Select Search for this only.

Select the database instance and both instance-wordpress instances by clicking the boxes next to their names.

Click Create widget.

Click Save dashboard.

Test the Widgets
Click Services in the top menu bar.

Click EC2 under Compute.

Click Load Balancers under LOAD BALANCING.

Copy the DNS name of the only available load balancer.

Open a new tab and navigate to the copied DNS name.

Click Continue.

For Site Title, enter "Lab".

For Username, enter "wpuser".

For Password, enter "Password1".

Click the box for Confirm use of weak password.

Enter our email address in the box provided.

Click Install WordPresS.

Click Log In.

Enter the credentials just created and log in to the site.

Switch back to the AWS Management Console.

Click CloudWatch from the left-hand menu.

Click Dashboards from the left-hand menu.

Click AppLayer.

Click custom at the top.

Select 5 Minutes.

Click the down arrow in the top left next to the refresh button.

Select Auto refresh and an interval of 10 Seconds.
```
