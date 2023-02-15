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

# Content Review February 1st, 2023
David Chong (Enablement management)
- AWS organizations: service control policies: type of organization policy that you can use to manage permissions in your organization. Offer central controls & makes sure accounts stay w/n org's access control guidelines 
- 6 types of policies
    - identity-based policy: IAM
    - resource-based policy: e.g., S3, KMS, etc. Attached to resources & attached to resource in the console of that resource
        - specifies which principal can use that resource
    - permissions boundaries
    - organizations SCPs: Organizations Service Control Policies
    - ACLs
    - session policies 
- evaluating policies: start w deny. if there's a deny anywhere in the chain, then it's deny. Chain looks through explicit deny > aws orgs > resource based policies > IAM permissions boundary > session policies > identity-based policies
- arn format: arn:partition:service:region:account-id: resource-id | resource-type/resource-id | resource-type:resource-id
- https://aws.amazon.com/s3/storage-classes-infographic/ good to know details on S3. 11 9's durability for all classes 
- s3 access points: able to make policies for each access point

# Missed knowledge check questions
- CloudEndure Migration use EC2 and EBS
- DataSync asynchronously xfers data b/w source & target storage 

# Content Review February 8th, 2023
- memcached: sub-millisecond latency, data partitioning, multi-threaded. Meant to be simpler
- redis: sub-millisecond latency, data partitioning, advanced data structures, snapshots, replication, transactions, Pub/Sub. NOT multi-threaded 
- DynamoDB: key-value. If that comes up on the exam, likely to narrow down the options (DAX, dynamoDB accelerator to up to 10x performance for DDB)

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

# Exam Strategy: Friday, February 10th, 2023 
- question: deploying an app in two regions, writing to a DB in it's region. The two DBs need to be eventually consistent. In conflict, queries should return most recent write 
    - read: have to have data conflict resolution. DDB has data conflict resolution in global tables 
    - DB schema not defined in the question
    - asks for least admin effort. RDS is not managed; DDB is. Also eventually consistent 
    - Using RDS w read-replicas is technically correct, but only partially - is for read-only queries - writing to multiple DB instances NOT SUPPORTED
- Change Data Capture can be used to xfer data b/w region's DBs, but data conflict resolution is not built in
- DO NOT READ TOO MUCH INTO THE QUESTIONS. MAKE NO ASSUMPTIONS, ONLY GO OFF THE DATA THAT IS THERE

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


