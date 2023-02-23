#Information
 - Title:     Illusion\n£ruler_magic_illusion_bg£\n\n[Root.GetSchoolMasteryIllusion]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.6
#Description
    Illusion\n£ruler_magic_illusion_bg£\n\n[Root.GetSchoolMasteryIllusion]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [illusion_1](../flags/illusion_1.md), and has ruler flag is illusion 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event [Study Illusion](../events/study_illusion.md) happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_illusion](../flags/ruler_studying_illusion.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_illusion](../flags/ruler_studying_illusion.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [illusion_3](../flags/illusion_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£spell_marvels_1£

###Available if:
<li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>mil power is at least 10</li><li>None of the following:</li><ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if does not have prestige is 30


###Efects:<ul><li>add mil power = -10</li><li>magic casted spell = yes</li><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md):</li><ul><li>add prestige = 5</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_marvels_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>add prestige = 2</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -10</li><li>add prestige = 2</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_1_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 10</li></ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic marvels cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -10</li><li>add prestige = 2</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_2£

###Available if:
<li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>mil power is at least 20</li><li>None of the following:</li><ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if does not have prestige is 30


###Efects:<ul><li>add mil power = -20</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_marvels_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>If has ruler flag is [rakshasa_patron](../flags/rakshasa_patron.md):</li><ul><li>add prestige = 10</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>else:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_marvels_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>add prestige = 5</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -20</li><li>add prestige = 5</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 20</li></ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic marvels cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -20</li><li>add prestige = 5</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_glamour_1£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>None of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul></ul><li>dip power is at least 25</li><li>adm power is at least 5</li><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_enchanted_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_otherworldly_glamour</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 10 if has personality is ai diplomat


###Efects:<ul><li>add dip power = -25</li><li>add adm power = -5</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_glamour</li><li>duration = 1825</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul><li>NOT:</li><ul><li>All of the following:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul></ul>

###Efects:<ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>else:</li><ul><li>custom tooltip = school_mastery_not_renowned_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_1_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>None of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>dip power is at least 25</li></ul><li>NOT:</li><ul><li>adm power is at least 5</li></ul><li>has ruler modifier magic_realm_illusion_glamour</li><li>has ruler modifier  magic_realm_illusion_enchanted_glamour</li><li>has ruler modifier   magic_realm_illusion_otherworldly_glamour</li></ul>

###Efects:<ul><li>If does not have dip power is 25:</li><ul><li>custom tooltip = magic_need_25_dip_tt</li></ul><li>If does not have adm power is 5:</li><ul><li>custom tooltip = magic_need_5_adm_tt</li></ul><li>If has ruler modifier is magic realm illusion glamour, and has ruler modifier is magic realm illusion enchanted glamour, and has ruler modifier is magic realm illusion otherworldly glamour:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_2£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>AND:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>has ruler flag  enchantment_1</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul><li>dip power is at least 25</li><li>adm power is at least 5</li><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_enchanted_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_otherworldly_glamour</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 10 if has personality is ai diplomat


###Efects:<ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>add dip power = -25</li><li>add adm power = -5</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_enchanted_glamour</li><li>duration = 1825</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>All of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li></ul></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>AND:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>has ruler flag  enchantment_1</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul>

###Efects:<ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>If does not have ruler flag is [illusion_1](../flags/illusion_1.md):</li><ul><li>custom tooltip = school_mastery_not_talented_tt</li></ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>Else if does not have ruler flag is [illusion_2](../flags/illusion_2.md):</li><ul><li>custom tooltip = school_mastery_not_renowned_tt</li></ul><li>If does not have ruler flag is [enchantment_1](../flags/enchantment_1.md):</li><ul><li>custom tooltip = school_mastery_enchantment_not_talented_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_enchanted_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_2_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [illusion_1](../flags/illusion_1.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>has ruler flag [enchantment_1](../flags/enchantment_1.md)</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>AND:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>has ruler flag  enchantment_1</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>dip power is at least 25</li></ul><li>NOT:</li><ul><li>adm power is at least 5</li></ul><li>has ruler modifier magic_realm_illusion_glamour</li><li>has ruler modifier  magic_realm_illusion_enchanted_glamour</li><li>has ruler modifier   magic_realm_illusion_otherworldly_glamour</li></ul>

###Efects:<ul><li>If does not have dip power is 25:</li><ul><li>custom tooltip = magic_need_25_dip_tt</li></ul><li>If does not have adm power is 5:</li><ul><li>custom tooltip = magic_need_5_adm_tt</li></ul><li>If has ruler modifier is magic realm illusion glamour, and has ruler modifier is magic realm illusion enchanted glamour, and has ruler modifier is magic realm illusion otherworldly glamour:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_enchanted_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_marvels_3£

###Available if:
<li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>mil power is at least 30</li><li>None of the following:</li><ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if does not have prestige is 30


###Efects:<ul><li>add mil power = -30</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_marvels_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>add prestige = 10</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -30</li><li>add prestige = 10</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_marvels_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>mil power is at least 30</li></ul><li>has ruler modifier magic_marvels_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic marvels cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = magic_need_10_mil_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add mil power = -30</li><li>add prestige = 10</li></ul><li>custom tooltip = magic_illusionary_marvels_desc_tt</li></ul>

___
##£spell_glamour_3£

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>AND:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>has ruler flag  enchantment_1</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>dip power is at least 25</li><li>adm power is at least 5</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_illusion_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_enchanted_glamour</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_illusion_otherworldly_glamour</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 10 if has personality is ai diplomat


###Efects:<ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>add dip power = -25</li><li>add adm power = -5</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_otherworldly_glamour</li><li>duration = 1825</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>None of the following:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>has ruler flag  enchantment_1</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul></ul>

###Efects:<ul><li>If has ruler flag is [huli_jing_patron](../flags/huli_jing_patron.md), and has ruler flag is gumiho patron:</li><ul><li>If does not have ruler flag is [illusion_2](../flags/illusion_2.md):</li><ul><li>custom tooltip = school_mastery_not_renowned_tt</li></ul><li>If does not have ruler flag is [enchantment_1](../flags/enchantment_1.md):</li><ul><li>custom tooltip = school_mastery_enchantment_not_talented_tt</li></ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>else:</li><ul><li>If does not have ruler flag is [illusion_3](../flags/illusion_3.md):</li><ul><li>custom tooltip = school_mastery_not_legendary_tt</li></ul><li>If does not have ruler flag is [enchantment_2](../flags/enchantment_2.md):</li><ul><li>custom tooltip = school_mastery_enchantment_not_renowned_tt</li></ul></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_otherworldly_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_glamour_3_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>has ruler flag  enchantment_2</li></ul><li>AND:</li><ul><li>has ruler flag [illusion_2](../flags/illusion_2.md)</li><li>Any of the following:</li><ul><li>has ruler flag [huli_jing_patron](../flags/huli_jing_patron.md)</li><li>has ruler flag  gumiho_patron</li></ul></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>dip power is at least 25</li></ul><li>NOT:</li><ul><li>adm power is at least 5</li></ul><li>has ruler modifier magic_realm_illusion_glamour</li><li>has ruler modifier  magic_realm_illusion_enchanted_glamour</li><li>has ruler modifier   magic_realm_illusion_otherworldly_glamour</li></ul>

###Efects:<ul><li>If does not have dip power is 25:</li><ul><li>custom tooltip = magic_need_25_dip_tt</li></ul><li>If does not have adm power is 5:</li><ul><li>custom tooltip = magic_need_5_adm_tt</li></ul><li>If has ruler modifier is magic realm illusion glamour, and has ruler modifier is magic realm illusion enchanted glamour, and has ruler modifier is magic realm illusion otherworldly glamour:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add dip power = -25</li><li>add adm power = -5</li><li>add ruler modifier:</li><ul><li>name = magic_realm_illusion_otherworldly_glamour</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_glamour_desc_tt</li></ul>

___
##£spell_simulacrum£

###Available if:
<li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>None of the following:</li><ul><li>magical project in progress is yes</li></ul><li>NOT:</li><ul><li>has ruler flag [magic_project_simulacrum_complete](../flags/magic_project_simulacrum_complete.md)</li></ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>mil power is at least 50</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li><li>magic casted spell = yes</li><li>set ruler flag [magic_project_simulacrum_started](../flags/magic_project_simulacrum_started.md)</li><li>custom tooltip = tooltip_magic_project_start</li><li>hidden effect:</li><ul><li>the event [Simulacrum Project: Stage 1](../events/simulacrum_project_stage_1.md) happens</li></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_simulacrum_desc_tt</li></ul>

___
##£spell_simulacrum_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_simulacrum_desc_tt</li></ul>

___
##£spell_simulacrum_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [illusion_3](../flags/illusion_3.md)</li><li>Any of the following:</li><ul><li>has ruler flag [magic_project_simulacrum_complete](../flags/magic_project_simulacrum_complete.md)</li><li>magical project in progress is yes</li><li>None of the following:</li><ul><li>adm power is at least 50</li></ul><li>NOT:</li><ul><li>dip power is at least 50</li></ul><li>NOT:</li><ul><li>mil power is at least 50</li></ul></ul>

###Efects:<ul><li>If has ruler flag is [magic_project_simulacrum_complete](../flags/magic_project_simulacrum_complete.md):</li><ul><li>custom tooltip = magic_project_already_done_tt</li></ul><li>else:</li><ul><li>If has ruler flag is [magic_project_simulacrum_started](../flags/magic_project_simulacrum_started.md):</li><ul><li>custom tooltip = magic_project_started_tt</li></ul><li>Else if has magical project in progress is yes:</li><ul><li>custom tooltip = magic_other_project_in_progress_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = magic_need_50_adm_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = magic_need_50_dip_tt</li></ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = magic_need_50_mil_tt</li></ul></ul><li>set country flag [illusion_menu](../flags/illusion_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_simulacrum_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
