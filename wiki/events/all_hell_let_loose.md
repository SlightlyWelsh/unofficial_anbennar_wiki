#Information
 - Title: All Hell Let Loose
 - ID: fed_religious.39
#Description
All Hell Let Loose
#Options

___
##We must teach them the ways of peace...

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = yukel_religious_war_tooltip</li><li>hidden effect:</li><ul><li>ROOT:</li><ul><li>declare war with cb:</li><ul><li>who = event_target:enuukLeader</li><li>casus belli = cb_federation_religious_war</li></ul><li>declare war with cb:</li><ul><li>who = event_target:kodaveLeader</li><li>casus belli = cb_federation_religious_war</li></ul></ul><li>If every known country has country flag is [yukel_faction](../flags/yukel_faction.md), and does not have country flag is [yukel_leader](../flags/yukel_leader.md):</li><ul><li>join all offensive wars of = ROOT</li></ul><li>If every known country has country flag is [enuuk_faction](../flags/enuuk_faction.md), and does not have country flag is [enuuk_leader](../flags/enuuk_leader.md):</li><ul><li>join all defensive wars of = event_target:enuukLeader</li></ul><li>If every known country has country flag is [kodave_faction](../flags/kodave_faction.md), and does not have country flag is [kodave_leader](../flags/kodave_leader.md):</li><ul><li>join all defensive wars of = event_target:kodaveLeader</li></ul><li>If every known country has country modifier is lake federation member:</li><ul><li>the event ˻fed_religious.40˼ happens</li></ul><li>the event ˻fed_religious.40˼ happens</li></ul></ul>
