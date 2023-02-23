#Information
 - Title:     Evocation\n£ruler_magic_evocation_bg£\n\n[Root.GetSchoolMasteryEvocation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.5
#Description
    Evocation\n£ruler_magic_evocation_bg£\n\n[Root.GetSchoolMasteryEvocation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [evocation_1](../flags/evocation_1.md), and has ruler flag is evocation 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event [Study Evocation](../events/study_evocation.md) happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_evocation](../flags/ruler_studying_evocation.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_evocation](../flags/ruler_studying_evocation.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [evocation_3](../flags/evocation_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£spell_war_1£

###Available if:
<li>has ruler flag [evocation_1](../flags/evocation_1.md)</li><li>mil power is at least 50</li><li>None of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_3</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -50</li><li>magic casted spell = yes</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_1</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_1</li><li>duration = 1825</li></ul></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_1](../flags/evocation_1.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_1</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_1_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [evocation_1](../flags/evocation_1.md)</li><li>None of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 50</li></ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li><li>has ruler modifier  magic_realm_evocation_war_magic_2</li><li>has ruler modifier   magic_realm_evocation_war_magic_3</li></ul>

###Efects:<ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = magic_need_50_mil_tt</li></ul><li>If has ruler modifier is magic realm evocation war magic 1, and has ruler modifier is magic realm evocation war magic 2, and has ruler modifier is magic realm evocation war magic 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_1</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_1</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_1</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_fireball£

###Available if:
<li>has ruler flag [evocation_1](../flags/evocation_1.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have mil power is 10


###Efects:<ul><li>the event [Greater Fireball](../events/greater_fireball.md) happens</li><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 1</li></ul><li>custom tooltip = magic_fireball_desc_tt</li></ul>

___
##£spell_fireball_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_1](../flags/evocation_1.md)</li></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 1</li></ul><li>custom tooltip = magic_fireball_desc_tt</li></ul>

___
##£spell_fireball_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [evocation_1](../flags/evocation_1.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 1</li></ul><li>custom tooltip = magic_fireball_desc_tt</li></ul>

___
##£spell_war_2£

###Available if:
<li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>mil power is at least 50</li><li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_3</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -50</li><li>magic casted spell = yes</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_2</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_2</li><li>duration = 1825</li></ul></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_2</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 50</li></ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li><li>has ruler modifier  magic_realm_evocation_war_magic_2</li><li>has ruler modifier   magic_realm_evocation_war_magic_3</li></ul>

###Efects:<ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = magic_need_50_mil_tt</li></ul><li>If has ruler modifier is magic realm evocation war magic 1, and has ruler modifier is magic realm evocation war magic 2, and has ruler modifier is magic realm evocation war magic 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_2</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_2</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_2</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_earthquake£

###Available if:
<li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have adm power is 20; and does not have mil power is 5


###Efects:<ul><li>the event [Earthquake](../events/earthquake.md) happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 3</li><li>add province modifier:</li><ul><li>name = siege_magic_earthquake</li><li>duration = 365</li></ul><li>add devastation = 10</li></ul><li>custom tooltip = magic_earthquake_desc_tt</li></ul>

___
##£spell_earthquake_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 3</li><li>add province modifier:</li><ul><li>name = siege_magic_earthquake</li><li>duration = 365</li></ul><li>add devastation = 10</li></ul><li>custom tooltip = magic_earthquake_desc_tt</li></ul>

___
##£spell_earthquake_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 3</li><li>add province modifier:</li><ul><li>name = siege_magic_earthquake</li><li>duration = 365</li></ul><li>add devastation = 10</li></ul><li>custom tooltip = magic_earthquake_desc_tt</li></ul>

___
##£spell_war_3£

###Available if:
<li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>mil power is at least 50</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_2</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_evocation_war_magic_3</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add mil power = -50</li><li>magic casted spell = yes</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_3</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_3</li><li>duration = 1825</li></ul></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_3</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_war_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 50</li></ul><li>has ruler modifier magic_realm_evocation_war_magic_1</li><li>has ruler modifier  magic_realm_evocation_war_magic_2</li><li>has ruler modifier   magic_realm_evocation_war_magic_3</li></ul>

###Efects:<ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = magic_need_50_mil_tt</li></ul><li>If has ruler modifier is magic realm evocation war magic 1, and has ruler modifier is magic realm evocation war magic 2, and has ruler modifier is magic realm evocation war magic 3:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -50</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_green_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [maiden_patron](../flags/maiden_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_ice_war_magic_3</li><li>duration = 1825</li></ul></ul><li>Else if has ruler flag is [bladedancer_patron](../flags/bladedancer_patron.md):</li><ul><li>custom tooltip = magic_booster_by_patron_tt</li><li>add ruler modifier:</li><ul><li>name = patron_diranbe_war_magic_3</li><li>duration = 1825</li></ul></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_evocation_war_magic_3</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_war_magic_desc_tt</li></ul>

___
##£spell_meteor£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>has ruler flag  rakshasa_patron</li></ul></ul><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have mil power is 50


###Efects:<ul><li>the event [Meteor Strike](../events/meteor_strike.md) happens</li><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md), and does not have ruler flag is [evocation_3](../flags/evocation_3.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 10</li><li>add devastation = 50</li></ul><li>custom tooltip = magic_meteor_desc_tt</li></ul>

___
##£spell_meteor_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>has ruler flag  rakshasa_patron</li></ul></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 10</li><li>add devastation = 50</li></ul><li>custom tooltip = magic_meteor_desc_tt</li></ul>

___
##£spell_meteor_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [evocation_3](../flags/evocation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [evocation_2](../flags/evocation_2.md)</li><li>has ruler flag  rakshasa_patron</li></ul></ul><li>OR:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###Efects:<ul><li>set country flag [evocation_menu](../flags/evocation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>tooltip:</li><ul><li>change siege = 10</li><li>add devastation = 50</li></ul><li>custom tooltip = magic_meteor_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
