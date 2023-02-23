#Information
 - Title: The Aftermath
 - ID: coup_in_palace_events.6
#Description
The Aftermath
#Options

___
##What now?

###Available if:
<li>custom trigger tooltip:</li><ul><li>tooltip is plot_succeeded_tooltip</li><li>has country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li></ul>

###Efects:<ul><li>If has consort regency:</li><ul><li>kill consort = yes</li><li>remove heir:</li><ul></ul><li>define ruler:</li><ul><li>max random adm = 3</li><li>max random dip = 3</li><li>max random mil = 3</li><li>claim = 5</li></ul></ul><li>else:</li><ul><li>custom tooltip = estate_regent_prevails_tt</li><li>hidden effect:</li><ul><li>change estate regent to ruler = yes</li></ul></ul><li>end disaster = coup_attempt_disaster</li><li>clr country flag [burgher_coup](../flags/burgher_coup.md)</li><li>clr country flag [church_coup](../flags/church_coup.md)</li><li>clr country flag [noble_coup](../flags/noble_coup.md)</li><li>clr country flag [coup_attempt_starts](../flags/coup_attempt_starts.md)</li><li>clr country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li><li>clr country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li><li>clr country flag [plot_ended_flag](../flags/plot_ended_flag.md)</li><li>hidden effect:</li><ul><li>country gets the modifier recent_coup_modifier for 20 years</li></ul></ul>

___
##The crown is victorious!

###Available if:
<li>custom trigger tooltip:</li><ul><li>tooltip is plot_failed_tooltip</li><li>has country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li></ul>

###Efects:<ul><li>end disaster = coup_attempt_disaster</li><li>add legitimacy = 25</li><li>add stability or adm power = yes</li><li>clr country flag [burgher_coup](../flags/burgher_coup.md)</li><li>clr country flag [church_coup](../flags/church_coup.md)</li><li>clr country flag [noble_coup](../flags/noble_coup.md)</li><li>clr country flag [coup_attempt_starts](../flags/coup_attempt_starts.md)</li><li>clr country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li><li>clr country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li><li>clr country flag [plot_ended_flag](../flags/plot_ended_flag.md)</li><li>hidden effect:</li><ul><li>country gets the modifier recent_coup_modifier for 20 years</li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_aftermath_1](the_aftermath_1.md)
