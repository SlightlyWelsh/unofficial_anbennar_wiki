This page has the same name as others. For full listing see bottom of [the base page](assassination_attempt.md).

#Information
 - Title: Assassination Attempt
 - ID: new_sun_cult.161
#Description
Assassination Attempt
#Options

___
##Hire the best surgeons we can find!

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is rulerAdmVar, and export to variable has value is ADM; and variable arithmetic trigger has export to variable has which is rulerDipVar, and export to variable has value is DIP; and variable arithmetic trigger has export to variable has which is rulerMilVar, and export to variable has value is MIL; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerDipVar; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerMilVar; and variable arithmetic trigger has check variable has which is rulerAdmVar, and check variable has value is 9


###Efects:<ul><li>set country flag [nsc_assassination_attempt](../flags/nsc_assassination_attempt.md)</li><li>nsc increase tension large effect = yes</li><li>add treasury = -50</li><li>If has adm is 2:</li><ul><li>change adm = -2</li><li>set ruler flag [nsc_adm_2](../flags/nsc_adm_2.md)</li></ul><li>Else if has adm is 1:</li><ul><li>change adm = -1</li><li>set ruler flag [nsc_adm_1](../flags/nsc_adm_1.md)</li></ul><li>If has dip is 2:</li><ul><li>change dip = -2</li><li>set ruler flag [nsc_dip_2](../flags/nsc_dip_2.md)</li></ul><li>Else if has dip is 1:</li><ul><li>change dip = -1</li><li>set ruler flag [nsc_dip_1](../flags/nsc_dip_1.md)</li></ul><li>If has mil is 2:</li><ul><li>change mil = -2</li><li>set ruler flag [nsc_mil_2](../flags/nsc_mil_2.md)</li></ul><li>Else if has mil is 1:</li><ul><li>change mil = -1</li><li>set ruler flag [nsc_mil_1](../flags/nsc_mil_1.md)</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_wounded_ruler</li><li>duration = -1</li></ul><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -25</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour_big</li></ul></ul>

___
##Place our [Root.Monarch.GetTitle]'s fate in the hands of Surael

###AI weighting:
AI weights this option at 1
 - Multiplied by 100 if has variable arithmetic trigger has export to variable has which is rulerAdmVar, and export to variable has value is ADM; and variable arithmetic trigger has export to variable has which is rulerDipVar, and export to variable has value is DIP; and variable arithmetic trigger has export to variable has which is rulerMilVar, and export to variable has value is MIL; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerDipVar; and variable arithmetic trigger has change variable has which is rulerAdmVar, and change variable has which is rulerMilVar; and does not have check variable has which is rulerAdmVar, and check variable has value is 9
 - Multiplied by 0 if does not have heir age is 15
 - Multiplied by 0 if does not have stability is 0


###Efects:<ul><li>set country flag [nsc_assassination_attempt](../flags/nsc_assassination_attempt.md)</li><li>nsc increase tension large effect = yes</li><li>If has adm is 2:</li><ul><li>change adm = -2</li><li>set ruler flag [nsc_adm_2](../flags/nsc_adm_2.md)</li></ul><li>Else if has adm is 1:</li><ul><li>change adm = -1</li><li>set ruler flag [nsc_adm_1](../flags/nsc_adm_1.md)</li></ul><li>If has dip is 2:</li><ul><li>change dip = -2</li><li>set ruler flag [nsc_dip_2](../flags/nsc_dip_2.md)</li></ul><li>Else if has dip is 1:</li><ul><li>change dip = -1</li><li>set ruler flag [nsc_dip_1](../flags/nsc_dip_1.md)</li></ul><li>If has mil is 2:</li><ul><li>change mil = -2</li><li>set ruler flag [nsc_mil_2](../flags/nsc_mil_2.md)</li></ul><li>Else if has mil is 1:</li><ul><li>change mil = -1</li><li>set ruler flag [nsc_mil_1](../flags/nsc_mil_1.md)</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_wounded_ruler</li><li>duration = 270</li></ul><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -25</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>custom tooltip = nsc_ruler_may_die_tt</li><li>hidden effect:</li><ul><li>random:</li><ul><li>chance = 50</li><li>set ruler flag [nsc_ruler_will_die](../flags/nsc_ruler_will_die.md)</li></ul></ul></ul>
