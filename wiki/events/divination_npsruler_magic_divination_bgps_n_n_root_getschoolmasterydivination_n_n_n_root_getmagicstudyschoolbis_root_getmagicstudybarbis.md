#Information
 - Title:     Divination\n£ruler_magic_divination_bg£\n\n[Root.GetSchoolMasteryDivination]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.3
#Description
    Divination\n£ruler_magic_divination_bg£\n\n[Root.GetSchoolMasteryDivination]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [divination_3](../flags/divination_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [divination_1](../flags/divination_1.md), and has ruler flag is divination 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event [Study Divination](../events/study_divination.md) happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_divination](../flags/ruler_studying_divination.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_divination](../flags/ruler_studying_divination.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [divination_3](../flags/divination_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [divination_3](../flags/divination_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul></ul>

___
##£spell_scrying_rivals£

###Available if:
<li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>adm power is at least 25</li><li>dip power is at least 25</li><li>any rival country:</li><ul><li>exists</li></ul><li>has ruler modifier magic_realm_divination_scrying_rivals</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 4 if is a great power


###Efects:<ul><li>magic casted spell = yes</li><li>magic scrying rivals cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 180 days</li></ul><li>every rival country:</li><ul><li>remove fow = 6</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_rivals_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying rivals cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 180 days</li></ul></ul><li>custom tooltip = magic_scrying_rival_effect_tt</li><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_rivals_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 25</li></ul><li>NOT:</li><ul><li>dip power is at least 25</li></ul><li>NOT:</li><ul><li>any rival country:</li><ul><li>exists</li></ul></ul><li>has ruler modifier magic_realm_divination_scrying_rivals</li></ul>

###Efects:<ul><li>If has ruler modifier is magic realm divination scrying rivals:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>If does not have adm power is 25:</li><ul><li>custom tooltip = magic_need_25_adm_tt</li></ul><li>If does not have dip power is 25:</li><ul><li>custom tooltip = magic_need_25_dip_tt</li></ul><li>If does not have any rival country has exists:</li><ul><li>custom tooltip = magic_need_valid_target_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying rivals cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_rivals for 180 days</li></ul></ul><li>custom tooltip = magic_scrying_rival_effect_tt</li><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_neighbours£

###Available if:
<li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>adm power is at least 50</li><li>any country:</li><ul><li>is neighbor of is this nation</li></ul><li>None of the following:</li><ul><li>has ruler modifier magic_realm_divination_scrying_neighbours</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 4 if has personality is ai diplomat


###Efects:<ul><li>magic casted spell = yes</li><li>magic scrying neighbours cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 180 days</li></ul><li>If every country is neighbor of is ROOT:</li><ul><li>remove fow = 6</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_neighbours_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying neighbours cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 180 days</li></ul></ul><li>custom tooltip = magic_scrying_neighbours_effect_tt</li><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_neighbours_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 50</li></ul><li>NOT:</li><ul><li>any country:</li><ul><li>is neighbor of is this nation</li></ul></ul><li>has ruler modifier magic_realm_divination_scrying_neighbours</li></ul>

###Efects:<ul><li>If has ruler modifier is magic realm divination scrying neighbours:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = magic_need_50_adm_tt</li></ul><li>If does not have any country is neighbor of is ROOT:</li><ul><li>custom tooltip = magic_need_valid_target_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying neighbours cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 1 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 225 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 300 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_neighbours for 180 days</li></ul></ul><li>custom tooltip = magic_scrying_neighbours_effect_tt</li><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_dissidents£

###Available if:
<li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>adm power is at least 50</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_divination_scrying_internal_dissidents</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 4 if has average unrest is 5
 - Multiplied by 4 if does not have stability is 1
 - Multiplied by 8 if has any subject country has liberty desire is 50


###Efects:<ul><li>magic casted spell = yes</li><li>magic scrying dissidents cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 6 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 3 years</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_dissidents_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying dissidents cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 6 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 3 years</li></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_dissidents_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 50</li></ul><li>has ruler modifier magic_realm_divination_scrying_internal_dissidents</li></ul>

###Efects:<ul><li>If has ruler modifier is magic realm divination scrying internal dissidents:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = magic_need_50_adm_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying dissidents cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 6 years</li><li>custom tooltip = magic_booster_by_patron_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_internal_dissidents for 3 years</li></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_affairs£

###Available if:
<li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>adm power is at least 50</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_divination_scrying_affairs</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 8 if has adm power is 200, and has dip power is 200, and has mil power is 200


###Efects:<ul><li>magic casted spell = yes</li><li>magic scrying realm cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 6 years</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 3 years</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_affairs_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying realm cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 6 years</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 3 years</li></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_affairs_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 50</li></ul><li>has ruler modifier magic_realm_divination_scrying_affairs</li></ul>

###Efects:<ul><li>If has ruler modifier is magic realm divination scrying affairs:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = magic_need_50_adm_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic scrying realm cost = yes</li><li>If has ruler flag is [ancestor_spirit_patron](../flags/ancestor_spirit_patron.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 6 years</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_1](../flags/tughayasa_better_divination_1.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 1375 days</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>Else if has 4527 has owned by is ROOT, and 4527 has province flag is [tughayasa_better_divination_2](../flags/tughayasa_better_divination_2.md):</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 5 years</li><li>custom tooltip = tughayasa_divination_booster_tt</li></ul><li>else:</li><ul><li>country gets the modifier magic_realm_divination_scrying_affairs for 3 years</li></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_loreseeker£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>has ruler flag  baku_patron</li></ul></ul><li>ruler studying magic is yes</li><li>magic legend lore cost trigger is yes</li><li>None of the following:</li><ul><li>has ruler modifier magic_loreseeker_cooldown</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>magic casted spell = yes</li><li>magic legend lore effect = yes</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_loreseeker_desc_tt</li><li>If has ruler flag is [baku_patron](../flags/baku_patron.md), and does not have ruler flag is [divination_1](../flags/divination_1.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul></ul>

___
##£spell_loreseeker_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>has ruler flag  baku_patron</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic legend lore effect = yes</li></ul><li>custom tooltip = magic_loreseeker_desc_tt</li></ul>

___
##£spell_loreseeker_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_1](../flags/divination_1.md)</li><li>has ruler flag  baku_patron</li></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>ruler studying magic is yes</li></ul><li>NOT:</li><ul><li>magic legend lore cost trigger is yes</li></ul><li>has ruler modifier magic_loreseeker_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic loreseeker cooldown:</li><ul><li>custom tooltip = magic_1_year_cooldown_tt</li></ul><li>magic legend lore cost tooltip = yes</li><li>If does not have ruler studying magic is yes:</li><ul><li>custom tooltip = magic_ruler_studying_magic_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>magic legend lore effect = yes</li></ul><li>custom tooltip = magic_loreseeker_desc_tt</li></ul>

___
##£spell_foresight£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [divination_3](../flags/divination_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>has ruler flag  nang_patron</li><li>has ruler flag   bladedancer_patron</li></ul></ul><li>adm power is at least 150</li><li>dip power is at least 150</li><li>mil power is at least 150</li><li>None of the following:</li><ul><li>has ruler modifier magic_realm_divination_foresight</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_realm_divination_foresight_madness</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_foresight_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has ruler has personality is careful personality
 - Multiplied by 0.25 if has ruler has personality is immortal personality
 - Multiplied by 0.5 if has ruler flag is [foresight_spell_11](../flags/foresight_spell_11.md), and has ruler flag is foresight spell 12, and has ruler flag is foresight spell 13, and has ruler flag is foresight spell 14, and has ruler flag is foresight spell 15
 - Multiplied by 0.25 if has ruler flag is [foresight_spell_16](../flags/foresight_spell_16.md), and has ruler flag is foresight spell 17, and has ruler flag is foresight spell 18, and has ruler flag is foresight spell 19, and has ruler flag is foresight spell 20
 - Multiplied by 1.5 if has ruler has personality is naive personality


###Efects:<ul><li>add adm power = -150</li><li>add dip power = -150</li><li>add mil power = -150</li><li>magic casted spell = yes</li><li>casted foresight spell flag = yes</li><li>apply foresight spell = yes</li><li>If has ruler flag is [nang_patron](../flags/nang_patron.md), and does not have ruler flag is [divination_3](../flags/divination_3.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>add ruler modifier:</li><ul><li>name = magic_foresight_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_foresight_desc_tt</li></ul>

___
##£spell_foresight_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [divination_3](../flags/divination_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>has ruler flag  nang_patron</li><li>has ruler flag   bladedancer_patron</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>casted foresight spell flag = yes</li><li>apply foresight spell = yes</li></ul><li>custom tooltip = magic_foresight_desc_tt</li></ul>

___
##£spell_foresight_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [divination_3](../flags/divination_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [divination_2](../flags/divination_2.md)</li><li>has ruler flag  nang_patron</li><li>has ruler flag   bladedancer_patron</li></ul></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>adm power is at least 150</li></ul><li>NOT:</li><ul><li>dip power is at least 150</li></ul><li>NOT:</li><ul><li>mil power is at least 150</li></ul><li>has ruler modifier magic_realm_divination_foresight</li><li>has ruler modifier  magic_realm_divination_foresight_madness</li><li>has ruler modifier   magic_foresight_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic foresight cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 150:</li><ul><li>custom tooltip = magic_need_150_adm_tt</li></ul><li>If does not have dip power is 150:</li><ul><li>custom tooltip = magic_need_150_dip_tt</li></ul><li>If does not have mil power is 150:</li><ul><li>custom tooltip = magic_need_150_mil_tt</li></ul><li>If has ruler modifier is magic realm divination foresight:</li><ul><li>custom tooltip = magic_spell_already_active_tt</li></ul><li>If has ruler modifier is magic realm divination foresight madness:</li><ul><li>custom tooltip = magic_foresight_madness_tt</li></ul><li>set country flag [divination_menu](../flags/divination_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_ruler_9_t](../events/missing_localisation_magic_ruler_9_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>casted foresight spell flag = yes</li><li>apply foresight spell = yes</li></ul><li>custom tooltip = magic_foresight_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event [£ruler_magic_menu_bg£\n\n[Root.GetMagicalInfamy]                                                          \n                                     [Root.GetMasteryDivination]\n                                     [Root.GetMasteryConjuration]       [Root.GetMasteryEnchantment]\n\n                                      [Root.GetMasteryNecromancy]            [Root.GetMasteryAbjuration]\n  [Root.GetMagicStudySchool]                               [Root.GetMasteryIllusion]       [Root.GetMasteryTransmutation]\n[Root.GetMagicStudyBar]                         [Root.GetMasteryEvocation]      ](../events/psruler_magic_menu_bgps_n_n_root_getmagicalinfamy_n_root_getmasterydivination_n_root_getmasteryconjuration_root_getmasteryenchantment_n_n_root_getmasterynecromancy_root_getmasteryabjuration_n_root_getmagicstudyschool_root_getmasteryillusion_root_getmasterytransmutation_n_root_getmagicstudybar_root_getmasteryevocation.md) happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
