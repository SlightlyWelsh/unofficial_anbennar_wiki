#Information
 - Title: Enforce our Rule
 - ID: cutdown.8
#Description
Enforce our Rule
#Options

___
##We shall break them

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = federation_plunge_into_war_tooltip</li><li>If has country modifier is federation gearing up:</li><ul><li>add yearly manpower = 15</li></ul><li>else:</li><ul><li>add yearly manpower = 10</li></ul><li>hidden effect:</li><ul><li>declare war with cb:</li><ul><li>who = event_target:cutdown_country</li><li>casus belli = cb_federation_war</li></ul><li>If every known country has country flag is [federation_blue](../flags/federation_blue.md):</li><ul><li>join all offensive wars of = ROOT</li></ul><li>If every known country has country flag is [federation_red](../flags/federation_red.md):</li><ul><li>join all defensive wars of = event_target:cutdown_country</li></ul></ul></ul>
