#Information
 - Title:     Necromancy\n£ruler_magic_necromancy_bg£\n\n[Root.GetSchoolMasteryNecromancy]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.7
#Description
    Necromancy\n£ruler_magic_necromancy_bg£\n\n[Root.GetSchoolMasteryNecromancy]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [necromancy_1](../flags/necromancy_1.md), and has ruler flag is necromancy 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>If has tag is I20, and  has reform is krakazol olzonog:</li><ul><li>custom tooltip = krakazol_no_necromancy_tooltip</li><li>hidden effect:</li><ul><li>the event ˻flavor_krakazol.210˼ happens</li></ul></ul><li>the event ˻magic_study.19˼ happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_necromancy](../flags/ruler_studying_necromancy.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_necromancy](../flags/ruler_studying_necromancy.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [necromancy_3](../flags/necromancy_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_life_drain£

###Available if:
<li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>adm power is at least 5</li><li>mil power is at least 5</li><li>None of the following:</li><ul><li>has ruler modifier magic_drain_cooldown</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add adm power = -5</li><li>add mil power = -5</li><li>custom tooltip = magic_absorb_life_effect_tt</li><li>the event ˻magic_ruler.13˼ happens</li><li>custom tooltip = magic_absorb_life_desc_tt</li></ul>

___
##£spell_life_drain_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -5</li><li>add mil power = -5</li></ul><li>custom tooltip = magic_absorb_life_effect_tt</li><li>custom tooltip = magic_absorb_life_desc_tt</li></ul>

___
##£spell_life_drain_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [necromancy_1](../flags/necromancy_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 5</li></ul><li>NOT:</li><ul><li>mil power is at least 5</li></ul><li>has ruler modifier magic_drain_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic drain cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 5:</li><ul><li>custom tooltip = magic_need_5_adm_tt</li></ul><li>If does not have mil power is 5:</li><ul><li>custom tooltip = magic_need_5_mil_tt</li></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -5</li><li>add mil power = -5</li></ul><li>custom tooltip = magic_absorb_life_effect_tt</li><li>custom tooltip = magic_absorb_life_desc_tt</li></ul>

___
##£spell_undead_army_1£

###Available if:
<li>has ruler flag [necromancy_2](../flags/necromancy_2.md)</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul><li>adm power is at least 15</li><li>dip power is at least 15</li><li>mil power is at least 15</li><li>NOT:</li><ul><li>has ruler modifier magic_undead_cooldown</li></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 4 if is at war
 - Multiplied by 0.5 if does not have ruler modifier is witch king modifier
 - Multiplied by 0 if has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is craven personality, and has ruler has personality is charismatic negotiator personality, and has army size percentage is 1


###Efects:<ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_undead_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul><li>custom tooltip = magic_undead_army_desc_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_undead_army_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_2](../flags/necromancy_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul></ul><li>custom tooltip = magic_undead_army_desc_tt</li></ul>

___
##£spell_undead_army_1_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [necromancy_2](../flags/necromancy_2.md)</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 15</li></ul><li>NOT:</li><ul><li>dip power is at least 15</li></ul><li>NOT:</li><ul><li>mil power is at least 15</li></ul><li>has ruler modifier magic_undead_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic undead cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 15:</li><ul><li>custom tooltip = magic_need_15_adm_tt</li></ul><li>If does not have dip power is 15:</li><ul><li>custom tooltip = magic_need_15_dip_tt</li></ul><li>If does not have mil power is 15:</li><ul><li>custom tooltip = magic_need_15_mil_tt</li></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul></ul><li>custom tooltip = magic_undead_army_desc_tt</li></ul>

___
##£spell_undead_army_2£

###Available if:
<li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li><li>adm power is at least 15</li><li>dip power is at least 15</li><li>mil power is at least 15</li><li>None of the following:</li><ul><li>has ruler modifier magic_undead_cooldown</li></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 4 if is at war
 - Multiplied by 0.5 if does not have ruler modifier is witch king modifier
 - Multiplied by 0 if has ruler has personality is benevolent personality, and has ruler has personality is careful personality, and has ruler has personality is craven personality, and has ruler has personality is charismatic negotiator personality, and has army size percentage is 1


###Efects:<ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_undead_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>cavalry = ROOT</li><li>cavalry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul><li>custom tooltip = magic_undead_army_desc_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_undead_army_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>cavalry = ROOT</li><li>cavalry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul></ul><li>custom tooltip = magic_undead_army_desc_tt</li></ul>

___
##£spell_undead_army_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 15</li></ul><li>NOT:</li><ul><li>dip power is at least 15</li></ul><li>NOT:</li><ul><li>mil power is at least 15</li></ul><li>has ruler modifier magic_undead_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic undead cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 15:</li><ul><li>custom tooltip = magic_need_15_adm_tt</li></ul><li>If does not have dip power is 15:</li><ul><li>custom tooltip = magic_need_15_dip_tt</li></ul><li>If does not have mil power is 15:</li><ul><li>custom tooltip = magic_need_15_mil_tt</li></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li><li>event target:undead army province:</li><ul><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>infantry = ROOT</li><li>cavalry = ROOT</li><li>cavalry = ROOT</li></ul><li>increase witch king points massive = yes</li><li>If does not have country modifier is undead military:</li><ul><li>clear racial military = yes</li><li>country gets the modifier undead_military until otherwise removed</li></ul><li>If does not have unit type is tech undead; and  has any racial military is yes:</li><ul><li>change unit type = tech_undead</li></ul></ul><li>custom tooltip = magic_undead_army_desc_tt</li></ul>

___
##£spell_lichdom£

###Available if:
<li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li><li>None of the following:</li><ul><li>magical project in progress is yes</li></ul><li>NOT:</li><ul><li>has ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [is_a_lich](../flags/is_a_lich.md)</li></ul><li>adm power is at least 300</li><li>dip power is at least 300</li><li>mil power is at least 300</li><li>is not lesser in union</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has ruler age is 40, and  has culture is short lived is yes
 - Multiplied by 0.25 if does not have culture is short lived is yes


###Efects:<ul><li>increase witch king points large = yes</li><li>add adm power = -300</li><li>add dip power = -300</li><li>add mil power = -300</li><li>magic casted spell = yes</li><li>set ruler flag [magic_project_lichdom_started](../flags/magic_project_lichdom_started.md)</li><li>custom tooltip = tooltip_magic_project_start</li><li>hidden effect:</li><ul><li>the event ˻magic_project_lichdom.1˼ happens</li></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_lichdom_desc_tt</li></ul>

___
##£spell_lichdom_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>increase witch king points large = yes</li><li>add adm power = -300</li><li>add dip power = -300</li><li>add mil power = -300</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_lichdom_desc_tt</li></ul>

___
##£spell_lichdom_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [necromancy_3](../flags/necromancy_3.md)</li><li>Any of the following:</li><ul><li>has ruler flag [is_a_vampire](../flags/is_a_vampire.md)</li><li>has ruler flag  is_a_lich</li><li>magical project in progress is yes</li><li>None of the following:</li><ul><li>adm power is at least 300</li></ul><li>NOT:</li><ul><li>dip power is at least 300</li></ul><li>NOT:</li><ul><li>mil power is at least 300</li></ul><li>is lesser in union</li></ul>

###Efects:<ul><li>If has ruler flag is [is_a_lich](../flags/is_a_lich.md):</li><ul><li>custom tooltip = magic_project_already_done_tt</li></ul><li>else:</li><ul><li>If has ruler flag is [magic_project_lichdom_started](../flags/magic_project_lichdom_started.md):</li><ul><li>custom tooltip = magic_project_started_tt</li></ul><li>Else if has magical project in progress is yes:</li><ul><li>custom tooltip = magic_other_project_in_progress_tt</li></ul><li>Else if has ruler flag is [is_a_vampire](../flags/is_a_vampire.md):</li><ul><li>custom tooltip = magic_vampires_cant_be_liches_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have adm power is 300:</li><ul><li>custom tooltip = magic_need_300_adm_tt</li></ul><li>If does not have dip power is 300:</li><ul><li>custom tooltip = magic_need_300_dip_tt</li></ul><li>If does not have mil power is 300:</li><ul><li>custom tooltip = magic_need_300_mil_tt</li></ul></ul><li>set country flag [necromancy_menu](../flags/necromancy_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>increase witch king points large = yes</li><li>add adm power = -300</li><li>add dip power = -300</li><li>add mil power = -300</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_lichdom_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
