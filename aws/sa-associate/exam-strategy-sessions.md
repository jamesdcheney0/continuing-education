# Exam strategy: Friday, February 3rd, 2023
- CloudEndure Migration use EC2 and EBS
- DataSync asynchronously xfers data b/w source & target storage 

# Exam Strategy: Friday, February 10th, 2023 
- question: deploying an app in two regions, writing to a DB in it's region. The two DBs need to be eventually consistent. In conflict, queries should return most recent write 
    - read: have to have data conflict resolution. DDB has data conflict resolution in global tables 
    - DB schema not defined in the question
    - asks for least admin effort. RDS is not managed; DDB is. Also eventually consistent 
    - Using RDS w read-replicas is technically correct, but only partially - is for read-only queries - writing to multiple DB instances NOT SUPPORTED
- Change Data Capture can be used to xfer data b/w region's DBs, but data conflict resolution is not built in
- DO NOT READ TOO MUCH INTO THE QUESTIONS. MAKE NO ASSUMPTIONS, ONLY GO OFF THE INFO THAT IS THERE

# Exam Strategy: Friday, February 17th, 2023 
- got all the questions right, and they made sense in context of what I've been studying this week 

# Exam Strategy: Friday, February 24th, 2023 
- reporting app on EC2 runs behind ALB. Instances run in Autoscaling group across multiple AZs. for complex reports, app can take up to 15 minutes to respond to request. SA concerned that users will receive errors if report request is in process during scale-in event
    - sticky sessions are an ALB thing, unrelated to autoscaling. Do not force instances that the sessions are attached to remain healthy; do not affect autoscaling scale-in decisions 
    - cooldown period prevents autoscaling from making decisions about further scale-down or scale-up deicions, but doesn't consider established sessions & allow instances to stay up longer 
    - increase the deregistration delay timeout for target group of instances to greater than 900 seconds - this is the only one that forces instances to stay up for a while before terminating 
- IPv6 is supported by NAT gateway and egress-only IGW 
- use IaC for software app. Wants to test app before send traffic to them & looking for efficient
    - use AWS CFN w parameter set to staging value in a separate environment other that prod (can't use snapshot deletion policy w CFN, doesn't snapshot all resources, and being able to just roll back stack if update fails is missing the point of the testing)
    - route53 failover routing: think DR

# Exam Tips from Creighton: Wednesday, March 1, 2023
- review all content
- exam readiness learning from this week
- take full-length practice exam with skillbuilder subscription 
    - if subscribing, take a look at cloudquest 

# Exam Strategy: Friday, March 3rd, 2023
- implement pilot light DR strat for existing on-prem app. app self-contained, need to DBs
    - warm standby: existing infrastructure that serves a portion of live traffic 
        - fast RTO/RPO
    - backup/restore
    - pilot light: existing infrastructure that is turned off, but ready to serve live data 