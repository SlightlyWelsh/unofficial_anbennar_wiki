#Information
 - Title: Warehouse Arson Attack
 - ID: new_sun_cult.166
#Description
Warehouse Arson Attack
#Options

___
##Oh my aching head

###Efects:<ul><li>nsc increase tension small effect = yes</li><li>owner:</li><ul><li>set country flag [nsc_arson](../flags/nsc_arson.md)</li><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -15</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour</li></ul></ul><li>add devastation = 20</li><li>add permanent province modifier:</li><ul><li>name = nsc_burned_warehouse</li><li>duration = 1825</li></ul><li>hidden effect:</li><ul><li>event target:nsc target country:</li><ul><li>set country flag [nsc_arson_on_@ROOT](../flags/nsc_arson_on_root.md)</li><li>the event [Accusations](../events/accusations.md) happens</li></ul></ul></ul>
