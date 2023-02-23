#Information
 - Title: Amussu – The Silent Awakens
 - ID: new_sun_cult.265
#Description
Amussu – The Silent Awakens
#Options

___
##Relics of power and God-Kings awakening? Surael watch over us all.

###Efects:<ul><li>custom tooltip = nsc_amussu_incident_starts_tt</li><li>hidden effect:</li><ul><li>event target:amussu province target:</li><ul><li>add permanent province modifier:</li><ul><li>name = nsc_amussu_province</li><li>duration = -1</li><li>desc = nsc_until_incident_end_tt</li></ul></ul><li>6106:</li><ul><li>add province triggered modifier = amussu_incident_monthly_pulse</li></ul><li>save global event target as = nsc_incident_target</li><li>set country flag [nsc_has_amussu_incident](../flags/nsc_has_amussu_incident.md)</li><li>set country flag [nsc_amussu_has_0_relics](../flags/nsc_amussu_has_0_relics.md)</li><li>REB:</li><ul><li>set variable:</li><ul><li>which = amussuPowerVar</li><li>value = 40</li></ul><li>set variable:</li><ul><li>which = amussuNbRelicsVar</li><li>value = 0</li></ul></ul><li>nsc set relic provinces effect = yes</li><li>nsc set next relic target effect = yes</li></ul><li>amussus grave surroundings:</li><ul><li>add devastation = 30</li></ul><li>REB:</li><ul><li>set country flag [nsc_amussu_invulnerable](../flags/nsc_amussu_invulnerable.md)</li></ul><li>the event [First Calamity: The Bloody Suran](../events/first_calamity_the_bloody_suran.md) happens</li></ul>
