#Information
 - Title: Propaganda in [From.GetName] Over
 - ID: new_sun_cult.67
#Description
Propaganda in [From.GetName] Over
#Options

___
##Praise Surael!

###Available if:
<li>FROM:</li><ul><li>exists</li><li>None of the following:</li><ul><li>has country flag [nsc_propaganda_fail](../flags/nsc_propaganda_fail.md)</li></ul></ul>

###Efects:<ul><li>nsc remove influencing vassal modifier = yes</li><li>FROM:</li><ul><li>clr country flag [nsc_influenced_vassal_@ROOT](../flags/nsc_influenced_vassal_root.md)</li></ul></ul>

___
##That's a shame.

###Available if:
<li>FROM:</li><ul><li>Any of the following:</li><ul><li>does not exist</li><li>has country flag [nsc_propaganda_fail](../flags/nsc_propaganda_fail.md)</li></ul></ul>

###Efects:<ul><li>nsc remove influencing vassal modifier = yes</li><li>FROM:</li><ul><li>clr country flag [nsc_influenced_vassal_@ROOT](../flags/nsc_influenced_vassal_root.md)</li><li>clr country flag [nsc_propaganda_fail](../flags/nsc_propaganda_fail.md)</li></ul></ul>
