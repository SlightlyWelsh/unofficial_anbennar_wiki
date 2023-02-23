#Information
 - Title: Sun Elven Nobles Are Worried
 - ID: new_sun_cult.196
#Description
Sun Elven Nobles Are Worried
#Options

___
##'Artificery should not be allowed at all!'

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = -2</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_ruler_pro_ban</li><li>duration = 3650</li></ul></ul>

___
##'If artificery is allowed, only the Chosens will be able to use it.'

###AI weighting:
AI weights this option at 33
 - Multiplied by 5 if has ruler has personality is zealot personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = -1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_ruler_elitist</li><li>duration = 3650</li></ul></ul>

___
##'Only the investigation results will influence our choice.'

###AI weighting:
AI weights this option at 33
 - Multiplied by 5 if has ruler has personality is free thinker personality
 - Multiplied by 5 if has ruler has personality is scholar personality
 - Multiplied by 5 if has ruler has personality is careful personality
 - Multiplied by 0 if has ruler has personality is mage personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_rise_of_artificery</li><li>value = 1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul>
