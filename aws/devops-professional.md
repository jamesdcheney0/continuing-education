# Compute 
## Amazon EC2
### EC2
- allows deploying virtual servers w/n aws env
- components
    - AMIs
        - image baseline w os + apps 
        - select one from aws/marketplace or make your own 
            - aws marketplace: online store that allows purchase of AMIs from trusted vendors
            - community amis 
    - instance types
        - primary parameters: vCPIs, memory, instance storage, network performance 
        - micro instances, general purpose, compute optimized, GPU instances, FPGA [field programmable gate array] instances, memory optimzed, storage optimized 
    - instance purchasing options
        - on-demand instances
            - launch at any time
            - flat rate, paid by second 
            - ideal for testing/dev
        - reserved instance
            - purchase for set period for reduced cost
            - purchased in one or three year time frame
                - all upfront payment
                - partial upfront payment
                - no upfront payment
        - scheduled instances
            - pay for reservations on recurring schedule, either daily, weekly, monthly
            - able to use it for non-continuous loads
        - spot instance
            - bid for unused EC2 resources
            - no guarantee of avaiability
            - only good for processing data that can be interrupted
        - on-demand capacity reservations
            - ensure that OD instances are always available 
    - tenancy
        - shared tenancy
            - instance luanched on any available host
        - dedicated instance
            - hosted on hardware that no other customer can access
            - additional charged
        - dedicated hosts
            - add'l visibility and control on physical host
            - able to use some host for multiple instances
    - user data
        - enter commands to run during first boot cycle of instance
    - storage options 
        - persistent storage
            - EBS volumes (separate from instance)
            - logically attached via AWS network
            - disconnecting volume rom instance will maintain data
        - ephemeral storage
            - physically attached to underlying host
            - when instance stopped or terminated, all saved data on disk is lost
            - reboot: data WILL remain intact
    - security
        - security groups (instance-level firewall)
        - key pair
            - made up of public and private key to encrypt login info for windows + linux instance & decrypt the same info to allow login
            - public key held and kept by AWS
            - private key customer's responsibility
            - can use the same key pair for multiple instances (not recommended)
        - customer's responsibility to keep instances up to date 
    - status checks
        - system status checks: underlying host issues (out of customer control)
            - best bet is to make a new instance that will likely be on a new host 
        - instance status checks: software/os based issues 
### EC2 Auto Scaling
- automatically increase or decrease resources 
- there is a distinction between AWS EC2 Auto Scaling and 'AWS Auto Scaling'
- advantage
    - infra can elastically provision resources w/o human touch
    - greater customer satisfaction
    - cost reduction 
### Components of Auto Scaling
- create launch configuration or launch template
    - which ami to use, instance types, instance purchase options, public ip, user data, storage config, SGs to use
    - launch template
        - newer and more advanced version of launch config
        - as a template, can build a standard config allowing simplification of how instance are launched for ASGs
        - can create new template or a new template version
            - able to create based on existing template 
    - launch configuration
        - has fewer configurable options than launch template
- ASG defines how many instances to create
    - able to select specific subnets to create new instances in
- autoscaling policy defines when to create and destroy instances
    - can be created during manual setup of ASG (doesn't require going into CW) 
## AWS Auto Scaling Policies
### Manual Scaling
- pros
    - can get ahead of event
    - reduce user downtime 
    - flexibility to scale up/down 
- cons
    - not scalable
    - not a good long-term solution
    - ideal for 'blue moon' and planned events 
### Dynamic Scaling (reactionary)
- step scaling (OG)
    - add or remove instance based on metrics. Commonly based on CPU usage
    - uses a cooldown policy to wait for a bit to allow new instance to come on before checking the metrics & responding again 
    - trigger points based on CW alarms 
        - can make multiple CW alarms for different targets, e.g. 60%, 80%, 95%, and they can take into account current triggers and not provision too many instances 
    - general advice
        - try to scale up more aggressively (since instances take a while to boot up) 
        - scale back down slower (since instances can be terminated almost immedaitely)
            - not as big of an issue now that billing is by the second 
- target tracking
    - tell system where to keep scaling at, e.g. one defined metric, and it manages it all 
        - customer doesn't need to add CW alarms and such
    - works better with larger ASGs
    - don't delete CW alarms target tracking makes
### Predictive Scaling
- goal is to scale up before load happens
- determines usual traffic with ML
    - best for cyclical traffic or recurring workloads 
- can use archived data from CW metrics to create a forecast of usage 
- can run in forecast only mode, and it not scale anything
- predictive scaling occurs at the top of the hour
- can be paired w dynamic autoscaling 
### Scheduled Scaling
- add + remove instances based on time 
- can save money, and works especially well with spot instances 
## Auto Scaling and Lifecycle Hooks
### Overview of Autoscaling and Lifecycle of Instances Created by ASG
- scale in
- scale out
- pending, in service, terminating, terminated 
    - may show in-service if the app is still going through user-data setup
    - lifecycle hooks
        - pending: waits for user-data to finish before showing in-service
            - requires a command to tell ASG when the app is finished, and that it's free to start
        - terminating-wait: wait for logs and connections to be drained before fully terminating 
            - best to manage this externally from the instance, in the ASG console. 
                - set a lifecycle hook in ASG console, then go to EventBridge and make a rule to respond to the lifecycle being triggered and trigger lambda or ssm or something 
        - 30-7200 seconds allowed options 
### EventBridge (aka CloudWatch Events)
- among other things, notified of all ASG events
    - can call lambda & run things
    - works especially well if things need to happen outside of creation and termination of instances 

## EC2 Image Builder
- automate creation of golden images 
    - customize software installed on image 
    - secure image w AWS-provided and/or custom templates
    - test image w AWS-provided tests and/or your own tests
    - destribute golden image to selected AWS regions 
- define a pipeline that can be automatically scheduled or manually triggered
- recipe must be created to define what to do
    -  supported OSs
        - Amazon Linux
        - Windows Server
        - Ubuntu
        - Redhat
        - CentOS
        - SUSE Linux Enterprise Server 
    - components that pipeline adds to the image
        - adds features or functionality
        - sequence of steps to run on ami prior to creation 
        - amazon has many available managed components to install 
        - build component
            - software and settings applied to image during build process
        - test component
            - test functionality, security, performance 
        - definition document
            - contains phases (logical groupings of steps)
                - build
                - validate
                    - validate that settings have been properly implmemented by build
                    - can ensure all components installed
                - test
                    - instance built based on image made from previous steps
                    - prove instance is fully operational upon boot
            - actions
                - general execution
                    - execute binary, shell, ps1
                - file download and upload
                - file system operations
                    - append, copy files/folders, etc
                - system actions
                    - reboot, registry, set OS 
        - can have the pipeline rerun automatically if dependencies or such update
        - must use semantic versioning
        - works well w AWS orgs 
## AWS Elastic Beanstalk
### What is AWS Elastic Beanstalk?
- managed service that allows upload code of web app along w env configs
- automatically provision & deploy resources req'd w/n AWS to make web app operational
- ideal service for engineers not familiar with infrastructure 
- support and maintain environment code like usual
- integrates w a variety of languages
    - packer builder
    - single container docker
    - multicontainer docker
    - preconfigured docker
    - Go
    - Java SE
    - Java w tomcat
    - .NET on Windows Server w IIS
    - node.js 
    - php
    - python
    - ruby
- service itself is free, but charged for price of resources used for hosting
- components
    - application version
        - reference to deployable code (typically s3)
    - environment
        - comprosed of ALL the resources created by EBs, not just an instance w the code
    - environment configuration
        - collection of parameters and settings that dictate how env will be setup
    - environment tier
        - how EBs provisions resources based on app (e.g., web app, vs worker env)
    - configuration template
        - provides baseline for new, unique env config
    - platform
        - culmination of components to build on
        - OS, programming langauage, server type, components of EBs
    - application
        - collection of different elements like envs, env configs
### Environment Tiers 
- environment tier: reflects how EBs provisions resources based on what the app is designed to do
- web server tier: HTTP requests 
    - uses the following services
        - Route53 to direct web traffic to the right servers
        - ELB: referenced by R53 + integrates w ASG
        - ASG: manage capacity planning of apps based on load 
        - EC2 instances: will run at least one instance to run app 
        - SGs: instances governed by SGs, and allows port 80 from all sources
    - host manager installed on every instance 
        - aids in deployment of app
        - collates metrics + events from EC2
        - gernerateing instance-level events
        - monitor app log files + app server
        - patch instance components 
        - push logs to S3
- worker tier: pulls from SQS Queue
    - uses the following services
        - SQS Q
        - IAM Service Role
            - each instance must have an instance profile to monitor the SQSQ
        - Autoscaling
        - EC2 instances: min of 1 used & attached to ASG
            - each instance in env reads from SQSQ
    - Daemon    
        - installed on each instance to pull requests from SQSQ & send data to app 
- both tiers can be used together 
- yaml and json must be saved with .config extension
### Deployment Options
- all at once (default)
    - roll the app to resources at the same time
    - would cause downtime 
- rolling
    - minimize amount of disruption vs all at once
    - deploy app in batches
        - once complete, moves onto another batch
    - small impact on availability
- rolling w additional batch
    - env updated in batches
    - adds another batch of instances w customer env to resource pool to ensure app availability not impacted 
    - after updates complete, removes add'l batch
- immutable
    - creates an entirely new set of instances
    - served through temp ASG behind ELB
    - env temporarily doubles in size 
    - old env removed + ASG updated
        - if new app fails, would failover to previous version & not terminate the old instances 
### Environment Config Demo
- under advanced configuration, there are a set of configuration presets, and the elements within those can be modified 
    - option groups: software, instances (SG options defined here), capacity, load balancer, rolling updates & deployments (deployment options defined here), security, monitoring, managed updates, notifications, network, database, tags 
### Monitoring and Health Checks
- basic health reporting
    - less granular measures
    - gain high-level overview of how env is running
    - metrics sent to CW in 5 minute intervals
    - in web server tier: ec2/elb checks
        - every 10 seconds, ELB sends health check to instances in ASG 
        - checks if ASG has at least one instance and instance(s) are healthy
        - checks that r53 is correctly routing
        - checks that SG
    - in worker tier: sqs checks 
        - ec2 instance status check referenced for instance health
            - system status check: if this fails, likely an issue w underlying host
            - instance status check: if this fails, likely requires customer troubleshooting
                - common issues: incorrect network config, corrupt file systems, exhuasted memory, incompatible kernel
        - checks that instance is polling SQS at least every 3 minutes 
- enhanced health reporting 
    - displays additional monitoring options 
        - can be sent to CW; incurs add'l cost 
    - when supported, has a health agent installed for system metrics + web server logs 
        - health agent able to probe deeper and more frequently (every 10s) than CW 
### Summary
- core components 
    - application version: specific reference to section of deployable code
    - environment: refers to app version that has been deployed w AWS resources
        - coomprised of ALL resources created by EBs
    - environment configuration: collection of parameters and settings that dictate how an env will have resources provisioned
    - environment tier; determines how EBs provisions resources based web or worker tier
    - configuration template: provides baseline for creating new, unique env config
    - platform: culmination of OS, programming language, server type, + components of EBs
    - applications: collection of envs, env config, app versions 
## Optimizing Compute
### Monitoring for Underutilized Compute Resources
- AWS Compute optimizer
    - tracks 
        - ec2 instances
        - ASGs
        - EBS volumes
        - AWS lambda 
    - underprovisioned: resources lack power
    - overprovisioned: too much power to resources
    - optimized: meet requirements of workload 
    - uses ML to monitor last 14 days of usage for recommendations 
    - for each instance, will provide three instance recommendations 
        - will have to manually modify instance 
    - have to opt into service
    - takes up to 12 hours after starting to provide recommendations, then refreshes daily
    - paid service
    - for ec2, only recommends selected ec2 instance types
    - for lambda, only makes recommendations if memory over-provisioned memory or under-provisioned cpu 
    - more robust than cost explorer (considers disk/network I/O metrics also)
    - does NOT calculate savings from reserved instances 
    - used for 'right-sizing 
- AWS cost explorer 
    - uses compute optimizer engine to provide recommendations on workload, either termination or modification
        - termination: <1% CPU utilization
        - modification: 1-40% CPU utilization 
    - only makes ec2 recommendations
    - considers reserved instances in recommendations 


## AWS App Runner
- fully managed service that allows to quickly build, deploy, and run containerized apps and microservices on AWS
- supports websites, APIs and backend services
- specify container image/registry location (or source code + build & start commands if not already containerized)
- will auto build container image for app, deploy + provide prod URL
- can add AR as a deployment target w/n CI/CD pipeline
- can auto build + deploy app when source code or container image updated
- supports autoscaling and will add or remove load-balanced instances based on request volume

## AWS Serverless Application Repository
- managed repo for serverless apps published by AWS, AWS partners, and other third-party devs
- typically leverage lambda, API gateway, and DDB + don't require customer to manage infra
- available under MIT open source license
- levearage SAM to define AWS resources
- devs can browse or search to find apps or publish their own for private or public reuse 
- when deploying apps, can specify custom config parameters to initialize app
- apps can be managed directly from console 

## Knowledge Check: Compute
- EBs application version: reference to a section of deployable code that typically points to S3 where the code may reside 
- key benefit of using EventBridge instead of auto-scaling lifecycle hooks to trigger actions is that EB can occur a few second early or late w/o significant impact 
- in EBs web server env, Host Manager aids in the deployment of the application
    - Daemon is installed on every EC2 instance in worker env to pull requests from SQSQ

# Serverless
## Understanding AWS Lambda to run and scale your code
### An Overview of AWS Lambda
- input
    - function invoked by console, SDKs, AWS toolkits, CLI, function URL, or triggers
    - can pass in events for code to process  
        - AWS services can pass in events 
- function
    - make up lambda
    - made up of code, perms, variables, and memory 
    - can write code in lambda or upload code
    - runtimes
        - java, go, powershell, node.js, C#, python, ruby, custom runtime 
- output
    - once function is triggered and code runs, code calls downstream services, like SQS, DDB, SNS etc
    - can monitor & log lambda
        - both invokations & how code is performating 
- cost
    - amount of requests sent to function
    - duration it runs (rounded to nearest 1ms)
    - amount of compute power provisioned for function 
- function can only run one concurrent function call at a time, with a limit of 50 concurrent runs 
- provisioned concurrency is provided by aws to keep functions 'warm'
### Invoking a Lambda Function
- every invokation goes through Lambda API 
    - synchronous (push-based) invocation
        - e.g., API gateway sends request from client to lambda, and lambda returns response to API gateway
        - if function fails, the function is responsible for retrying
        - can invoke synchronously with CLI
    - asynchronous (event-based) invocation
        - no response to originating service
        - e.g., if object placed in bucket, event goes to lambda and not back to S3 
        - handles retries if the function returns an error or is throttled
        - uses built-in queue 
        - failed events can go to DLQ or lambda destinations 
    - stream (poll-based) invocation
        - used when pulling from DDB streams, SQS, kinesis streams 
        - event source mapping
            - links event source to lambda function
            - differs basd on event sources used
            - can be created w CLI 
- which model is right for workload
    - stream (poll-based)
        - use case: processing messages from a stream or a queue
        - advantages: message filtering
    - synchronous
        - use case: if app needs to wait for response 
        - advantages: helps maintain order 
    - asynchronous
        - use case: if function runs for long periods of time and does not need to wait for response
        - advantages: automatic retries, built-in queue, DLQ for failed events 
    - AWS service 
        - if aws service invokes, customer cannot select invocation type; service picks the call type 
### monitoring your Lambda Function Demo
- categories
    - invocation metrics
        - invocation
        - error count and success rates
    - performance
        - duration
        - iteratorAge (for polling) 
    - concurrency
- for each function, CW makes new log group 

## Which services should I use to build a decoupled architecture
### Decoupling Applications with Queuing Services
- decoupling
    - allow each component to perform its tasks independently
    - change in one component does not affec thte rest
    - component failure is isolated 
- SQS used to add a queue between each layer, so the layers aren't dependent on the one before them (loose coupling)
    - if instance fails to process message, the message is left in SQS 
    - apps adding messages to Q called producers
    - apps reading messages from Q called consumer 
        - when message picked up by consumer, it is locked & made invisible to other consumers until the message is processed
        - every message processed at least once 
    - delay Q: able to set a predefined delay which acts like visibility timeout
    - visibility timeout by default is 30s
        - minimum 0 seconds, maximum 12 hours 
            - if consumer needs more than 12 hours to process message, use Amazon Step Functions 
        - timeout can be set for entire queue or per individual message 
- SQS
    - how consumer listens
        - short polling
            - sends a receive message request, and SQS sends a response, even if no responses available
            - occurs when WaitTimeSeconds parameter of a ReceiveMessage request is set to 0. Can happen in two ways
                - ReceiveMessage sets WaitTimeSeconds to 0
                - ReceiveMessage doesn't set WaitTimeSeconds
        - long polling
            - consumer sends WaitTimeSeconds parameter of >0 and <20 seconds 
            - if the ReceiveMeessageWaitTimeSeconds Q attribute is set to a number >0: 
                - SQS sends response after it collects at least one message available and up to the max number of messages specified in request by MaxNumberOfMessages
            - empty response only happens when specified wait time expires
    - message size
        - min size: 1 byte
        - max size: 256KiB (default)
        - SQS extended client library
            - enabled processing of large messages up to 2GB w S3
            - allows to define if messages should be stored in S3 all the time or only when the message size is bigger than 256KB limit 
        - can also send message w link to object stored in S3 bucket 
    - standard Qs 
        - do not guarasntee message order & only guarantees at-least-once delivery
        - there can be max of 120k in-flight messages
        - if short polling, quote can cause consumer to get OverLimit error
        - if long polling, no error messages, but should always delete messages from Q after processed 
    - FIFO Qs
        - perform slower than standard Qs
        - maintain message order as FIFO and implement exactly-once delivery
        - can have max 20k messages while processing 
    - malformed messages/corrupted messages
        - DLQ can be defined to capture messages that aren't able to be deleted after being processed X times 
        - DLQ redrive sends corrected message back into Q
            - if FIFO Q, would affect the order of the Q
        - DLQ should be monitored quickly & examined as quickly as possible (with Lambda or human touch)
        - SNS often used w DLQ for notifications 
### Notifications with Simple Notification Service
- SNS: one-to-many distribution model 
- topic: interaction point similar to a mailbox
    - does not store messages; only pushes to subscribers
    - cannot recall messages 
- publisher: sends the message
- subscribers: recipients of messages
    - message types
        - apple, MS, AWS, adibu, fire-based messaging
        - http
        - email 
        - lambda
        - sms
            - can be marked as transactional or promotional
- SNS can send messages for SQSQs
- can seamlessly scale from few to many messages
    - max 12m messages/day 
- max message size: 256KB
- breaks messages in 64KB chunks
- can use SNS Extedned Client for Java to push messages up to 2GB & uses S3 to do so
    - subscribers from SQS can use SQS Extended client Library for Java to retrieve the payloads from s3
    - lambda functions + other endpoints must use Payload Offloading Java Common Library for AWS to access objects stored in S3 
- message filtering
    - allows subscribers to only receive some messages that interest them
    - defined in JSON format
    - SNS compares the attributes on the filter and only sends if attributes match filter policy atributes 
    - decouples message routing logic from publisher, and allows to use single topic for different conditions 
- SNS delivery policy
    - used to control retry patterns
        - linear
        - geometric
        - exponential backoff
        - maximum/minimum retry delays 
    - when retry policy exhausted, SNS can move message to DLQ 
        - SQSQ that SNS subscription can target for messages that can't be delivered
- SNS vs SQS
    - delivery: push (passive) vs poll (active)
    - message persistency: no vs yes 
    - producer/consumer: publish/subscribe vs send/receive
- to send to multiple SQSQs (fan-out)
    - create an SNS topic, subscribe SQSQs to topic
### Advanced SNS Messaging with FIFO SNS Topics
- using FIFO SNS topics + FIFO queues, can accomplish idempotency at the messaging layer instead of having to modify apps 
- in general, SNS trys to deliver messages in the order they were received, but not guaranteed due to network conditions 
- idempotency: processing a message more than once should be okay
    - all read operations are idempotent by nature
    - write or modify operations should be designed so that processing a message more than once does not create any errors or inconsistencies 
- FIFO topics
    - configure a message group ID when publishing to a SNS FIFO topic
    - all messages sent and delivered in order of arrival
    - can enable content-based message deduplication to prevent dupes
        - makes SNS use SHA256 hash to create dedupe ID using body of message
            - SQS FIFO Qs can then make sure it hasn't received any dupes 
    - can process 300 messages per second or 10MB per second, whichever limit is hit first. These are hard limits 
    - message ordering + dedup achieved at messaging layers 
### Migrating existing queues and topics used for decoupling to AWS w/o code rewrite 
- can directly use Amazon MQ if the following messaging APIs are already in use in another env
    - Java Message Service (JMS)
    - .NET Message Service (NMS)
    - MQ Telemetry Transport (MQTT)
    - WebSockets 
- Amazon MQ used to migrate apps w/o rewriting code
    - cost-effective
    - automated admin + maintenance
    - HA
    - storage implemented across multiple AZs
    - message encryption in transit using SSL & at rest w AES256
    - network isolution w private endpoint in VPC 
    - integrates w CW for metric monitoring + CT for logging 

## AWS Step Functions
- create interactive & complex functions 
- Step Functions: state machine service
    - it's like a vending machine: usually in idle state, waiting for customer, then when it receives money, picks an item & delivers to customer
- can run lambda functions in ways that lambda can't natively do so itself
- can run functions in parallel, sequence, retry, if/then 
- able to get past the 15 minute lambda code restriction by using less monolithic functions 
- amazon state language, similar to json, to allow the function to do its thing 
    - creates a visual flow graph for understanding behind the scenes & show inputs & outputs
- available state types
    - pass state
        - debugging state
        - used when first creating; allows passing info directly to outputs 
    - task state
        - what functions to run
        - usually substate to other states
    - choice state
        - if/then decision for more app logic
    - wait 
        - can wait until specific time, or for a certain amount of time
    - success state
        - can be used for choice or ending state
    - fail 
        - must have error message & cause
    - parallel state
        - waits for all processes to finish before moving on
    - map state
        - iterate through list of items and process through them
- use combinations of these states to make a complex state machine 
- asynchronous callbacks
- can nest child state machines in parent state machines 

## Serverless Application Model
- open-source framework for building serverless apps in AWS
- can use any language w runtime defined in lambda
- define + deploy serverless resources (functions, APIs, DBs) using YAML templates
- during deployment process, SAM will transform those templates into CFN
- SAM CLI provides env that allows build, test, debug of SAM apps locally 
    - `sam build` to build app locally & transform YAML SAM template into CFN
    - `sam package` upload CFN template + code to S3 
    - `sam deploy` create + execute CFN change set, deploying app 


# Storage
## S3 Storage Classes
- standard
    - high throughput (HT), low latency (LL)
    - frequent access to data
    - eleven 9s durability
    - 99.99% availability 
    - SSL/TLS to encrypt data in transit & at rest
    - lifecycle rules 
- intelligent-tiering (INT)
    - frequent and infrequent access; unpredictable access patterns 
        - objects placed in frequent access or infrequent access tiers 
    - 99.9% availability 
    - same HT + LL, durability, SSL/TLS + lifecycle rules as standard
- standard-infrequent access (S-IA)
    - infrequent access 
    - 99.9% availability
    - same HT + LL, durability, SSL/TLS + lifecycle rules as standard
- one-zone infrequent access (Z-IA)
    - infrequent access
    - same durability, but only across one AZ
    - 99.5% availability
    - 20% cheaper than standard 
    - same HT + LL, SSL/TLS + lifecycle rules 
- S3 Glacier
    - separate service from S3, but directly interacts w S3 lifecycle rules 
    - cheaper storage than S3
        - cold storage: low-cost, long-term backup + archiving
        - storage access not instance
    - eleven 9s of durability
    - retrieval takes up to several hours for access
    - vaults (regional)
        - container for glacier archives 
        - archives: any archives, similar to S3
        - can have unlimited number of archives in a vault 
    - glacier doesn't have a GUI; can only create vaults, set data retrieval policies and event notifications 
        - moving data into S3 requires creating vaults, then moving data into vaults using APIs, SDKs, CLI
        - archive removal, similar process. Have to create a removal job in console, then pull with code 
    - retrieval options
        - expedited 
            - must be under 250 MB
            - availabile in 5 minutes
        - standard
            - any size data withdrawl
            - available in 3-5 hours
        - bulk
            - PB of data at a time
            - 5-12 hours
- S3 glacier deep archive (G_DA)
    - best for records must be held for a long time but not urgently accessed 
    - retrieval option: withdrawn in 12 hours or less 
- main differences b/w classes in durability and availability
    - how important is the data, and how often it will be accessed are key questions to be asked. 

## S3 Management Features
### Versioning
- allows for multiple versions of the same file to exist 
- managed automatically against objects in a bucket with versioning enabled
- no enabled by default
    - once enabled, cannot disable, only suspend
- versioning states
    - unversioned
    - versioning-enabled
    - versioning-suspended
- more pricey, since more data is being stored 
- there's a switch that can be flipped to hide or show version IDs in the console 
- deleting versioned objects 
    - if hiding versions (default option) and deleted object, a delete marker will be added and hide the item from the console. Showing the versions will show the remaining versions
        - deleting the delete marker will restore the object
    - must delete all the versions of the object to fully delete the object 
### Server-Access Logging
- captures details of requests made to objects in bucket
- made on a best-effort basis; no guarantee that every request will be captured 
- recording of events is not instantaneous
- can enable during creation or after creation
- log delivery group must be allowed to deliver files to target bucket 
- source & target buckets must be in same region & should be different
- permissions of S3 access log gropu can only be assigned via S3 ACLs
- log names: <target-prefix>YYYY-MM-DD-hh-mm-ss-uniqueString
    - canonical user ID for the bucket owner listed at the top of the log 
    - `-` in any field indicates no data was gathered 
### Object-Level Logging
- closely related to CloudTrail
    - CT records & tracks all API requests made 
        - associates additional metadata to requests\
- can configure CT to track all buckets or at bucket level, either in CT console or in S3 bucket properties 
### Transfer Acceleration
- uses CloudFront 
- when performing transfer acceleration, routes traffic to edge location, then to S3 w AWS network
- increased cost for data in and out 
- bucket name must be DNS compliant and not use any `.` in name 

## Amazon S3 Security
### Using Policies to Control Access
- identity-based policies
    - attached to IAM identity requiring access
    - associated to user, group, role 
    - define resource in policy 
- resource-based policies
    - associated w resources
    - ACLs 
        - control access to bucket & specific objects w/n bucket by groups & AWS accounts
        - can set different permissions per object
        - different permissions applied depending on where ACL is applied
        - conditional statements and explicit deny not allowed
        - kinda like file permissions on linux where it differs based on owner/group/user 
        - can allow other accounts with ACLs 
        - there is no write permissions granted with ACLs
    - bucket policies
        - written in JSON 
        - can either write own policy, create in GUI, or use templates
        - apply to bucket & objects in bucket 
- when to use IBP vs RBP
    - IBP
        - centrally manage access control methods
        - able to use 1 or 2 policies across multiple buckets
        - can control access for more than one service at a time
        - limits: 2kb in size for user, 5kb for group, 10kb for roles
    - RBP
        - if wanting to maintain security for one bucket alone 
        - able to allow access from external account
        - can be up to 20kb in size 
- policy evaluation logic 
    - all policies viewed together
    - conflicts handled according to least priviledge 
    - to gain access, there must be an explicit allow 
    - if there is a deny that exists, it will override any allows 
### Cross Origin Resource Sharing (CORS) with S3
- allows specific resources on a web page to be requested from a different domain than its own 
    - allows one to build client-side web apps and if required, can utilise CORS support to access resources stored in s3 
- CORS policies contains rules based on origin

## Amazon S3 Encryption
### Server-Side Encryption with S3 Managed Keys (SSE-S3)
- minimal configuration
- management of encryptiuon keys managed by AWS
- upload data & S3 will manage encryption
- encrypiton process
    - client uploads data to s3 
    - creates plaintext s3 data key & encrypted object stored
    - plaintext s3 data key encryption w s3 master key + encrypted key stored, then plaintext key forgotten
- decryption process
    - uses encrypted data key + master key to decrypt plaintext key
    - plaintext key used to decrypt data 
### SSE-KMS
- S3 uses KMS to generate encryption keys
- greater flexibility of key management: disable, rotate, apply access controls to CMK
- encryption process 
    - upload to s3, s3 requests keys from KMS CMK. 
    - using CMK, creates plaintext data key + encrypted data key that are sent to s3
    - s3 combinas plaintext data key + object data, which is stored as encrypted object with the encrypted data key + plaintext key removed from memory
- decryption process
    - request from s3, encrypted data key sent to KMS
    - KMS takes the encrypted key + cmk to generate plaintext key
    - plaintext key plus encrypted object data used to decrypt data + send to client 
### SSE-C
- provide own master keys
- customer provided key would be sent w data to S3 & S3 would then perform encryption
- encryption process
    - client uploads object + customer key over HTTPS
    - s3 uses customer key to encrypt object data + creates salted HMAC value of key for future validation and both are stored on s3. plaintext key removed from memory
- decryption process 
    - client requests data + sends customer key to s3 
    - customer key is validated by being compared to HMAC value
    - customer key combined w encrypted object data to return object data 
    - object data sent back to client 
### Client-Side Encryption with KMS Managed Keys (CSE-KMS)
- uses KMS to generate data encryption keys
- KMS is called upon via the client
- encryption takes place client-side & encrypted data sent to S3
- encryption process
    - using AWS SDK (like java client) requests data using CMK-ID from KMS
    - KMS generates plaintext data key + cipher blob of the same data key
    - both keys sent to client
    - client combines object data w plaintext data key to create object data
    - client uploads encrypted data + cipher blob to s3 
        - cipher blob stored as metadata of encrypted data in s3 
- decryption process
    - request data
    - s3 sends encrypted data + cipher bolb to client
    - client sends cipher blob to KMS
    - KMS combinees cipher bolb w CMK to greate plaintext key which is sent to client to decrypt 
### CSE-C
- utilize own keys
- use AWS SDK client to encrypt data before sending to S3 
- encryption process
    - using AWS SDK, randomly generate plaintext data key to encrypt object
    - object data + plaintext key create encrypted object data 
    - customer CMK + client generated plaintext data key create encrypted data key
    - client sends data + key to s3
        - key stored as metadata in s3 
- decryption process
    - client requests data, aws sends encrypted data object and key
    - client cmk + encrypted data key used to generate plaintext data key
    - plaintext data key + encrypted object to decrypt the object 

## Amazon S3 Replication and Bucket Key Encryption
### Amazon S3 Replication
- asynchronously copy from a bucket to a single or multiple buckets in the same or other regions or accounts 
- same-region replication (S3-SRR)
    - for compliance and legal regulations
    - data aggregation and consolation
- cross-region replication (S3-CRR)
    - compliance and legal regulations 
    - enhance data latency for business and customer use 
- multi-destination
    - replicate objects from single source bucket to multiple destination buckets 
- uses rules to manage the process 
    - can apply to specific objects or all objects 
- *source and destination buckets must have versioning enabled*
- if source bucket has s3 lock feature enabled, destination bucket must also have it enabled 
- IAM role is used to define permissions req'd to allow s3 to replicate data 
- points of consideration b/w buckets in different accounts
    - when using CRR destination bucket owner must ensure perms in place to grant source owner access to replicate objects to bucket
    - destination buckets cannot be configured as Requester Pays buckets 
- only objects added a bucket AFTER replication has been config'd will be replicated
    - any objects w/n bucket prior to replication rules being created will not be replicated
- can only work w SSE-S3 or SSE-KMS if it is config's w/n replication rule
- cross-region replication w KMS requests specifying the ARN of the destination CMK (which are region-specific)
- replica modification sync
    - allows replication of metadata bi-directionally
    - maintains synchronization of
        - tagging info
        - object lock retention info
        - ACLs
    - enabled w/n replication rule
    - statistics can be captured w/n CW 
### Bucket Key Encryption w SSE-KMS
- CMK (customer master key)
    - customer managed CMK
        - created & managed by customers
        - customer has full management and control
    - AWS Managed CMK
        - created and managed by AWS on customer's behalf
        - used by other AWS services that integrate w KMS
        - can view policies, but can't change
    - AWS Owned CMK
        - not visible w/n KMS console 
        - unable to manage keys in any way
- DEK (data encryption keys)
    - used to encrypt data
    - created by CMKs, used OUTSIDE of KMS
    - CMK creates two data keys when it generates a key request; plaintext data key + encrypted data key 
- bucket keys 
    - reduce overall spend when using SSE-KMS by reducing the amount of requests and traffic from S3 to KMS
    - setup process
        - bucket created w SSE-KMS bucket key enabled
        - s3 requests bucket key from KMS
        - KMS uses CMK to generate S3 bucket key
        - bucket key sent to s3
        - bucket key associated w bucket 
    - encryption process 
        - object uploaded
        - bucket key generates data keys (encrypted + plaintext)
        - data keys used to encrypt object data: object data + plaintext key + encryption algorithm creates encrypted object data + encrytped data key stored in s3, and plaintext key removed from memory
        - by not needing to request CMK from KMS, makes it cheaper and easier to get encryption keys
    - decryption process
        - object requested
        - s3 combines encrypted data key with bucket key to generate plaintext key
        - plaintext key used to decrypt object data & then removed from memory 
        
## Amazon S3 Lifecycle Configurations
### The Case for Lifecycle Configurations
- s3 intelligent tieiring
    - pay monthly object monitoring and automation charge 
        - tiers: frequent, infrequent, archival
    - for unknown/unpredictable workloads
- lifecycle configuration
    - move data to lower cost storage or delete it automatically 
    - most cost-effective strategy when objects + workloads have defined lifecycle and usage 
### Components of a Lifecycle Configuration
- technically an xml file
- contains a set of rules
    - each rule split into four components
        - ID: i.e the name
        - filter: which objects to take action on
            - filter on prefix, tag, size - have to `and` to combine multiple filters 
            - max filter object size is 5TB
        - status: enabled/disabled
        - rule (action section)
            - what to do with objects
            - options
                - transition: move data automatically b/w classes 
                    - based on object age
                    - if versioning turned on, only works w current version of object 
                - expiration: automatically delete data from s3 
                    - based on object age
                    - if versioning turned on, only works w current version of object 
                - NoncurrentVersionTransition: 
                    - used to move objects with versioning
                    - can retain b/w 1-100 versions 
                - NoncurrentVersionExpiration: 
                    - used to delete objects with versioning
                - ExpiredObjectDeleteMarker
                    - able to delete old objects with delete markers
                - AbortIncompleteMultipartUpload 
                    - set how many days a multipart upload can remain in progress 
### Creating a Lifecycle Configuration Demo
- to define via CLI, must use JSON, even though the rules are in XML... would have to convert from XML to JSON

## Amazon Elastic Block Store
- presistent & durable block-level storage 
- independent of EC2 instances, and logically attached 
- EBS volume can only be attached to one instance (instance can have more than one volume)
- backups (snapshots)
    - manually
    - automatic w cloudwatch events 
    - incremental by default
    - new volumes can be created from snapshots 
    - able to copy snapshot b/w regions 
- every write to EBS volume is replicated w/n AZ
- volumes only available w/n AZ 
- types
    - SSD
        - suited for work w smaller blocks (DBs, boot volumes)
        - gp2
        - io1: enhanced iops for workloads 
    - HD
        - suited for higher throughput 
        - can't be used as boot volumes
        - st1: throughput intensive
        - sc1 (cold HDD): large & meant to be accessed infrequently
- security
    - enable volume encryption at creation 
        - uses KMS CMKs
    - snapshots from encrypted snapshots remain encrypted
    - can force all volumes in region to be encrypted at creation
- creation
    - during creation of new instance
        - decide what happens when instance gets destroyed
    - w/n console as bespoke volume 
        - specify AZ 
    - able to be resized, either by just making it bigger, or by creating a snapshot & restoring to a larger volume 
    

## Introduction to Amazon EFS
### What is the Amazon Elastic File System
- low-latency access from multiple instances at once 
- store files that are accessable as network resources 
- ec2 instances connect via mount points
    - mount points can be made in multiple AZs 
- replicated across multiple AZs in a region 
- not currently available in all regions 
### Storage Classes and Performance Options 
- storage classes
    - standard
        - default 
    - infrequent access (IA)
        - reduced cost, and higher latency
        - charged for amount of storage used, and charged for read & writes (best for storing for archive purposes)
    - lifecycle management
        - 14, 30, 60, 90 days will move from standard to IA
        - once file is accessed again, timer is reset and moved to standard 
        - exceptions: won't store metadata, or files under 128 kb
        - if EFS created after 2/13/19, can be turned on/off 
- performance modes 
    - defined during creation
    - general purpose
        - up to 7k file system operations per second 
        - lower latency 
        - CW will show the max iops
    - max i/o
        - greater than 7k file system operations
        - higher latency than general purpose 
- throughput modes (measured in MiB)
    - bursting throughput
        - default
        - throughput scales as file system size increases
        - 100 MiB/s per TiB
        - duration of burst is also based on file system size 
        - burst credits are added when file system is running under 15 MiB/s
    - provisioned throughput 
        - incurs add'l charges for bursting above provisioned throughput 

## Performance Factors Across AWS Storage Services
### Block vs Object vs File Storage
- block storage: think hard drives and SANs (EBS)
- object storage: large, unstructed data w limitless capacity (S3)
- file storage: data stored in files & stored in hierarchy of storage (EFS, FSx)
### Block Storage
- used for low-latency and high-performance workloads
- block: fixed-sized chunk of data that can be read in one i/o request 
    - data divided into blocks
    - blocks don't need to be in sequence to be properly read 
- must be formatted to be understood by OS
- instance store volumes are also block-storage based, but are also ephemeral
- EBS performance
    - use appropriate volume type for workload 
    - ssd better for small random ops
    - hd better for sequential reads/writes 
- EBS optimized instances
    - i/o traffic may compete w other network traffic by default, this separates I/O traffic from other network traffic 
- other performance factors 
    - performance of st1 and sc1 volumes will be degraded while snapshotting
    - when initializing a new volume from snapshot, performance will be degraded until each block on the volume has been accessed at least once
    - all blocks must be downloaded from s3 and written to new volume
    - mitigated by initialization (`dd` or `fio`)
    - can increase i/o w RAID 0, although there is a risk of data loss 
    - can test and validate performance by benchmarking 
### Object Storage
- s3 great for large amounts of unstructured data
- all storage items called objects 
- updating an object requires rewriting entire object 
- must be accessed via web or cli, not network
- HA & durable
- low cost & scalable
- cross-region replication for data recovery possible
- object metadata
    - includes globally unique identifier and add'l metadata
    - may be system-defined or user-defined
    - object key + version ID identifies object uniquely in S3 
- performance factors 
    - improve performance
        - instances + buckets should be in the same region if they're dependent on each other
        - use s3 transfer acceleration if add'l regions are required to be used (cloudfront edge locations)
        - put cloudfront in front of bucket for static websites
        - multipart upload
            - required for 5GB+ files, recommended for 100MB+ files
    - download performance
        - think of s3 as a large, distributed system
        - improve download performance by downloading multiple chunks of an object at a time 
            - add `range` to http headers to perform byte-range fetch 
### File Storage
- maintains hierarchy of files that live inside folders
- used for network-shared file systems including NAS devices
- files can be accessed concurrently from multiple clients
- lives on top of block storage 
- EFS
    - works w linux instances
    - performance factors
        - performance type: general or high throughput 
        - throughput: bursting or provisioned 
- FSx
    - supports several other operating systems on FSx
        - FSx for NetApp
        - for OpenZFS
        - for Windows File Server
        - for Lustre
    - initial throughput capacity configured when file system created
    - capacities range from 32-2048 MB/s 
        - can be adjusted over time 

## Optimizing Storage
### Monitoring for Underutilized Storage Resources
- right-sizing storage 
    - monitor for under- or over-utilized services with CW 
    - if volume is idle, snapshot + terminate
    - use lifecycle manage to manage & delete snapshots
    - use customer CW metrics to find under- and over-provisioned volumes 
    - use compute optimizer 
        - makes throughput and IOPS recommendations for gp SSD volumes
        - makes IOPS recommendations for io SSD volumes 
    - s3 object access logs to find buckets/objects that aren't frequently access 
        - use s3 analytics to determine when to move data to different class 
        - s3 intelligent-tiering class w unpredictable storage patterns 

## Creating a Hybrid Storage Solution Using AWS Storage Gateway
### The Fundamentals of Storage Gateway
- enable hybrid connection b/w on-prem and cloud
- deployment options
    - VM in on-prem environment
    - AWS Storage Gateway Hardware Appliance locally
    - AWS EC2 instance 
    - requires 150MB space for local deployment
        - uses as cache for data uploaded to AWS and uses cache for low-latency access 
- connects to AWS Storage Gateway Management Service which connects to AWS storage options 
- types
    - s3 file gateway
        - store objects in s3 using NFS or SMD
        - storage/request pricing: same as s3 
        - charged based on TB/month of data trasnferred to on-prem gateway
    - FSx file gateway
        - store objects in FSx for Windows File Server using SMB
        - storage/request pricing: same as FSx for windows 
        - charged based on TB/month of data trasnferred to on-prem gateway
    - tape gateway
        - replaces physical tape libraries. Stored in s3 & can be exported to glacier
    - volume gateway
        - store data in block storage using iSCSI
### Storage Gateway Use Cases
- s3 file gateway
    - use case: backup and archiving of hadoop & DBs
    - file gateway cache can be adjusted to meet needs of workload
    - cache can be up to 64TB; optimized for large files, images, db backups 
    - 10 file shares w 100 active users per gateway
- FSx file gateway
    - requires vpn to connect to aws 
    - integrates w AD & SMB 
    - cache optimized for small and mixed file workloads and office documents 
    - unlimited file shares w 500 active users per gateway
- tape gateway
    - use case: replacing physical tape backup service 
    - serves as drop-in replacement for tape library 
    - have to mount virtual tape drives and media changer on gateway device on-prem. Communicates w iSCSI
    - can archive in glacier 
- volume gateway
    - use case: migrating SQL DB to cloud
        - store snapshots 
    - after creating gateway, create storage volumes in AWS to send data to, and can make EBS snapshots from those volumes 
        - can be restored as EBS volumes for ec2 instances or be used by the gateway
    - cached volumes
        - store data in s3 & keep copy of frequently accessed data locally
    - stored volumes
        - store all data locally & back up data to s3 asynchronously (also uses cache & compresses data in transit)

## Cross-Region Backups with AWS Backup Service
### Terminology
- backup rule: specifies when and where to back up data & what to do with it over time
- backup plan: associate of one or more rules to which resources can be assigned
- resource: item to back up (ec2 instance, volume, RDS)
- vault: aws-managed encrypted storage location for backups 
- vault lock: provides ability to meet compliance requirements for data
    - follows WORM model
- job: action of creating backup or restoring backup following backup plan 
### Basic Usage and Encryption Demo
- AWS backups maintains the same encryption as the resource already has. It will not encrypt unencrypted data 

# Databases
## DynamoDB Basics
### What is Amazon DynamoDB
- fully managed serverless noSQL (not only SQL) service 
- most common noSQL data models
    - key-value (most common)
        - collection of key value pairs
        - key is unique value for record
        - must be highly partitionable and scalable 
    - document
    - graph
    - wide-column databases
### DynamoDB Key Features
- HA: data automatically replicated across three AZs in region
    - replication b/w AZs is usually quick, but DDB does use eventual consistency
    - strong consistency: w every read request, can define whether to use strong or eventual consistency
        - reads may take a small performance impact 
    - ACID compliance: atomicity, consistency, isolation, durability 
- durable
    - global tables: replicate data across regions
        - creates replica tables in chosen regions
        - active active tables; read from any table and write to table nearest to user 
    - backups: for compliance, or roll back to positive state
        - on-demand: compliance/archiving
        - point-in-time recovery: roll back to state in past 35 days 
        - integrates w AWS backup
- scalable
    - infinitely scalable
    - performance is constant regardless of size of db 
    - best for OLTP workloads that require high scalability & data durability
        - easier to architect new workload, rather than try to change an existing workload
        - use cases where the data is fairly small and changes quickly (leaderboards, shopping cart data, user metadata)
    - no good for OLAP
- fast
### DynamoDB Terminology
- tables: stores data 
    - collections of objects
- items: term for row/records in dynamodb
- attributes: i.e., a column in RDB
- partition key: store data in logical data partition behind the scenes 
- all items need
    - an appropriate partition key
    - varying sets of attributes (not all attributes need to be filled)
- sort keys: sort data w/n same partition key 
- composite primary key: partition key + sort key
- read and write levels 
    - provisioned throughput mode: specify RCU & WCUs
        - 4kb: 1 RCU for strongly consistent read; .5 RCU for eventually consistent read, 2 RCUs for transaction
        - WCU: one write capacity unit per second for items up to 1 KB
            - transactions require 2 WCUs per second for items up to 1 KB
        - good choice w steady traffic
        - can use in combination w DDB autoscaling based on traffic & stay w/n provisioned throughput
        - can reserve capacity for minimum level of usage
        - pay for provisioned capacity
    - on-demand capacity mode 
        - DDB decides how many RCU/WCUs app needs based on traffic
        - just-in-time approach
        - automatically handles autoscaling 
        - costs more per request
        - pay per request and for storage used  
### Comparing DynamoDB to Other Databases
- relational DBs
    - scale vertically (increase size of instance)
    - generally have to manage scalability
- DDB
    - scales horizontally (get more instances)
    - flexibily manages scaling
    - 'schemaless'; don't have to define table schema in advance
        - can adjust tables and data types on the fly
    - built in scan and query statements are less flexible than complex SQL
    - only has a few native data types 
    - limitations
        - maximum item size 400KB
            - if frequently storing large items, have to store in s3, then refer w DDB
        - soft limits: max tables, max throughput 
### Interacting with DynamoDB
- console
- CLI 
- SDKs 
- NoSQL workbench for DDB (visual IDE for creating tables)
- each API operation has a name, set of parameters, set of outputs 
    - e.g. CreateTable: specify table name, # of RCUs, WCUs. output: operation successful, etc 
- control plane operations
    - API calls: ListTable, DescribeTable, CreateTable/UpdateTable/DeleteTable
- data plane operations
    - perform create, read, update, and delete on tables
    - API calls: GetItem API (need specific primary key of item), returns 0 or 1; BatchGetItem API: returns up to 100 values; Query; Scan (reading entire table); PartiQL; PutItem API, UpdateItem API, DeleteItem API, BatchWriteItem API, PartiQL
- transaction opterations
    - for ACID compliance: TransactGetItems API, TransactWriteItems API, PartiQL

## Amazon DynamoDB
### Reading and Writing to DynamoDB from the Console
- CRUD: create, replace, update, delete 
### Writing to DynamoDB From Code
- e.g., writing from lambda
### Querying and Scanning DynamoDB From Code
- query: if sort + partition key are known
    - highly recommended to be used as table scales 
- scan: slow & expensive, best to be avoided 
### DynamoDB Performance Considerations 
- will lots of data be written?
- will write operations occur infrequently, or will data be read in constant & ongoing state?
- are there records in other tables that need to be related? 
- Read & Write Capacity Units (manageable with provisioned mode)
    - RCUs: the number of strongly consistent reads per second, or eventually consistent reads per second, for an item up to 4KB in size
        - items larger than 4KB need add'l RCUs
        - DDB will show average item size for items in DDB
    - WCUs: the number of write requests per second for an item up to 1KB in size
        - chunks over 4KB will need add'l capacity units 
    - choose appropriate number of RCUs/WCUs based on average item size 
- Queries
    - used to retrieve one or more items from a table or a secondary index; specifies the partition key and the sort key (if there is one)
    - efficient b/c of use of partition & sort keys to specify what to return
- Scans
    - reads _every_ item on the table or index and returns data attributes for items that match filter expression
    - only use scan operation when query operation can't be used
- DDB Indexing
    - Global Secondary Index (GSI): index w partition key + sort key that can differ from those on the base table 
    - Local Secondary Index (LSI): index w same partition key as table, but different sort key 
### Amazon DynamoDB Backup Capabilities
- automatic
    - PITR (point-in-time recovery): don't need to set backup retition period or backup time period
        - either enabled or disabled
        - retention period: 35 days 
            - DDB will be able to be restored for 35 days after deleting
- manual (on-demand backups)
    - exist until manually deleted; especially useful for compliance
    - no performance impact against DDB during backup
    - every time an on-demand backup is taken, the ENTIRE table is backed up (NOT incremental)
### Restoring an Amazon DynamoDB Database
- during restore, have the option to change some configuration settings
    - restoring w or w/o secondary indexes
    - restoring to different region
    - encrypting db using KMS key

## Creating DynamoDB Tables and Indices
### DynamoDB Table Access Provisioning
- access provisions should be controlled per table, or even items in tables to enforce least priviledge 
- for condition, if using `dynamodb:LeadingKeys` (for defining which application users can access the table) the part after condition must be `"ForAllValues:StringEquals":`
### Modeling a DynamoDB Table
- data storage: items and attributes
- schemas: dynamic
- querying: item collections 
- requires a primary key that must be defined up front & unique per item on table
    - all other attributes can be duplicates 
- DDB Data Model
    - table w items as rows and attributes as columns
    - all attributes do not need to be defined 
- primary key: partition key + sort key (either partition OR sort key must be unique)
- global secondary index: allows for alternate partition and sort key
    - can be created any time
    - requires its own throughput capacity
    - eventually consistent only
    - max 20 per table
- local secondary index (less commonly used)
    - defined during table creation
    - only allows for alternate sort key
    - uses existing throughput of ddb table
    - allows for strong consistency
    - max 5 per table 
    - if LSI is used along with primary key, the partition key must be the unique one
        - i.e., if the table is for songs/artists, if partition key is artist & sort key is song number, that fulfills the requirements of the primary key. However, if an LSI is added for 'album' - album + artist isn't unique enough. GSI would have to be used, and sort on album and song number 
### Data Modeling Before Table Creation Is Essential
- consider data set and access patterns before creating table  
    - identify if global or local sort keys are needed 
- use NoSQL workbench for DDB
    - client-side app for managing NoSQL DBs
### Create a DynamoDB Table using the AWS Console
- simplest way to create 
- most common way, esp using a script to leverage the CLI or SDKs 
- have to deffine table name, partition key and sort key + define the data type for the keys 
- class options: standard access, standard-IA 
- DDB tables always encrypted 
- creating global secondary index effectively creates another table, which also requires defining capacity (RCU/WCUs) for the table
    - can create or delete GSI at any time 
        - can be helpful when rare queries are needed, to create a GSI, then delete after done w the query 
- when adding an item, can also define add'l data 
- provides more reliable and efficient results, especially when dealing with large sets of data 

## Working with Large Tables in DynamoDB
### Introduction to Partitioning
- behind the scenes, DDB segments data into partitions 
- primary key is called a partition key b/c it helps DDB decide which partition to put data in 
    - aka 'hash key'
- compound primary key (partition key + sort key)
    - physically stores the items near each other in the partition 
- each partition is ~10 GB of data
- new partition is added when partition is >10GB or RCUs goes over 3k, or WCU over 1k
    - this is all invisible to the customer, and DDB does some balancing behind the scenes 
### Balancing Partitions in Large Tables
- high cardinality (many unique values)
- low cardinality (few unique values)
- WCU/RCU for DDB are split evenly b/w all partitions
    - if one partition is receiving more read/write capacity it is called "hot partition"
        - may get ProvisionedThroughputExceeded if the hot partition keeps reading too much & throttles 
- the goal is to have many smaller partitions so that queries are balanced across the nodes
    - split data so read/write traffic is evenly split across system
    - DDB does a few things to mitigate this
        - burst capacity: allows greater throughput for the hot partition for a period of time
        - adaptive capacity: enabled the hot partition to consume more throughput permanently 
    - structural changes to ease the burden 
        - DAX to cache reads 
        - good partition key strategy 

## Amazon RDS
### Amazon Relational Database Service
- provision, create, and scale databases
- DB types 
    - sql: best open source SQL DB
    - mariaDB
    - postgresSQL: second best open-source
    - amazon aurora
    - oracle 
    - SQL server (w licensing options)
- instance types
    - general purpose, memory optimized 
- multi-az
    - second RDS deployed in same region as primary db
    - failover process managed by AWS (takes 60-120 seconds; depending on size and activity of DB)
    - failover occurs when
        - patching maintence
        - host failure
        - az failure
        - primary instance rebooted
        - db instance class on primary modified 
- scaling RDS
    - storage
        - storage autoscaling
            - everything but amazon aurora support EBS 
            - minimum for gp2 is 20GB, up to 64TB for most, or 16TB for SQL server 
            - provisioned IOPS min storage 100GB, min IOPS 8k, max 80k (40k for SQL server)
            - autoscaling, set a minimum storage of 100GB up to a customer-defined limit
        - aurora scaling occurs automatically
    - compute scaling
        - vertical scaling (bigger)
            - can choose immediate or wait for update window 
        - horizontal scaling (more)
            - read replica
                - takes a snapshot of DB, then securely and asyncronously linked to primary db
- automated services
    - patches + backups 
    - considered to be a container service, since no access to underlying infrastructure
    - automatic backups enabled on all new RDS 
    - manual backups create snapshots that can only be deleted manually 
    - backtrack can be enabled to step back the aurora db up to 72 hours 
### RDS Backup Capabilities
- automatic backups of instance
    - performed daily
    - retention period of 0-35 days
        - if set to 0, backups will not occur
    - if DB created w CLI, default retention period is 1 day. Creating w console supplies default 7 day backup period 
    - can define specifically when to backup instance
        - if not defined, AWS will pick a 30 minute window in an 8 hour period that varies based on region
    - during first few second of auto backup process, there's a small IO penalty 
    - make sure backup window and maintenance window do not overlap
- manual backup w snapshots
    - no point in time recovery, can only backup to the specific time the backup was made 
    - not restricted by expiration periods 
- AWS Backup service to create backup of RDS DB
    - Considered a manual backup by RDS
    - create backup policies/backup plans to perform backups 
    - supports all db engines 
- when deleting DB, can choose to make final snapshot, but will only last as long as retention period 
### Restoring an RDS Database 
- RDS backups transaction logs to S3 every 5 minutes. Point in time recovery can restore to those 5 minute intervals (for automatic backups)
- for manual backups, can only restore to the time the snapshot was taken, not to a point in time 
    - can restore to a new storage volume type, but will take longer than restoring to the same storage volume 
### Copying & Sharing RDS Snapshots
- can copy automated or manual snapshots w/n same region or other regions
    - when copying b/w regions, ensure target region supports cross-region snapshot copies 
- can copy snapshots across AWS accounts
- if source is automated snapshot, target snapshot will be classed as manual snapshot
- option and parameter groups NOT copied across regions 
- can share publicly or privately 
- encrypted snapshots
    - if taken from encrypted DB, snapshot will be encrypted
    - if copied to same region, can use same KMS key
    - if copied to different region, must use a KMS key for the target region
    - when copying, can choose to encrypt an unecrypted snapshot, then create db from the encrypted snapshot 
    - can't share encrypted snapshot w public option 

## When to Use RDS Multi-AZ & Read Replicas
### RDS Multi AZ
- used to help with resilience and business continuity
- configures a secondary RDS instances w/n different AZ in the same region as primary instance
- purpose is to provide failover option for primary RDS instance 
- data replication happens synchronously 
- uses failover mechanism on Oracle, MySQL, MariaDB, and PostgreSQL
    - takes 60-120 seconds for DNS record to update 
    - occurs automatically 
    - occurs in the following scenarios affecting the primary instance
        - patching maintenance
        - host failure
        - AZ failure
        - instance rebooted w failover
        - db instance class modified 
    - RDS failover triggers an event (RDS-EVENT-0025) that can notify SNS to let customer know about failvoer
- SQL Server Mirroring (Multi-AZ for SQL Server)
    - supported on SQL server 2008 R2, 2012, 2014, 2016, 2017; standard and enterprise 
    - provisions secondary RDS instance in separate AZ to help w resilience and fault tolerance
    - both primary and secondary instances in SQL Server mirroring use the same endpoint 
    - must have env configured correctly
        - DB subnet group must be config'd w min of 2 different AZs
        - specify which AZ the mirrored instance will reside in
        - can check which AZ mirror is in w CLI 
- Aurora
    - fault tolerant by default
    - cluster replicates the data across different instances in different AZs
    - can automatically provision and launch new primary instance; can take up to 10 minutes
    - multi-AZ on aurora cluster allows RDS to provision replica w/n different AZ automatically 
        - should failure occure, replica instance is promoted to new primary instance w/o waiting 10 minutes for HA + resiliency
    - can create up to 15 replicas if required, each w different priority 
### Read Replicas
- not use for resiliency for failover
- used to serve read-only traffic for DB, to help performance 
- to create
    - snapshot is taken from db
    - once snapshot complete, RR instance created
    - RR maintains secure asynchronous link b/w itself and primary DB
- can deploy more than one read replica for primary DB
- adding more replicas allows scaling of read performance
- able to deploy in different regions
- can promote read replica to replace primary DB 
- mysql 
    - must have backup retention period greater than 0
    - only v 5.6 for nesting
    - only possible when using InnoDB
    - possible to have nested read replica chains. Can only be 4 layers deep
    - can only have 5 read replicas per db, although each of the nested ones can also count as a DB
- mariaDB
    - must have backup retention period greater than 0, same nesting rules apply
    - any regions supported 
- postgreSQL 
    - must have backup retention period greater than 0
    - must run 9.3.5 or later for RR
    - native PostgreSQL streaming replication used to handle replication & creation of read replica
    - connection b/w master and RR repliaces data asynchronously b/w the two instances 
    - a role is used to manage replication when using PostgreSQL 
    - can create multi-az RR instance
    - does not allow nested RR 

## Amazon Redshift
### Amazon Redshift
- fast, fully-managed, petabyte-scale data warehouse that uses standard SQL
- acts as RDB management service 
- data warehouse: consolidates data from multiple sources to consolidate data 
- Extraction: retrieves data & moves to staging area
- Transformation: preparing data to be more easily consumed 
- Loading: inserting the transformed data into a storage medium 
- Amazon Redshift Cluster
    - core component of redshift service
    - runs redshift engine, which contains a DB
    - grouping of compute nodes; must have at least one
        - RA3 or dense compute nodes 
        - if there is more than one node, a leader node will also be created 
            - leader node coordinates compute nodes and external apps; essentially a gateway for BI apps using OBDC or JIDC
        - each compute node is split into 'node slices'
            - each node slice works on operations sent by the leader node 
- performance features
    - massively parallel processing (MPP): leader node can distribute plans across multiple compute nodes at once
    - columnar data storage: reduce # of times DB has to perform disk I/O
    - result caching: reduce time it takes to perform queries by storing some queries in leader node 
- integrates w CW: cpu utilization, throughput, query/load performance
- during creation, can choose up to 10 IAM roles to associate w cluster to allow access to other services 

## Amazon DocumentDB
### Amazon DocumentDB (With MongoDB Compatibility)
- runs in VPC
- non-relational fully managed service
- Highly scalable, fast, HA
- store json-like documents and query + index them 
- fully compatible w MongoDB database, which can migrate to AWS w AWS (DMS) Database Migration Service
- can scale storage and compute separately 
    -  will automatically increase storage by 10G each time if running low, up to 64TB
- architecture
    - composed of cluster, composed of up to 16 DB instances
    - shared cluster storage volume across all clusters 
    - one primary DB instance performs write operations; the others (if configured) are RR and only serve read requests
        - can process a high volume of read requests
        - can have 15 read replicas
        - data maintained synchronously b/w primary + replicas 
- connectivity
    - cluster endpoint: points directly to current primary DB instance of cluster
        - should be used by apps that require read + write access to db
        - if primary DB instance files, will point to the new primary instance w/o any changes required
    - reader endpoint
        - used to connect to read replicas 
        - allows apps to access db for read requests
        - a single reader endpoint exists, even if there are multiple RRs
    - instance endpoint
        - every instance w/n cluster will also have a unique instance endpoint
- backups
    - performs auto backups based on settings from creation of DB 
        - backups occur daily, and backup retention period is 0-35 days 
            - 0 day backup disables backups + PITR
        - timing of backup can be defined by customer 
    - supports point-in-time recovery
        - captures transaction logs when DB changes are made 
### Demo: Creating DocumentDB Cluster

## High Availability with Amazon Aurora
### Amazon Aurora HA Options
- db service w superior MySQL + PostgreSQL engine compliance
- separates compute + storage from each other
    - able to dial up and down available of data
    - RR can easily be introduced and removed
- compute layer can be provisioned in several configurations
    - implemented using ec2 instances (which don't show in console)
- storage
    - shared among all compute nodes
    - data stored in 10Gbit blocks, which are copied 6x in three different AZs
    - exposed to compute instances as a single volume 
- data management RDS vs aurora
    - RDS: data needs to be replicated from the master to each of its replicas 
    - Aurora: no need for replication, since it uses & shares single logical volume 
- data consistency
    - uses a quorum and gossip protocol baked w/n storage layer to ensure data remains consistence
    - reads require quorum of three and writes a quorum of four
    - peer to peer gossip protocol used to ensure data copied across each of 6 nodes 
    - provides 6-way replicated storage across 3 AZs
    - only supported in regions w 3+ AZs
    - provides auto + manual failover of the master which takes approx 30 seconds 
        - in event of failover, Aurora will either launch replacement master or promote a read replica 
- connection endpoints
    - created by Aurora to allow connection to cluster 
    - cluster endpoint: points to current master DB instance. Allows app to perform read + write
    - reader endpoint: load balances read requests across cluster
    - custom endpoint: casn be used to group instances based on instance size or parameter group
        - can dedicate custom endpoint for specific role or task w/n org
    - instance endpoint: maps directly to a cluster instance. Used for fine-grained control over instances
    - general points
        - read intensive workloads should connect via reader endpoint 
        - reader + custom connection endpoints designed to load balance connections across their members
        - connection endpoint load balancing is implemnted internally using R53 DNS
        - be careful in the client layer to not cache the connection endpoint lookups longer than their specified TTLs
        - connection endpoints mostly applicable and used in single master w multiple RR setups 
### Aurora Single Master - Multiple Read Replicas
- can have up to 15 read replicas
- replicas are asynchronous & done in ms
- RR can be deployed in different AZs w/n VPCs or cross region replicas
- RR able to increase read throughput
- if master goes down, any reader can be promoted to master
    - each replica can be tagged w label indicating priority of promotion
- this type of cluster supports being stopped and started manually in its entirety
    - when stopped or started, all underlying compute instances are either stopped or started
    - if cluster remains stopped for up to 7 days, it will automatically restart 
- daily backup automatically performed, w 1-35 day retention period 
    - can specify back-up window
    - can perform on-demand manual snapshots, which are stored indefinitely until manually deleted 
### Aurora Multi Master
- configure pair of masters in active active configuration
- max of four masters
- can read/write to any of the master instances 
- if instance outage occurs in an AZ, all db writes are redirected to remaining active instance w/o need to perform failover 
- CANNOT add read replicas 
- incoming DB connections are not load balanced by the service
    - load balancing connection logic must be implemented and performed w/n client 

## Aurora Serverless
### Aurora Serverless
- autoscales compute layer based on demand 
- best for variable workloads, or those with low usage
- configure upper and lower limits for capacities
    - defined with ACUs - Aurora Capacity Units 
- HA: underpinned by the same fault tolerant self-healing storage layer; nothing to configure 
- can entirely shut down compute if there's no demand 
- configured w single connection endpoint that's used for read + writes 
- web service data API feature
    - optional feature that enables http endpoint for DB, without needing to connecting with standard SQL programs 
    - makes implmenting lambda functions to perform data lookups/mutations to make queries easier
- performs continuous automatic backup, default 1 day, up to 35
    - allows PITR
    - restores performed to new serverless db cluster 

## Aurora Serverless v2
- provides instant on-demand scaling to support spikes in demand (says it can save 90% on capacity)
- offers compatibility w MySQL and PostgreSQL w/o need to provision or manage infrastructure
- performance
    - scale up & down based on demand. v2 can scale in ms, vs seconds in v1
    - can scale down in <1 minute, more granularity in scaling up (in .5 ACU increments)
        - v1 takes longer to scale down, and scale up was only done by doubling ACUs
    - can scale while transactions in process (v1 unable to do that)
    - supports features found in provisioned Aurora, including RDS proxy, global dbs, and RR (can be spread across multi-az deployment for HA)
    - can mix v2 and provisioned aurora instances in the same cluster
    - not necessarily a replacement for v1
    - can upgrading v1 to v2 by restoring snapshot to v2 

## Amazon ElastiCache
### Amazon ElastiCache
- deploy in-memory data stores in the cloud 
- overview of in-memory caching
    - used to increase read-only performance
    - store commonly stored info w/o having to read from RDS
    - instead of vertically scaling DB, can add in-memory caching to decrease the need to scale up on persistent data store
- engines
    - memcached
        - high performance, sub-ms latency in-memory, key-value store service that can either be used as a cache or a data store
        - suits workloads where they are fairly consistent 
        - simple & performant 
    - redis
        - in-memory data store designed for high performance. provides sub-ms latency on huge scale to real-time apps 
        - generally provides more robust features compared to memcached
        - has an option to enable cluster mode
            - w cluster mode enabled, each cluster can have 90 shards. w/o, can only have 1 shard
- elasticache nodes 
    - fixed size, chunk of secure, network-attached RAM
- redis shard (node group)
    - group of up to 6 EC nodes 
- redis cluster
    - group of 1-90 redis shards
- memcached cluster
    - cluster of one or more nodes 
- common use cases 
    - online gaming (statistical information)
    - social network (session info)
    - real-time analytics (ads & recommendations)
- should not be used when data persistence is necessary, working w primary records, or write performance needed 

## Amazon MemoryDB for Redis
- fully-managed, in-memory, redis-compatible data store
- designed for ultra-fast low-latency access to data store w microsecond read and single-digit millisecond write latencies
- deployed as a cluter serving a dataset that is partitioned into shards
    - each shard has a primary node and up to 5 read replica nodes 
        - nodes can be spread across AZs for HA 
- clusters may be up to 500 nodes
- supports data storage up to 100 TB 
- transaction logs are distributed across AZs to ensure data is durable, consistent, and quickly recoverable
- data tiering allows moving less-freqently accessed data to disk
- supports encryption in transit and at rest 
- snapshots for easy backup & restore of cluster 

## Which DB Service Should I use
### Choosing a Relational DB on AWS
- highly structured data, relationships b/w data needed, database enforcement of relationships, ACID compliance - use cases of RDB
- unmanaged db vs managed db 
    - managed: RDS vs Redshift
        - redshift: OLAP use cases, fast query time for petabyte-scale data. Best when data is well understood. Charged for uptime, not per query
        - RDS: OLTP use cases
            - engine choice considerations: skill levels, dev preference, framework (i.e. postgresql popular among python devs), existing tech
            - RDS custom: runs either oracle or SQL server instances, can have host-level access, while AWS manages setup, operation, scaling 
            - aurora: best for massive scale w consistent traffic 
                - serverless: can turn off when not being used 
### Choosing a Non-Relational DB on AWS 
- flexible data storage, growth & scale beyond vertical scale, document/graph/ledger db needed 
- NoSQL db services (DynamoDB, DocumentDB, Amazon Keyspaces for Apache Cassandra)
    - cassandra not ACID transaction compliant
    - DocumentDB: max data modeling flexibility. optimized for storing data in JSON format. Good for read-heavy workloads + rich data
    - DynamoDB: low latency at massive scale, infinitely scalable & provides single-digit low latency. Better for more defined workloads & access patterns
        - most mature noSQL db service in AWS 
        - access data w key-value format 
    - keyspaces mostly used when cassandra workload is needed 
- in-memory db (if a caching layer is needed)
    - dynamoDB accelerator (DAX): best option for caching layer for DDB 
        - not beneificial if requests require strong consistency or transactions 
        - lowers latency from milliseconds to microseconds if app can tolerate eventual consistency 
    - elasticache: if using any other db, use for caching 
        - memcached: simple caching w key-value lookups
            - use case doesn't require persistence, lists or sets, pub/sub, replication, or transactions
        - redis: if persistence, lists or sets, pub/sub, replication, or transactions are required
            - memorydb for redis provides a fully-managed redis cluster w much higher durability than EC
            - common on online games, machine learning, analytics 
- amazon neptune (graph db)
    - can make queries based on starting point
    - best when the relationship of the data is as important as the data itself (i.e. social media networks, recommendation engines)
    - stores data across 6 nodes in 3 AZs & supports 15 RRs 
- amazon timestream
    - collect, store, and process time series data at any scale (often useful in IOT scenarios (i.e. tracking stock price over time))
    - separates ingestion, storage, and query layers, enabling them to scale independently
    - ingestion layer uses timestamp to write data at nanosecond granularity
    - storage layer consists of in-memory for recent data, and magnetic store for older data 
- amazon quantum ledger database (QLDB)
    - provides that any entry has not been modified after the fact 
    - immutable and append-only
    - uses partiQL which supports SQL-compatible access 

## Database Migration Service
- managed service that runs in AWS, running on an ec2 that customer can configure
- connects to source db, reads the data, formats data for consumption by target db, then loads data into target db
- can import from commercial and open-source db sources 
    - check aws website for latest supported dbs
- supports homogenous (same to same) and heterogeneous (b/w different db engines) migrations 
- what does it do? 
    - manages data b/w one service and another
    - does not manage the migration of the schema; the target db must be created first for DMS to work
    - may use aws db schema conversion tool to facilitate the migration of the entire system
    - AWS DB schema conversion tool is an app that is downloaded, installed, and ran on local machine. Works nicely w DMS, and needs to be run before DMS 
        - new schema only required when heterogeneous migration is needed 
        - if migrating same db to same db, can export db schema w native db tools 
- why use DMS: modernization, reduce license fees, proof of concept 

## Best Practices 
- data classification
    - all data is not equal; e.g. credit card processing vs click stream processing 
    - create as many levels of control and access as needed 
    - keep it simple & easy to understand, should be able to explain data classifications w just a few sentences
    - perform risk assessment of data
    - re-evaluate data on a regular basis 
- encryption at rest and in transit
    - encryption usually a click away at creation
    - RDS has transparent data protection for some engines 
    - comms b/w app & rds should be encrypted 
    - DDB has encryption by default. encrypts attribute values for each item in table using unique encrypted key 
- protect data by limiting attack surface 
    - layered networks, allowing the minimum amount of traffic to the next layer 
- WAF for SQL injection protections (SQL injection makes up 2/3 of all attacks against apps)
    - control what types of traffic are allowed into app 
- MFA for avoiding accidental or malicious deletion 
    - i.e. MFA delete 
- working w least privilege 
    - only able to change or modify what is necessary 
    - use roles more frequently when working w data 
        - it's challenging to accidentally assume a role in the console 
- GuardDuty
    - ML security service that monitors logs and looks for threats 


DMS Challenge
I kept getting the error `Test Endpoint failed: Application-Status: 1020912, Application-Message: Cannot connect to ODBC provider Network error has occurred, Application-Detailed-Message: RetCode: SQL_ERROR SqlState: 08001 NativeError: 101 Message: [unixODBC]timeout expired` on the target endpoint. tried making new endpoint, tried endpoint and instance endpoint urls, no change. idk. gave up 


# Networking and Content Delivery
## VPC Fundamentals
### What is a VPC
- 5 VPCs per region per account 
- isolated segment of AWS cloud for personal use 
- must have a name and CIDR address (/16 through /28)
### Subnets
- split vpc into separate networks 
- public subnet: accessible from the internet 
    - have to add IGW & route on RT to IGW; only one RT per subnet 
- private subnet: inaccessible from the internet 
- reserved IP addresses in each subnet 
    - .0: network
    - .1: AWS routing
    - .2: AWS DNS
    - .3: AWS Future
    - .255: broadcast 

## VPC Security and Control
### NACLs
- as soon as traffic matches a rule, that rule is applied 
- works at subnet level 
### Security Groups 
### NAT Gateway
- lives in public subnet, only accepts outbound traffic from private subnets when route tables are updated appropriately 
### VPC Endpoints
- access AWS services using AWS network
- interface endpoints
    - ENIs w/n subnet for apps 
    - service it's associated w cannot connect to the VPC; instance must connect to service 
- gateway endpoints
    - connects to s3 or DDB 
    - can update route tables in VPC at creation 
    - only works w ipv4 
### VPN & Direct Connect
- VPN connection
    - create Virtual Private Gateway on VPC
    - customer gateway on datacenter dside 
    - iniate tunnel b/w endpoints; can only be established from customer gateway side 
    - update routes on route table w destination as the VGW
    - if CGW supports BGP (border gateway protocol), multi routing (?) is available 
- direct connect 
    - uses private infrastructure to connect directly to VPC 
    - router established in datacenter
    - customer- and aws-side routers in an intermediary direct connect location 
    - able to connect to AWS region 
    - private virtual interface connects from DC to customer-side router, then to AWS router, then to VGW
    - second interface is a public virtual interface which connects similarly, although can connect to public AWS resources 
    - speeds from 1 Gbps to 10 Gbps

## What is AWS PrivateLink
- involves service providers and service consumers 
- AWS capability enabling AWS-based service providers to create and offer endpoint services to their consumers privately and securely using the AWS global network 
- use cases
    - allows customers to access services provided by PL service providers w/o requiring public internet connectivity
        - only consumer can initiate connection
    - a means to maintain regulatory compliance by preventing sensitive data from traversing the public internet
    - allows on-prem resources ability to connect to AWS service endpoint over an AWS Direct Connect or VPN connection 

## Connecting Networks w AWS Transit Gateway
- VPC peering: secure & painless method of connecting VPCs. Falls apart when trying to communicate multiple vpcs to each other 
- network transit hub/regional router 
- can add direct connect b/w TG & on-prem
- basics
    - managed service; HA, on-demand scalability
    - regional service 
    - has associated route table; can have multiple RTs 
    - types of attachments (can attach multiple)
        - VPCs
        - VPN connections
        - AWS Direct Connect Gateways
        - AWS Transit Gateway Connect Attachments
        - AWS Transit Gateway Peering Connections 
- connecting w TGW 
    - can work in different regions, but there is another step
    - create connection points in VPC & define what AZ they're defined in. ENI created & requires a single IP address
        - ENI only allows traffic from the AZ (and subnets w/n that AZ) to communicate to the TGW. If multiple AZs needed, multiple ENIs required 
    - gotchas 
        - TGW does not support DNS resolution for custom DNS names of attached VPCs set up using private hosted zones in Route53
        - cannot create an attachment for a VPC subnet that resides in an AWS local Zone 
- routing traffic to TGW
    - update VPC routing table. add 10.0.0.0/8 to point to TGW 
    - TGW has a default route table; starts as empty
    - tell RT which CIDR blocks correlate to which VPCs 
    - cannot connect VPCs w same CIDR range 
- adding onsite VPN link
    - create VPN attachment w/n TGW
    - select on-prem CGW (or create new one)
        - if creating new CGW, will require static public IP address & BGP ASN
    - choose static or dynamic routing 
        - if gateway device supports BGP, use dynamic routing. Otherwise, use static 
    - add route for CGW to TGW RT 
- steps to create AWS direct connection 
    - setup AWS direct connection via one of AWS Direct Connect delivery partner
    - create new Direct Connect Gateway w/n Direct Connect 
    - Create a Transit Viretual Interface (VIF) w/n direct connect console 
        - VIF: VLAN that transports traffic from direct connect gateway to TGW 
    - associate Transit VIF w TGW 
- if only wanting partial connectivity (not allowing all to all)
    - create multiple route tables, e.g. one that sends 0.0.0.0/0 to the VPN, and one that only manages internal traffic
    - can create very unique network topology with multiple RTs 
- steps to create onsite VPN link
    - check for most specific route
    - check for static route entries (prefers static over dynamic)
    - check VPC  propagated routes
    - check BGP propagated routes from DCGW
    - check BPG propagated routes from AWS site-to-site VPN 
- connecting to VPCs & attachment in different regions 
    - TGW peering connections
        - allows creation between different transit gateways; can't directly attach to VPC in another region 
    - steps to create TGW peering attachment
        - create peering attachment on TGW
        - specify another TGW w/n different AWS region
        - request to peer is sent to other TGW
        - acceptor TGW accepts request
        - add static route to RT that points to TGW peering attachment 
    - recommended to use unique ASNs for peered TGWs to take advantage of future route propagation capabilities 
    - does not support resolving public IPv4 addresses to private IPv4 addresses 
- AWS TGW connect 
    - allows extending SD-WAN into cloud w/o setting up IPSEC VPNs b/w network and TGW
    - supports GRE (generic routing e)
    - supports BGP 
    - TGW connect is a new attachment, but uses existing VPC or direct connect attachment for third-party appliance to connect to 
- limits
    - 5k TGW attachments 
    - 1.25Gbps per VPN tunnel (each connection has 2 VPN tunnels)
    - max bandwidth is 50Gbps per VPC (at burst load) per VPC/DCGW/peered TGW connection 
    - max number of TGWs is 5 per region per account (if hitting this limit, should think about splitting into multiple accounts)
    - 5 TGW attachments per VPC

## VPC Sharing Using the AWS Resource Access Manager
### Introducing VPC Sharing
- centralizing management & creation of VPCs leads to more secure networks (requires AWS organizations)
- actually sharing subnets in VPCs and VPC-level resources
- have VPC owner: account that created VPC & shares w other 
    - responsible for VPC-level resources 
        - subnets, RTs, NACLs, VPC peering connections, IGWs, NAT Gateways, TGWs, VPGWs, VPC endpoints/endpoint services, enabling VPC flow logs for VPC/subnets
- participants are responsible for EC2/RDS, SGs, ENI-specific flow logs 
- best practice
    - create dedicated networking AWS account
- use cases
    - cost optimization 
    - network segmentation
        - using different VPCs for different compute environments (dev/prod/security)
        - w VPC sharing, can have fewer VPCs, and share the different VPCs for the different AWS accounts 
### Introducing Resources Access Manager (RAM)
- used to work w VPC sharing, allows sharing of AWS resources from a centralized account 
    - able to share Aurora DB clusters, dedicated hosts, resource groups, VPC subnets 
    - must first enable sharing through RAM console or CLI 
        - create resource share; define name of share & list of resources to share. Then assign permissions that principals are allowed. Can share w all accounts in OU and any additional ones added. 
### Capabilities of VPC Sharing
- limitations
    - VPC owners can only share VPCs w accounts in its own AWS organization
    - default VPC in each region cannot be shared 
    - VPC sharing participants cannot launch resources using default VPC security group or security groups created by other participants; must use their own SGs 
    - VPC sharing participants can create ALBs + NLBs & can register targets they deployed to shared subnets
    - only VPC owner can deploy gateway load balancers to shared SNs 
- each partitipant pays only for the resources they deploy and data transfer 
- owner of VPC pays transfer costs for NAT gateway, gateways, and endpoint service
- VPC owner can unshare VPC at any time. participants can't add new resources, but can modify existing resources & existing resources remain
    - VPC owner can't delete subnet until everything out of it 

## DNS & Content Delivery on AWS
### Working w Amazon CloudFront
- main role is caching of content to be closer to user 
- allows customers to distribute content with low latency and high speed 
- works with static (s3) and dynamic (ec2, lambda) content 
- first must create a distribution, then edge locations for the caching
    - define protocols, ports, TTLs, custom headers, price class, and lots more
    - when creating, get assigned an automatic domain name, which is then mapped w DNS to a user-friendly address. Can define custom origin name
- three caching layers
    - edge locations (300+)
    - regional edge caches
    - AWS origin shield (not enabled by default)
        - causes multiple cache requests to be consolidated to one query against content 
- with more caches, more content is served by cache 
### Amazon CloudFront Patterns
- using CFt to cache when ALB is the origin
    - CFt works w any public endpoint - AWS or external
    - if ALB is public facing, it is still possible to contact ALB w/o using CFt 
        - customer headers can make it so that ALB only allows requests with specific headers that come from CFt 
        - it is important to rotate the custom header for the LB 
            - add a second header in CFt distribution, add a rule for the new header in LB, then remove old rule and old header 
- use CFt when s3 is origin 
    - by default, s3 static hosting only supports http
    - can force https in front of s3 w CFt. need a certificate from ACM 
        - CFt works w ACM in the north viriginia region; requests must be made here 
    - use Origin Access Identity and S3 bucket policies to prevent direct access to s3 
        - associate OAI w CFt distribution 
### Using Amazon Route 53 - Introduction
- allows for domain name registration, dns & traffic management
- uses edge locations 
- 100% SLA from AWS 
### Amazon Route 53 and DNS Records
- AWS domain name management service 
- public hosted zone: defines how traffic is routed on the internet
- private hosted zone: defines how traffic is routed in the VPC
    - VPC resources must have DNS hostname and DNS support enabled 
- records
    - NS (name server)
        - creates four records in each hosted zone
        - identifies DNS servers for given hosted zone
    - SOA (start of authority)
        - define authoritative DNS service for a given zone 
    - supported records: A (IPv4), AAAA (IPv6), MX (mail exchange), TXT (text record), CNAME (canonical name; map hostname to hostname)
    - Alias record is unique to R53; maps custom name to AWS resource 
    - apex record: top level name 
- TTL: amount of time record is considered valid 
- routing policy: defines how to answer DNS query
### Amazon Route 53 Health Checks
- independent resources that can be used when creating a record
- sends info to endpoint every 30 seconds to determine if healthy or not; can be selected to be every 10 seconds 
- can verify tiers of application before determining if app is healthy 
- can monitor state of CW alarm 
- if health check not associated with a record, R53 treats those records as always healthy 
- w HTTP endpoint health check, can define a string to look for to make sure the response is healthy 
### Amazon Route 53 Routing Policies
- routing policy for record that defines how to answer DNS query
- simple: provides IP address associated w a name 
    - do not support health checks (all other routing policies do)
- weighted routing: can define weight per ip address; assign value to prefer IP address over another
    - 0 weight means to not route to it 
- geolocation: tags records w location that can be Default, Continent, or Country
    - allows distribution of the IP of a resource that can cater to customers in different countries/languages
    - ip check verifies customer's location & corresponding location record is returned 
- geoproximity
    - requires using r53 traffic flow feature & create traffic policy
    - tagged w AWS region or using coordinates
    - based on distance and a defined bias (from -99 to 99)
        - can route more traffic to endpoint by using positive value
        - route less traffic to endpoint by using negative value 
- failover
    - route traffic to primary resource
    - based on health check, can redirect to secondary resource
    - define primary and secondary records, also need health check defined 
- latency: choose record w lowest latency to customer
    - create records w same name & assign to regions
    - lowest recorded latency & healthy is chosen; not necessarily closest
- multivalue answer
    - can answer up to 8 IP address corresponding to health checks
    - if less than 8 records are available, returns all healthy hosts 
### Amazon Route 53 Traffic Flow
- simplified maintaining and creating records in large operations (e.g. fleet of web servers for same domain)
- able to use a visual editor to combine multiple routing policies and health checks in a single configuration
- traffic policy versions
    - old versions remain
    - can define hundreds of records
- policy records 
    - can be used to create multiple records in separate hosted zones
- note: geoproximity only available if traffic flow is used 
### Amazon Route 53 Resolver
- DNS server for VPCs that integrates with data center using DX or VPN connection
- create inbound and outbound endpoints in VPCs
    - inbound queries help queries from data center resolve to r53 resolver
    rules trigger when a query is made to data center domain & how it responds 
- r53 resolver dns firewall
    - use firewall rule group to identify how the firewall inspects traffic flowing out of VPC
    - to begin filtering, associate the rule group to the VPCs to protect 
### Application Recovery Controller
- feature that continuously monitors an app's ability to recover from failure
- readiness check 
    - monitor aws resource configuration (capacity & networking routing)
    - can check health for ASGs, EC2, EBS, ELBs, RDS, DDB tables 
    - ensure readiness environment is scaled and configured in case of failure
    - before failure happens 
        - check AWS service limits; ensure enough capacity can be deployed
        - verify if capacity and scaling setups for apps are the same across regions 
- routing control 
    - works along side readiness checks 
    - can manually force failover
- safety rules
    - can prevent failover to unprepared replicas 
- control panel: group of routing controls for a specific app 

## Amazon API Gateway
### Introcution to API Gateway
- build, publish, monitor, maintain, secure APIs in AWS 
- supports web app, serverless, containers
- serverless & able to monitor 100ks of requests 
- endpoint types
    - edge-optimized API endpoint
        - best for many geographically distinct and distributed clients
        - brings API closer to clients and reduces TLS overhead
        - good for mobile, web, IoT apps 
    - regional API endpoint 
        - when planning to use own CDN (not cloudfront)
        - works well when expecting all API calls to become w/n a specific region
    - private API endpoint
        - can only be accessed from w/n VPC through interface VPC endpoint
        - internal APIs like microservices or internal apps 
        - get a lot of control of networking space for security
- supported protocols 
    - HTTP (REST) Endpoints
        - REST API (older)
            - meant to deal w all aspects of API lifecycle
            - ideal for all-inclusive set of features needed to build, manage, and publish APIs
        - HTTP API
            - ideal for proxying APIs for lambda or HTTP endpoint, building modern APIs w OIDC & OAuth2, and/or workloads that are likely to grow very large APIs for latency-sensitive worklaods 
            - 70% cheaper than REST API
        - serve HTTP requests w HTTP methods (Get, Post, Put Delete)
    - websocket endpoint
        - maintains persistent connection b/w backend & client (duplex communication)
        - good for real-time apps, chat apps, game app streaming, streaming services, mobile
        - requires a good internet connection
        - very use-case specific
- supported back ends 
    - proxy integration
        - pass-through setup where API gateway passes requests to back end w no changes
        - easy setup, good for rapid prototyping
    - direct integration
        - modifies the request as it passes through API gateway & modify response on its way to client
        - decouples API GW from the backend's request and response payloads, headers, status codes
        - make changes & not be locked into backend service's response 
- integration types
    - lambda functions (proxy or direct)
    - http integrations
        - public facing endpoints inside or outside of AWS 
    - mock integration (direct only)
        - create a response w/o backend integration
        - good for testing or placeholder data 
    - AWS service integration (direct only)
        - connects to any AWS service
        - enables users access to AWS services w/o use of IAM
    - VPC link integration (direct only)
    - integrations
        - REST API: lambda functions, HTTP endpoints, mock endpoints, any AWS services, VPC link
        - HTTP API: HTTP endpoints, any AWS services
        - websocket endpoint: lambda functions, HTTP endpoints, any AWS services 
- API Gateway Authorizers 
    - IAM Authorizer
        - uses IAM to create unique credentials to assign to clients 
        - client must have signature version 4 and 'Execute-API' permissions 
        - supported by REST API, HTTP API, WebSocket Endpoint 
    - lambda authorizer
        - to run a custom authorization model, using third-party or legacy authorizer
        - supported by REST API, HTTP API, WebSocket Endpoint 
    - cognito authorizer
        - direct integration to cognito user pools
        - only supported by REST API
    - JWT authorizer
        - use anything that's OAuth2 compliant (can technically use cognito authorizer this way)
        - only supported by HTTP API
- API gateway security
    - deep integrations with WAF to resist malicious attacks 
    - protects from common web exploits like XSS, sql injection 
- API management & usage
    - can set usage plans to repond to API keys distributed to customers, e.g. for premium vs free subscribers 
    - can set quotas and billing for customers
    - can be used for internal APIs & give keys to devs so their power is limited 
- Caching your responses 
    - cost-effective way to decrease cost and increase response to common responses 
    - define TTL; default is 300s. Can set b/w 0 and 3600 seconds 
        - even having a 1 second cache can greatly improve capacity w high demand 
    - limited to REST API 
- metrics & monitoring
    - 7 key dimensions API gateway tracks
        - CacheHitCount
        - CacheMissCount
        - Count (# of API requests in period)
        - IntegrationLatency (delay b/w sending request to backend & receiving response)
        - Latency (b/w gateway and customer)
    - metrics sent every minute 
- more guidance for choosing b/w HTTP and REST APIs
    - REST API
        - not able to use native OIDC/OAuth2
        - can't provide private integration with ALB (can work around by sending request to NLB then to ALB)
        - supports usage plans, API keys, custom domain names
        - only way to modify request or cache
        - for security, supports mutual TLS auth, certs for backend auth, AWS WAF, resource policies
        - monitoring: access logs to CW logs, Amazon Kinesis Data Firehose, execution logs, CW metrics, AWS x-ray
    - HTTP API
        - only supports custom domain names, and only supports TLS 1.2 
        - for security, only supports mutual TLS auth
        - monitoring: access logs to CW logs, CW metrics 
- pricing
    - REST API
        - first 333 million API calls per month $3.50 per million requests, and gets cheaper from there, down to $1.51 permillion requests for 40+ billion requests/mo
    - HTTP API
        - first 300 million API calls/mo, $1 per million requests, and $.90 per million requests after that 
### Advanced API Gateway
- request lifecycle
    - travels through a series of checkpoints to read through requests to make sure they're legit & will be processed well
    - each stop allows reject, modify, update, enhance of request 
    - phase 1: method request: client-side request to access the backend with HTTP verbs (get/put/delete)
        - used for API Authorization, validating the request itself, verify API keys 
    - phase 2: integration request: before backend services receive method request
        - ensures requests are in a form the backend can process 
    - phase 3: integration response
        - modify & change response before client sees it 
        - set up mapping templates for integration response (e.g. translating ddb output to regular JSON)
    - phase 4: method response
        - final moment to standardize outputs and make sure they're reasonable
        - can fail & let client know API had an issue
- security of APIs w API GW
    - DDoS protection w WAF 
        - works directly w API GW when using regional endpoint. Have more control over CFt than w edge-optimized 
        - when using CFt + WAF w API GW, must configure the following settings 
            - configure caching behavior for CFt distros to forward all headers to API GW regional endpoint
            - config CFt to add customer header into its request back to the origin
            - create & add API key into the custom header & config w API GW 
    - edge optimized endpoint: work through Amazon CloudFront, managed by API gateway
    - limiting access with cross-origin resource sharing (CORS)
        - restrict access from specific domains 
            - must implement options pre-flight request 
    - API limits
        - by default, each API can manage 10k requests/second/region/account. It can handle up to 5k requests in a burst in a single ms
        - can set lower throttling per stage and per route 
            - can set limits on specific http verbs 
    - mutual TLS auth
        - enables certificate-based mutual TLS authentication using x.509 certs 
        - to set up
            - create & upload CA public key certificate bundle to API gateway
                - can create keys using ACM private CA service, or OpenSSL 
    - private integration w backend services 
        - e.g. exposing resources in VPC
        - set up VPC endpoint that connects with VPC providing the service. Travels purely through AWS private network
            - can connect to ALB/NLB/AWS Cloud Map
            - if no traffic is sent over VPC link for 60 days, the ENIs attached to it will be disabled 


## Elastic Load Balancing
### What is an ELB
- manage and control the flow of inbound requests destined to a group of targets 
    - targets: ec2, lambda, range of IP addresses, containers 
    - targets can be across different AZs 
- by default, HA, since it's managed 
    - advantage of using ELB is that it's managed by AWS & elastic, so able to scale up and down 
- LB types
    - application: HTTP/HTTPS
        - operates at request level
        - advanced routing, TLS termination, and visibility features target at app architectures
    - network
        - ultra-high performance w low latency
        - operates at connection level, routing traffic to targets w/n VPC
        - handles millions of requests per second 
    - classic
        - for apps built in ec2 classic env 
- ELB components
    - listener: defines how inbound connects are routed to TGs based on ports & protocols set as conditions
        - at least one must be defined
    - target group: group of resources for ELB to route requests to
        - can configure ELB w multiple target groups & each associated w different listener and rules
    - rules: associated to each listener w/n ELB
        - define how an incoming request gets routed to which TG 
    - can contain 1 or more listeners, each listener can contain 1 or more rules, and each rule can contain 1 or more conditions. All conditions in the rule equal a single action 
    - health checks: performed against resources defined w/n TG
        - allow ELB to contact each target using specific protocol to receive response
    - internet-facing ELB: nodes of ELB accessible via internet & can be resolved w public IP address
        - allows ELB to serve incoming requests from the internet & routing traffic to TGs
        - when communicating internally, uses a private IP address
    - internal ELB: only has an internal IP address
        - can only serve requests that originate from w/n your VPC 
    - ELB nodes 
        - required which AZ for ELB to operate in. For each AZ, ELB node will be added to that AZ 
        - must have an ELB node associated to any AZs for which traffic will be routed to
        - used to distribute traffic to TGs
    - cross-zone load balancing
        - when disabled, ELB will only distribute traffic to tagets w/n AZ 
        - when enabled, ELBs will distribute all incoming traffic evenly b/w targets 
### SSL Server Certificates
- when using HTTPS as a listener
- to allow ALB to receive encrypted traffic over HTTPS, will need server certificate & associated security policy
- SSL & TLS are cryptographic protocols. Used interchangeably when discussing certificates on ALB 
- server cert used by ALB is X.509 cert
    - digital ID provisioned by CA like ACM
    - cert used to terminate encrypted connection from client, decrypt request, then forward to resources in ELB TG 
- when selecting HTTPS as listener, will need to select source
    - choose cert from ACM, upload cert to ACM, choose cert from IAM, upload cert to IAM
    - integration w ACM simplifies the certificate process
    - IAM used when deploying ELBs in regions that don't support ACM
### ALBs
- operates at layer 7, application layer (http, ftp, smtp, nfs)
- best for advanced routing + visibility features
- best to set up TGs before ALB 
### NLBs
- operates at layer 4, transport layer; balance requests based on TCP or UDP protocols 
- supported listeners: TLS, TCP, UDP
- able to process millions of requests per seconds 
- only way to have a static IP address attached to a load balancer 
- cross-zone load balancing can be enabled or disabled 
### Using ELB and Auto Scaling Together
- when ELB attached to ASG, ELB automatically detects instances in TG & begins to distribute all traffic to resources in ASG 
### Introduction to Gateway Load Balancer 
- single point of access for all inbound and outbound traffic to AWS VPC. Routes traffic to autoscaled nirtual networking appliances that ensure that traffic IP does not overlap
- enables sticky, transparent, symmetric flow 

## Quiz
- S3 is supported both by interface endpoints and gateway endpoints 
- interface endpoints use PrivateLink to establish a private and secure connection, while Gateway Endpoints are used w/n route tables to reach supported services 
- HTTPS listener options include choose/upload a cert from ACM or IAM
- AWS VPC sharing includes sharing AWS DX connections across accounts 
- best practice in VPC sharing: use a dedicated networking VPC to facilitate VPC sharing 
- API gateway stages include method/integration request/response 
- when a subnet is created, needs a name & CIDR block address 
- must use public virtual interfaces (VIFs) to create AWS-managed VPN connection of DX connection to connect to AWS public endpoints
- Direct Connect Gateway used to connect AWS DX connection to VPCs in remote regions 

# Management and Governance
## Amazon CloudWatch
### What is Amazon CloudWatch
- global service: window into health of apps & infrastructure 
- provides insights & the ability to take action on them
- components
    - dashboards
        - w console or API, build page using visual widgets 
        - can share w users & folks who don't have access to account 
    - metrics & anomaly detection
        - different services will offer different metrics
        - for ec2: collated over 5 minutes; detailed monitoring in 1 minute increment a paid option 
        - anomaly detection allows CW to implement ML to detect unusual activity
    - alarms
        - tightly integrate w metrics
        - allow setting alarms based on threshold for metrics 
        - states of alarm
            - okay: w/n threshold
            - alarm: exceeded threshold
            - insufficient_data 
    - EventBridge
        - provides means of connecting apps to different AWS services to enable actions to occur against real-time changes
        - rules: acts as filter for incoming streams of event traffic & routes events to target
        - targets: where events are sent by rules (e.g. aws services). in JSON format
        - event bus: component that receeives event from apps & rules are associated w specific event bus
    - Logs: centralized location to store logs from different outputs
        - use CW logs insights to inform how to react to log data
        - unified CW agent: can collect logs + metric data from EC2 instances (as well as on-prem) and gives add'l log info
    - CW insights: provide ability to get more info from data that's collected
        - log: analyze logs in CW logs at scale in seconds using interactive queries delivering visualizations
        - container: collate & group metric data from different container services and apps w/n AWS
            - also capture & monitor diagnostic data
            - at cluster, node, and app level
        - lambda
            - get a deeper understanding of apps using lambda
            - gathers and aggregates system metrics 
            - must be created per function w/n the monitoring/tools part of the function 
### CloudWatch Dashboards
- can run queries using data in widgets
- AWS offers automatic dashboards
- eight types of widgets
    - line chart, stacked area chart, number widget, bar chart, pie chart, text widget (supports markdown), log tables (from log insights), alarm status 
- can perform math on a widget
- can aggregate metrics across entire resource (e.g. all instances in ASG)
- can be written as code, but the sizing and spacing must be defined. Up to 100 widgets supported by code 
- can add annotations to periods of graph, e.g. at a specific point in time
    - can add horizontal and vertical annotations
- can link to dashbaords in different regions or accounts 
    - must enable cross-account cross-region access b/w source and destination account 
    - can share a specific dashbaord & specific emails, or to anyone who has a link, or define an SSO provider to allow users to access 
- for free, get three dashboards with 50 widgets. More than that, $3/dashboard/mo
- avoid plotting too much data in graphs, which can slow down loading & clutter graphs 
### Anomaly Detection
- powered by ML, improves CW Alarms by automating their creation & maintenance, which removes most manual intervention which makes alarms more effective & efficient
- automates the process of creating and maintain CW alarms 
    - automatically goes into alarm state if problem detected 
- ML: once model has been created, it can be reused 
    - look for patterns that might be otherwise easy to miss. Learns from data over time 
    - AI is a precursor to machine learning, and is influenced by the human who is part of the programming
        - ML takes the human out, but is only as good as the data involved  
- when turned on, able to identify what's 'normal' vs what is not 
    - normal: analzying historical values for a chosen metrics & looks for predictable patterns that repeat hourly, daily, or weekly 
    - after collecting historical data, creates a model to predict the future, and to differentiate between normal and problematic data
    - anomaly detection doesn't work with workloads that aren't repetitive 
    - alarms can be set for when alarms go above or below the band
    - AWS has ~12k models that customers can use, so generally don't have to DIY
    - Amazon CW Anamoly Detection: any standard or custom CW metric can be used as long as it has a discernible trend or pattern
        - once built, model will be updated every 5 minutes w new data 
    - enabled w console, CLI, SDK
    - for the best result, at least three days of data is recommended
    - when creating a model, can exclude abnormal time ranges from data 
    - upsides: can create alarms that are dynamic and flexible, although it needs some time to figure out trends
    - downsides: it accepts changes as 'the new normal', e.g. if an app fails and has a zombie process, at first it will alarm, then eventually (over the course of a few hours) will go to being okay with that new baseline of data 
- anomaly detection alarm: based on a metric's expected value. Don't have static states
- anomaly detection band
    - grey: anomaly detection band
    - blue: metric data
    - red: anomaly (metric data outside anomaly detection band)
### CloudWatch Subscriptions
- get access to real-time feed of cloudwatch logs that can be delivered to other streams, like Kinesis or Lambda
- getting started
    - create receiving resource that will take in the logs (e.g. kinesis stream)
    - create subscription filters to determine what to send
        - log group name: must be provided and any log events w/n group will be subject to filtering, and when matched will be passed to other service
        - filter pattern: what logs to match 
            - matching: match w everything, single term matching, include a term and exclude a term by adding a `-`, require matching multiple terms 
            - OR matching: match multiple terms with the `?` operator, match on specific words positioned w/n a string 
        - destination ARN: where matched data is going 
        - role ARN: grant permissions required to post data to destination resource 
        - distribution method: by default, distributed by log stream
            - logs are base64 encoded and sent in gzip format to receiving resource
    - able to cross-account share data to kinesis streams
        - need to create a log data sender that is populated by CW logs info
        - log data recipient: must allow the receiving of logs
        - both require a CW logs destination to be created 
        - log group & destination must be in same region, but kinesis stream can be in another region 
    
## AWS CloudTrail
### What is AWS CloudTrail
- record and track events: API requests AND non API requests 
    - records actions made in console, CLI, SDK
- CT events
    - management events (aka control plane operations)
        - track info about management operations taken against AWS resources w/n account
        - e.g. create events or rotation of KMS or user console sign-in
    - data events (aka data plane operations)
        - show info about resource operations performed on or in a resource 
        - e.g. get/delete/put object in s3, put/get/list snapshot 
    - CT insight events
        - triggered by unusual activity w/n account
        - stored in a different folder in s3 to the management and data events 
- by default, records all events in account in event history 
    - records previous 90 days of activity
- CT trail
    - track and respond to specific events 
    - can be sent to S3 or CW logs 
    - types
        - all region trail
            - applies to all regions w/n account & records events in each region that is being operated in
            - delivers to specified s3 bucket
            - enables capture & record of data across entire account
        - single region trail
            - only created via CLI
            - can customize which regions interested in recording data for
            - delivered to s3
        - AWS organization trail
            - captures ALL events from ALL accounts that belong to AWS org
            - can be configured to capture events from just a single region or all regions 
            - management account must be used to create the trail, which will be associated & applied to ALL member accounts
            - member accounts only have access to view the trail and the log files it generates; can't affect trail config
- CT lake
    - store, select, SQL query CT events
    - can store up to 7 years
    - can collect events from own account, config, and data centers 
### The Benefits of Using CloudTrail
- improve security: identify things that happen, and things that shouldn't have happened 
    - find out the how and who & put in preventative measures
- consolidate records
    - consolidate records from more than one region into single s3 to provide convenient way to analyze data
- enhanced visibility
    - understand the what, when and who of what's going on
    - early warning of unusual behavior
    - CT insights tracks & identifies unusual behavior detected w/n account based on the action of a write API 
- auditing and compliance
    - data from CT logs can help maintain governance and regulatory requirements
    - each event captures info like principal, account ID, username + session info, time of event, source, eventname API, region, source IP address 
### Managing CloudTrail Permissions
- AWS managed policies
    - AWSCloudTrailServiceRolePolicy (ServiceLinkedRole)
    - AWSCloudTrailFullAccess (has access to some s3, KMS, SNS, CW logs perms)
    - AWSCloudTrail_ReadOnlyAccess
        - get*, describe*, list*, lookupevents
- permissions are automatically applied only if cloudtrail creates the resource, e.g. s3 or sns
    - existing s3 buckets or sns topics must have the appropriate permissions manually applied 
### CloudTrail Event Log Files
- CT trails: enable capture, track, retain events across AWS accounts
    - w/o trails events can only be viewed w/n event history in console and only up to 90 days old 
    - CT lake: when created, can store review and query events w/n AWS account
        - accumulates events into event data stores, and keeps them up to 7 years 
- CT logs: written in JSON  
    - login source
        - signin.amazonaws.com: IAM user in console
        - console.amazonaws.com: root user in console 
        - lambda.amazonaws.com: service in which request was made (in this case, lambda)
        - aws-sdk-java: request was made w the AWS SDK for java
        - aws-cli/1.3.23 Python/2.7.6 Linux/2.7.18-164.e15: request was made w AWS CLI installed on Linux \
- new logs are made every 5 minutes, then delievered to S3 or CT logs
- aggregate logs from multiple accounts into one s3 bucket
    - enable CT by creating a trail in the AWS account all logs will be delivered to
    - update backet policy on destination bucket to allow other accounts to write logs to it 
    - create new trail in other AWS accounts & select use existing S3 bucket
        - add bucket name & accept warning
        - use same prefix used when configuring the original bucket 
        - new trail will deliver its log files to the s3 bucket  
### Leveraging Amazon CloudWatch to Monitor AWS CloudTrail Log Files 
- can enable CW logs when creating CT trail 
- by sending CT info to CW logs helps manage all the logs
    - metric filters: search & count specific value or term w/n events 
        - create filter pattern to determine what to track & monitor 
    - contributor insights: visualize who top contributors are using time-series data 
        - must create keys to specific the users 
        - can help spot security issues & iron out performance issues
    - cw log insights: purpose-built query langage base don detectable fields w/n log to run queries 
        - has a range of built-in sample queries 
        - queries can be saved & run later. results can be viewed up to 7 days 
## AWS Config
### What is AWS Config
- resource management begs the following questions 
    - what resouces do we have? 
    - are there aany security vulnerabilities?
    - how are the resources linked w/n the env?
    - is there a history of the changes in resources over time?
    - is the infra compliant w specific governance controls?
    - is there accurate auditing info?
- records & captures resource changes w/n AWS account
    - can capture resource changes and stores w/n configuration item
    - capture resources changes
    - store configuration history
    - provide snapshot in time of configs (including metadata)
    - notifications about changes on a resource 
    - provides CT integration to determine who made changes and when
    - use Rules to check compliance
    - perform security analysis 
    - identify relationships 
- captures data for most common services: ACM, CT, EBS, EC2, SSM, ELB, IAM, Redshift, RDS, S3, VPC
- region-specific. Must set up config in each region & can have different settings b/w region 
    - there's an option to track global services as well 
### Key Components of AWS Config
- AWS Resources
    - anything that gets created, updated, deleted 
- Configuration Item: json file that contains configuration info, relationship info + other metadata
    - created when a supported resource has any sort of change, and info for any resources that are affected 
    - used w config history, streams, snapshots 
- Configuration Stream: when new CIs are created, sent to Config stream, in the form of an SNS topic
    - also used by config when other events occur: config history files delivered, config snapshot started, compliance changes for resource, evaluations begin, AWS Config fails to deliver notifications 
- Configuration History: uses CIs to produce a history of changes to a resource
    - can be accessed programmatically via CLI or console 
    - config history file sent to s3 bucket set up at the beginning of the AWS config
        - config history delievered every 6 hours
- Configuration Snapshot: takes a point-in-time snapshot of all supported resources config'd in region
    - captures all the CIs in a region and delivered to s3
- Configuration Recorder: the 'engine' of the service; responsible for recording all changes and for generating CIs 
    - can be stopped & restarted 
    - if stopped, will still monitor the changes, but won't record them, and can't view history while it's stopped (but can before it was stopped or after it restarts)
- Config Rules: enforce specific compliance controls using lambda
    - rules created in Config, and Lambda provides the logic
        - can use AWS managed rules or manually create rules 
    - sends a notification via SNS if the rules are violated; up to customer to take action
- Resource Relationships: identifies relationship between resources & updates applicable CI data 
- SNS topic: used as a Configuration Stream for notifications
- s3 bucket: used to store all Configuration History files and Snapshots 
- AWS Config Permissions: an IAM role is required to allow AWS Config to obtain the correct permissions to interact w other services 
- summary: 
    - configure elements for the Config recorder
    - aws config dsicovers all supported resources
    - for any change on a resource, a CI will be created & send notification
    - Config checks current config rules to evaluate if change is noncompliant
    - if config snapshot take, config will create a snapshot and deliver to the s3 bucket
    - after 6 hours config history file will be sent to s3 
## AWS CloudFormation
### What is AWS CloudFormation
- automate creation, updating, and deletion of infrastructure
- CF temple: JSON or YAML documents
- stack: output of a cf template
    - stacks are 'all or nothing'; they're either fully created or fully destroyed 
- does not support all AWS resources 
### Anatomy of a CloudFormation Template
- AWSTemplateFormatVersion: version of template; 2010-09-09
- Description: for documentation
- Parameters: assign values to resources & set default values 
    - sudo parameters: pre-defined parameters by AWS; can reference whenever in template
    - to refer to a parameter, use `!Ref` and logical ID of parameter 
- Mappings: beneficial for cross-region usability of templates
- Conditions: determine what resources are made based on conditions (think if/else)
- Transform: specify macros to use in template
- Resources: only required section ofthe template 
    - requires logical ID, type, properties, and set of properties 
- Outputs: pass out values returned by resources 
- intrinsic functions
    - `!Ref`
    - `!GetAtt`: get value of a resource
        - e.g. `Value: !GetAtt EC2instance.PublicIp`
    - `!FindInMap`: pick values based on parameters
        - e.g. `ImageId: !FindInMap [RegionMap, !Ref "AWS::Region", HVM64]`
            - the HVM64 bit is important for interpreting the proper imageid
    - `Fn::Join`: join multiple values together, can also join with specified delimiter 

## Advanced CloudFormation Skills
### State Machines
- a stack is a state machine w/n cloud formation
- CF turns templates and parameters into a stack
    - create: template + parameters > CF create operation > stack
        - when triggered, figures out from the template what resource to create first (e.g. one that has no other dependencies), then create dependent resources
        - CF can create two resources in parallel
    - update: template + parameters + present stack > CF update operation > stack
        - CFN needs to know the existing resources to get to the new stack 
    - delete: present stack > CF delete operation > nothing 
- this distinction is important because AWS resources in general follow a similar lifecycle process 
    - create: properties > resource provider logic > new resource
    - update: properties + previous resource > resource provider logic > fresh resource
    - delete: resource > resource provider logic > nothing 
### Data Flow
- stack status lifecycle    
    - ROLLBACK_FAILED requires stack deletion. it is a fairly serious condition and may cause DELETE_FAILED too 
- cloudFormation data flow
    - User (human or machine) requests change which contains command type, template parameters, and metadata
    - request issued to CFN service
    - CFN acknolwedges or errors
        - can only identify malformed code, basic logic 
    - a request comes back to user with pass or fail validation
        - pass only returns ARN of stack that has been started 
    - user can poll for status for stack 
        - stack status can be used for further logic
    - CFN issues resource commands to a 'stack instance' - which is a representation of a reusable template
    - stack instance issues credentials and causes resources to be created 
        - the resource is responsible for understanding the parameters to create
    - the resource notifies the stack instance about the status
    - stack instance notifies CFN status
    - CFN can then publish results to SNS
    - SNS can broadcast message to user or consumers 
        - user subscription to manually monitor what's going on the stack
        - subscriber (i.e. lambda) can take the notification & respond w custom behavior, then can notify user about any changes that were made by the service 
### Lifecycle Demos 
- must be able to detect stack status and be able to deal with the errors
### Nested Stacks 
- master stack treats child stack as a resource 
    - master stack sits on top of everything; e.g., runs the ELB, RDS, EC2, and depends on the child stack to establish networking 
    - master stack depends on the child stack. Seems kinda backwards 
- stack action with parameters ONLY uses the master stack
    - stack action w params sent to CFN, and pointed to S3 to grab the other templates 
### Custom Resources
- resource life cycle   
    - CFT interpreter layer understands how to
        - check for JSON syntax issues
        - validate CFN JSONSchema v4
        - resolve DependsOn and implicit dependnecy order
        - interpret Fn:func intrinsic functions
        - provide intrinsic variable
        - delegate service call logic to service wrappers
        - track stack statuses and emit events to SNS 
    - parameters are sent into resource & outputs come from the resource to provide attributes to other resources 
    - core CFN sends Create, Update, Delete requests to CFN service wrappers, in a 'fire and forget' manner
        - after CFN service wrappers do their things, they send a signed URL to an S3 bucket and CFN monitors that bucket 
- CFN custom resources
    - resource developer maintains and publishes custom resource service that uses custom logic for creating CFN
    - template developer may or may not also be the resource developer 
    - in the custom:: item, must add ARN of custom resource provider to tell CFN where to emit an event when updating a resource
    - there's a lot of things that need to be included in the template & request to get good data back 
    - using lambda to execute the custom logic is a popular way of implementing custom resources 

## AWS OpsWorks
- configuration management service that allows use of managed instances of Puppet or Chef to manage infra in AWS 
- OpsWorks for Puppet Enterprise
    - fully managed Puppet servers for infra/app management
- OpsWorks for Chef Automate
    - same, but for Chef
- OpsWorks Stacks
    - model app infra as stacks, which consists of series of layers that represent groups of instances or resources that are managed together as a single cohesive unit
    - monitor the health of instances & auto replace unhealthy instances 
    - supports use of Chef cookbooks 

## AWS Logging
### The Benefits of Logging
- w/o logging, could be delay of resolution of incident & safeguarding of env 
- logs general contain a huge amount of info & retained on persistent storage (e.g. system logs)
- some logs can be monitored in real-time
- audit control
    - contain a lot of metadata, like date-stamps and source info like IP address or username
    - help meet compliance controls
- incident resolution
    - being able to resolve an incident ASAP is very helpful
    - quicker resolution = better customer experience
- monitoring & alerting
    - quickly identify potential issues
    - define thresholds against metrics for auto notifications
- trend analysis
    - able to establish what's routine and what isn't, and can identify threats & anomalies easier 
- understanding infrastructure
    - having inside like at infro performance & communication is key
    - have more info about env is always better than not enough 
### CloudWatch Logging Agent
- 'unified cloudwatch agent'
    - enables collection of logs from EC2 instances & on-prem servers
    - this is in addition to the standard metrics from CW 
    - supports flavors of linux + windows 
- to install
    - create a role to allow CW to collect data & instance interact w SSM
    - download & install agent
    - configure & start CW agent
    - easiest to just do this all through SSM
- creating roles
    - one role used to install the agent & send metrics to CW (should be applied to all instances)
    - one used w parameter store w/n SSM, to store a configuration info file to agent (should be used once on one instance then detached)
        - on the first instance configured, must create CW Agent Configuration File
            - file store config params that specify which metrics & logs to capture from instance
            - can be created manually or w a wizard (on the instance)
                - manually provides more granular configuration 
### VPC Flow Logs
- capture IP traffic info that flows b/w ENIs in VPC 
- helps reolsve incidents w network communication & traffic flow
- help spot traffic reaching a destination where it shouldn't be
- log data captured sent to CW logs
- limitations   
    - for VPC peered connections, can only see FL of peered VPCs w/n same account
    - can't get info from ENIs in ec2-classic
    - once a VPC FL has been created it can't be edited
    - traffic not acaptured: 
        - DHCP traffic w/n VPC
        - traffic from instances destined for Amazon DNS server
        - traffic destined to the IP addresses for the VPC default router
        - traffic to the instance metadata and time sync service IPs 
        - traffic relating to Windows activation 
        - traffic b/w NLB ENI & endpoint network interface 
- flow log sources
    - ENI on an instance
    - subnet w/n VPC
    - VPC itself 
- publishing data to CW 
    - every ENI that publishes data to CW LG uses different log stream
    - w/n each stream the FL event data shows content of log entries
    - each log captures data during windows of 10-15 minutes 
- permissions
    - to push FL data to CW LG, IAM role is required w the relevant permissions 
    - VPC FL service must be able to assume the role 
- FL record syntax
    - version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status 

## AWS Systems Manager
### Introduction to AWS Systems Manager
- set of fully managed services that enable ongoing management of systems at scale, automated configuration, and secure and reliable configuration 
- works in ec2, on-prem data center, or other cloud platforms 
- most SSM functionality is free 
### Systems Manager is a Good Fit in the AWS Tool Set
- systems manager explorer is an operational data dashboard for multiple accounts & regions 
- integrates w CW dashboards & personal health dashboard 
### Managing Resource Groups
### AWS SSM Requirements and Building Blocks
### AWS SSM Operations
### AWS SSM Run Command 
### AWS SSM Parameter Store
### Maintenance Windows 
### AWS SSM Document 
### AWS SSM Feature Review
### Patch Manager
## AWS Secrets Manager
### Using AWS Secrets Manager to Manage, Rotate, and Retrieve Secrets
## Parameter Store vs Secrets Manager
## AWS Service Catalog
## AWS Organizations
### AWS Organizations 
### Implementing AWS Organizations 
### Securing Your Organizations with Service Control Policies
### Using AWS SSO to Simplify Access Across Your AWS Organization
## AWS Control Tower 
## AWS Trusted Advisor
### What is Trusted Advisor
### Using AWS TA to Monitor for Underutilized Resources
## AWS License Manager
## AWS Managed Grafana
## Amazon Managed Service for Prometheus
## AWS Health
### Overview of the AWS Health Dashboard
### Reviewing Past Issues in the Health Dashboard
### Reacting To Account-Specific Health Events With AWS EventBridge
### Enterprise-Level Services
## AWS Proton
## AWS Resilience Hub