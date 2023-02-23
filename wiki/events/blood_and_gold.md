#Information
 - Title: Blood and Gold
 - ID: goldisland.12
#Description
Blood and Gold
#Options

___
##Glory to [Root.GetName]!

###Available if:
<li>has country flag [leader_illegitimate](../flags/leader_illegitimate.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation gain 5 points = yes</li><li>add prestige = 20</li><li>5239:</li><ul><li>remove province triggered modifier = federation_unlawful_occupation</li></ul><li>If every country has country flag is [support_illegitimate](../flags/support_illegitimate.md):</li><ul><li>add prestige = 10</li><li>lake federation gain 2 points = yes</li></ul><li>event target:global fed legitimate:</li><ul><li>add prestige = -20</li><li>lake federation lose 2 points = yes</li></ul><li>If every country has country flag is [support_legitimate](../flags/support_legitimate.md):</li><ul><li>add prestige = -5</li><li>lake federation lose 2 points = yes</li></ul></ul>

___
##Missing localisation: goldisland_12_b

###Available if:
<li>has country flag [leader_legitimate](../flags/leader_legitimate.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation gain 5 points = yes</li><li>add prestige = 20</li><li>If every country has country flag is [support_legitimate](../flags/support_legitimate.md):</li><ul><li>add prestige = 10</li><li>lake federation gain 2 points = yes</li></ul><li>event target:global fed illegitimate:</li><ul><li>add prestige = -20</li><li>lake federation lose 2 points = yes</li></ul><li>If every country has country flag is [support_illegitimate](../flags/support_illegitimate.md):</li><ul><li>add prestige = -5</li><li>lake federation lose 2 points = yes</li></ul><li>If has tag is J06, and has tag is J07; and  does not have tag is J06; and does not have tag is J07; and  has J06 has exists; and  has J07 has exists:</li><ul><li>hidden effect:</li><ul><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>If has tag is J06:</li><ul><li>5239:</li><ul><li>remove core = J06</li><li>cede province = J07</li><li>add core = J07</li></ul><li>hidden effect:</li><ul><li>J07:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>clr country flag [unlawful_ultakal](../flags/unlawful_ultakal.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul><li>else:</li><ul><li>5239:</li><ul><li>remove core = J07</li><li>cede province = J06</li><li>add core = J06</li></ul><li>hidden effect:</li><ul><li>J06:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>clr country flag [unlawful_ultakal](../flags/unlawful_ultakal.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul><li>custom tooltip = restablish_decree_tooltip</li></ul><li>else:</li><ul><li>5239:</li><ul><li>remove core = owner</li><li>cede province = ROOT</li><li>add core = ROOT</li><li>remove province triggered modifier = federation_unlawful_occupation</li></ul></ul></ul>
