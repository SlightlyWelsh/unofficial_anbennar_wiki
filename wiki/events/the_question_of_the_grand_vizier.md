#Information
 - Title: The Question of the Grand Vizier
 - ID: rahenraj.2100
#Description
The Question of the Grand Vizier
#Options

___
##Keep the current Grand Vizier of [current_vizier.GetName]

###Available if:
<li>any subject country:</li><ul><li>has country flag [raj_vizier](../flags/raj_vizier.md)</li></ul><li>has country flag [vizier_nomination_on_new_raja](../flags/vizier_nomination_on_new_raja.md)</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have check variable has which is vizierScore, and check variable has which is event target:shortlisted vizier 1


###Efects:<ul><li>goto = current_vizier_capital</li><li>custom tooltip = raj_vizier_stats_current_tt</li><li>raj cohesion change absolute:</li><ul><li>amount = 10</li></ul><li>set country flag [raj_same_vizier](../flags/raj_same_vizier.md)</li></ul>

___
##Nominate the [current_vizier.Monarch.GetTitle] of [current_vizier.GetName], heir of the previous Grand Vizier

###Available if:
<li>any subject country:</li><ul><li>has country flag [raj_vizier](../flags/raj_vizier.md)</li></ul><li>None of the following:</li><ul><li>has country flag [vizier_nomination_on_new_raja](../flags/vizier_nomination_on_new_raja.md)</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if does not have check variable has which is vizierScore, and check variable has which is event target:shortlisted vizier 1


###Efects:<ul><li>goto = current_vizier_capital</li><li>custom tooltip = raj_vizier_stats_current_tt</li><li>raj cohesion change absolute:</li><ul><li>amount = 5</li></ul><li>raj vizier sway change:</li><ul><li>amount = -10</li></ul><li>set country flag [raj_same_vizier](../flags/raj_same_vizier.md)</li><li>clr country flag [raj_swayed_senaptia](../flags/raj_swayed_senaptia.md)</li><li>clr country flag [raj_gathered_ministries](../flags/raj_gathered_ministries.md)</li><li>clr country flag [raj_outmaneuvered_raja](../flags/raj_outmaneuvered_raja.md)</li><li>clr country flag [raj_discredited_raja](../flags/raj_discredited_raja.md)</li><li>clr country flag [raj_became_raja_confident](../flags/raj_became_raja_confident.md)</li></ul>

___
##Nominate the [shortlisted_vizier_1.Monarch.GetTitle] of [shortlisted_vizier_1.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_1</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>goto = shortlisted_vizier_1_capital</li><li>custom tooltip = raj_vizier_stats_1_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_1</li></ul></ul>

___
##Nominate the [shortlisted_vizier_2.Monarch.GetTitle] of [shortlisted_vizier_2.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_2</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_2_capital</li><li>custom tooltip = raj_vizier_stats_2_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_2</li></ul></ul>

___
##Nominate the [shortlisted_vizier_3.Monarch.GetTitle] of [shortlisted_vizier_3.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_3</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_3_capital</li><li>custom tooltip = raj_vizier_stats_3_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_3</li></ul></ul>

___
##Nominate the [shortlisted_vizier_4.Monarch.GetTitle] of [shortlisted_vizier_4.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_4</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_4_capital</li><li>custom tooltip = raj_vizier_stats_4_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_4</li></ul></ul>

___
##Nominate the [shortlisted_vizier_5.Monarch.GetTitle] of [shortlisted_vizier_5.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_5</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_5_capital</li><li>custom tooltip = raj_vizier_stats_5_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_5</li></ul></ul>

___
##Nominate the [shortlisted_vizier_6.Monarch.GetTitle] of [shortlisted_vizier_6.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_6</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_6_capital</li><li>custom tooltip = raj_vizier_stats_6_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_6</li></ul></ul>

___
##Nominate the [shortlisted_vizier_7.Monarch.GetTitle] of [shortlisted_vizier_7.GetName]

###Available if:
<li>has saved event target shortlisted_vizier_7</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>goto = shortlisted_vizier_7_capital</li><li>custom tooltip = raj_vizier_stats_7_tt</li><li>raj vizier nomination effects:</li><ul><li>scope = event_target:shortlisted_vizier_7</li></ul></ul>
