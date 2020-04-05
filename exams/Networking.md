### <span style="color: black">&#x1F535; Networking

### 1. Which of these are the components of an AWS VPN?

* VPN Connection
* Customer Gateway
* Virtual Private Gateway

```
Correct Answer: B
Why is this correct?
A VPN connection is a component of an AWS VPN.

Video for reference: AWS VPN

Correct Answer: D
Why is this correct?
A customer gateway is a component of an AWS VPN.

Video for reference: AWS VPN

Correct Answer: E
Why is this correct?
A Virtual Private Gateway is a component of an AWS VPN.

Video for reference: AWS VPN
```

### 2. Which of the following lists the characteristics of AWS Direct Connect? Please select the most appropriate answer.

> Dedicated throughput, consistent network performance, and reduced bandwidth costs

```
AWS Direct Connect provides dedicated throughput, consistent network performance, and reduced bandwidth costs.

Video for reference: AWS Direct Connect
```

### 3. Which is a characteristic of an Elastic IP (EIP)?

> Attachable to one instance at a time

### 4. The VPC-VPC peering connection ratio is which of these?

> 1:1

```
VPC:VPC peering connections are a 1:1 connection.

```

### 5. What step is used to assign an Elastic IP (EIP) to an instance?

> Association

```
Association is the step used to assign an EIP to an instance.

Video for reference: EC2: Elastic IP (EIP) and Elastic Network Interfaces (ENI)
```

### 6. Which VPC networking component needs to be secured per best practices of an AWS VPN?

* Security Group
* NACL
* Subnet

```
Subnets, NACLs, and security groups all need to be secured per best practices of an AWS VPN.


```

### 7. What are the characteristics of SSL Offloading?

* Scalable and Elastic SSL encryption
* Improved application performance
* Ease of ACM certificate management
* Improved processing performance when using SSL

```
Correct Answer: B
Why is this correct?
SSL Offloading provides scalable and elastic SSL encryption to instances.

Video for reference: ELB: SSL Offloading

Correct Answer: C
Why is this correct?
SSL Offloading will save on processing, thus improving application performance.

Video for reference: ELB: SSL Offloading

Correct Answer: D
Why is this correct?
SSL Offloading will provide ease of certificate management. Only the ELB will have a certificate rather than having to manage certificates for many instances.

Video for reference: ELB: SSL Offloading

Correct Answer: F
Why is this correct?
SSL Offloading will improve processing performance when using SSL.

Video for reference: ELB: SSL Offloading
```

### 8. Which of the following is a characteristic of a sticky session?

* Enabled on the Classic Load Balancer after creation
* Enabled on the target group
* Maintains a user's session state
* Uses cookies to identify sessions

```
The characteristics of a sticky session are that enablement on creation with a Classic Load Balancer. Sticky sessions enabled on the target group. A sticky session holds cookies to identify sessions, and it maintains the user's session state.


```

### 9. What AWS VPC feature would you choose to connect and improve network performance between two VPCs without transiting the public internet?

> VPC Peering

```
VPC Peering is a way to connect two VPCs and improve network performance.


```

### 10. How many Virtual Private Gateways does a VPC receive?

> 1

```
VPCs using AWS VPN will only receive one Virtual Private Gateway.
```

### 11. VPC Flow Logs can be created for which of the following? Please select the most appropriate answer.

* VPC
* Subnet
* Network Interface
* VPC Flow Logs can only be created for VPCs and Subnets

### 12. What is the rate of time at which an unassociated Elastic IP (EIP) will be charged?

> Hourly

### 13. What is the CIDR block for the default VPC?

> 172.31.0.0/16

### 14. What are the components of Amazon CloudFront? Please select the most appropriate answer.

> Origins, Distribution, Edge Locations, and Regional Edge Caches

```
Origins, distribution, Edge locations, and regional Edge caches are all components of Amazon CloudFront.


```

### 15. What connection speeds does AWS Direct Connect provide?

* 1 Gbps
* 10 Gbps

```
AWS Direct Connect provides connection speeds at 10 Gbps.

Video for reference: AWS Direct Connect

Correct Answer: F
Why is this correct?
AWS Direct Connect provides connection speeds at 1 Gbps.
```

### 16. Which IP pairings could not be used for a VPC peering connection?

> 172.31.0.0 and 172.31.0.0

```
VPC peering connections cannot be made between two VPCs with the same IP.

```

### 17. Which of these is not a benefit of a VPC?

> VPCs can span regions

```
VPCs cannot span AWS regions, and each region has its VPC.


```

### 18. Which service captures the VPC Flow Logs metadata?

> CloudWatch

### 19. What AWS service is the primary cause for network bottlenecks?

> EC2

### 20. Which of the following make up the components of a load-balancer? Please select the most appropriate answer.

> Load-balancer, Target Group, and Listener

```
A load-balancer consists of a listener, a target group, and the load-balancer.

```

### 21. What type of load balancer functions on layer 7?

> Application Load Balancer

### 22. Which of these IP addresses are reserved by AWS in a 10.0.0.0/24 CIDR block?

* 10.0.0.0
* 10.0.0.2
* 10.0.0.1
* 10.0.0.3
* 10.0.0.255
