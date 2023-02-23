#Information
 - Title: Our Vassal's Smugglers
 - ID: subject_interaction_events.15
#Description
Our Vassal's Smugglers
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Force them to stop the smuggling, now!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = 10</li><li>If random subject country has country flag is [si_smuggler_vassal_flag](../flags/si_smuggler_vassal_flag.md):</li><ul><li>set country flag [si_stop_smuggling_flag](../flags/si_stop_smuggling_flag.md)</li><li>the event [Busted!](../events/busted.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_smuggling_hindered</li></ul><li>tooltip:</li><ul><li>remove country modifier = si_state_smuggling</li></ul><li>clr country flag [si_smuggler_vassal_flag](../flags/si_smuggler_vassal_flag.md)</li></ul></ul>

___
##They may continue this small endeavor.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add years of income = 0.25</li><li>add prestige = -10</li><li>If every subject country does not have country flag is [si_smuggler_vassal_flag](../flags/si_smuggler_vassal_flag.md):</li><ul><li>add liberty desire = 5</li></ul><li>If random subject country has country flag is [si_smuggler_vassal_flag](../flags/si_smuggler_vassal_flag.md):</li><ul><li>set country flag [si_small_smuggling_flag](../flags/si_small_smuggling_flag.md)</li><li>the event [Busted!](../events/busted.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_small_smuggling_ok</li></ul><li>clr country flag [si_smuggler_vassal_flag](../flags/si_smuggler_vassal_flag.md)</li></ul></ul>
