#Information
 - Title: The Call of Aelantir
 - ID: new_sun_cult.148
#Description
The Call of Aelantir
#Options

___
##[Root.Monarch.GetName] should publicly express [Root.Monarch.GetHerHis] enthusiasm.

###AI weighting:
AI weights this option at 33
 - Multiplied by 100 if has personality is ai colonialist
 - Multiplied by 10 if has ruler has personality is expansionist personality
 - Multiplied by 10 if has ruler has personality is navigator personality
 - Multiplied by 5 if has ruler has personality is naive personality
 - Multiplied by 0 if does not have num of total ports is 1


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 2</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_aelantir_enthusiast</li><li>duration = 1825</li></ul></ul>

___
##[Root.Monarch.GetName] should refrain from making any comment for now.

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has ruler has personality is careful personality
 - Multiplied by 10 if has ruler has personality is free thinker personality


###Efects:<ul><li>add prestige = 10</li><li>add ruler modifier:</li><ul><li>name = nsc_aelantir_neutral</li><li>duration = 1825</li></ul></ul>

___
##[Root.Monarch.GetName] should make a speech to calm down the general frenzy.

###AI weighting:
AI weights this option at 33
 - Multiplied by 10 if has ruler has personality is zealot personality
 - Multiplied by 5 if has ruler has personality is strict personality
 - Multiplied by 5 if has ruler has personality is silver tongue personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>add prestige = -10</li></ul>
