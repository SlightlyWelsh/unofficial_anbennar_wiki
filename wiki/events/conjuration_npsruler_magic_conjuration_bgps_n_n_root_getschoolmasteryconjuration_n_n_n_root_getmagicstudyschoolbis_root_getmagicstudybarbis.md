#Information
 - Title:     Conjuration\n£ruler_magic_conjuration_bg£\n\n[Root.GetSchoolMasteryConjuration]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.2
#Description
    Conjuration\n£ruler_magic_conjuration_bg£\n\n[Root.GetSchoolMasteryConjuration]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [conjuration_3](../flags/conjuration_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [conjuration_1](../flags/conjuration_1.md), and has ruler flag is conjuration 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event ˻magic_study.4˼ happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_conjuration](../flags/ruler_studying_conjuration.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_conjuration](../flags/ruler_studying_conjuration.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [conjuration_3](../flags/conjuration_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [conjuration_3](../flags/conjuration_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_feast_1£

###Available if:
<li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li><li>dip power is at least 15</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_feast_cooldown</li></ul><li>any ally:</li><ul><li>exists</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat
 - Multiplied by 2 if does not have prestige is 20


###Efects:<ul><li>add dip power = -15</li><li>the event ˻magic_ruler.11˼ happens</li><li>custom tooltip = magic_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_feast_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -15</li></ul><li>custom tooltip = magic_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_feast_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul><li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>any ally:</li><ul><li>exists</li></ul></ul><li>NOT:</li><ul><li>dip power is at least 15</li></ul><li>has ruler modifier magic_feast_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic feast cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have any ally has exists:</li><ul><li>custom tooltip = magic_need_an_ally_tt</li></ul><li>If does not have dip power is 15:</li><ul><li>custom tooltip = magic_need_15_dip_tt</li></ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -15</li></ul><li>custom tooltip = magic_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_elemantal£

###Available if:
<li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20; and does not have mil power is 20


###Efects:<ul><li>the event ˻magic_siege.2˼ happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_elemental_besieger</li><li>duration = 84</li></ul></ul><li>custom tooltip = magic_elemental_desc_tt</li></ul>

___
##£spell_elemantal_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li></ul>

###Efects:<ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_elemental_besieger</li><li>duration = 84</li></ul></ul><li>custom tooltip = magic_elemental_desc_tt</li></ul>

___
##£spell_elemantal_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [conjuration_1](../flags/conjuration_1.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_elemental_besieger</li><li>duration = 84</li></ul></ul><li>custom tooltip = magic_elemental_desc_tt</li></ul>

___
##£spell_feast_2£

###Available if:
<li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>dip power is at least 15</li><li>None of the following:</li><ul><li>has ruler modifier magic_feast_cooldown</li></ul><li>any ally:</li><ul><li>exists</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat
 - Multiplied by 2 if does not have prestige is 20


###Efects:<ul><li>add dip power = -15</li><li>the event ˻magic_ruler.11˼ happens</li><li>custom tooltip = magic_greater_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_feast_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -15</li></ul><li>custom tooltip = magic_greater_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_feast_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 15</li></ul><li>NOT:</li><ul><li>any ally:</li><ul><li>exists</li></ul></ul><li>has ruler modifier magic_feast_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic feast cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have any ally has exists:</li><ul><li>custom tooltip = magic_need_an_ally_tt</li></ul><li>If does not have dip power is 15:</li><ul><li>custom tooltip = magic_need_15_dip_tt</li></ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -15</li></ul><li>custom tooltip = magic_greater_feast_effect_tt</li><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_thunderstorm£

###Available if:
<li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have dip power is 20; and does not have mil power is 20


###Efects:<ul><li>the event ˻magic_siege.17˼ happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 5</li><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = siege_magic_thunderstorm</li><li>duration = 182</li></ul></ul><li>custom tooltip = magic_thunderstorm_desc_tt</li></ul>

___
##£spell_thunderstorm_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li></ul>

###Efects:<ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 5</li><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = siege_magic_thunderstorm</li><li>duration = 182</li></ul></ul><li>custom tooltip = magic_thunderstorm_desc_tt</li></ul>

___
##£spell_thunderstorm_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 5</li><li>add devastation = 5</li><li>add province modifier:</li><ul><li>name = siege_magic_thunderstorm</li><li>duration = 182</li></ul></ul><li>custom tooltip = magic_thunderstorm_desc_tt</li></ul>

___
##£spell_magical_fortress£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [conjuration_3](../flags/conjuration_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>has ruler flag  ancestor_spirit_patron</li></ul></ul><li>adm power is at least 100</li><li>dip power is at least 100</li><li>mil power is at least 100</li><li>None of the following:</li><ul><li>has ruler modifier magic_fortress_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if is at war, and does not have war score is 20
 - Multiplied by 4 if has personality is ai militarist, and has personality is ai capitalist


###Efects:<ul><li>add adm power = -100</li><li>add dip power = -100</li><li>add mil power = -100</li><li>the event ˻magic_ruler.12˼ happens</li><li>custom tooltip = magic_fortress_effect_tt</li><li>custom tooltip = magic_fortress_desc_tt</li></ul>

___
##£spell_magical_fortress_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [conjuration_3](../flags/conjuration_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>has ruler flag  ancestor_spirit_patron</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>add dip power = -100</li><li>add mil power = -100</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>custom tooltip = magic_fortress_effect_tt</li><li>custom tooltip = magic_fortress_desc_tt</li></ul>

___
##£spell_magical_fortress_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [conjuration_3](../flags/conjuration_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [conjuration_2](../flags/conjuration_2.md)</li><li>has ruler flag  ancestor_spirit_patron</li></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>adm power is at least 100</li></ul><li>NOT:</li><ul><li>dip power is at least 100</li></ul><li>NOT:</li><ul><li>mil power is at least 100</li></ul><li>NOT:</li><ul><li>dip power is at least 15</li></ul><li>has ruler modifier magic_fortress_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic fortress cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 100:</li><ul><li>custom tooltip = magic_need_100_adm_tt</li></ul><li>If does not have dip power is 100:</li><ul><li>custom tooltip = magic_need_100_dip_tt</li></ul><li>If does not have mil power is 100:</li><ul><li>custom tooltip = magic_need_100_mil_tt</li></ul><li>set country flag [conjuration_menu](../flags/conjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>add dip power = -100</li><li>add mil power = -100</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>custom tooltip = magic_fortress_effect_tt</li><li>custom tooltip = magic_fortress_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul></ul>
