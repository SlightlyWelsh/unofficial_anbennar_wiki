#Information
 - Title: Enuuk Followers, Assemble!
 - ID: fed_religious.14
#Description
Enuuk Followers, Assemble!
#Options

___
##There will be only war

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = enuuk_religious_war_tooltip</li><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>declare war with cb:</li><ul><li>who = event_target:kodaveLeader</li><li>casus belli = cb_federation_religious_war</li></ul></ul><li>If every known country has country flag is [enuuk_faction](../flags/enuuk_faction.md), and does not have country flag is [enuuk_leader](../flags/enuuk_leader.md):</li><ul><li>join all offensive wars of = ROOT</li></ul><li>event target:yukelLeader:</li><ul><li>declare war with cb:</li><ul><li>who = ROOT</li><li>casus belli = cb_federation_religious_war</li></ul><li>declare war with cb:</li><ul><li>who = event_target:kodaveLeader</li><li>casus belli = cb_federation_religious_war</li></ul></ul><li>If every known country has country flag is [enuuk_faction](../flags/enuuk_faction.md), and does not have country flag is [enuuk_leader](../flags/enuuk_leader.md):</li><ul><li>join all defensive wars of = ROOT</li></ul><li>If every known country has country flag is [kodave_faction](../flags/kodave_faction.md), and does not have country flag is [kodave_leader](../flags/kodave_leader.md):</li><ul><li>join all defensive wars of = event_target:kodaveLeader</li></ul><li>If every known country has country flag is [yukel_faction](../flags/yukel_faction.md), and does not have country flag is [yukel_leader](../flags/yukel_leader.md):</li><ul><li>join all offensive wars of = event_target:yukelLeader</li></ul></ul></ul>
