#Information
 - Title: The Plundering of [Root.GetName]
 - ID: spirits.010
#Description
The Plundering of [Root.GetName]
#Options

___
##The secrets of the so-called Gods are ours!

###Available if:
<li>owner:</li><ul><li>has estate estate_artificers</li><li>Any of the following:</li><ul><li>artifice has points for basic is yes</li><li>has estate privilege artifice_invention_korashi_drills</li></ul></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if has religion is high philosophy


###Efects:<ul><li>owner:</li><ul><li>If does not have estate privilege is artifice invention korashi drills:</li><ul><li>set estate privilege = artifice_invention_korashi_drills</li></ul></ul></ul>

___
##End this barbarous despoiling

###Available if:
<li>owner:</li><ul><li>has estate estate_artificers</li></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 2 if has owner has religion group is halessi
 - Multiplied by 10 if has owner has religion group is raheni


###Efects:<ul><li>hidden effect:</li><ul><li>clr province flag [temple_being_plundered](../flags/temple_being_plundered.md)</li><li>clr province flag [permanent_precursor_relics](../flags/permanent_precursor_relics.md)</li><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = num_precursor_relics</li><li>value = 1</li></ul></ul></ul><li>set from saved trade goods = yes</li></ul>

___
##Interesting...if only we could make our own Korashi Drills.

###Available if:
<li>None of the following:</li><ul><li>owner:</li><ul><li>has estate estate_artificers</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>hidden effect:</li><ul><li>clr province flag [temple_being_plundered](../flags/temple_being_plundered.md)</li><li>clr province flag [permanent_precursor_relics](../flags/permanent_precursor_relics.md)</li><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = num_precursor_relics</li><li>value = 1</li></ul></ul></ul><li>set from saved trade goods = yes</li></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_plundering_of_root_getname_1](the_plundering_of_root_getname_1.md)
