#Information
 - Title: [From.Country.GetName] asks for help
 - ID: subject_interaction_events.2
#Description
[From.Country.GetName] asks for help
#Options

___
##Send them gold and soldiers.

###Efects:<ul><li>add treasury = -100</li><li>add manpower = -2</li><li>FROM:</li><ul><li>set country flag [si_pretender_help_flag](../flags/si_pretender_help_flag.md)</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_sent_help</li></ul><li>the event [Help Arrives?](../events/help_arrives.md) happens</li><li>tooltip:</li><ul><li>add treasury = 100</li><li>add manpower = 2</li></ul></ul></ul>

___
##They will have to deal with it themselves.

###Efects:<ul><li>FROM:</li><ul><li>set country flag [si_no_help_flag](../flags/si_no_help_flag.md)</li><li>the event [Help Arrives?](../events/help_arrives.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_refused_send_help</li></ul></ul></ul>
