
### <span style="color: black">&#x1F535; Storages

IOPS (количество операций ввода/вывода – от англ. Input/Output Operations Per Second)

EFS - Network filesystem, expensive compared to EBS

EBS - A block storage (so you need to format it). This means you are able to choose which type of file system you want, fast, choose IOPS

gp2 (SSD)  | 128-160    | volume size                   |
| EBS volume | Throughput |           Throughput          |
|    type    |   MiB/s    |         dependent on..        |
|------------|------------|-------------------------------|
| gp2 (SSD)  | 128-160    | volume size                   |
| io1 (SSD)  | 0.25-500   | IOPS (256Kib/s per IOPS)      |
| st1 (HDD)  | 20-500     | volume size (40Mib/s per TiB) |
| sc1 (HDD)  | 6-250      | volume size (12Mib/s per TiB) |

S3 - object store (not a file system), mages and videos, archiving, logs, the cheapest

Glacier is:

Long term archive storage
Extremely cheap to store
Potentially very expensive to retrieve
Takes up to 4 hours to "read back" your data (so only store items you know you won't need to retrieve for a long time)
