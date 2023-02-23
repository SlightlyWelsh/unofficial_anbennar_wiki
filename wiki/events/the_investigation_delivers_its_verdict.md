#Information
 - Title: The Investigation Delivers its Verdict
 - ID: new_sun_cult.207
#Description
The Investigation Delivers its Verdict
#Options

___
##Now let's get some formal guilds set up for further study!

###Available if:
<li>incident variable value:</li><ul><li>incident is incident_rise_of_artificery</li><li>value is at least 3</li></ul>

###Efects:<ul><li>country gets the modifier nsc_conceded_artificery until otherwise removed</li><li>decrease nsc isolation level = yes</li><li>custom tooltip = nsc_artificery_enabled_tt</li><li>set country flag [nsc_artificery_enabled](../flags/nsc_artificery_enabled.md)</li><li>end incident = incident_rise_of_artificery</li><li>hidden effect:</li><ul><li>the event [The Artificers of $COUNTRY$](../events/the_artificers_of_country.md) happens</li></ul></ul>

___
##We are already drafting plans for a new royal artificers guild!

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_rise_of_artificery</li><li>value is at least 3</li></ul></ul><li>incident variable value:</li><ul><li>incident is incident_rise_of_artificery</li><li>value is -2</li></ul>

###Efects:<ul><li>custom tooltip = nsc_artificery_semi_enabled_tt</li><li>set country flag [nsc_artificery_enabled](../flags/nsc_artificery_enabled.md)</li><li>set country flag [nsc_sun_elf_artificery](../flags/nsc_sun_elf_artificery.md)</li><li>end incident = incident_rise_of_artificery</li><li>hidden effect:</li><ul><li>the event [The Artificers of $COUNTRY$](../events/the_artificers_of_country.md) happens</li></ul></ul>

___
##I will sleep easier when these foul devices are eradicated.

###Available if:
<li>None of the following:</li><ul><li>incident variable value:</li><ul><li>incident is incident_rise_of_artificery</li><li>value is -2</li></ul></ul>

###Efects:<ul><li>country gets the modifier nsc_restricted_artificery until otherwise removed</li><li>increase nsc isolation level = yes</li><li>custom tooltip = nsc_artificery_banned_tt</li><li>If has estate is estate mages:</li><ul><li>If has estate privilege is estate mages battlemage academies:</li><ul><li>remove estate privilege = estate_mages_battlemage_academies</li></ul><li>set estate privilege = estate_mages_empowered_mages</li></ul><li>end incident = incident_rise_of_artificery</li></ul>
