### <span style="color: black">&#x1F535; Querying Data in S3 with Amazon Athena


Introduction
Welcome to this hands-on AWS lab for querying data in Amazon S3 with Amazon Athena. This lab allows you to practice analyzing data stored in S3 using SQL queries in Athena.

Solution
Begin by logging in to the AWS Management Console using the credentials provided on the hands-on lab page.

### Gather S3 Bucket's ARN for later use

```
Navigate to the S3 service
Check the box next to the bucket we've got in there
In the overlay that slides in (which contains details about the bucket) click Copy Bucket ARN
```

### Create a Table from S3 Bucket Metadata
```
Navigate to the Amazon Athena service:
Click Get Started if this is our first trip into Athena, otherwise continue to #2
Under Database > Tables, select Create Table > from S3 bucket data.

Step 1: Name and Location:
Database: aws_service_logs
Table: cf_access_optimized
Location: s3://Name of the generated S3 bucket/ (including trailing slash)
Paste in the S3 Bucket ARN we copied earlier, being sure to remove "arn:aws:s3:::" from the beginning of the data we paste in

Step 2: Data Format
Select Parquet

Step 3: Columns

Bulk add columns using this data:

time timestamp, location string, bytes bigint, requestip string, method string, host string, uri string, status int, referrer string, useragent string, querystring string, cookie string, resulttype string, requestid string, hostheader string, requestprotocol string, requestbytes bigint, timetaken double, xforwardedfor string, sslprotocol string, sslcipher string, responseresulttype string, httpversion string

Step 4: Partitions

Column Name: year, Column Type: string
Column Name: month, Column Type: string
Column Name: day, Column Type: string
Click Create table
Click Run query on the generated SQL statement. Ensure the S3 bucket location in the query matches the one generated in your lab environment.

```

### Add Partition Metadata
```
Open a new query tab
Run the following query: MSCK REPAIR TABLE aws_service_logs.cf_access_optimized
Verify the partitions were created with the following query:
SELECT count(*) AS rowcount FROM aws_service_logs.cf_access_optimized
You should see 207535 rows present in the table.
To look at a bit of actual data from this table (just ten rows' worth) we can run this query:
SELECT * FROM aws_service_logs.cf_access_optimized LIMIT 10

```

### Query the Total Bytes Served in a Date Range

```
Add another query tab, then let's look at the timestamps on our newest and oldest data. Run these two queries:

SELECT * FROM aws_service_logs.cf_access_optimized LIMIT 10 ORDER BY time DESC LIMIT 10
SELECT * FROM aws_service_logs.cf_access_optimized LIMIT 10 ORDER BY time ASC LIMIT 10
Our newest timestamp is from 2018-11-07, and the oldest is from 2018-11-02.

Now let's look at a sum of the bytes column for data between 11-02 and 11-03:

SELECT SUM(bytes) AS total_bytes
FROM aws_service_logs.cf_access_optimized
WHERE time BETWEEN TIMESTAMP '2018-11-02' AND TIMESTAMP '2018-11-03'
Observe the value for total_bytes equals 87310409.
```
