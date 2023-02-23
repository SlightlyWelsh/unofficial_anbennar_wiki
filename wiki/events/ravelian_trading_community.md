#Information
 - Title: Ravelian Trading Community
 - ID: new_sun_cult.213
#Description
Ravelian Trading Community
#Options

___
##What harm can come from more - and more lucrative - trade?

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change adm = 1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change dip = 1</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>change mil = 1</li></ul>

###Efects:<ul><li>goto = ravelian_province</li><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -2</li></ul><li>event target:ravelian province:</li><ul><li>add permanent province modifier:</li><ul><li>name = nsc_ravelian_society</li><li>duration = -1</li></ul></ul></ul>

___
##Whatever their merit, they do not belong in [ravelian_province.GetName].

###AI weighting:
AI weights this option at 45
 - Multiplied by 5 if isolationism is 3


###Efects:<ul><li>custom tooltip = nsc_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 1</li></ul><li>country gets the modifier nsc_kept_control_of_trade for 10 years</li><li>event target:ravelian province:</li><ul><li>set province flag [denied_ravelian_society](../flags/denied_ravelian_society.md)</li></ul></ul>

___
##Ban Ravelians from holding title to land to see these communities all nipped in the bud.

###AI weighting:
AI weights this option at 45
 - Multiplied by 2 if isolationism is 3
 - Multiplied by 5 if isolationism is 4


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>custom tooltip = nsc_ravelian_communities_disabled_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 4</li></ul><li>country gets the modifier nsc_kept_control_of_trade for 10 years</li><li>set country flag [nsc_banned_ravelian_communities](../flags/nsc_banned_ravelian_communities.md)</li></ul>
