#Information
 - Title: Missing localisation: ynn_events_20_t
 - ID: ynn_events.20
#Description

#Options

___
##Missing localisation: ynn_events_20_a

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [ynnic_debug_subjugation](../flags/ynnic_debug_subjugation.md)</li></ul><li>tooltip:</li><ul><li>FROM:</li><ul><li>create subject:</li><ul><li>subject type = ynnic_iosahar</li><li>subject = ROOT</li></ul></ul></ul><li>every subject country:</li><ul><li>If has junior union with is ROOT:</li><ul><li>break union = ROOT</li></ul><li>Else if is subject of type is ynnic iosahar, and has country modifier is ynn diplo:</li><ul><li>FROM:</li><ul><li>create subject:</li><ul><li>subject type = ynnic_iosahar</li><li>subject = PREV</li></ul></ul></ul><li>else:</li><ul><li>grant independence = yes</li></ul></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>If every known country has alliance with is FROM, and  has capital scope has superregion is ynn superregion:</li><ul><li>FROM:</li><ul><li>break alliance = PREV</li></ul></ul></ul></ul><li>If does not have country modifier is ynn diplo:</li><ul><li>country gets the modifier ynn_diplo until otherwise removed</li><li>If has country flag is [ynn_iosahar_breakup_debug](../flags/ynn_iosahar_breakup_debug.md):</li><ul><li>clr country flag [ynn_iosahar_breakup_debug](../flags/ynn_iosahar_breakup_debug.md)</li></ul><li>Else if has tag is G32, and  has reform is malacnar monarchy:</li><ul><li>FROM:</li><ul><li>the event [The Fate of Malacnar](../events/the_fate_of_malacnar.md) happens</li></ul></ul><li>else:</li><ul><li>FROM:</li><ul><li>the event [Partition [From.GetName]?](../events/partition_from_getname.md) happens</li></ul></ul></ul></ul>
