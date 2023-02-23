#Information
 - Title: Disgruntled Sun Elf Officers
 - ID: new_sun_cult.153
#Description
Disgruntled Sun Elf Officers
#Options

___
##Let them go.

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has personality is ai colonialist
 - Multiplied by 10 if has ruler has personality is expansionist personality
 - Multiplied by 5 if has ruler has personality is naive personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>add manpower = -5</li><li>add army tradition = -5</li><li>country gets the modifier nsc_officers_left for 10 years</li></ul>

___
##Force them to stay.

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has ruler has personality is strict personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>country gets the modifier nsc_disgruntled_officers for 10 years</li><li>If has num of owned provinces with has culture is sun elf, and num of owned provinces with has value is 1:</li><ul><li>If random owned province has culture is sun elf:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul><li>else:</li><ul><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul></ul>

___
##Reform the army to convince them to stay.

###AI weighting:
AI weights this option at 33
 - Multiplied by 5 if has ruler has personality is tactical genius personality
 - Multiplied by 5 if has ruler has personality is martial educator personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -2</li></ul><li>add mil power = -100</li><li>add army tradition = 5</li></ul>

___
##Let [Root.Monarch.GetName] speak to them.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is charismatic_negotiator_personality</li><li>ruler has personality  is silver_tongue_personality</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>country gets the modifier nsc_bullshited_officers for 10 years</li></ul>
