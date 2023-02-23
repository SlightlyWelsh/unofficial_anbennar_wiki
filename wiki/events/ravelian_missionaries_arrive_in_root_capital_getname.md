#Information
 - Title: Ravelian Missionaries Arrive in [Root.Capital.GetName]
 - ID: new_sun_cult.211
#Description
Ravelian Missionaries Arrive in [Root.Capital.GetName]
#Options

___
##[Root.Monarch.GetName] will be happy to learn from them

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change adm = 1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = 1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change mil = 1</li></ul>

###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -3</li></ul><li>country gets the modifier nsc_ravelian_influence for 10 years</li></ul>

___
##Let them stay, their knowledge might be beneficial to the city

###AI weighting:
AI weights this option at 45


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -2</li></ul><li>country gets the modifier nsc_ravelian_influence for 10 years</li></ul>

___
##We must defend our faith, expel them!

###AI weighting:
AI weights this option at 45
 - Multiplied by 5 if isolationism is 3


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 1</li></ul><li>add stability or adm power = yes</li><li>country gets the modifier nsc_expelled_ravelian_missionaries for 10 years</li></ul>
