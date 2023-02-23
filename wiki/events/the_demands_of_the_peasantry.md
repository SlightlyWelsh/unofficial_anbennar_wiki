#Information
 - Title: The Demands of the Peasantry
 - ID: new_sun_cult.61
#Description
The Demands of the Peasantry
#Options

___
##Refuse. The sun does not fear a spot of rain, nor do we fear their tantrum.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.75 if has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 2


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 1</li></ul><li>add adm power = 50</li><li>event target:nsc peasant target 1:</li><ul><li>add unrest = 10</li></ul><li>event target:nsc peasant target 2:</li><ul><li>add unrest = 10</li></ul></ul>

___
##Allow it. We are trying to win these people over, not turn them away.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -1
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2
 - Multiplied by 0.1 if has tag is F25


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>add adm power = -50</li><li>event target:nsc peasant target 1:</li><ul><li>add unrest = -5</li></ul><li>event target:nsc peasant target 2:</li><ul><li>add unrest = -5</li></ul></ul>
