### <span style="color: black">&#x1F535; Automating EBS Snapshot Creation with CloudWatch Events and SNS

### In this hands-on lab, we will be creating a CloudWatch Events rule to automate the creation of EBS snapshots and notify system admins.

### EBS snapshots are essential for any backup/disaster recovery plan. Automating the creation process allows for reliable backup planning. And by utilizing SNS in this process, we can inform an administrator when each snapshot creation job has begun.

```
Navigate to the SNS service in the AWS Console (either by entering "SNS" in the search bar or by locating it in the Services menu). Click Get started, then Create topic.

Enter the following in the Create new topic menu:

Topic name: EBSSnap
Display name: EBSSnap
Then, click Create topic.

Next, click Create Subscription, and enter the following in the Create subscription menu:

Topic ARN: (No change; this field will autopopulate)
Protocol: Email
Endpoint: YOUR_EMAIL_ADDRESS
Then click Create subscription.

We'll see a pending status for the new subscription. Check your email inbox, and click the subscription confirmation link in the email you just received. Refresh the screen in the AWS Console to see that the subscription is now confirmed.
```

### Creating a CloudWatch Event Rule to Automate EBS Snapshot Creation

Now we'll create the CloudWatch event rule that will snapshot the specified EBS volume once per day and initiate an email via SNS.

```
Navigate to EC2, and click Volumes in the sidebar. Select any volume and copy its volume ID (found in the Description tab) to your clipboard.
```

```
Next, navigate to CloudWatch, and click Rules in the sidebar. Click Create rule. In the Event Source menu, select Schedule. For Fixed rate of, enter "1" and change the dropdown to Days.

Under Targets, click Add target, and do the following:

Change the default Lambda function in the dropdown to EC2 CreateSnapshot API call.
For Volume ID, paste in the volume ID we just copied to the clipboard.
Click Add target.
Change the default Lambda function in the dropdown to SNS topic.
For Topic, select our newly created SNS topic (EBSSnap) from the dropdown.
Click Configure details.
On the Configure rule details screen, type "EBSSnap" for Name. For State, the checkbox next to Enabled should be checked. Click Create rule.

Now we need to confirm that our new CloudWatch event rule is working as expected by checking that a new EBS snapshot was created.

Wait a few minutes, and then check your email for a message from SNS.

Back in the AWS Console, navigate to EC2, and click Snapshots in the sidebar to make sure a new snapshot is listed.
```

Conclusion
Congratulations on completing this lab!
