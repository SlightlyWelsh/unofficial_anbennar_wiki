This page has the same name as others. For full listing see bottom of [the base page](shall_we_yield.md).

#Information
 - Title: Shall we Yield?
 - ID: goldisland.10
#Description
Shall we Yield?
#Options

___
##We shall not yield either!

###AI weighting:
AI weights this option at 100
 - Multiplied by 1.15 if does not have check variable has power difference is 0
 - Multiplied by 1.15 if does not have check variable has power difference is -10
 - Multiplied by 1.15 if does not have check variable has power difference is -20
 - Multiplied by 1.15 if does not have check variable has power difference is -30
 - Multiplied by 1.15 if does not have check variable has power difference is -40
 - Multiplied by 1.15 if does not have check variable has power difference is -50
 - Multiplied by 1.15 if does not have check variable has power difference is -80
 - Multiplied by 1.15 if does not have check variable has power difference is -100


###Efects:<ul><li>custom tooltip = we_shall_not_yield_either_tooltip</li><li>hidden effect:</li><ul><li>set global flag [federation_golden_war](../flags/federation_golden_war.md)</li><li>event target:global fed illegitimate:</li><ul><li>declare war with cb:</li><ul><li>who = ROOT</li><li>casus belli = cb_federation_war_gold_island</li></ul></ul><li>If every country has country flag is [support_illegitimate](../flags/support_illegitimate.md):</li><ul><li>join all offensive wars of = event_target:global_fed_illegitimate</li></ul><li>If every country has country flag is [support_legitimate](../flags/support_legitimate.md):</li><ul><li>join all defensive wars of = ROOT</li></ul></ul></ul>

___
##We can't fight their numbers...

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.15 if has REB has check variable has power difference is 0
 - Multiplied by 1.15 if has REB has check variable has power difference is 10
 - Multiplied by 1.15 if has REB has check variable has power difference is 20
 - Multiplied by 1.15 if has REB has check variable has power difference is 30
 - Multiplied by 1.15 if has REB has check variable has power difference is 40
 - Multiplied by 1.15 if has REB has check variable has power difference is 50
 - Multiplied by 1.15 if has REB has check variable has power difference is 80
 - Multiplied by 1.15 if has REB has check variable has power difference is 100


###Efects:<ul><li>lake federation lose 2 points = yes</li><li>add prestige = -20</li><li>If every country has country flag is [support_legitimate](../flags/support_legitimate.md):</li><ul><li>add prestige = -5</li><li>lake federation lose 2 points = yes</li></ul><li>event target:global fed illegitimate:</li><ul><li>add prestige = 20</li><li>lake federation gain 2 points = yes</li></ul><li>If every country has country flag is [support_illegitimate](../flags/support_illegitimate.md):</li><ul><li>add prestige = 10</li><li>lake federation gain 2 points = yes</li></ul><li>5239:</li><ul><li>remove province triggered modifier = federation_unlawful_occupation</li></ul><li>hidden effect:</li><ul><li>clr global flag [federation_crisis](../flags/federation_crisis.md)</li><li>clr global flag [federation_crisis_goldisland](../flags/federation_crisis_goldisland.md)</li><li>If every country has country modifier is lake federation member:</li><ul><li>clr country flag [leader_illegitimate](../flags/leader_illegitimate.md)</li><li>clr country flag [leader_legitimate](../flags/leader_legitimate.md)</li><li>clr country flag [support_illegitimate](../flags/support_illegitimate.md)</li><li>clr country flag [support_legitimate](../flags/support_legitimate.md)</li><li>clr country flag [ultakal_owner](../flags/ultakal_owner.md)</li><li>clr country flag [unlawful_ultakal](../flags/unlawful_ultakal.md)</li><li>clr country flag [asked_illegitimate](../flags/asked_illegitimate.md)</li><li>clr country flag [asked_legitimate](../flags/asked_legitimate.md)</li></ul></ul></ul>
