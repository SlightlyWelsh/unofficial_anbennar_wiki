This page has the same name as others. For full listing see bottom of [the base page](missing_localisation_spirits_006_t.md).

#Information
 - Title: Missing localisation: spirits_006_t
 - ID: spirits.500
#Description

#Options

___
##Missing localisation: spirits_006_a

###Available if:
<li>None of the following:</li><ul><li>religion is lefthand_path</li></ul>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>If has event target:temple quest target has province flag is [restart_temple_quest](../flags/restart_temple_quest.md):</li><ul><li>event target:temple quest target:</li><ul><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>clr province flag [restart_temple_quest](../flags/restart_temple_quest.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>Else if has any owned province has province modifier is temple heart trail:</li><ul><li>If random owned province has province modifier is temple heart trail:</li><ul><li>save event target as = temple_quest_target</li><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>else:</li><ul><li>If random owned province has province modifier is temple complex, and has province modifier is damaged temple complex, and has province modifier is derelict temple complex, and has province modifier is ruined temple complex:</li><ul><li>save event target as = temple_quest_target</li><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>the event [Temple Quest Preparations](../events/temple_quest_preparations.md) happens</li></ul>

___
##Missing localisation: spirits_006_a

###Available if:
<li>religion is lefthand_path</li>

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>If has event target:temple quest target has province flag is [restart_temple_quest](../flags/restart_temple_quest.md):</li><ul><li>event target:temple quest target:</li><ul><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>clr province flag [restart_temple_quest](../flags/restart_temple_quest.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>Else if has any owned province has province modifier is temple heart trail:</li><ul><li>If random owned province has province modifier is temple heart trail:</li><ul><li>save event target as = temple_quest_target</li><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>else:</li><ul><li>If random owned province has province modifier is temple complex, and has province modifier is damaged temple complex, and has province modifier is derelict temple complex; and does not have province modifier is temple heart discovered:</li><ul><li>save event target as = temple_quest_target</li><li>set province flag [temple_being_quested](../flags/temple_being_quested.md)</li><li>set variable:</li><ul><li>which = DaysSinceTempleEntryVar</li><li>value = 1</li></ul></ul></ul><li>the event [Temple Quest Preparations](../events/temple_quest_preparations.md) happens</li></ul>

___
##Missing localisation: spirits_006_a

###Available if:
<li>None of the following:</li><ul><li>religion is lefthand_path</li></ul>

###AI weighting:
AI weights this option at 67
 - Multiplied by 0 if has country flag is [first_temple_quest](../flags/first_temple_quest.md)
 - Multiplied by 0 if has any owned province has province modifier is temple heart trail

