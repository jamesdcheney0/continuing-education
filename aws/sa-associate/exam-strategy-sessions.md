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