#Information
 - Title: Yamima's Gambit
 - ID: flavour_bulwar_tag.9
#Description
Yamima's Gambit
#Options

___
##Accept her offer

###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_naqtazan</li><li>value = -3</li></ul><li>F25:</li><ul><li>add opinion:</li><ul><li>who = F39</li><li>modifier = bulwar_conspired_against</li></ul><li>remove historical friend = ROOT</li><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>remove historical friend = F25</li></ul><li>set ai attitude:</li><ul><li>attitude = attitude_hostile</li><li>who = ROOT</li><li>locked = no</li></ul></ul><li>custom tooltip = bulwar_will_leave_naqtazan_tt</li><li>clr country flag [naqtazan_member](../flags/naqtazan_member.md)</li></ul><li>F41:</li><ul><li>custom tooltip = bulwar_will_join_naqtazan_tt</li><li>create alliance = ROOT</li><li>If every known country does not have tag is F25; and  has country flag is [naqtazan_member](../flags/naqtazan_member.md):</li><ul><li>create alliance = PREV</li></ul><li>set country flag [naqtazan_member](../flags/naqtazan_member.md)</li><li>grant independence = yes</li><li>hidden effect:</li><ul><li>If every known country has war with is PREV:</li><ul><li>white peace = PREV</li></ul></ul></ul></ul>

___
##Denounce her to Sareyand

###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>F25:</li><ul><li>If every known country has country flag is [naqtazan_member](../flags/naqtazan_member.md):</li><ul><li>create alliance = PREV</li></ul></ul><li>add incident variable value:</li><ul><li>incident = incident_naqtazan</li><li>value = 1</li></ul><li>reverse add opinion:</li><ul><li>who = F25</li><li>modifier = bulwar_denounced_yamima</li></ul></ul>
