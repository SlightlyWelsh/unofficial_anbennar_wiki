#Information
 - Title: Reforming our Training
 - ID: new_sun_cult.71
#Description
Reforming our Training
#Options

___
##Follow the old guard's advice and focus on lightly trained troops and skilled officers.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.75 if has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 1
 - Multiplied by 0.75 if has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 2
 - Multiplied by 5 if has tag is F25


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 1</li></ul><li>country gets the modifier nsc_leader_training for 10 years</li></ul>

___
##Follow the vanguard's advice and focus on long and rigorous training in small groups.

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>country gets the modifier nsc_rigorous_training for 10 years</li></ul>

___
##Rely on the humans and focus on lightly trained troops.

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2
 - Multiplied by 0.5 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -3
 - Multiplied by 0.5 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -4
 - Multiplied by 0.1 if has tag is F25


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>country gets the modifier nsc_fast_training for 10 years</li></ul>
