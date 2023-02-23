#Information
 - Title: Ravelian Societies
 - ID: new_sun_cult.214
#Description
Ravelian Societies
#Options

___
##Intriguing. Make sure I see their latest findings.

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###Efects:<ul><li>goto = ravelian_province</li><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -1</li></ul><li>event target:ravelian province:</li><ul><li>add permanent province modifier:</li><ul><li>name = nsc_ravelian_society</li><li>duration = -1</li></ul></ul></ul>

___
##One drop of poison pollutes the whole barrel. Ban these societies!

###AI weighting:
AI weights this option at 90
 - Multiplied by 2 if isolationism is 3
 - Multiplied by 5 if isolationism is 4


###Efects:<ul><li>goto = ravelian_province</li><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 1</li></ul><li>event target:ravelian province:</li><ul><li>set province flag [denied_ravelian_society](../flags/denied_ravelian_society.md)</li></ul></ul>
