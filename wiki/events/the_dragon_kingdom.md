#Information
 - Title: The Dragon Kingdom
 - ID: ynn_events.17
#Description
The Dragon Kingdom
#Options

___
##It is time to bury the antlers.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>remove country modifier = ynn_diplo</li><li>If has ynnic iosahar is 1:</li><ul><li>custom tooltip = ynn_17_tooltip</li><li>hidden effect:</li><ul><li>If every subject country is subject of type is ynnic iosahar, and  has primary culture is rzentur, and does not have country flag is [ynn_civil_war_iosahar](../flags/ynn_civil_war_iosahar.md):</li><ul><li>remove country modifier = ynn_diplo</li><li>ROOT:</li><ul><li>create subject:</li><ul><li>subject type = vassal</li><li>subject = PREV</li></ul></ul></ul><li>every subject country:</li><ul><li>add liberty desire = 20</li><li>add trust:</li><ul><li>who = ROOT</li><li>value = -10</li></ul></ul></ul><li>If has saved event target is iosahar ynn 17, and  has any subject country is subject of type is ynnic iosahar, and any subject country has country flag is [ynn_civil_war_iosahar](../flags/ynn_civil_war_iosahar.md); and  has any subject country is subject of type is ynnic iosahar, and does not have primary culture is rzentur; and does not have country flag is [ynn_civil_war_iosahar](../flags/ynn_civil_war_iosahar.md); and any subject country has liberty desire is 20:</li><ul><li>custom tooltip = ynn_17_tooltip_really_good_idea</li><li>hidden effect:</li><ul><li>event target:iosahar ynn 17:</li><ul><li>set country flag [ynn_civil_war_iosahar](../flags/ynn_civil_war_iosahar.md)</li><li>the event [Overlord Infringes on Tradition](../events/overlord_infringes_on_tradition.md) happens</li></ul></ul></ul><li>Else if has saved event target is iosahar ynn 17:</li><ul><li>hidden effect:</li><ul><li>event target:iosahar ynn 17:</li><ul><li>remove country modifier = ynn_diplo</li><li>ROOT:</li><ul><li>create subject:</li><ul><li>subject type = vassal</li><li>subject = PREV</li></ul></ul><li>clr country flag [ynn_civil_war_iosahar](../flags/ynn_civil_war_iosahar.md)</li></ul><li>If every subject country is subject of type is ynnic iosahar, and does not have primary culture is rzentur:</li><ul><li>remove country modifier = ynn_diplo</li><li>ROOT:</li><ul><li>create subject:</li><ul><li>subject type = vassal</li><li>subject = PREV</li></ul></ul></ul></ul></ul></ul><li>country gets the modifier ruling_like_dragons for 20 years</li></ul>

___
##We will conquer the Ynnics using their laws.

###Available if:
<li>ynnic iosahar is at least 2</li>

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if does not have tag is G23

