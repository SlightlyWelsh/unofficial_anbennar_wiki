#Information
 - Title: Demands From the Surani Nobility
 - ID: flavor_azka_sur.19
#Description
Demands From the Surani Nobility
#Options

___
##Give up to their demands

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_half_a_king</li><li>value = 2</li></ul><li>change estate land share:</li><ul><li>estate = all</li><li>share = 10</li></ul><li>country gets the modifier azka_sur_concessions for 10 years</li></ul>

___
##These are unacceptable

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_half_a_king</li><li>value = -1</li></ul><li>custom tooltip = azka_sur_nobles_angered_tt</li><li>hidden effect:</li><ul><li>change variable:</li><ul><li>noblesPissiness = 1</li></ul></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_nobles</li><li>desc = azka_sur_refused_concessions</li><li>loyalty = -20</li><li>duration = 3650</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_church</li><li>desc = azka_sur_refused_concessions</li><li>loyalty = -20</li><li>duration = 3650</li></ul></ul></ul>
