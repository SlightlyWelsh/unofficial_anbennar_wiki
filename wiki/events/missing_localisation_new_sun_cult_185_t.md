#Information
 - Title: Missing localisation: new_sun_cult_185_t
 - ID: new_sun_cult.185
#Description

#Options

___
##Missing localisation: new_sun_cult_185_a

###Efects:<ul><li>If has FROM has exists, and is not subject, and is subject of type is tributary state; and FROM is not lesser in union:</li><ul><li>If is not controlled by the AI:</li><ul><li>FROM:</li><ul><li>change variable:</li><ul><li>which = nscInvestigationOf_@ROOT</li><li>value = 1</li></ul><li>set variable:</li><ul><li>which = nscPerCentInvestigationOf_@ROOT</li><li>which = nscInvestigationOf_@ROOT</li></ul><li>divide variable:</li><ul><li>which = nscPerCentInvestigationOf_@ROOT</li><li>value = 24</li></ul><li>multiply variable:</li><ul><li>which = nscPerCentInvestigationOf_@ROOT</li><li>value = 100</li></ul></ul></ul></ul><li>else:</li><ul><li>If does not have country flag is [nsc_investigation_stopped_@FROM](../flags/nsc_investigation_stopped_from.md):</li><ul><li>set country flag [nsc_investigation_stopped_@FROM](../flags/nsc_investigation_stopped_from.md)</li><li>If has exists is FROM:</li><ul><li>FROM:</li><ul><li>clr country flag [nsc_is_investigated_by_@ROOT](../flags/nsc_is_investigated_by_root.md)</li></ul></ul><li>the event [Investigation in [From.From.GetName] Cancelled](../events/investigation_in_from_from_getname_cancelled.md) happens</li></ul></ul></ul>
