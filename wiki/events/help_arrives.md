#Information
 - Title: Help Arrives?
 - ID: subject_interaction_events.3
#Description
Help Arrives?
#Options

___
##[From.Monarch.GetName] of [From.Country.GetName] sent us gold and soldiers!

###Available if:
<li>has country flag [si_pretender_help_flag](../flags/si_pretender_help_flag.md)</li>

###Efects:<ul><li>add treasury = 100</li><li>add manpower = 2</li><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_help</li></ul></ul><li>clr country flag [si_pretender_help_flag](../flags/si_pretender_help_flag.md)</li></ul>

___
##[From.Monarch.GetName] refused to send us help!

###Available if:
<li>has country flag [si_no_help_flag](../flags/si_no_help_flag.md)</li>

###Efects:<ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_refused_send_help</li></ul></ul><li>clr country flag [si_no_help_flag](../flags/si_no_help_flag.md)</li></ul>
