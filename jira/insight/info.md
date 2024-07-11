# What is Insight? 
- Implement asset management 
    - physical things + digital assets (apps, services, contracts)
    - benefit: instead of spreadsheets or external DBs, have everything in Jira
- insight object schemas
    - store asset & configuration item data
    - can make multiple asset repos and object schemas (asset configuration DBs)
        - no limitation on what can be stored
        - defined by attributes provided for object 
    - organize all the parts of IT business 
    - can view visibility of relationship of supported objects 
        - able to view all the info in the Jira tickets 
- a database of anything
    - can capture and manage anything; people assets, manage relationships b/w those
- insight conceptual model 
    - schemas
        - collection of object types and their objects
        - if bringing in data from other systems, best to map it to a single object schema to have flexibility to match import 
    - object types
        - a type of object, where objects of that type will share the same attributes
    - objects
        - usually represent a real life object
            - e.g. person, server, IP address, piece of hardware
        - not just for IT assets
            - also for people (employees, skills, partners, roles, depts, ID cards), facilit ies, practices (workflows, processes, risk level, approvers, delegates, lead times), anything (ECUs, partical accelerator, gurneys)
    - attributes
        - available 'fields' on the object. text attribute, date attribute, etc 

# Sandbox Experiments
- in the search function (here)[https://issue-sandbox.lift.mhpcc.hpc.mil/jira/secure/insight/search?criteria=objectType%3DUsers%20AND%20%22User%20Type%22%3DCIV&schema=22]
    - insight dropdown > search for objects. Seems to save most recent object schema for searching w/n. Can switch b/w schemas 
`objectType=Users AND "User Type"=CIV` returned a result from my object schema. 

I made three custom fields, a new project, an insight db, a scheme, and screen schemes 

how to force fields to only show results if they're also attached to them..? 

my experimentation go to `objectType="Mission site"` in james-base-select custom field. It lists the sites, but doesn't force a sort further down based on what site is selected 
tried `"Mission site"=${"Mission site"}` but nothing showed up after that 

I'm waiting for Lynn to help point me in the right direction on this one 
    need to watch a lot more videos on insight 

    objectType="Mission site" AND object IN connectedTickets()

- Lynn: take little bites. add stuff, make little things work, even if manually, and as more understanding comes, then can implement more automation 
    - don't have to make things sort only whats available right away. should be easy to implement later, but I need something to be able to implement it in. Something working w/o automation is better than nothing working and still trying to figure out automation 

## NL Insight Collaboration
### 20231117
Jeanie, Matthew, Tabitha
#### Tabitha
- track users to know tools, access, groups for onboarding/offboarding
    - currently in service desk has a task ticket 'master user ticket' with labels to short stuff 
        - Has ~300 users currently tracking 
    - wants to list project, role, software 
    - asked for field editor access for fields + how to inactivate a field 
    - can import automatically roles w/n lift and not have to manually recreate? 
        - pulling roles from jira/confluence? 
    - user type w/n object type addributes lists groups 
        - when selecting groups, only allow users from that group to be listed
    - how to allow access to other insight objects https://community.atlassian.com/t5/Marketplace-Apps-Integrations/Insight-how-to-reference-Object-Types-from-another-Schemas/qaq-p/727235
        - object schema dropdown -> configure -> allow others to select objects from this schema 

## Insight
link project to insight asset management: https://confluence.atlassian.com/servicemanagementserver050/4-link-your-project-to-insight-asset-management-1142253575.html 
17033 - follow up w customer
16111 - follow up w customer 
15893 - learn insight, finish it out 
only two LOG IT tickets assigned to Lynn that Cody may have been talking about 
    - Kyle says spend all my time on these two & any other zephyr/insight ones, and particularly LOG IT
    - Caleb to focus on submitted queue 
    - if users don't respond w/n two weeks, close ticket 


## Matthew Working Session https://issue.lift.mhpcc.hpc.mil/jira/browse/NLSD-15893
- Link project to insight https://confluence.atlassian.com/servicemanagementserver050/4-link-your-project-to-insight-asset-management-1142253575.html
    - create custom field, configure it to point at the right object schema, reference it in the appropriate Jira issue type 
- lynn needed things for combo boxes 
    - fields based off of 445TS_ConfigurationItems
    - I just need to create the fields so he can find them and add them 
    - made security impact analysis (SIA) submitted 
- goal: on CR if they select mission site, only the buildings associated with that should show up 
- some of the fields aren't showing on the ticket screen, but secondary issue to the create issue screen having section II 
- Change (Test) issue type could be removed 
- don't worry about hard drives 
Matthew is going to update the fields that he wants



## Gregory working session 
Lynn was helping build out change request forms in lift and insight object schema. wasn't able to finish tickets out. Talked with Cody.
Purpose: review progress of tickets, answer my questions, more regular meeting cadence 
- Lynn got them grouped w other folks who are starting to use Insight. Has a regular meeting every other friday at 1200 EST, going to invite me into that 
- have two insight DBs set up, one for configuration items and a service desk w insights where trying to track all the users, their tools, etc - esp for onboarding/offboarding.    
    - those same users are going to need to be referenced by other insight 
    - 16621 for Tabith's users and that request ^ 
        - currently has master user ticket to try to track things, and trying to move to insight 
        - confused on how to relate ones to others 
            - env toolset in, roles toolsets have, track what groups user is in; wants to avoid redundancy 
                - jira is currently listing the groups users are in - any way to transform that so insight can do thing 
                - mostly tracking users w labels, but Tabitha is doing an audit and will be able to export users into a csv-type document that can then be imported into LOG IT-Account Services insight 
            - way to have multiple roles/groups attached to a user? currently we're only seeing dropdowns that allow single selections 
            - will want custom fields that can benefit from insight 
- high-level use case
    - digitize change request form & apply automated workflow to it. Link CR ticket to CI item in insight DB
    - two forms of CR: high-level and low-level
        - high-level: affected projects, what systems to change
    - reduce the need of a manual word form
        - lynn has CR stuff broken into tabs in the sandbox (LOGIT asset manager)
        - gaps lynn wasn't able to address
            - missing fields in the individual tabs
                - his team can do cross-comparision b/w what's on form and what needs to be on it
            - applying workflow to it 
            - being able to select specific configuration/configuration item and view those relationships & track those relationships 
    - LOGITCR - ITSM (prod)
        - team has built out the structure they want, now need to associate CI items w ticket/record
        - LOGITAM-ITSM (sandbox)
- would like to have a weekly touch point 
- Greg 
    - owes me cross-comparison of what has been developed so far and what's missing on the change request
    - will highlight fields that related to Tabitha's insight DB
    - will schedule weekly touchpoint 

## Insight Questions
- Object Schema -> Object Type -> Object 
- how to make an insight attribute select multiple objects w/n object type? 
- how to make an insight custom field ONLY show objects it's related to
    - am I relating objects to each other properly? 
- Lynn: LOGIT 
    - using insight for object management, they're building out schemas
        - helping connect Jira tickets to update automate 
    - where she left it: trying to configure jira ticket screens & determine what fields to correlate to schema 
- correlated attribute to correlated custom field 
- update IP address for Jira so I can look at how insight has been used in DELOS 

## 20231201 Insight conversation 
- Jeanie
    - relationship b/w fields
    - query/report data 
        - any way to search for/select specific things and produce a specific report 
    - software asset
        - trying to achieve: inside software, have components, and they want to share the individual components of the software (the four under software asset in RAIDER Software Assets)
            - want to grab baseline 
            - in jira, can make a branch in jira ticket, and it'll go to bb and make the branch, then establish comms b/w the branches
                - not seeing comms b/w insight and bb, although able to put in a link 
                    - want to import hundreds of inputs/outputs/parameters under sw asset -> objects -> behaviors 
                        - in confluence, wrote a script that pulls info into a spreadsheet 
                            - hasn't experimented with importing things 
        - wants to be able to use a filter on a dashboard to view information from insight 
    - raider software
        - how to relate between software schema and software asset 
        - each baseline exclusive to the OS, and everything else is dependent on the baseline being accurate 
    - they fly drones. There's objectives, behaviors, units that need to swap
        - raytheon and BAE systems both provide different OSs. components w/n might get swapped/shared 
    - goal they're trying to get to: go into software asset db and go in and select a UoP or behavior or objective or OPM, go out into the BB repo and search for the component 
        - each UoP component has a baseline link to BB, wants tool to go to control domain location in BB, and produce a single executable, then put the components in another baseline branch & another jira ticket to allow continued development for different use 
            - in jira, can go into a ticket and make a branch
            - confluence was doing a lot of that 
- Raymond 
    - Jira, how to navigate better
- Greg
    - importing data into insight 
- any way for Lynn to be able to join us on a semi-consistent basis? We're all running blind 
- tabitha
    - importing
        - how to import to multiple objects to multiple objectTypes 
        - lynn pulled in Jira users currently associated w project, not that she was importing via csv 
        - failed to connect to the CSV file selected 

# Sandra Masters NLSD-13166: Zephyr issues for MyNavy HR NP2 
Maria Murphy was w NL/MyNavyHR from the beginning and learned Zephyr on the fly; MNHR was already familiar with Zephyr 
tests -> test status -> cycle summary -> all releases -> unreleased -> see test cycles that have been scheduled or completed. 
    - currently on Build 64 -> just complete payroll table setup and on/off cycle. When hovering over the green/red bar by those projects status bar, it says how many have passed/failed/etc (test execution status)
        - if you click on the test execution and click the link of the name of it that takes to all the tests. 
            - the descrepancy becomes apparent when clicking execution status drop down and selecting a status and seeing what count shows up. When picking a different status shows a different count 
Linton found descrepancy. What seemed to fix it; sometimes it was corrected by just an index of zephyr data, and sometimes both zephyr and jira. (Linton doesn't remember specifics one way or another)
MyNavyHR: linton: maryland, sandra: alabama, other members in NOLA 
    - Ryan, Alex (both in NOLA), Atul (austin): tools team 
NP2 is the largest user of zephyr at this point, and initial users of Jira and Zephyr. Have other teams coming online with Zephyr, but aren't using much, so don't have much other comparision
- what to figure out: in the search screen, it was run while it still seems to be in Zephyr data b/c still have filters on the side panel 
    - but if you go and grab the filter from the advanced search in that same page and run it as a normal JQL query under issue searching, a different number of executions occur. At one point, was just searching in normal jira issues search screen, but moved to the zephyr-specific screen at some point in the past 
    - discrepancies tend to come in the middle of a cycle with a unmatched number of unexecuted, but also just randomly 
        - could it be because of testers changing statuses manually and confusing the system? 
- to get everything over, they had a custom script they had to write
- history/test details history fields
    - TDH doesn't include anything related to test executions - why?
        - smartbear had a tool that would export test details but not executions
    - *is there any way to (on the back side) that test execution data is retained?* 
        - e.g.: work w reservists & N16 folks. sometimes there's misunderstandings and they'll put into a status, then a couple days later change the status back
            - on day 1, records blocked, then a couple days gets recorded again w new execution status. Ends up getting counted twice with the different execution status. At the bottom of the line, numbers aren't in sync 
                - they've got a ticket in for that 
        - is that data even somewhere in the DB somewhere? 
            - the import scripts they used may have information on what queries were used 
            - do those changes get overwritten, or does it keep history of changes & there's a way to access it
                - haven't looked to see if easyBI can look at any of that information 
        - today (20231205) first day of a new test cycle 
            - linton is the metrics guy for the test team 

me: 
- easyBI gets data once every 24 hours - is there a defined period of how often Jira talks to Zephyr? Is it desycronized between zephyr and jira? 
- reach out to smartbear and ask if they've heard of anything like this 

# Confluence & granting user access
- in HPC home page, manage users and make sure app is allowed, then edit and make sure username matches the username in user management in confluence, copy the password, set it, and make sure they've got confluence-users group 

# Tier 1 & 2 meeting 20231206 
tickets: wait till users confirm resolutions before closing tickets 
tag natasha and cody on my two CR tickets that require lots of custom fields? 

Todd: onboarding
Natasha: tickets w custom fields + insight - chat offline. caleb said for sure keep doing logit 
caleb mentioned I still don't have admin drop down 

krb conf file maybe not configured right?
Cody: run parallels or something 

# Cody & Dennis
banner on cli for homepage? backend mysql set up 
sys admin who's setting up app, needs somebody w mysql/db/backend knowledge to set up and attach to app 
stigged? 

# Session w Caleb 20231213 
copied fmddt, so only FMDDT (long name) was on the one, and still couldn't remove the Key Result issue. error: You do not have the correct permissions to move the issues from project Financial Management Data & Digital Transformation for issue type Key Result

# Session w NL folks 
Jeanie making a spreadsheet of questions & try to work through 
do Natasha and Cody have experience w Insight? 
Matt: able to pull from db scheme to baseline, point-in-time image 
    take snapshot of current schema

Can JIRA Issue forms have a Save button and a Submit button? Reason for asking is I do not want to run the workflow process until the user of the form officially "Submits" the form for review. If they "Save" the form they are allowed to go back in and add, edit, delete information. Once it is submitted the form is locked from editing so that it can be reviewed. 

show attributes of another object in another object? 

Matthew for me: (need to know by 1/24) - is there a way to export issues created in object schemas & import into another jira? 
export the whole object schema + objects inside as well as the issue screen (i.e. the one we've been working on)
- if we had 'configuration manager' plugin installed - yes, from insight
    - only export Jira supports is CSV 
    - plugin costs money, and likely not going to be added
        - if users are requesting it and willing to pay for it - put in a ticket 
            - need to confirm that CMJ can in fact do that 
                - would expect Jira custom fields would be made 
    - CMJ: for exporting insight-related things from Jira, gotta pay 
    - insight export: can export an object schema whenever 
- custom fields not exportable 


reindexing MyNavy HR NP2
when complete, reindex the zephyr portion of it & comment when both have been finished in the ticket 


# 20240107 Jira/LIFT Insight session 
Go live: end of March 
- Tabitha: would like to chat about starting to look at getting everything connected
    - able to add data to insights from user input? is there some sort of automation? both for approvals and the objects? 
        - is there a way, through an approval process, to add items to insights schema? 
        - I told her I'm 99% sure that there is no way to update CIs via creating a jira ticket in and of itself (and I'm also not sure if there's automation that can accomplish that) 
    - how to link things 
        - able to connect to confluence and automatically pull in the confluence groups? 
        - in service desk for accts, want to do the same thing greg is doing - connect fields & get add'l fields 
            - i.e. projects request field point to the insights fields w multi select (same w access role) 
                - she'll make what should link to what 
        - how to do imports? 
            - specifically where it has relationships to multiple items & attributes 
                - are the relationsihps to other object types automatic? - share w Tabitha 
    - for request types, is there a way to change who approves based on what app is being requested? or would need diff issues to set up that workflow? 
        - cody workflows, any status update 
- Greg: (he's the sandbox account guy)
    - feedback: 
        - wants to indicate more fields that are required 
        - dropdown lists: able to remove none? only on req'd fields, I think 
        - configuration item information
            - on the way to finalizing insights import. how to link 
                - are they planning to import in sandbox? yes, test there, then move to prod sometime 

# Cody: for approvals, post functions in the workflows should be where approval steps live 
Work with Matthew on looking into workflows 

# 20240112
- Jeanie: *can we set up a workspace in Jira/Confluence to collaborate insight there, so we can share stuff*  
    - still needs the ability to run reports against insight & create jira dashboards 
        - Matthew has tried to do dashboard things w insights: when widget gets added, nothing happens (Jeanie has had the same experience) 
    - research insight report integration with jira widgets 
        - https://community.atlassian.com/t5/Jira-Service-Management/Creating-Jira-Reports-with-Insight-Objects/qaq-p/1855355
        - when sandbox is back up, experiment with reports 
    - has a lot of jira queries set in confluence that pull data every 15 minutes. She gets them from her saved filters, then goes to advanced, where it has the JQL listed, then copies that over the 'Insert Jira Issue/Filter' field option in confluence 
    - schedule for every other week so folks can reserve a spot and talk about specific things 

# 20240117
- Greg: validated changes in sandbox. working on insights build out. Have been working to get internal feedback. next week, hoping to get a list of fields that need to be integrated w the change form
    - sandbox currently down; possibilities of automated workflows to commit changes to insights database from the change form? 
        - how to review changes from customer, then when approved, make edits & changes to insight db 
            - *ask Lynn, Paul, Tina whether this is even possible*
- Tabitha: might be scheduling an insights deep dive soon 
    - any way to import multiple object types? 
    - biggest asks for Dennis: SMEs, training set up, automated workflows w approvals using insights (from a jira & jira service management perspective), importing multiple object types 
    - has a grey waiting for approval box that approvals are set up in 
        - how to set up approvals?
            - i made a custom field 'Approved Users' which she's able to view in the insight fields picker, but isn't picking up any objects from the defined object type 
    - in our service desk, do we have something where there's something approving set up? does another team have approvals set up 
        - ask Cody about how approvals setup works 
- if sandbox is up on Monday, Greg will plan to do the importing object workflow 


# 20240122 Insights Training 
- limitation: Herb is in the midst of onboarding & can't access systems
- the issues: 
    - tabitha: manage all users w/n lift + all toolsets & access users have access to, from a dev perspective 
        - i.e. poc for offboarding, gov vs contract users
        - in insights, want to add users w/o having to re-add them 
            - haven't been able to pull in data about users from confluence 
            - want to avoid 'hand-jamming' users into insights  
                - able to import from CSV *for single object type* right now - possible to do multiple object types? Herb: depends on relationships. Has separately done them or external process in the past (API calls to import/update data) 
- herb: options for Jira to update Insight based on approvals & post workflow functions 
- herb: aiming to be as available as he can, and in the midst of wrapping up on another project over next couple weeks 
    - get herb added to the JIRA-LIFT/CM Team Working Session herb.lamb@rightstar.com (should be switching to mil.mil soon); has diff address for CUI 
    - plus weekly working session 
- herb will look into multi-object type import in another sandbox he has access to 
- deadline: Tabitha: deploying onto first aircraft in spring & ship june. Would like to be able to deploy insights with those deployments 
- cody: NLSD-15893: wanting to set up approvals. also NLSD-17033

good example - CMED project workflow & postfunctions (Mary Lemue set them up & is an expert on it) - call Cody on cell if I can't figure it out 

## Trying to find approvals 
https://issue.lift.mhpcc.hpc.mil/jira/secure/admin/workflows/ViewWorkflowTransition.jspa?workflowMode=draft&workflowName=AOCCMINT+RFV+Workflow+2.3.1&workflowTransition=251&descriptorTab=validators&workflowStep=17
- transition -> validators (AOCCMINT RFV Workflow 2.3.1) -> the transition requires the following criteria to be valid: If a Comment is not provided, report the following error: Please comment on the reason for returning to Approval Process 

- only project type *service* supports 'Add Approver' 
    - change in workflow, approvers have to be in group, could try to send tickets to a queue or a JQL monitors changes 
        - https://community.atlassian.com/t5/Jira-Software-articles/Add-an-approval-step-using-Jira-Software-and-Work-Management/ba-p/2182531
        - groups/roles only, or users also? seems like no users 
            - groups are mapped to roles 
            - make multiple roles for different users/groups to point at to get perms to have access 
    - other option would to be change project type 
        - multiple groups in PUM & point at diff groups in workflow 
- tell Matthew & Greg/Tabith (separately) about the blocker 
- for service projects, create custom field: user picker (multiple), then in configure, able to define only specific users/groups 
    - able to get approvals working in KTP in sandbox, but approver didn't notified 
changing project type changes permission schemes, what users can see and do - it's a big change 

# 20240201 Jira-Lift/CM Working session (w Herb)
- Herb has access to things now as admin 
    - ability to import multiple objects at once into insight w single process 
        - less flexibility; everything would have to be defined
        - or could do a json object for each individual object & import one object type at a time for more flexibility 
    - service project approvals
        - when there's a thing that needs approvals to move in transition, the system will add approve/decline buttons on particular issue & pending approvals based on approvers for that step
            - indicate source of approvers & what the approve/decline thresholds are
            - limitation: if individuals can approve/decline, a decline doesn't require comments be added 
        - workaround: have to manually build-out functionality using other Jira functionalities (not as easy, but equally transparent)
            - when using service, able to allow users who are only approvers, and don't have to be users 
            - people able to be notified with the work around? can create automation to create notifications (also some plugins that handle some of that) 
            - can be better when declining a thing and giving reasons for why 
            - can still use a group defined as insight objects to identify users 
- What does he know about Zephyr? 


# 20240209
- Matthew Contri
    - updates on workflow/approval processes 
    - insight gadget for jira dashboards - how does it work? 
        - 445th CMO dashboard 
        - would like to run reports to show counts of what systems OS are running 
            - widget dropdown has nothing in it. Matthew not able to create a filter or report in insight
- Jeanie 
    - wanting to make template schemas in the Jira collaboration project 
    - how to get tabitha's user base to build a schema from it? 
        - able to clone schema and not data? Matthew thinks it's fairly easy 
    - able to put Jeanie's insights into shared templates? 
- Tabitha 
    - herb was supposed to look into getting a plugin or something for insight on confluence
    - for dashboard sharing, user has to have access to project, dashboard, and filter to see how it all works 
    - insights macro(s) avaiable in wiki? How to utilize the dashboard gadget/widget 
        - how to have more complex insight reports


# Chat w David 
- struggling to fill from contract/personal perspective 
    - two options: 
        - put me on DELOS. Chris would like to have me back
            - in transition. Users going from DELOS to thru-hiker. similar to DI2E to DELOS
            - 95% sure all slots will stay the same; will probably be sub to booz-allen on thru-hiker
            - if I'm fine with the transition, best 
        - or on TENA, which is like NL. 
    - NL program requires notification to pulling folks off. Will call cody 
        - maybe a week or so 

# 20240212
- can we start moving from sandbox to prod? - ask Cody & Natasha if that's fine 
- if still using insights and custom fields. is process diff in getting insight custom fields created vs jira
    - instructed by program to no longer use insights as CI DB
        - now has to all be drop-downs and values in jira itself 
    - if there's push-back, i.e. jira fields would be a pain, and could use insights as the backbone of the form, and do the DB otherwise & be able to go back to leadership 
    - talk to Cody, Natasha, Dennis(?) - is there any problem going forward this way, performance-wise. Is this going to be doable? 
        - don't want to start changing the way we're doing this, then getting pushback from LIFT leadership 
        - depending on what I hear there, update the ticket for Greg/Tabitha to request the move from sandbox to prod 
            - ideally an answer before Thursday, when they chat w Cody & Dennis 
    - Tabitha & co can fill in the data required on the custom fields

