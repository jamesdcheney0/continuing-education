Gregory Dokuchitz
LOGIT asset manager project 
# Low Level CR form
- in the sandbox, each section is represented by a tab in the issue type 
    - some of those filled out from the form, some still don't reflect all the options from the form
    - when selecting create, want to create a change request 
    - asset configuration: what CI or info system components are impacted; goal is to link to select w insights schema
        - need to finish object schema & populate it (before?) linking it 
        - system: able to select systems and subsystems. would prefer cascading list 
    - change impacts
    - CM automation tool inputs
        - still needs to be built out; give users info req'd to fill out spreadsheet + provide link for spreadsheet too
- on the word doc, the 'red level' titles correlate w tabs on the form
    - has identified w comments 
        - issue types: what is going to be resolved from a business perspective once CR is implemented? 
            - need data field & choices on form (in Jira)
    - there's one section in the middle-ish missing
- once this is built out, hoping to be able to duplicate and add a couple bits for the high level CR form
- approval disapproval needs to be somewhere, but  not necessarily it's own tab 

- greg
    - identify gaps/changes in comments and update in jira
    - link to sandbox jira 
    - currently working on insight object schema 
        - may need assistance/guidance when time comes to adding data in there 
            - I SHOULD TEST OUT HOW TO IMPORT CSV INTO INSIGHT OBJECT SCHEMA 

# 20231122 working session 
Originating Source - checklist
- play around with checklist custom field 
Change Impact Notes

Project Work Plan
cascading drop down for recommended packaging - ask Lynn about this; Greg seems to recall Lynn offering that as a solution 

CM Automation Tool Inputs 
- is there a comment box? 

Additional Comments section - add that, leave it optional 

approval/disapproval
- approved/disapproved as buttons
- optional justification text box if disapproved 

# 20231124 solo working on it
- Lynn put in attachment and attachment URL field in CM Automation Tools. the fields don't seem to be showing up, and they're global fields, so how do I configure those to be project specific without setting defaults for the entire server? 
    - I made a multi-line text box with the link in it, and when I try to create a ticket, it seems to show one of Lynn's text boxes, but not mine
- it looks like in general you can make a multi-line text box display read-only text. 
    - i tried with a single line text box and it both cut it off and gave the option to edit the text 
- how to make required fields? I've read that removes the 'none' option from radio fields 
    - need to create a field configuration scheme 
- created LOGITAM Field Configuration Scheme, then found LOGITAM was already there. used that as default configuration scheme, then assigned change screen to it 
    - assigned change to it (somehow...?)
    - when I edit the fields, it says it only affects one project now, although it still shows all the screens that field is used in 
- on the template download link, the flavor text is part of the 'edit' on the main 'fields' screen, not part of the 'configure' 

# 20231128 working session 
## Greg
- talked to Lynn about change information > originating source/issue types addressed - able to be conditional 
    - an ask of drop down to a text box would require an outside plugin https://community.atlassian.com/t5/Jira-questions/How-Do-I-Use-Multi-Cascading-Fields-To-Display-A-Text-Box/qaq-p/962949
- could issue types link to a jira issue ticket 
- esp problem/defect or enhancement/change request and if those are selected, then link to an existing jira ticket 
    - could add notes in the field (in theory, my latest ones didn't seem to show up...) to direct users to attach (which I think is what I did)
    - can't link issues without admin in the ticket
        - https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-linking/
        - would have to just link the ticket to the issue after the fact 
- project work plan: recommended packaging + ability to select delivery method 
    - recommended packaging is one drop down, delivery method another 
        - has to be at least one, but could be multiple 
            - drop down where only one option can be selected, but if other, then a text box of some sort (how I've been doing it with the text boxes would be fine)
                - Could reach out to Cody at some point and ask if something like that is doable in the future - but for now, just stick with the text box for explainations 
- CM automation tool inputs 
    - option one preferred 
    - wants to see ability to attach document before creating ticket (is that possible) - if we can, then that should be a required field 
        - have to create ticket & attach it 
- does Approval/Disapproval need to be a tab, or included in a workflow when sent to approver 
    - remove the tab, then try via workflow for the approval/disapproval and comments 
        - do they have a workflow setup? 
            - we can create a workflow, we just need to know how to set it up - preferably starting point, end point, middle point: tell what workflow should begin as (open -> in progress -> closed [for example]) 
    - in system information (with the two drop down options) can the 'other' field be a text box? 
        - relies on the hierarchy in insights 
## Tabitha
- showed greg the insight linking that we figured out last time in the insight screen sharing session
- how to manage what attributes users can see from insight based on what groups they're in - doesn't necessarily want to show all roles/groups/etc attached to a user that a ticket is related to 
    - jira forum said that objectType visibility permissions can be adjusted, but not per asset https://community.atlassian.com/t5/Jira-questions/How-to-limit-access-to-an-asset-category-in-Insight/qaq-p/1950739
    - confirmed able to adjust roles/groups in objectType similar to how Schema can be adjusted

# 20231204 working session 
import errors
check perms for greg to see if he's able to import to insight - recap on that with screenshare here 
new req: CM automation tool input tab, new approach 
rather than having it as its own tab, create new tab w 'Configuration Item Information' and move affected configuration items, along w template download link, and be able to select existing CI & ability to input CI (radio button: existing or new CI) - want to be able to select a CI or have a 
name of ci/function/version/element type/etc - CI would be selected from CI DB 

1. Issue Type Addressed: Remove DIACAP as we currently only use RMF (feedback provided by Jason in one of our CR form reviews) (under issue types addressed on first tab)
    - done 
2. Change Reason: For Other, are we able to add a condition for a free text box?
    - tabitha: dynamic form, where based on field, another field comes up 
        - in service desk, lynn was doing cascading - if you choose an option, other options open up 
        - cody did a bunch of dynamic forms in setting up their service desk 
            - extension -> dynamic forms 
3. System: For Other, are we able to add a condition for a free text box?
    - dynamic text box possible at all? 
- project work plan: able to add attachment? 
    - can we add a description to instruct the user when/were to add the attachment 
Project Work Plan: Are we able to add an area to upload attachments, if there are any relevant to the CR?

tabitha: please make sure that fields are available through field editor on the specific project 

tabitha: approver workflow; project settings -> workflows (showed LOGITIISD) -> there's one with approvals. when it was config'd, it would tend to get lost & not sure where ticket was. has used service request instead. Question: there's an approver w automation. when it goes from in progress to waiting for approval, how to config that and figure out approvers 

done 
update CM automation tool input tab
    - done 
research how to make fields available to admin users of specific projects - I asked the NL chat 
    - she's referring to custom field editor 
        - issues -> field editor 
        - for me to edit it, cog -> manage apps -> customfield editor -> permission editor 
            - kyle wasn't able to add a custom field from zephyr 
                - hypothesis: zephyr & insight fields can't be linked to permission editor 
            - if the field does come up, edit it, then add their group under context permissions 
    *look into this more* 
        - I tried googling, but haven't come on the right string to get what I want. My queries: 
            - jira custom field editor insight field
            - can't add some fields to permission editor insight field jira
            - jira permission editor insight field
            - jira "permission editor" insight field
research if there's any way to do dynamic text boxes - need to ask Paul & Tina 
    - only way to do that in create/edit screen, if box isn't filled, then doesn't show on view (which is the opposite of what they're trying to do)

## To do: 
- research: for approvers, how do you pick what users can approve things? 
    project settings -> permissions -> ?
    - try creating a test ticket and seeing who it gets approved to - ask Tabitha if she's okay with it, or if she wants to define via insight
        - see if there's a way to define which user should pick it or if it gets automatically assigned  

- Configuration Item Information fields
    - Affected Configuration Items (description): For exisiting CIs, please select from the above dropdown list/search bar. To add a new CI, please enter the CI information in the fields below.
    - xAdd New Configuration Items (title, but not sure it's doable)(maybe single line text box "fill values below?") - the way I did it is not my favorite 
    - xHardware (another title; how to do?)
        - xHostname (textbox, single line for the ones that don't otherwise specify something) 
        - xName 
        - xPurpose 
        - xFirmware/OS Version 
        - xModel 
        - xHardware Type (dropdown: physical, virtual)
        - xEnvironment (dropdown: DDIL Lite, NAVAIR, Mobile Client)
        - xNetwork
    - xSoftware (another title)
        - xName 
        - xAcronym
        - xVersion
        - xFunction 
        - xPROD (dropdown: true/false)
- in field configuration, description can be edited. Options can't be though(?). This is also the spot to make it required or not 

## 20231211 Jira-LIFT/CM team huddle 
- remove template download link field 
- insights imports: to perform import, doesn't give abaility to import or sync immediately. Have to configure a cron job, rather than doing it with a click of a button 