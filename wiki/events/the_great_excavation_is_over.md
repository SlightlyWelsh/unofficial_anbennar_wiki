#Information
 - Title: The Great Excavation is Over!
 - ID: new_sun_cult.206
#Description
The Great Excavation is Over!
#Options

___
##This will greatly benefit our mages.

###Available if:
<li>has country flag [nsc_excavation_successful](../flags/nsc_excavation_successful.md)</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 10 if has ruler has personality is mage personality
 - Multiplied by 5 if has ruler has personality is careful personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = -2</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>country gets the modifier nsc_mage_relics for 25 years</li><li>If every owned province has province flag is [nsc_excavation_target](../flags/nsc_excavation_target.md):</li><ul><li>add permanent province modifier:</li><ul><li>name = genie_relics</li><li>duration = -1</li></ul></ul><li>remove country modifier = nsc_excavation_underway</li><li>remove country modifier = nsc_great_excavation_underway</li></ul>

___
##This will greatly benefit our artificers.

###Available if:
<li>has country flag [nsc_excavation_successful](../flags/nsc_excavation_successful.md)</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 10 if has ruler has personality is free thinker personality
 - Multiplied by 5 if has ruler has personality is scholar personality
 - Multiplied by 0 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = 2</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>country gets the modifier nsc_artificer_relics for 25 years</li><li>If every owned province has province flag is [nsc_excavation_target](../flags/nsc_excavation_target.md):</li><ul><li>add permanent province modifier:</li><ul><li>name = genie_relics</li><li>duration = -1</li></ul></ul><li>remove country modifier = nsc_excavation_underway</li><li>remove country modifier = nsc_great_excavation_underway</li></ul>

___
##This will greatly benefit all who work in [Root.GetName].

###Available if:
<li>has country flag [nsc_excavation_successful](../flags/nsc_excavation_successful.md)</li>

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>country gets the modifier nsc_both_relics for 25 years</li><li>If every owned province has province flag is [nsc_excavation_target](../flags/nsc_excavation_target.md):</li><ul><li>add permanent province modifier:</li><ul><li>name = genie_relics</li><li>duration = -1</li></ul></ul><li>remove country modifier = nsc_excavation_underway</li><li>remove country modifier = nsc_great_excavation_underway</li></ul>

___
##The State will keep hold of the relics.

###Available if:
<li>has country flag [nsc_excavation_successful](../flags/nsc_excavation_successful.md)</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 5 if has ruler has personality is greedy personality
 - Multiplied by 0 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 35


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -5</li></ul><li>If every owned province has province flag is [nsc_excavation_target](../flags/nsc_excavation_target.md):</li><ul><li>add permanent province modifier:</li><ul><li>name = genie_relics</li><li>duration = -1</li></ul><li>add province modifier:</li><ul><li>name = nsc_state_relics</li><li>duration = 9125</li></ul></ul><li>remove country modifier = nsc_excavation_underway</li><li>remove country modifier = nsc_great_excavation_underway</li></ul>

___
##Have you checked everywhere?

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_excavation_successful](../flags/nsc_excavation_successful.md)</li></ul>

###Efects:<ul><li>add prestige = -5</li><li>remove country modifier = nsc_excavation_underway</li><li>remove country modifier = nsc_great_excavation_underway</li></ul>
