# Well Architected Best Practices (4hr webex class) 
## Links 
- Map for each of the well-architected pillars, and best practices within [here](https://wa.aws.amazon.com/wat.map.en.html)
- Main page for well-architected framework [here](https://wa.aws.amazon.com/index.en.html) - kinda like an engineer-level overview
- AWS Well-Architected review in a more customer friendly look [here](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc)
- classroom labs for the 5 well architected skill builder labs [here](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/14923/classroom-labs-aws-well-architected-best-practices) - requires AWS skillbuilder
- Well-Architected framework concepts [here](https://wa.aws.amazon.com/wat.concepts.wa-concepts.en.html) 
## General Design Principles
- Stop guessing your capacity needs (scale automatically)
- Test systems at production scale 
    - able to emulate prod deployments with the 'infinite' capacity of the cloud (that is, more capacity than anyone would be willing to pay for)
- Automate to make architectural experimentation easier
- Allow for evolutionary architectures
    - discard the paradigm of 'if it isn't broke, doesn't fix it' from on-prem data centers
- Drive architectures using data
- Improve through game days 
## Well Architected Review
Learn | Measure | Improve - with customer
- Not an audit - work together to improve results
    - everyone wins if customer has a well architected environment 
- Not architecture astronauts (not AWS dictating what they think is best, but based on experience with other customers over time) - use practical, grounded, sensible, and proven advice
- Not a one-time check - examine workloads continuously 
### AWS Well-Architected tool
- takes well-architected framework and provides a tool that asks questions & gives answers 
- workload can refer to segments of business, from an exec perspective, e.g. CRM, shipping, etc 
- in the console for AWA, each of the questions (there are 58 total) w/n the design principles best practices are listed and can be answered or skipped based on workload that is being evaluated 
## Best Practices
- within each principle, there are links to answers to questions on how to design for each pillar
- E.g. https://wa.aws.amazon.com/wat.pillar.operationalExcellence.en.html, under organization header, there are three questions, OPS 1-3 that answer best practices for 'organization'

## Operational Excellence 
- how organization supports business objectives; run workloads effectively, continuously improve processes 
### Design Principles
- Perform operations as code
    - if it's possible to do something consistently, repeatably, and trackably - do it! 
    - AWS systems manager is one way to do that with instances (like an operations control center) 
        - patch manager, run command 
- Make frequent, small, reversible changes
    - using CI/CD, DevOps, etc 
- Refine operations procedures frequently
    - e.g., started ssh'ing directly to server, then to an instance in cloud, and now using session manager to connect to managed node to avoid having port 22 open 
- Anticipate failure; ties in with Reliability pillar
    - accept that 'everything fails all the time'
- Learn from all operational failures 
    - document postmortem results & refine processes 

## Security
- Protect information and systems
### Design Principles
- Implement a strong identity foundation
    - anti-pattern: account overcrowding - that is, excessive number of VPCs within, with lots of different permissions 
    - suggestion: have multiple accounts per function, and mostly prefer a VPC (or function) per account 
- Enable traceability
    - gain visibility to spot issues before they impact business, improve security posture & reduce environment risk profile
    - AWS Security Hub, Amazon GuardDuty, Amazon Inspector, Amazon CloudWatch, AWS Config, AWS CloudTrail, VPC Flow Logs 
- Apply security at all layers
    - create network layers
    - control traffic (and security) at all layers
    - implement inspection and protection 
- Automated security best practices
    - anti-pattern: manual auditing
    - DevSecOps: security as code; proactive controls enforced by code 
    - Continuous detective controls w AWS services 
        - Amazon Inspector (for EC2), Amazon Macie (for S3), AWS Trusted Advisor, AWS Config Rules, GuardDuty
- Protect data in transit and at rest
    - Can use Amazon Macie, AWS KMS, AWS CloudHSM, AWS ACM, SSE
    - S3 now has encryption turned on by default 
    - Encryption should be less of 'what should we encrypt?' and more 'what SHOULDN'T we encrypt?'
- Keep people away from data
    - rather than providing direct access to data, have users log requests (e.g., as a ticket) and use services and automation to grab what they're looking for (e.g., rather than directly accessing DocumentDB, forcing users to put in a ticket that calls lambda that grabs document information)
- Prepare for security events 
    - during an incident, containing the event and returning to a known good state are important elements of a response plan
        - Amazon Detective, AWS Config rules, AWS Lambda

## Reliability
- the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues
### Design Principles
- Automatically recover from failure
    - use stateless processes 
- Test recovery procedures
    - e.g., Netflix' Chaos Monkey
- Scale horizontally to increase aggregate workload availability
    - vertical vs horizontal scaling
- Stop guessing capacity
    - Use elasticity by increasing & decreasing it
        - Using cloudwatch to track and adjust autoscaling needs 
- Manage change through automation 
    - that is, making changes to cloud infrastructure; ideally, approved and tracked. Can be done with AWS SSM change manager

## Performance Efficiency
- encompasses the efficient use of computing resources to meet requirements and maintain efficiency as demand changes and technologies evolve
### Design Principles
- Democratize advanced technologies 
    - i.e., taking IT services that AWS has available that may have not been available due to on-prem environments
    - e.g., setting up IoT, ML, AI infrastructures)
- Go global in minutes
    - can simply copy code into new regions (if using IaC) [there are information import/export laws to abide by, of course] and be available to new customers far easier than making a new data center 
- Use serverless architectures 
    - use 'serverless' applications offered by AWS, and just deal with the code, and not underlying infrastructure 
- Experiment more often
    - e.g., try out new instances types when they come out 
- Consider mechanical sympathy
    - using a tool or system with an understanding of how it operates best 
        - create target tracking scaling policies for EC2 autoscaling
        - create Amazon CloudWatch dashboard
        - perform a stress test to validate scaling policy

## Cost Optimization
- Encourages the ability to run systems that deliver business value at the lowest price point 
### Design Principles 
- Implement cloud financial management (CFM)
    - https://aws.amazon.com/aws-cost-management/
    - help finance team in organization work together with engineers 
- Adopt a consumption model
    - pay-as-you-go model; avoid paying a fixed amount for fixed resources, regardless of utilization
        - ideal to have cost and usage as close together as possible. 
    - pay for what you use; shut down instances while not being used, esp for dev instances that aren't being needed 
- Measure overall efficiency
    - look at cost compared to investment. Able to calculate cost and the results of increased capacity (e.g., greater consumer purchasing, etc)
- Stop spending money on undifferentied heavy lifting
    - transition to serverless architectures; instead of instances on 100% of the time, transition to using lambda functions for different things 
- Analyze and attribute expenditure
    - identify usage and cost
        - get granular with tags 

## Sustainability
- Minimize the environmental impacts of running cloud workloads 
### Design Principles
- Understand your impact
- Establish sustainability goals
- Maximize utilization
    - right-sizing workloads (also part of saving cost)
- Anticipate and adopt new, more efficient hardware and software offerings
- Use managed services
- Reduce the downstream impact of your cloud workloads 