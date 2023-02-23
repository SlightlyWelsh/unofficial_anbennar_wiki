#Information
 - Title: The Demands of the Merchants
 - ID: new_sun_cult.60
#Description
The Demands of the Merchants
#Options

___
##Refuse. Pittance or not, that money is ours.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30
 - Multiplied by 0.75 if has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 2


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li></ul></ul>

___
##Lower taxes? Cheeky humans, tax them even more!

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 2</li></ul><li>add treasury = 100</li><li>country gets the modifier nsc_high_tolls for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul><li>event target:nsc merchant target 1:</li><ul><li>add unrest = 10</li></ul><li>event target:nsc merchant target 2:</li><ul><li>add unrest = 10</li></ul></ul>

___
##Allow it. They are right, richer humans means more taxable wealth anyway.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -1
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2
 - Multiplied by 0.1 if has tag is F25


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>country gets the modifier nsc_less_tolls for 10 years</li><li>event target:nsc merchant target 1:</li><ul><li>add unrest = -5</li></ul><li>event target:nsc merchant target 2:</li><ul><li>add unrest = -5</li></ul></ul>
