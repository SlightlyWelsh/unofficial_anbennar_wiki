#Information
 - Title:     Enchantment\n£ruler_magic_enchantment_bg£\n\n[Root.GetSchoolMasteryEnchantment]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.4
#Description
    Enchantment\n£ruler_magic_enchantment_bg£\n\n[Root.GetSchoolMasteryEnchantment]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [enchantment_1](../flags/enchantment_1.md), and has ruler flag is enchantment 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event ˻magic_study.10˼ happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_enchantment](../flags/ruler_studying_enchantment.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_enchantment](../flags/ruler_studying_enchantment.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [enchantment_3](../flags/enchantment_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_charm_estates_1£

###Available if:
<li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_charm_estates_cooldown</li><li>duration = 3650</li><li>hidden = yes</li></ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 3650</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic charm estates cooldown:</li><ul><li>custom tooltip = magic_10_year_cooldown_tt</li></ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_1</li><li>loyalty = 3</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_diplomats_1£

###Available if:
<li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>has ruler modifier  magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>has ruler modifier   magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm impress foreign diplomats 1, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 2, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_military_1£

###Available if:
<li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 3 if is at war


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li><li>has ruler modifier  magic_realm_enchantment_charm_inspire_military_2</li><li>has ruler modifier   magic_realm_enchantment_charm_inspire_military_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm inspire military 1, and has ruler modifier is magic realm enchantment charm inspire military 2, and has ruler modifier is magic realm enchantment charm inspire military 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_subjects_1£

###Available if:
<li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have num of subjects is 1
 - Multiplied by 5 if has any subject country has liberty desire is 50


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li><li>has ruler modifier  magic_realm_enchantment_charm_assuage_subjects_2</li><li>has ruler modifier   magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm assuage subjects 1, and has ruler modifier is magic realm enchantment charm assuage subjects 2, and has ruler modifier is magic realm enchantment charm assuage subjects 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_estates_2£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_charm_estates_cooldown</li><li>duration = 3650</li><li>hidden = yes</li></ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 12</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 12</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_2_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic charm estates cooldown:</li><ul><li>custom tooltip = magic_10_year_cooldown_tt</li></ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 12</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_2</li><li>loyalty = 6</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_diplomats_2£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_2_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>has ruler modifier  magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>has ruler modifier   magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm impress foreign diplomats 1, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 2, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_military_2£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 3 if is at war


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_2_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li><li>has ruler modifier  magic_realm_enchantment_charm_inspire_military_2</li><li>has ruler modifier   magic_realm_enchantment_charm_inspire_military_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm inspire military 1, and has ruler modifier is magic realm enchantment charm inspire military 2, and has ruler modifier is magic realm enchantment charm inspire military 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_subjects_2£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have num of subjects is 1
 - Multiplied by 5 if has any subject country has liberty desire is 50


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_2_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li><li>has ruler modifier  magic_realm_enchantment_charm_assuage_subjects_2</li><li>has ruler modifier   magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm assuage subjects 1, and has ruler modifier is magic realm enchantment charm assuage subjects 2, and has ruler modifier is magic realm enchantment charm assuage subjects 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_memories_oversight£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>adm power is at least 150</li><li>mil power is at least 80</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_modify_memories_overlook_national_blunders</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has prestige is 1, and does not have prestige is 50


###Efects:<ul><li>add adm power = -150</li><li>add mil power = -80</li><li>magic casted spell = yes</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_memories_blunder_desc_tt</li></ul>

___
##£spell_memories_oversight_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_blunder_desc_tt</li></ul>

___
##£spell_memories_oversight_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 150</li></ul><li>NOT:</li><ul><li>mil power is at least 80</li></ul><li>has ruler modifier magic_realm_enchantment_modify_memories_overlook_national_blunders</li></ul>

###Efects:<ul><li>If does not have adm power is 150:</li><ul><li>custom tooltip = magic_need_150_adm_tt</li></ul><li>If does not have mil power is 80:</li><ul><li>custom tooltip = magic_need_80_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment modify memories overlook national blunders:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_overlook_national_blunders</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_blunder_desc_tt</li></ul>

___
##£spell_memories_subservience£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>adm power is at least 150</li><li>mil power is at least 80</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_modify_memories_encourage_subservience</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has prestige is 1, and does not have prestige is 50


###Efects:<ul><li>add adm power = -150</li><li>add mil power = -80</li><li>magic casted spell = yes</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_memories_subservience_desc_tt</li></ul>

___
##£spell_memories_subservience_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_subservience_desc_tt</li></ul>

___
##£spell_memories_subservience_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 150</li></ul><li>NOT:</li><ul><li>mil power is at least 80</li></ul><li>has ruler modifier magic_realm_enchantment_modify_memories_encourage_subservience</li></ul>

###Efects:<ul><li>If does not have adm power is 150:</li><ul><li>custom tooltip = magic_need_150_adm_tt</li></ul><li>If does not have mil power is 80:</li><ul><li>custom tooltip = magic_need_80_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment modify memories encourage subservience:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_encourage_subservience</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_subservience_desc_tt</li></ul>

___
##£spell_memories_erasure£

###Available if:
<li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>adm power is at least 150</li><li>mil power is at least 80</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_modify_memories_forget_atrocities</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has prestige is 1, and does not have prestige is 50


###Efects:<ul><li>add adm power = -150</li><li>add mil power = -80</li><li>magic casted spell = yes</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_memories_atrocities_desc_tt</li></ul>

___
##£spell_memories_erasure_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_atrocities_desc_tt</li></ul>

___
##£spell_memories_erasure_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_2](../flags/enchantment_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 150</li></ul><li>NOT:</li><ul><li>mil power is at least 80</li></ul><li>has ruler modifier magic_realm_enchantment_modify_memories_forget_atrocities</li></ul>

###Efects:<ul><li>If does not have adm power is 150:</li><ul><li>custom tooltip = magic_need_150_adm_tt</li></ul><li>If does not have mil power is 80:</li><ul><li>custom tooltip = magic_need_80_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment modify memories forget atrocities:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -150</li><li>add mil power = -80</li><li>If has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_modify_memories_forget_atrocities</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_memories_atrocities_desc_tt</li></ul>

___
##£spell_dominate_surrender£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20


###Efects:<ul><li>the event ˻magic_siege.5˼ happens</li><li>If has ruler flag is [baku_patron](../flags/baku_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change controller = ROOT</li></ul><li>custom tooltip = magic_dominate_desc_tt</li></ul>

___
##£spell_dominate_surrender_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change controller = ROOT</li></ul><li>custom tooltip = magic_dominate_desc_tt</li></ul>

___
##£spell_dominate_surrender_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change controller = ROOT</li></ul><li>custom tooltip = magic_dominate_desc_tt</li></ul>

___
##£spell_charm_estates_3£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 30; and does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_charm_estates_cooldown</li><li>duration = 3650</li><li>hidden = yes</li></ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 20</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 3650</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 20</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_estates_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_charm_estates_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic charm estates cooldown:</li><ul><li>custom tooltip = magic_10_year_cooldown_tt</li></ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 20</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 5475</li></ul></ul><li>else:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = all</li><li>desc = EST_VAL_REALM_MAGIC_SWAYING_THE_ESTATES_ENCHANTMENT_3</li><li>loyalty = 10</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_charm_estates_desc_tt</li></ul>

___
##£spell_charm_diplomats_3£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_diplomats_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_impress_foreign_diplomats_1</li><li>has ruler modifier  magic_realm_enchantment_charm_impress_foreign_diplomats_2</li><li>has ruler modifier   magic_realm_enchantment_charm_impress_foreign_diplomats_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm impress foreign diplomats 1, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 2, and has ruler modifier is magic realm enchantment charm impress foreign diplomats 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_impress_foreign_diplomats_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_diplomats_desc_tt</li></ul>

___
##£spell_charm_military_3£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai militarist
 - Multiplied by 3 if is at war


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_military_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_inspire_military_1</li><li>has ruler modifier  magic_realm_enchantment_charm_inspire_military_2</li><li>has ruler modifier   magic_realm_enchantment_charm_inspire_military_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm inspire military 1, and has ruler modifier is magic realm enchantment charm inspire military 2, and has ruler modifier is magic realm enchantment charm inspire military 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_inspire_military_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_military_desc_tt</li></ul>

___
##£spell_charm_subjects_3£

###Available if:
<li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>dip power is at least 30</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have num of subjects is 1
 - Multiplied by 5 if has any subject country has liberty desire is 50


###Efects:<ul><li>add dip power = -30</li><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 1825</li></ul></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£spell_charm_subjects_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [enchantment_3](../flags/enchantment_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 30</li></ul><li>NOT:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_realm_enchantment_charm_assuage_subjects_1</li><li>has ruler modifier  magic_realm_enchantment_charm_assuage_subjects_2</li><li>has ruler modifier   magic_realm_enchantment_charm_assuage_subjects_3</li></ul>

###Efects:<ul><li>If does not have dip power is 30:</li><ul><li>custom tooltip = magic_need_30_dip_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>If has ruler modifier is magic realm enchantment charm assuage subjects 1, and has ruler modifier is magic realm enchantment charm assuage subjects 2, and has ruler modifier is magic realm enchantment charm assuage subjects 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [enchantment_menu](../flags/enchantment_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -30</li><li>add mil power = -10</li><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 3650</li></ul></ul><li>Else if has country flag is [Y63_enchantment_upgrade](../flags/y63_enchantment_upgrade.md):</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 2736</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_enchantment_charm_assuage_subjects_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_charm_subject_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
