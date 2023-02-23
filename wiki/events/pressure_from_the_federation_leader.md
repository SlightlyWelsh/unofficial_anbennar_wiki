#Information
 - Title: Pressure from the Federation Leader
 - ID: goldisland.2
#Description
Pressure from the Federation Leader
#Options

___
##Give it Back

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.01 if has country flag is [unlawful_ultakal](../flags/unlawful_ultakal.md)


###Efects:<ul><li>add treasury = -500</li><li>If has tag is J06:</li><ul><li>J07:</li><ul><li>add treasury = 500</li></ul><li>5239:</li><ul><li>remove core = J06</li><li>cede province = J07</li><li>add core = J07</li></ul><li>hidden effect:</li><ul><li>J06:</li><ul><li>country gets the modifier ultakal_decree until otherwise removed</li></ul><li>J07:</li><ul><li>country gets the modifier ultakal_decree until otherwise removed</li></ul><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>hidden effect:</li><ul><li>J07:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul><li>Else if has tag is J07:</li><ul><li>J06:</li><ul><li>add treasury = 500</li></ul><li>5239:</li><ul><li>remove core = J07</li><li>cede province = J06</li><li>add core = J06</li></ul><li>hidden effect:</li><ul><li>J06:</li><ul><li>country gets the modifier ultakal_decree until otherwise removed</li></ul><li>J07:</li><ul><li>country gets the modifier ultakal_decree until otherwise removed</li></ul><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>hidden effect:</li><ul><li>J06:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul><li>else:</li><ul><li>5239:</li><ul><li>remove core = ROOT</li><li>cede province = event_target:country</li><li>add core = event_target:country</li></ul><li>event target:country:</li><ul><li>add treasury = 500</li></ul></ul><li>custom tooltip = restablish_decree_tooltip</li><li>hidden effect:</li><ul><li>clr global flag [federation_crisis_goldisland](../flags/federation_crisis_goldisland.md)</li></ul><li>hidden effect:</li><ul><li>set global flag [federation_golden_island_timer](../flags/federation_golden_island_timer.md)</li></ul></ul>

___
##Ultakal, as it should always have been, is ours

###AI weighting:
AI weights this option at 15
 - Multiplied by 2 if has country flag is [unlawful_ultakal](../flags/unlawful_ultakal.md)


###Efects:<ul><li>hidden effect:</li><ul><li>set global flag [federation_crisis](../flags/federation_crisis.md)</li></ul><li>the event [The Refusal](../events/the_refusal.md) happens</li></ul>
