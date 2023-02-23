#Information
 - Title: Famous Adventurer Returns
 - ID: new_sun_cult.156
#Description
Famous Adventurer Returns
#Options

___
##Hail them as a hero! After all, they did bring loot.

###AI weighting:
AI weights this option at 45
 - Multiplied by 5 if has ruler has personality is entrepreneur personality
 - Multiplied by 5 if has ruler has personality is expansionist personality
 - Multiplied by 5 if has ruler has personality is navigator personality
 - Multiplied by 5 if has ruler has personality is careful personality


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 1</li></ul><li>add prestige = 10</li><li>add splendor = 50</li></ul>

___
##Hail them as a hero and subsidise their future adventures!

###Available if:
<li>sailors is at least 200</li>

###AI weighting:
AI weights this option at 45
 - Multiplied by 100 if has personality is ai colonialist
 - Multiplied by 10 if has ruler has personality is entrepreneur personality
 - Multiplied by 10 if has ruler has personality is expansionist personality
 - Multiplied by 10 if has ruler has personality is navigator personality
 - Multiplied by 0 if does not have years of income is 0.25


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = 2</li></ul><li>add years of income = -0.25</li><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 10</li></ul><li>create conquistador:</li><ul><li>tradition = 50</li></ul><li>add prestige = 25</li><li>add splendor = 75</li></ul>

___
##So they are gifting us part of the loot, eh... Why not TAKE IT ALL!?

###AI weighting:
AI weights this option at 10
 - Multiplied by 50 if has ruler has personality is malevolent personality
 - Multiplied by 50 if has ruler has personality is greedy personality
 - Multiplied by 50 if has ruler has personality is cruel personality


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_call_of_aelantir</li><li>value = -2</li></ul><li>add years of income = 0.50</li><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -20</li></ul><li>add prestige = -25</li><li>add splendor = 100</li></ul>
