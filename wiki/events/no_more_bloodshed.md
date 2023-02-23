#Information
 - Title: No More Bloodshed
 - ID: cutdown.9
#Description
No More Bloodshed
#Options

___
##The Federation Leader Triumphs

###Available if:
<li>has country flag [federation_blue_leader](../flags/federation_blue_leader.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation gain 5 points = yes</li><li>If every known country has country flag is [federation_blue](../flags/federation_blue.md):</li><ul><li>lake federation gain 2 points = yes</li></ul><li>If every known country has country flag is [federation_red](../flags/federation_red.md):</li><ul><li>lake federation lose 2 points = yes</li></ul><li>event target:cutdown country:</li><ul><li>lake federation lose 10 points = yes</li><li>country gets the modifier federation_cutdown for 50 years</li><li>custom tooltip = cutdown_give_back_all_province_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is southern isles region, and has region is northern isles region:</li><ul><li>set province flag [debug_province](../flags/debug_province.md)</li><li>remove core = event_target:cutdown_country</li><li>add core = previous_owner</li><li>cede province = previous_owner</li></ul><li>If asia has province flag is [debug_province](../flags/debug_province.md), and  has owned by is event target:cutdown country:</li><ul><li>add core = event_target:cutdown_country</li><li>clr province flag [debug_province](../flags/debug_province.md)</li></ul></ul></ul></ul>

___
##[cutdown_country.GetName] Victory

###Available if:
<li>has country flag [federation_red_leader](../flags/federation_red_leader.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>lake federation gain 5 points = yes</li><li>If every known country has country flag is [federation_red](../flags/federation_red.md):</li><ul><li>lake federation gain 2 points = yes</li></ul><li>If every known country has country flag is [federation_blue](../flags/federation_blue.md):</li><ul><li>lake federation lose 2 points = yes</li></ul><li>If random known country has country flag is [federation_blue_leader](../flags/federation_blue_leader.md):</li><ul><li>lake federation lose 10 points = yes</li></ul></ul>
