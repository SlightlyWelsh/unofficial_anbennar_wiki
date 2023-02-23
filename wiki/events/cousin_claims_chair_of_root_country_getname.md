#Information
 - Title: Cousin Claims Chair of [Root.Country.GetName]
 - ID: subject_interaction_events.6
#Description
Cousin Claims Chair of [Root.Country.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Depose our cousin!

###Efects:<ul><li>If random subject country has country flag is [si_subject_state](../flags/si_subject_state.md):</li><ul><li>define ruler:</li><ul><li>dynasty = ROOT</li><li>culture = ROOT</li><li>religion = ROOT</li></ul><li>If random province has owned by is ROOT, and does not have a capital:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>friend = PREV</li><li>size = 1</li></ul></ul><li>clr country flag [si_subject_state](../flags/si_subject_state.md)</li></ul></ul>

___
##Try to bribe them.

###Efects:<ul><li>add corruption = 0.5</li><li>add treasury = -100</li><li>If random subject country has country flag is [si_subject_state](../flags/si_subject_state.md):</li><ul><li>add treasury = 100</li><li>clr country flag [si_subject_state](../flags/si_subject_state.md)</li></ul></ul>
