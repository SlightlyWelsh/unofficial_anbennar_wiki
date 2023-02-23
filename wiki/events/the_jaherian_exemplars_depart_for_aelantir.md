#Information
 - Title: The Jaherian Exemplars Depart for Aelantir
 - ID: new_sun_cult.147
#Description
The Jaherian Exemplars Depart for Aelantir
#Options

___
##Send them a farewell gift.

###AI weighting:
AI weights this option at 25
 - Multiplied by 25 if has personality is ai colonialist
 - Multiplied by 5 if has ruler has personality is expansionist personality
 - Multiplied by 5 if has ruler has personality is navigator personality
 - Multiplied by 0 if does not have treasury is 25


###Efects:<ul><li>custom tooltip = nsc_incident_aelantir_start_tt</li><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>add treasury = -25</li><li>If has exists is H66:</li><ul><li>H66:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>sea zone:</li><ul><li>discover country = ROOT</li></ul></ul><li>capital scope:</li><ul><li>every empty neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul><li>If has exists is H67:</li><ul><li>H67:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>sea zone:</li><ul><li>discover country = ROOT</li></ul></ul><li>capital scope:</li><ul><li>every neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul></ul>

___
##Send some men with them, so we may take part in the rediscovery.

###Available if:
<li>manpower is at least 3</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 25 if has personality is ai colonialist
 - Multiplied by 5 if has ruler has personality is expansionist personality
 - Multiplied by 5 if has ruler has personality is navigator personality


###Efects:<ul><li>custom tooltip = nsc_incident_aelantir_start_tt</li><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>add manpower = -3</li><li>If has exists is H66:</li><ul><li>H66:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>sea zone:</li><ul><li>discover country = ROOT</li></ul></ul><li>capital scope:</li><ul><li>every empty neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul><li>If has exists is H67:</li><ul><li>H67:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>sea zone:</li><ul><li>discover country = ROOT</li></ul></ul><li>capital scope:</li><ul><li>every empty neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul></ul>

___
##Send them men to take part and a gift to show our good will.

###Available if:
<li>manpower is at least 3</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 100 if has personality is ai colonialist
 - Multiplied by 10 if has ruler has personality is expansionist personality
 - Multiplied by 10 if has ruler has personality is navigator personality
 - Multiplied by 0 if does not have treasury is 25


###Efects:<ul><li>custom tooltip = nsc_incident_aelantir_start_tt</li><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 2</li></ul><li>add treasury = -25</li><li>add manpower = -3</li><li>If has exists is H66:</li><ul><li>H66:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_big_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>every empty neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul><li>If has exists is H67:</li><ul><li>H67:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_big_support_exemplars</li></ul><li>capital scope:</li><ul><li>discover country = ROOT</li></ul><li>capital scope:</li><ul><li>every empty neighbor province:</li><ul><li>discover country = ROOT</li></ul></ul></ul></ul></ul>

___
##This is none of our concern, our home is Bulwar.

###AI weighting:
AI weights this option at 25
 - Multiplied by 10 if has ruler has personality is zealot personality
 - Multiplied by 5 if has ruler has personality is strict personality
 - Multiplied by 10 if has ruler has personality is careful personality


###Efects:<ul><li>custom tooltip = nsc_incident_aelantir_start_tt</li><li>add prestige = -5</li></ul>

___
##Brand them as deserters who have abandoned their duties to the people of Bulwar!

###AI weighting:
AI weights this option at 25
 - Multiplied by 10 if has ruler has personality is zealot personality
 - Multiplied by 0 if has ruler has personality is kind hearted personality


###Efects:<ul><li>custom tooltip = nsc_incident_aelantir_start_tt</li><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -1</li></ul><li>country gets the modifier nsc_criticised_exemplars for 10 years</li><li>If has exists is H66:</li><ul><li>H66:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_criticised_exemplars_opinion</li></ul></ul></ul><li>If has exists is H67:</li><ul><li>H67:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_criticised_exemplars_opinion</li></ul></ul></ul></ul>
