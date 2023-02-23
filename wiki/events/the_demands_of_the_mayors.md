#Information
 - Title: The Demands of the Mayors
 - ID: new_sun_cult.59
#Description
The Demands of the Mayors
#Options

___
##Refuse. There is only one sun in the sky, and there must be only one court.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.1 if does not have manpower is 1
 - Multiplied by 0.1 if is at war
 - Multiplied by 0.75 if has incident variable value has incident is incident bulwar under threat, and incident variable value has value is 2


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 1</li></ul><li>event target:nsc mayor target 1:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>add unrest = 10</li></ul><li>event target:nsc mayor target 2:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul><li>add unrest = 10</li></ul></ul>

___
##Allow it. We will put the freed-up scribes to better use.

###AI weighting:
AI weights this option at 66
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -1
 - Multiplied by 0.75 if does not have incident variable value has incident is incident bulwar under threat, and incident variable value has value is -2
 - Multiplied by 0.1 if has tag is F25


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>event target:nsc mayor target 1:</li><ul><li>add local autonomy = 25</li><li>add unrest = -5</li></ul><li>event target:nsc mayor target 2:</li><ul><li>add local autonomy = 25</li><li>add unrest = -5</li></ul></ul>
