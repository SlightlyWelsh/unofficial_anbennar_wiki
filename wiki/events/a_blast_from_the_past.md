#Information
 - Title: A Blast From The Past
 - ID: new_sun_cult.287
#Description
A Blast From The Past
#Options

___
##I wish to be worshipped as a God-King

###Available if:
<li>has country flag [nsc_beat_amussu](../flags/nsc_beat_amussu.md)</li>

###Efects:<ul><li>end incident = incident_silent_as_the_grave</li><li>If is chosen country is yes:</li><ul><li>increase nsc isolation level = yes</li></ul><li>else:</li><ul><li>decrease nsc isolation level = yes</li></ul><li>add stability or adm power = yes</li><li>country gets the modifier nsc_god_king_wish until otherwise removed</li><li>If has REB has check variable has which is amussuNbRelicsVar, and check variable has value is 1:</li><ul><li>the event [Amussu's Relics](../events/amussu_s_relics.md) happens</li></ul></ul>

___
##I wish to oversee a prosperous realm!

###Available if:
<li>has country flag [nsc_beat_amussu](../flags/nsc_beat_amussu.md)</li>

###Efects:<ul><li>end incident = incident_silent_as_the_grave</li><li>add stability or adm power = yes</li><li>country gets the modifier nsc_prosperity_wish until otherwise removed</li><li>If has REB has check variable has which is amussuNbRelicsVar, and check variable has value is 1:</li><ul><li>the event [Amussu's Relics](../events/amussu_s_relics.md) happens</li></ul></ul>

___
##I wish to ensure all my subjects rise!

###Available if:
<li>has country flag [nsc_beat_amussu](../flags/nsc_beat_amussu.md)</li>

###Efects:<ul><li>end incident = incident_silent_as_the_grave</li><li>If is chosen country is yes:</li><ul><li>decrease nsc isolation level = yes</li></ul><li>else:</li><ul><li>increase nsc isolation level = yes</li></ul><li>add stability or adm power = yes</li><li>country gets the modifier nsc_subjects_wish until otherwise removed</li><li>If has REB has check variable has which is amussuNbRelicsVar, and check variable has value is 1:</li><ul><li>the event [Amussu's Relics](../events/amussu_s_relics.md) happens</li></ul></ul>

___
##Surael, we have failed you...

###Available if:
<li>None of the following:</li><ul><li>has country flag [nsc_beat_amussu](../flags/nsc_beat_amussu.md)</li></ul>

###Efects:<ul><li>end incident = incident_silent_as_the_grave</li><li>custom tooltip = nsc_relics_lost_tt</li><li>reduce stability or adm power = yes</li><li>event target:amussu modifier target:</li><ul><li>add devastation = 100</li><li>add base tax = -2</li><li>add base production = -2</li><li>add base manpower = -2</li><li>set province flag [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md)</li><li>If every neighbor province does not have province flag is [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md):</li><ul><li>add devastation = 75</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li><li>set province flag [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md)</li><li>If every neighbor province does not have province flag is [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md):</li><ul><li>add devastation = 50</li><li>set province flag [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md)</li></ul><li>If every neighbor province does not have province flag is [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md):</li><ul><li>add devastation = 25</li><li>set province flag [nsc_amussu_devastation](../flags/nsc_amussu_devastation.md)</li></ul></ul></ul></ul>
