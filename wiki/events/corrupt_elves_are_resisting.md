#Information
 - Title: Corrupt Elves Are Resisting
 - ID: new_sun_cult.53
#Description
Corrupt Elves Are Resisting
#Options

___
##Well, it would be rude to refuse a gift...

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = 1</li></ul><li>add treasury = 150</li><li>add corruption = 2</li><li>random:</li><ul><li>chance = 50</li><li>add ruler personality = greedy_personality</li></ul><li>set country flag [nsc_took_bribe](../flags/nsc_took_bribe.md)</li></ul>

___
##This is truly unacceptable - strip them of their rank and send them to jail!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_bulwar_under_threat</li><li>value = -1</li></ul><li>If random owned province has culture is sun elf:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul><li>If random owned province has culture is sun elf:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul>
