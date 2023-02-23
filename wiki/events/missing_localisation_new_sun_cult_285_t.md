#Information
 - Title: Missing localisation: new_sun_cult_285_t
 - ID: new_sun_cult.285
#Description

#Options

___
##Missing localisation: new_sun_cult_285_a

###Efects:<ul><li>clr province flag [nsc_amussu_battle_tick](../flags/nsc_amussu_battle_tick.md)</li><li>remove province triggered modifier = nsc_amussu_battle_daily_pulse</li><li>If does not have num of units in province has who is REB, and num of units in province has amount is 1:</li><ul><li>If random country has country flag is [nsc_has_amussu_incident](../flags/nsc_has_amussu_incident.md):</li><ul><li>set country flag [nsc_beat_amussu](../flags/nsc_beat_amussu.md)</li><li>the event [A Blast From The Past](../events/a_blast_from_the_past.md) happens</li></ul></ul><li>Else if has REB has had country flag is [nsc_amussu_last_relic](../flags/nsc_amussu_last_relic.md) for 180 days:</li><ul><li>If random country has country flag is [nsc_has_amussu_incident](../flags/nsc_has_amussu_incident.md):</li><ul><li>the event [A Blast From The Past](../events/a_blast_from_the_past.md) happens</li></ul></ul><li>else:</li><ul><li>If random country has country flag is [nsc_has_amussu_incident](../flags/nsc_has_amussu_incident.md):</li><ul><li>the event [Defeat](../events/defeat.md) happens</li></ul></ul><li>owner:</li><ul><li>disband rebels = amussu_main_rebels</li></ul></ul>
