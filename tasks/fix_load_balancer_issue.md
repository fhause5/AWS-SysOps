### <span style="color: black">&#x1F535; The ELB's security group does not allow HTTP traffic.

How to Fix the Issue

### Add an allow rule for HTTP traffic (port 80) to the ELB's security group.

```
Navigate to EC2 > Load Balancers.
With the load balancer selected, scroll to the Security section in the

Description section, and click the listed security group.

With the security group selected, scroll to the Inbound section, and click Edit.

Change the Type to HTTP, and click Save.

Click Load Balancers in the left-hand menu.

Copy the load balancer's DNS name in the Description section, and paste it into a new browser tab. The page won't be able to load.
```


Hint #2
The Issue

### EC2 instance health checks are not passing.

How to Fix the Issue

Change health check "ping port" on the ELB to port 80.
```
Back in the AWS console, click the Instances tab on the load balancers page, where we'll see the instances associated with our load balancer are marked as OutOfService.

In the Health check tab, click Edit Health Check.

In the dialog, change Ping Port to 80, and click Save.

Back in the Instances tab, we should see they're now listed as InService.

Reload the load balancer DNS in the browser, which should now display the Linux AMI/Apache test page.
```
