#Information
 - Title: Appease your Vassals
 - ID: new_sun_cult.63
#Description
Appease your Vassals
#Options

___
##Lower the tax. They need their money more than we do.

###Available if:
<li>None of the following:</li><ul><li>has country modifier nsc_lowered_vassal_levies</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>country gets the modifier nsc_lowered_vassal_levies for 10 years</li><li>every subject country:</li><ul><li>country gets the modifier nsc_lowered_vassal_levies_vassal for 10 years</li></ul><li>clr country flag [nsc_appeasing_vassals](../flags/nsc_appeasing_vassals.md)</li></ul>

___
##Lower the levy, their soldiers can be used to protect their own lands.

###Available if:
<li>None of the following:</li><ul><li>has country modifier nsc_lowered_vassal_troops</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>country gets the modifier nsc_lowered_vassal_troops for 10 years</li><li>every subject country:</li><ul><li>country gets the modifier nsc_lowered_vassal_troops_vassal for 10 years</li></ul><li>clr country flag [nsc_appeasing_vassals](../flags/nsc_appeasing_vassals.md)</li></ul>

___
##Prepare some propaganda, to remind them of our status as the Chosen.

###Available if:
<li>num of missionaries is at least 1</li><li>any subject country:</li><ul><li>religion is bulwari_sun_cult</li><li>None of the following:</li><ul><li>isolationism is at least 4</li></ul></ul><li>has dlc "Mandate of Heaven"</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have liberty desire is 50
 - Multiplied by 0 if does not have country modifier is nsc lowered vassal levies
 - Multiplied by 0 if does not have country modifier is nsc lowered vassal troops


###Efects:<ul><li>the event [Propaganda Campaign](../events/propaganda_campaign.md) happens</li></ul>

___
##Go Back.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>highlight = yes</li><li>If is controlled by the AI:</li><ul><li>country gets the modifier nsc_ai_took_vassal_decision for 5 years</li></ul></ul>
