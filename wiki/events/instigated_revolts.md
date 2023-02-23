#Information
 - Title: Instigated Revolts
 - ID: new_sun_cult.168
#Description
Instigated Revolts
#Options

___
##Send some riot squads

###Efects:<ul><li>nsc increase tension medium effect = yes</li><li>owner:</li><ul><li>set country flag [nsc_instigated_revolts](../flags/nsc_instigated_revolts.md)</li><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -20</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour</li></ul></ul><li>add unrest = 10</li><li>If has owner is not controlled by the AI:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 1</li></ul></ul><li>hidden effect:</li><ul><li>event target:nsc target country:</li><ul><li>set country flag [nsc_instigated_revolts_on_@ROOT](../flags/nsc_instigated_revolts_on_root.md)</li><li>the event ˻new_sun_cult.169˼ happens</li></ul></ul></ul>
