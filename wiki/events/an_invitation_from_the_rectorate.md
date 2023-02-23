#Information
 - Title: An Invitation from the Rectorate
 - ID: new_sun_cult.217
#Description
An Invitation from the Rectorate
#Options

___
##Send [Root.Heir.GetTitle] [Root.Heir.GetName] accompanied by the most amazing delegation seen in recent memory!

###Available if:
<li>has heir</li><li>heir age is at least 15</li>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>custom tooltip = nsc_send_heir_away_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -3</li></ul><li>add years of income = -0.5</li><li>add prestige = 15</li><li>exile heir as = exiled_heir_@ROOT</li><li>hidden effect:</li><ul><li>set ruler flag [was_ruler_when_heir_left](../flags/was_ruler_when_heir_left.md)</li><li>set country flag [nsc_sent_heir](../flags/nsc_sent_heir.md)</li><li>random list:</li><ul><li>50:</li><ul><li>the event ˻new_sun_cult.218˼ happens</li></ul><li>50:</li><ul><li>the event ˻new_sun_cult.219˼ happens</li></ul></ul></ul></ul>

___
##Send the most amazing delegation seen in recent memory!

###Available if:
<li>Any of the following:</li><ul><li>does not have heir</li><li>None of the following:</li><ul><li>heir age is at least 15</li></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if does not haveolationism is 2
 - Multiplied by 5 if does not haveolationism is 1
 - Multiplied by 0 if is vassal, and  has overlord has religion is bulwari sun cult; and does not have liberty desire is 50


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -3</li></ul><li>add years of income = -0.5</li><li>add prestige = 15</li><li>hidden effect:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event ˻new_sun_cult.218˼ happens</li></ul><li>50:</li><ul><li>the event ˻new_sun_cult.219˼ happens</li></ul></ul></ul></ul>

___
##We shall go, but we cannot spare a huge delegation

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>custom tooltip = nsc_chosen_role_down_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = -2</li></ul><li>add years of income = -0.2</li><li>add prestige = 5</li><li>hidden effect:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event ˻new_sun_cult.218˼ happens</li></ul><li>50:</li><ul><li>the event ˻new_sun_cult.219˼ happens</li></ul></ul></ul></ul>

___
##Ignore them.

###AI weighting:
AI weights this option at 30
 - Multiplied by 10 if isolationism is 4


###Efects:<ul><li>custom tooltip = nsc_much_chosen_role_up_tt</li><li>add incident variable value:</li><ul><li>incident = incident_spread_of_ravelianism</li><li>value = 3</li></ul><li>If every known country has religion is ravelian:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_refused_rectorate_invitation</li></ul></ul><li>hidden effect:</li><ul><li>the event ˻new_sun_cult.220˼ happens</li></ul></ul>
