#Information
 - Title: Kalyin's Will
 - ID: fed_religious.24
#Description
Kalyin's Will
#Options

___
##The Goddess' will we shall oblige!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>country gets the modifier lake_kalyin_zeal until otherwise removed</li><li>custom tooltip = kalyin_will_tooltip</li><li>hidden effect:</li><ul><li>set global flag [second_federation_religious_war](../flags/second_federation_religious_war.md)</li><li>declare war with cb:</li><ul><li>who = event_target:antiKalyin</li><li>casus belli = cb_federation_religious_war_kalyin</li></ul><li>If every known country has country modifier is lake federation member, and  has religion is kalyin worshippers:</li><ul><li>join all offensive wars of = ROOT</li><li>country gets the modifier lake_kalyin_zeal until otherwise removed</li></ul><li>If every known country has country modifier is lake federation member, and has religion is kodave followers, and has religion is enuuk followers, and has religion is yukel followers; and does not have country flag is [anti_kalyin_leader](../flags/anti_kalyin_leader.md):</li><ul><li>join all defensive wars of = event_target:antiKalyin</li></ul></ul></ul>
