#Information
 - Title: Investigation in [From.GetName] Over
 - ID: new_sun_cult.189
#Description
Investigation in [From.GetName] Over
#Options

___
##Excellent.

###Efects:<ul><li>custom tooltip = nsc_global_investigation_progress_faster</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>set country flag [nsc_was_fully_investigated_by_@ROOT](../flags/nsc_was_fully_investigated_by_root.md)</li><li>clr country flag [nsc_is_investigated_by_@ROOT](../flags/nsc_is_investigated_by_root.md)</li><li>change variable:</li><ul><li>which = investigationAgainstVar</li><li>value = -1</li></ul><li>the event [Investigation from [From.GetName] Over](../events/investigation_from_from_getname_over.md) happens</li></ul><li>nsc remove investigation ongoing modifier = yes</li><li>hidden effect:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = nscLocalInvestigationProgressVar</li><li>value = 1</li></ul></ul><li>calculate local investigation impact = yes</li></ul></ul></ul>
