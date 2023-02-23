#Information
 - Title: Study Abjuration
 - ID: magic_study.1
#Description
Study Abjuration
#Options

___
##Spend more effort

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add adm power = -25</li><li>add dip power = -25</li><li>magic study start effect = yes</li><li>set ruler flag [ruler_studying_abjuration](../flags/ruler_studying_abjuration.md)</li><li>If has ruler flag is [patron_favored_abjuration](../flags/patron_favored_abjuration.md):</li><ul><li>custom tooltip = patron_xp_bonus_tt</li><li>update magic study experience modifier:</li><ul><li>value = 25</li></ul><li>set country flag [patron_xp_bonus](../flags/patron_xp_bonus.md)</li></ul><li>Else if has ruler flag is [patron_disfavored_abjuration](../flags/patron_disfavored_abjuration.md):</li><ul><li>custom tooltip = patron_xp_malus_tt</li><li>update magic study experience modifier:</li><ul><li>value = -25</li></ul><li>set country flag [patron_xp_malus](../flags/patron_xp_malus.md)</li></ul></ul>

___
##Spend more money

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = -0.5</li><li>set ruler flag [money_magic_study](../flags/money_magic_study.md)</li><li>magic study start effect = yes</li><li>set ruler flag [ruler_studying_abjuration](../flags/ruler_studying_abjuration.md)</li><li>If has ruler flag is [patron_favored_abjuration](../flags/patron_favored_abjuration.md):</li><ul><li>custom tooltip = patron_xp_bonus_tt</li><li>update magic study experience modifier:</li><ul><li>value = 25</li></ul><li>set country flag [patron_xp_bonus](../flags/patron_xp_bonus.md)</li></ul><li>Else if has ruler flag is [patron_disfavored_abjuration](../flags/patron_disfavored_abjuration.md):</li><ul><li>custom tooltip = patron_xp_malus_tt</li><li>update magic study experience modifier:</li><ul><li>value = -25</li></ul><li>set country flag [patron_xp_malus](../flags/patron_xp_malus.md)</li></ul></ul>

___
##Abjuration

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li></ul><li>has country flag [aelnar_empowerment](../flags/aelnar_empowerment.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has ruler flag is [abjuration_2](../flags/abjuration_2.md):</li><ul><li>If has check variable has nbConnadh is 10000:</li><ul><li>custom tooltip = upgrade_to_legendary_tooltip</li><li>magic study level up abjuration = yes</li><li>increase witch king points large = yes</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>nbConnadh = 10000</li></ul></ul></ul><li>else:</li><ul><li>custom tooltip = not_enough_need_10000_tooltip</li></ul></ul><li>Else if has ruler flag is [abjuration_1](../flags/abjuration_1.md):</li><ul><li>If has check variable has nbConnadh is 5000:</li><ul><li>custom tooltip = upgrade_to_renowned_tooltip</li><li>magic study level up abjuration = yes</li><li>increase witch king points large = yes</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>nbConnadh = 5000</li></ul></ul></ul><li>else:</li><ul><li>custom tooltip = not_enough_need_5000_tooltip</li></ul></ul><li>else:</li><ul><li>If has check variable has nbConnadh is 2500:</li><ul><li>custom tooltip = upgrade_to_talented_tooltip</li><li>magic study level up abjuration = yes</li><li>increase witch king points large = yes</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>nbConnadh = 2500</li></ul></ul></ul><li>else:</li><ul><li>custom tooltip = not_enough_need_2500_tooltip</li></ul></ul></ul>

___
##Go back

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_study_menu_cooldown</li><li>duration = 730</li><li>hidden = yes</li></ul></ul></ul>
