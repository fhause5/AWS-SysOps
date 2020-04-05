
### <span style="color: black">&#x1F535; Managing Data in S3 with Versioning and Lifecycle Rules


Introduction

### In this hands-on lab, we'll configure the following in S3:

* Enable versioning on an S3 bucket.
* Configure lifecycle rules to automatically transition objects to lower-cost storage classes.
* Change image files to reduced redundancy storage as the organization has means to recreate them if they are lost.


### Enable Versioning on the Provided S3 Bucket

```
Navigate to S3.
In the Properties tab for the bucket, click on the Versioning box.
Click the button beside Enable versioning.
Click Save.
```

### Assign a Lifecycle Rule to Objects in the Log Folder

```
In the Management tab of the bucket, click Add lifecycle rule.
Enter a name for the rule (e.g., "LogsRule").
Add a prefix of "Logs".
Click Next.
On the Transitions screen, check Current version.
Click Add transition, and set the following values:
Object creation: Transition to Standard-IA after
Days after creation: 90
Click Next.
Leave the expiration defaults, and click Next.
Click Save.
```

### Assign a Lifecycle Rule to Objects in the Images Folder

```
Navigate to the Management tab of the bucket.
Click Add lifecycle rule.
Enter a name for the rule (e.g., "ImagesRule").
Add a prefix of "Images".

Click Next.
On the Transitions screen, check Current version.
Click Add transition, and set the following values:
Object creation: Transition to One Zone-IA after
Days after creation: 30
Click Next.

Leave the expiration defaults, and click Next.
Click Save.
Add a Lifecycle Rule to Move the Older Log File to Glacier after 180 Days
Click the Logs folder in the bucket.
Check the box beside 2018.csv.
Click Actions, and select Add tags.
Set the following values:
Key: Type
Value: OldLogs
Click Save, and then Save Tags.
Go back to the bucket, and choose the Management tab.

Click Add lifecycle rule.
Enter a name for the rule (e.g., "TaggedImagesRule").
In the prefix/tag box:
Type "Type", and click tag Type.
Press Enter.

Add "OldLogs" after the pipe.
Press Enter.
The final result should look like: tag Type | OldLogs. Click Next.
On the Transitions screen, check Current version.
Click Add transition, and set the following values:
Object creation: Transition to Glacier after
Days after creation: 180
Note: You will be asked if you understand that the lifecycle rule will increase the one-time lifecycle request cost if it transitions small objects.

Click Next.
Leave the expiration defaults, and click Next.
Click Save.
```
