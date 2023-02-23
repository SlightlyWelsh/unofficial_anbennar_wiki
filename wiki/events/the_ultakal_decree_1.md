This page has the same name as others. For full listing see bottom of [the base page](the_ultakal_decree.md).

#Information
 - Title: The Ultakal Decree
 - ID: lake.43
#Description
The Ultakal Decree
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Give them the province

###AI weighting:
AI weights this option at 95
 - Multiplied by 10 if has ruler has personality is righteous personality
 - Multiplied by 1.5 if has ruler has personality is kind hearted personality
 - Multiplied by 1.5 if has ruler has personality is lawgiver personality


###Efects:<ul><li>add prestige = 5</li><li>hidden effect:</li><ul><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>If has tag is J06:</li><ul><li>5239:</li><ul><li>remove core = J06</li><li>cede province = J07</li><li>add core = J07</li></ul><li>hidden effect:</li><ul><li>J07:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul><li>else:</li><ul><li>5239:</li><ul><li>remove core = J07</li><li>cede province = J06</li><li>add core = J06</li></ul><li>hidden effect:</li><ul><li>J06:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul></ul></ul></ul>

___
##Keep it, because why not?

###Available if:
<li>None of the following:</li><ul><li>has global flag [federation_crisis](../flags/federation_crisis.md)</li></ul><li>any country:</li><ul><li>is lake federation leader is yes</li></ul>

###AI weighting:
AI weights this option at 5
 - Multiplied by 100 if has ruler has personality is malevolent personality
 - Multiplied by 5 if has ruler has personality is fierce negotiator personality
 - Multiplied by 3 if has ruler has personality is drunkard personality
 - Multiplied by 4 if has ruler has personality is greedy personality


###Efects:<ul><li>lake federation lose 2 points = yes</li><li>J06:</li><ul><li>remove country modifier = ultakal_decree</li></ul><li>J07:</li><ul><li>remove country modifier = ultakal_decree</li></ul><li>custom tooltip = break_ultakal_decree_tooltip</li><li>hidden effect:</li><ul><li>J06:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>J07:</li><ul><li>set country flag [ultakal_owner](../flags/ultakal_owner.md)</li></ul><li>set country flag [unlawful_ultakal](../flags/unlawful_ultakal.md)</li><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>the event [Missing localisation: goldisland_0_t](../events/missing_localisation_goldisland_0_t.md) happens</li></ul></ul>
