# https://issue.lift.mhpcc.hpc.mil/jira/browse/NLSD-15893

SECTION I - ORIGINATOR and SECTION III - SPECIFICATIONS:
Please allow the following fields to be shown (currently I cannot see them on the form)
	SECTION I:
		Submitted By
		Submitter Phone DCN
		Origination Date
		Estimated Hours
		Estimated Cost
		Date Sent

	SECTION III:
	Reason
	*NOTE: Is there any way to remove the verbiage "(text)" from the Impact field, honestly that just looks sloppy and it is obvious that it is a text field.
        -> when I looked at it and tried to edit, I could change the description but not the field name. field names can only be changed globally, which I did; Impact (text) to Impact

SECTION II - CONFIGURATION CONTROL (MS stands for Multiple Select)

Assigning new fields to all issue types, 445th project, and screens 23202 & 23203 tab 2 select
Mission Site: Site= ${Site} (REQUIRED)(SINGLE SELECT) 18800
`objectType="Mission Site"` - made it required in JSEE: CHANGE MANAGEMENT Default Field Configuration, and that affected the correct project 
Building: Site= ${Site} (REQUIRED)(SINGLE SELECT): 18802 
trying an Insight Referenced Object (single) field. Cannot force single select/radio buttons. I don't think that's the move. *how to create referenced filtering in insight object*. `objectType="Building"`
    `objectType = "Building" AND "Mission site" = ${Mission Site}`
    `Building = ${Building} AND "Mission site" = ${Mission Site}` both give error `<iql,Placeholder not supported in current context>` when I put them in the Filter Scope (iql). 
    `Filter Scope (IQL)             objectType="Building"`
    `Filter Issue Scope (IQL)       Building = ${Building} AND "Mission site" = ${Mission Site}`
    is legitimate code, but says no matches in ticket creation. Did just the mission site portion and got the same error. w no IQL issue scope, everything shows up. just doing building has not matches also. tried `Site=${Site}` in FIS, no matches 
    *is there somewhere I can test iql?* 
        https://issue.lift.mhpcc.hpc.mil/jira/secure/insight/search?filter=-1000&schema=17 
    *how do I force sorting based on what its properties are??* 
        https://www.youtube.com/watch?v=8oRZhGGB-ns
        under filters, for the object I want to sort on, i.e. buildings only on specific site, added 
        ` = ${customfield_18800}` with the custom field # correlating to the one of 
        `objectType = `
        Mission Site - that's where the variable comes from! :D 

is there a way when something is selected to sort the results below it by only what options are possible w/n the selection? 


*list parent object name in front of the child object label* 
xMission Capability Room: Building = ${Building} (REQUIRED)(SINGLE SELECT) 18803
	xCockpit: Room = ${Room} 18804
        xx added an insight custom field - multiple select w parent custom field 'mission capability room' and 'inbound references' and didn't even have options I could find in the insight schema... (per Paul Tierney's recommendation)
		xDisplay: Cockpit = ${Cockpit} (MS) 18808
            tried `"Cockpit" in ${customfield_18804}`; replacing `=` with `in` and no change
		xOther: Cockpit = ${Cockpit} (MS)
		xSim Hardware: Cockpit = ${Cockpit} (MS)
        `Cockpit = ${customfield_18804}`

	Flyer: Room = ${Room} 
    objectType = Flyer
    "Mission Capability Room" = ${customfield_18803}

	Mission Station: Room = ${Room} 
    objectType = "Mission Station"
    "Mission Capability Room" = ${customfield_18803}
        "Mission Station" = ${customfield_18812}
		xKVM Switch: Mission Station = ${Mission Station} (MS)
		xMonitor: Mission Station = ${Mission Station} (MS)
		xWorkstation: Mission Station = ${Mission Station} (MS)
            Mission Station Workstation Hard Drive: Room = ${Room} (MS)
		xOther: Mission Station = ${Mission Station} (MS)

        for all these child objects, I don't think he meant the name/parent label to be in the insight part, but that the actual description identified the relationship? 

FINISH HERE FOR TONIGHT

	Mission Rack: Room = ${Room}
    objectType = "Mission Rack"
    "Mission Capability Room" = ${customfield_18803}
        "Mission Rack" = ${customfield_18818}
		xBay Storage Server: Mission Rack = ${Mission Rack} (MS)
		xConsole: Mission Rack = ${Mission Rack} (MS)
		xInstrumentation: Mission Rack = ${Mission Rack} (MS)
		xKVM Switch: Mission Rack = ${Mission Rack} (MS)
		xNetwork Switch: Mission Rack = ${Mission Rack} (MS)
		xOther: Mission Rack = ${Mission Rack} (MS) (by having the secondary sort key, insight/jira is able to identify the correct Other field to grab)
		xPDU: Mission Rack = ${Mission Rack} (MS)
		xRack Mounted PC: Mission Rack = ${Mission Rack} (MS)
            xRack Mounted PC Hard Drive: Room = ${Room} (MS)
		xUPS: Mission Rack = ${Mission Rack} (MS)
		xWorkstation: Mission Rack = ${Mission Rack} (MS)
            xMission Rack Workstation Hard Drive: Room = ${Room} (MS) 
		xVideo Encoder: Mission Rack = ${Mission Rack} (MS)
        
	
    Virtual Air Threat: Room = ${Room}
    objectType = "Virtual Air Threat"
    "Mission Capability Room" = ${customfield_18803}
        "Virtual Air Threat" = ${customfield_18912}
		xMonitor: Virtual Air Threat = ${Virtual Air Threat} (MS)
		xOther: Virtual Air Threat = ${Virtual Air Threat} (MS)
		xWorkstation: Virtual Air Threat = ${Virtual Air Threat} (MS)
            xVAT Workstation Hard Drive : Room = ${Room} (MS)
		Sim Hardware: Virtual Air Threat = ${Virtual Air Threat} (MS)

Mission Station
  Workstation "Mission Station" = ${customfield_18815}
    xOperating System: Workstation = {$Workstation} (Single Select)
    
    xInstalled Software: Workstation = {$Workstation} (Multi Select)
Mission Rack
  Rack Mounted PC "Mission Rack" Workstation = ${customfield_18095}
    Operating System: Rack Mounted PC = {$Rack Mounted PC} (Single Select) RMPC
    Installed Software: Rack Mounted PC = {$Rack Mounted PC} (Multi Select) RMPC
  Workstation "Mission Rack" Workstation = ${customfield_18908}
    Operating System: Workstation = {$Workstation} (Single Select) (MR Workstation)
    Installed Software: Workstation = {$Workstation} (Multi Select) (MR Workstation)
Virtual Air Threat
  Workstation "Virtual Air Threat" Workstation = ${customfield_18915}
    Operating System: Workstation = {$Workstation} (Single Select) (VAT Workstation)
    Installed Software: Workstation = {$Workstation} (Multi Select) (VAT Workstation)


objectType = "Operating System"
objectType = "Installed Software"
    remember to re-organize all these guys - in both the view and the create issue screens 

for workstation, label it MS Workstation and change the Mission STation Configuration thing and see how it looks, for me and Matthew (also change the other applicable labels) 

# 20231216
approval processes - min of three approvals req'd for workflow 
flight chief -> security (give an approval + sometimes contingency) -> CCB chair 
currently, there's a check box and digital sign
wanting to move from digital sign?
- is there a way to (initiator will usually submit CR and do add'l work on it thruout the week). Save and submit 
    - possible to do via workflow? i.e., first set to 'still gathering info' then customer able to change to 'ready for review' 
- follow up on questions from the last 'info' meeting to team - find out by end of jan 
- ask team on how to set up approval workflows
- waiting for visio from matt on workflow + req'd fields 
- batch delete issues? 
- how to workflows 
    - box for 'Add approval.' doesn't show up https://confluence.atlassian.com/adminjiraserver/configuring-jira-service-management-approvals-938847527.html
    - user validator (JMWE) allows only specific roles/groups/etc to transition to approved 
        - no notifying of users - *NEED TO TALK TO CODY OR NATASHA* 