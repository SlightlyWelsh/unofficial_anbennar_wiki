#Information
 - Title:     Abjuration\n£ruler_magic_abjuration_bg£\n\n[Root.GetSchoolMasteryAbjuration]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.1
#Description
    Abjuration\n£ruler_magic_abjuration_bg£\n\n[Root.GetSchoolMasteryAbjuration]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [abjuration_1](../flags/abjuration_1.md), and has ruler flag is abjuration 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event [Study Abjuration](../events/study_abjuration.md) happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_abjuration](../flags/ruler_studying_abjuration.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_abjuration](../flags/ruler_studying_abjuration.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [abjuration_3](../flags/abjuration_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£spell_ward_1£

###Available if:
<li>has ruler flag [abjuration_1](../flags/abjuration_1.md)</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li></ul><li>adm power is at least 30</li><li>dip power is at least 5</li><li>NOT:</li><ul><li>has ruler modifier magic_ward_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if is at war, and does not have war score is 20


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -5</li><li>the event [Choose Ward Target](../events/choose_ward_target.md) happens</li><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_ward_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [abjuration_1](../flags/abjuration_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li><li>custom tooltip = magic_selected_province_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_ward_1_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li></ul><li>has ruler flag [abjuration_1](../flags/abjuration_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 30</li></ul><li>NOT:</li><ul><li>dip power is at least 5</li></ul><li>has ruler modifier magic_ward_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic ward cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 30:</li><ul><li>custom tooltip = magic_need_30_adm_tt</li></ul><li>If does not have dip power is 5:</li><ul><li>custom tooltip = magic_need_5_dip_tt</li></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li><li>custom tooltip = magic_selected_province_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_ward_2£

###Available if:
<li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li><li>adm power is at least 30</li><li>dip power is at least 5</li><li>None of the following:</li><ul><li>has ruler modifier magic_ward_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if is at war, and does not have war score is 20


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -5</li><li>the event [Choose Ward Target](../events/choose_ward_target.md) happens</li><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_empowered_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_ward_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li><li>custom tooltip = magic_selected_province_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_empowered_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_ward_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [abjuration_2](../flags/abjuration_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 30</li></ul><li>NOT:</li><ul><li>dip power is at least 5</li></ul><li>has ruler modifier magic_ward_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic ward cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 30:</li><ul><li>custom tooltip = magic_need_30_adm_tt</li></ul><li>If does not have dip power is 5:</li><ul><li>custom tooltip = magic_need_5_dip_tt</li></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li><li>custom tooltip = magic_selected_province_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_empowered_ward</li><li>duration = 9131</li></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_field_freedom£

###Available if:
<li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>None of the following:</li><ul><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 5 if is at war, and does not have war score is 40


###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_freedom</li><li>duration = 1825</li></ul></ul></ul><li>magic field adm cost = yes</li><li>magic casted spell = yes</li><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_freedom</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_field_effect_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_freedom</li><li>duration = 1825</li></ul></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_freedom_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_freedom</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_freedom_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul>

###Efects:<ul><li>custom tooltip = province_has_abjuration_field_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_freedom</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_forbidance£

###Available if:
<li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>None of the following:</li><ul><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 5 if is at war, and does not have war score is 40


###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_forbiddance</li><li>duration = 365</li></ul></ul></ul><li>magic field adm cost = yes</li><li>magic casted spell = yes</li><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_forbiddance</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_field_effect_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_forbiddance</li><li>duration = 1825</li></ul></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_forbidance_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_forbiddance</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_forbidance_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul>

###Efects:<ul><li>custom tooltip = province_has_abjuration_field_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_forbiddance</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_fortification£

###Available if:
<li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>None of the following:</li><ul><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul></ul>

###AI weighting:
AI weights this option at 20
 - Multiplied by 5 if is at war, and does not have war score is 40


###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_fortification</li><li>duration = 1825</li></ul></ul></ul><li>magic field adm cost = yes</li><li>magic casted spell = yes</li><li>hidden effect:</li><ul><li>If every owned province is in capital area:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_fortification</li><li>duration = 1825</li></ul></ul></ul><li>custom tooltip = magic_field_effect_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_fortification</li><li>duration = 1825</li></ul></ul><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_fortification_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_fortification</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£spell_field_fortification_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [abjuration_3](../flags/abjuration_3.md)</li><li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has province modifier magic_realm_abjuration_field_of_freedom</li><li>has province modifier  magic_realm_abjuration_field_of_forbiddance</li><li>has province modifier   magic_realm_abjuration_field_of_fortification</li></ul></ul>

###Efects:<ul><li>custom tooltip = province_has_abjuration_field_tt</li><li>set country flag [abjuration_menu](../flags/abjuration_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic field adm cost = yes</li><li>custom tooltip = magic_field_effect_tt</li><li>add province modifier:</li><ul><li>name = magic_realm_abjuration_field_of_fortification</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_field_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
