# AWS SA Associate Accelerator
## Links 
- Stream: https://www.twitch.tv/aws_namer_programs 
- Accelerator home page: https://mpa-saa-accelerator-q12023.splashthat.com/
- Learning materials: https://explore.skillbuilder.aws/learn/lp/1651/Solution%2520Architect%2520Associate%2520Accelerator%2520-%2520Partner%2520Learning%2520Plan (I usually have to click it twice and sign in twice...) 
    - Not every video in here is required for certification 
    - The hands on labs essentially book-end the learning objectives for the week. Each week of the program will also have an email come out with objectives for the week 

## Info
- Twitch sessions are recorded. The instructor-led 4 hour courses are NOT recorded. 
- labs and tests require monthly charge. Probably able to reimburse with Octo if necessary. 
- This program is ~3 months
- Once past 85% on learning plan (in week 6), will qualify in the running for raffle for voucher
- Recommend 8-9 hours/week of studying. 1.6-1.8 hours/day of studying weekdays only. Pacing helps maintain knowledge & keep committed 
- watch for easter eggs in links in emails and weekly wed/fri chats 
- get stickers by participating in chat. 
    - call out when he says 'you guys' in chat 

# AWS Technical Essentials
- Every action made in AWS is an API call that is authenticated and authorized. 
    - Management console, CLI, SDKs
- Authentication: ensures the user is who they say they are
- Authorization: what actions a user can perform
- 'main route table' is the route table created by default 
- NACL: firewall at the subnet-level. They're stateless; inbound and outbound ports required to be listed 
- Instance security group: stateful; can remember connections & allow returning ephemeral responses 
- block storage: think little pieces making up a larger file. Object: each file is a single entity 

# DynamoDB review
## How DynamoDB Works
- designed for online transaction processing (OLTP), with known request patterns 
- online analytical processing (OLAP) loads are better handled by SQL
- data stored in tables
- items placed in tables
- attributes: essential the 'key' of an item. aka partition key
    - optionally, sort key can be defined
    - primary key: made up of paritition (+optional sort key); must be unique
    - supported types: number, string, binary (base64 encoded), boolean, null
    - can use sets of numbers, strings, and binaries; sets do not preserve order
- schema flexibility  
- durability/availability
    - data written at least twice in separate facilities
    - 99.99% availability
- eventual consistency: default behavior, w strong consistency available for each read operation. best practice to design around eventual consistency 
- RCU (read capacity unit): consumed while reading an item up to 4KB in size each second
    - single item can never be read at more than 3000 RCU
    - eventually consistent reads are 1/2 cost of strongly consistent; 2 4KB EC consumes only 1 RCU
- WCU write capacity unit: consumed while writing an item up to 1KB in size each second 
    - updating a single attribute in an item requires writing the entire item 
    - single item can never be read at more than 1000 WCU
- able to burst and use 'adaptive capacity'
### Basic item requests
- PutItem
- UpdateItem
- DeleteItem (costs the same number of WCUs to delete as to create)
- GetItem
- BatchWriteItem/BatchGetItem
- Scan: scans entire table; not to be done often; can consume all provisioned throughput of table if done poorly
- Query: specify partition key & sort key expression to match 
    - sums the size of all items in the result set & rounds to the nearest 4KB, instead of counting sizes for each individual item identified in the search
### Indexes
- secondary index: direct Query and Scan calls to index instead of base table
- LSI (local secondary index): local to a particular partition key; has the same partition key as the base table 
    - use sparingly; each index will result in add'l writes
    - limit collection size for partition key to ~10GB of data
- GSI (global secondary index): think of it as a completely separate table that DDB replicates to from the base table
    - created & deleted at will
    - generally recommended; but don't build indexes that aren't needed
### Streams
- strictly ordered flow of information according to the changes to the table
- durable & kept up to 24hrs

## Operating DynamoDB
- 400 errors addressed by user
- 500 errors problems DDB will take care of 
- auto scales in response to actual traffic patterns 
    - set RCU and WCU man, max, and target utilization %
- global tables: DDB tables operated across multiple regions 
    - 5 9's, and primary reason to use is to provide extremely low latency to global clients 
    - multi-master, conflicts resolved w last-write-wins
    - strong consistency not possible
- TTL (time-to-live): expire old items to keep storage cost low. Doesn't cost WCU
    - w/n a day or two of epoch-formatted defined time, DDB will delete for free 
- DAX (DynamoDB Acclerator): provides an API-compatible cache for DDB tables
    - highly-available cluster of nodes accessible w/n VPC
    - can decrease amount of RCUs required on table and can smooth out spiky/imbalanced read loads 
- backups
    - manual
    - PITR (point in time recovery): keeps 35-day rolling window of information about table 

## Design Considerations
- uniform workloads
    - choose a partition key with an even distribution of item data and traffic across hash space. A good partition key has a high 'cardinality' - meaning lots of unique values
        - e.g. in keeping track of user status for a mobile game, UserId would be a good partition key; CountryCode would not
- hot and cold data
    - can delete tables (doesn't require WCUs)
    - consider cold tier storage which uses S3
- items limited to 400kB
- use optimistic locking with version number 

## Assessment Review
- facts about consistency:
    - DAX passes strongly consistent reads through but doesn't cache them
    - stringly consistent reads can be made via a VPC endpoint
    - LSI and GSI both support eventually consistent reads
    - you can make two EC reads (each up to 4KB) for one RCU
    - all successful writes are redundantly stored and durable - there is no eventual or strong consistencyu choice to be made for writes (only reads)
    - LSI can only be defined at time of base table creation - cannot be deleted w/o deleting base table
    - DDB streams cannot be used to audit read activity for a table 
    - optimistic currency control in DDB provides a form of locking; read, transformat, conditionally write, retry as required is a description of the mechanism

# DMS Notes
- AWS DMS > resource management > replication instances 
- create endpoints in AWS DMS portal 
    - target endpoint: 
        - when loading data into a MySQL DB by using AWS DMS, disable foreign key w `initstmt=SET FOREIGN_KEY_CHECKS=0`
    - can test endpoints before creation
- replication task: AWS DMS > migration > database migration tasks
    - identify replication instance, source/target endpoint, migration type
    - when migrating existing data & replicating ongoing changes: source MySQL database requires binary log to be enabled and set to row 
- completing migration
    - read & write from both DBs for a time
    - change app config to use new db
    - once new db is configrmed working, start deleting DMS stuff, like replication task, endpoints, replication instance 
    - delete source db when ready

# Auto Scaling overview 
- auto scaling can support appliation-wide scaling; not just ec2. 
    - Able to manage EC2 + EC2 spot fleet, ECS, Aurora, DynamoDB from same AWS AS policy. Needs to all be made in the same CloudFormation stack 
    - all scalable resources show in the same console when using this service 

# Application Load Balancer
- targets can be in multiple groups 

# Application Discovery Service
- migration tool to identify, map, and store computing inventory
- integrated w AWS migration hub 
    - can filter through agents/connectors in the hub (after discovery)
    - provides data on hardware specifications and OS/OS version
    - provides system process information w/n VMs/instances as well - collects every running process 
    - able to export data to .csv
- agent discovery 
    - requires agent installation on existing instances/VMs/etc 
    - better data collection 
- agentless discovery
    - download VM to hypervisor and that VM collects info
    - less robust data collection 



# Amazon S3 File Gateway
## When to consider hybrid cloud
- based on specific customer use case, where migrating totally to the cloud is unfeasible, but wish to use cloud features 
- hybrid cloud storage: use data on prem & store in AWS 
## Storage Gateway
- helps store on-prem data in the cloud
- storage: S3, glacier, FSx, AWS backup, EBS
- mgmt + monitoring: use Storage Gateway mgmt console to manage & monitor the gateway & associate resources
    - integrates w IAM, KMS, CloudTrail, CloudWatch, EventBridge 
- uses std storage protocols: NFS, SMB, iSCSI, iSCSI VTL
- can be a VM or hardware appliance 
### Types of Storage Gateways
- S3 File Gateway
    - appears as network file share
    - moves data to object format
    - has a local cache
- FSx File Gateway
    - mostly focused on supporting Windows file shares
    - local cache of frequently used data is stored 
    - can replace on-prem NAS
    - uses SMB
- Tape Gateway
    - create virtual tapes in VTL using Storage Gateway console 
    - Available for immediate access through S3
    - Archived tapes stored in S3 Glacier flexible retrieval/deep archive 
- Volume Gateway
    - provides iSCSI target; can create block storage volumes & mount as iSCSI devices from on-prem or EC2 app servers
    - cached mode: primary data written to S3, frequent data cached locally
    - stored mode: primary data stored local & entire dataset avaiable for low-latency access while asynchronously backed up to AWS
### S3 File Gateway
- provides applications a file interface to seamlessly and durably store files as objects in S3 
- primary use cases
    - backing up data to cloud 
        - can use NFS and/or SMB to mount shares directly on db and app servers
        - windows ACL support to control access to backup files
        - incremental backups 
    - archiving long-term, retention-based data 
        - basically all the same points as backing up ^ 
    - building data lakes
        - use up to 64 TB of cache per dateway & set up auto cache refresh @ 5 min intervals 
- how it works
    - NFS: linux
    - SMB: windows 
    - each file share is paried w single S3 bucket & uses appliance's local cache
    - appliance can have multiple NFS and SMB file shares 
    - files written to share become objects in S3 w/ one-to-one mapping b/w files & objects 
    - cache refresh will find objects in S3 bucket that were added, removed, or replaced since gateway last listed bucket's contents & cached them
        - automated refresh based on timer value b/w 5 minutes & 30 days 
            - time reflects contents of that file share no longer than the set time ago
- pricing model
    - pay for only what is used
    - charged for data transferred, type & amount of storage used, and requests made
        - request: data written: up to max $125/gateway/mo. $0.01/GB to write data, first 100 GB free 
        - transfer out from storage gateway to on-prem gateway has tiers of charges 
    - if storage gateway is an appliance, also charge associated with the physical appliance 