#Information
 - Title:     Transmutation\n£ruler_magic_transmutation_bg£\n\n[Root.GetSchoolMasteryTransmutation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
 - ID: magic_ruler.8
#Description
    Transmutation\n£ruler_magic_transmutation_bg£\n\n[Root.GetSchoolMasteryTransmutation]                                                       \n\n\n[Root.GetMagicStudySchoolBis]   [Root.GetMagicStudyBarBis]                                                    
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If is controlled by the AI:</li><ul><li>add ruler modifier:</li><ul><li>name = magic_realm_menu_cooldown</li><li>duration = 1825</li><li>hidden = yes</li></ul><li>close single menu = yes</li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>

___
##£magic_button_study£

###Available if:
<li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>NOT:</li><ul><li>ruler studying magic is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has ruler flag is [transmutation_1](../flags/transmutation_1.md), and has ruler flag is transmutation 2


###Efects:<ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>the event ˻magic_study.22˼ happens</li></ul>

___
##£magic_button_study_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [ruler_studying_transmutation](../flags/ruler_studying_transmutation.md)</li><li>None of the following:</li><ul><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>magic study clear study effects = yes</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£magic_button_study_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [ruler_studying_transmutation](../flags/ruler_studying_transmutation.md)</li></ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>ruler studying magic is yes</li><li>has finished magical studies yes</li></ul>

###Efects:<ul><li>custom tooltip = cant_study_magic_tt</li><li>If has ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>custom tooltip = school_mastery_at_max_tt</li></ul><li>If has ruler studying magic is yes:</li><ul><li>custom tooltip = already_studying_magic_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul></ul>

___
##£spell_plant_1£

###Available if:
<li>has ruler flag [transmutation_1](../flags/transmutation_1.md)</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul><li>adm power is at least 30</li><li>dip power is at least 5</li><li>NOT:</li><ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -5</li><li>the event ˻magic_ruler.17˼ happens</li><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_1](../flags/transmutation_1.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_talented_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_1_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_1](../flags/transmutation_1.md)</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul></ul><li>NOT:</li><ul><li>adm power is at least 30</li></ul><li>NOT:</li><ul><li>dip power is at least 5</li></ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic plant cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 30:</li><ul><li>custom tooltip = magic_need_30_adm_tt</li></ul><li>If does not have dip power is 5:</li><ul><li>custom tooltip = magic_need_5_dip_tt</li></ul><li>If does not have any owned province has province with farm goods is yes, and any owned province has no plant growth province modifiers is yes:</li><ul><li>custom tooltip = magic_need_province_with_farms_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_2£

###Available if:
<li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul><li>adm power is at least 30</li><li>dip power is at least 5</li><li>NOT:</li><ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -5</li><li>the event ˻magic_ruler.17˼ happens</li><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul></ul><li>NOT:</li><ul><li>adm power is at least 30</li></ul><li>NOT:</li><ul><li>dip power is at least 5</li></ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic plant cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 30:</li><ul><li>custom tooltip = magic_need_30_adm_tt</li></ul><li>If does not have dip power is 5:</li><ul><li>custom tooltip = magic_need_5_dip_tt</li></ul><li>If does not have any owned province has province with farm goods is yes, and any owned province has no plant growth province modifiers is yes:</li><ul><li>custom tooltip = magic_need_province_with_farms_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_enhance_1£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_1</li></ul></ul><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul></ul><li>NOT:</li><ul><li>has ruler modifier magic_enhance_cooldown</li></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>adm is at least 6</li></ul><li>NOT:</li><ul><li>dip is at least 6</li></ul><li>NOT:</li><ul><li>mil is at least 6</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md), and does not have ruler flag is [transmutation_2](../flags/transmutation_2.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_1_tt</li><li>the event ˻magic_ruler.18˼ happens</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_enhance_1_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_1</li></ul></ul></ul><li>NOT:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_1_tt</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_enhance_1_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_1</li></ul></ul><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul></ul><li>OR:</li><ul><li>has ruler modifier magic_enhance_cooldown</li><li>All of the following:</li><ul><li>adm is at least 6</li><li>dip is at least 6</li><li>mil is at least 6</li></ul></ul>

###Efects:<ul><li>If has ruler modifier is magic enhance cooldown:</li><ul><li>custom tooltip = magic_5_year_cooldown_tt</li></ul><li>If has adm is 6, and  has dip is 6, and  has mil is 6:</li><ul><li>custom tooltip = magic_need_ruler_without_max_skills_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_1_tt</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_conception_1£

###Available if:
<li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>has ruler flag  abjuration_1</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>adm power is at least 100</li><li>NOT:</li><ul><li>government is theocracy</li></ul><li>NOT:</li><ul><li>has adventurer reform yes</li></ul><li>has government attribute heir</li><li>is not lesser in union</li><li>NOT:</li><ul><li>ruler is immortal is yes</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_conception_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if does not have heir
 - Multiplied by 2 if has heir, and does not have heir has mage personality is yes, and does not have heir flag is [heir_consort_mage_personality](../flags/heir_consort_mage_personality.md)


###Efects:<ul><li>add adm power = -100</li><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_conception_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>tooltip:</li><ul><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>70:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>60:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>10:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.20˼ happens</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_conception_1_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [abjuration_1](../flags/abjuration_1.md)</li></ul></ul><li>None of the following:</li><ul><li>All of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>has ruler flag  abjuration_1</li></ul></ul>

###Efects:<ul><li>If does not have ruler flag is [transmutation_2](../flags/transmutation_2.md):</li><ul><li>custom tooltip = school_mastery_not_renowned_tt</li></ul><li>If does not have ruler flag is [abjuration_1](../flags/abjuration_1.md):</li><ul><li>custom tooltip = school_mastery_abjuration_not_talented_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>70:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>60:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>10:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_conception_1_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>has ruler flag  abjuration_1</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 100</li></ul><li>government is theocracy</li><li>has adventurer reform yes</li><li>NOT:</li><ul><li>has government attribute heir</li></ul><li>is lesser in union</li><li>ruler is immortal is yes</li><li>has ruler modifier magic_conception_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic conception cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 100:</li><ul><li>custom tooltip = magic_need_100_adm_tt</li></ul><li>If has government is theocracy:</li><ul><li>custom tooltip = magic_no_theocracy_tt</li></ul><li>If does not have government attribute is heir:</li><ul><li>custom tooltip = magic_government_allow_heirs_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If has ruler is immortal is yes:</li><ul><li>custom tooltip = magic_ruler_is_mortal_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>70:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>60:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>10:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_giant£

###Available if:
<li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has current age is age of revolutions


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 5</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_giant_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>the event ˻magic_siege.20˼ happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_giant_desc_tt</li></ul>

___
##£spell_giant_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 5</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_giant_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = school_mastery_not_renowned_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_giant_desc_tt</li></ul>

___
##£spell_giant_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_2](../flags/transmutation_2.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 5</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_giant_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_giant_desc_tt</li></ul>

___
##£spell_plant_3£

###Available if:
<li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul><li>adm power is at least 30</li><li>dip power is at least 5</li><li>None of the following:</li><ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>add adm power = -30</li><li>add dip power = -5</li><li>the event ˻magic_ruler.17˼ happens</li><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_4</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_3_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_4</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_3_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>any owned province:</li><ul><li>province with farm goods is yes</li><li>has no plant growth province modifiers yes</li></ul></ul><li>NOT:</li><ul><li>adm power is at least 30</li></ul><li>NOT:</li><ul><li>dip power is at least 5</li></ul><li>has ruler modifier magic_plant_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic plant cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 30:</li><ul><li>custom tooltip = magic_need_30_adm_tt</li></ul><li>If does not have dip power is 5:</li><ul><li>custom tooltip = magic_need_5_dip_tt</li></ul><li>If does not have any owned province has province with farm goods is yes, and any owned province has no plant growth province modifiers is yes:</li><ul><li>custom tooltip = magic_need_province_with_farms_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -30</li><li>add dip power = -5</li></ul><li>custom tooltip = magic_selected_province_tt</li><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_4</li><li>duration = 1825</li></ul></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_enhance_2£

###Available if:
<li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_enhance_cooldown</li></ul><li>OR:</li><ul><li>None of the following:</li><ul><li>adm is at least 6</li></ul><li>NOT:</li><ul><li>dip is at least 6</li></ul><li>NOT:</li><ul><li>mil is at least 6</li></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_2_tt</li><li>the event ˻magic_ruler.18˼ happens</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_enhance_2_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_2_tt</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_enhance_2_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>All of the following:</li><ul><li>has ruler flag [hoko_patron](../flags/hoko_patron.md)</li><li>has ruler flag  transmutation_2</li></ul></ul><li>OR:</li><ul><li>has ruler modifier magic_enhance_cooldown</li><li>All of the following:</li><ul><li>adm is at least 6</li><li>dip is at least 6</li><li>mil is at least 6</li></ul></ul>

###Efects:<ul><li>If has ruler modifier is magic enhance cooldown:</li><ul><li>custom tooltip = magic_5_year_cooldown_tt</li></ul><li>If has adm is 6, and  has dip is 6, and  has mil is 6:</li><ul><li>custom tooltip = magic_need_ruler_without_max_skills_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>If has ruler flag is [hoko_patron](../flags/hoko_patron.md):</li><ul><li>custom tooltip = magic_spell_available_by_patron_tt</li></ul><li>custom tooltip = magic_enhance_effect_2_tt</li><li>custom tooltip = magic_enhance_desc_tt</li></ul>

___
##£spell_conception_2£

###Available if:
<li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>has ruler flag  abjuration_1</li><li>adm power is at least 100</li><li>None of the following:</li><ul><li>government is theocracy</li></ul><li>NOT:</li><ul><li>has adventurer reform yes</li></ul><li>has government attribute heir</li><li>is not lesser in union</li><li>NOT:</li><ul><li>ruler is immortal is yes</li></ul><li>NOT:</li><ul><li>has ruler modifier magic_conception_cooldown</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if does not have heir
 - Multiplied by 2 if has heir, and does not have heir has mage personality is yes, and does not have heir flag is [heir_consort_mage_personality](../flags/heir_consort_mage_personality.md)


###Efects:<ul><li>magic casted spell = yes</li><li>add ruler modifier:</li><ul><li>name = magic_conception_cooldown</li><li>duration = 30</li><li>hidden = yes</li></ul><li>add adm power = -100</li><li>tooltip:</li><ul><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>45:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>50:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>65:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>30:</li><ul></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.20˼ happens</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_conception_2_g£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul><li>NOT:</li><ul><li>has ruler flag [abjuration_1](../flags/abjuration_1.md)</li></ul></ul>

###Efects:<ul><li>If does not have ruler flag is [transmutation_3](../flags/transmutation_3.md):</li><ul><li>custom tooltip = school_mastery_not_legendary_tt</li></ul><li>If does not have ruler flag is [abjuration_1](../flags/abjuration_1.md):</li><ul><li>custom tooltip = school_mastery_abjuration_not_talented_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>45:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>50:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>65:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>30:</li><ul></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_conception_2_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>has ruler flag  abjuration_1</li><li>Any of the following:</li><ul><li>None of the following:</li><ul><li>adm power is at least 100</li></ul><li>government is theocracy</li><li>has adventurer reform yes</li><li>NOT:</li><ul><li>has government attribute heir</li></ul><li>is lesser in union</li><li>ruler is immortal is yes</li><li>has ruler modifier magic_conception_cooldown</li></ul>

###Efects:<ul><li>If has ruler modifier is magic conception cooldown:</li><ul><li>custom tooltip = magic_1_month_cooldown_tt</li></ul><li>If does not have adm power is 100:</li><ul><li>custom tooltip = magic_need_100_adm_tt</li></ul><li>If has government is theocracy:</li><ul><li>custom tooltip = magic_no_theocracy_tt</li></ul><li>If does not have government attribute is heir:</li><ul><li>custom tooltip = magic_government_allow_heirs_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If has ruler is immortal is yes:</li><ul><li>custom tooltip = magic_ruler_is_mortal_tt</li></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add adm power = -100</li><li>If does not have consort:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>45:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 20</li><li>no consort with heir = yes</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>50:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul></ul></ul><li>Else if has ruler has mage personality is yes, and  has consort has mage personality is yes:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>65:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>30:</li><ul></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>tooltip:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 100</li><li>hidden = yes</li></ul><li>set heir mage effect = yes</li></ul><li>40:</li><ul></ul><li>5:</li><ul><li>kill ruler = yes</li></ul><li>5:</li><ul><li>remove consort = yes</li></ul></ul></ul></ul></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_dragon£

###Available if:
<li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>is at war</li><li>is not lesser in union</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul><li>None of the following:</li><ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###AI weighting:
AI weights this option at 50


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 10</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_dragon_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>the event ˻magic_siege.23˼ happens</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_dragon_desc_tt</li></ul>

___
##£spell_dragon_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 10</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_dragon_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_dragon_desc_tt</li></ul>

___
##£spell_dragon_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>Any of the following:</li><ul><li>is not at war</li><li>is lesser in union</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li><li>unit has leader</li></ul></ul></ul><li>has ruler modifier magic_siege_cooldown</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>change controller = ROOT</li><li>add devastation = 10</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>tooltip:</li><ul><li>add province modifier:</li><ul><li>name = siege_magic_dragon_besieger</li><li>duration = 14</li></ul></ul></ul>

###Efects:<ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>If has ruler modifier is magic siege cooldown:</li><ul><li>custom tooltip = magic_siege_cooldown_tt</li></ul><li>If is not at war:</li><ul><li>custom tooltip = magic_is_at_war_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If does not have any army has location has fort level is 1, and location has sieged by is ROOT, and location has unit has leader:</li><ul><li>custom tooltip = magic_leadered_army_sieging_tt</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>custom tooltip = magic_dragon_desc_tt</li></ul>

___
##£spell_homunculus£

###Available if:
<li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>None of the following:</li><ul><li>magical project in progress is yes</li></ul><li>NOT:</li><ul><li>has ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li></ul><li>adm power is at least 50</li><li>dip power is at least 50</li><li>mil power is at least 50</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>increase witch king points medium = yes</li><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li><li>magic casted spell = yes</li><li>set ruler flag [magic_project_homunculus_started](../flags/magic_project_homunculus_started.md)</li><li>custom tooltip = tooltip_magic_project_start</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_homunculus_desc_tt</li></ul>

___
##£spell_homunculus_g£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li></ul>

###Efects:<ul><li>custom tooltip = school_mastery_not_legendary_tt</li><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>increase witch king points medium = yes</li><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_homunculus_desc_tt</li></ul>

___
##£spell_homunculus_r£

###Available if:
<li>is not controlled by the AI</li><li>has ruler flag [transmutation_3](../flags/transmutation_3.md)</li><li>Any of the following:</li><ul><li>magical project in progress is yes</li><li>has ruler flag [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md)</li><li>None of the following:</li><ul><li>adm power is at least 50</li></ul><li>NOT:</li><ul><li>dip power is at least 50</li></ul><li>NOT:</li><ul><li>mil power is at least 50</li></ul></ul>

###Efects:<ul><li>If has ruler flag is [magic_project_homunculus_complete](../flags/magic_project_homunculus_complete.md):</li><ul><li>custom tooltip = magic_project_already_done_tt</li></ul><li>else:</li><ul><li>If has ruler flag is [magic_project_homunculus_started](../flags/magic_project_homunculus_started.md):</li><ul><li>custom tooltip = magic_project_started_tt</li></ul><li>Else if has magical project in progress is yes:</li><ul><li>custom tooltip = magic_other_project_in_progress_tt</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = magic_need_50_adm_tt</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = magic_need_50_dip_tt</li></ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = magic_need_50_mil_tt</li></ul></ul><li>set country flag [transmutation_menu](../flags/transmutation_menu.md)</li><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li><li>hidden effect:</li><ul><li>the event ˻magic_ruler.9˼ happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>increase witch king points medium = yes</li><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li></ul><li>custom tooltip = tooltip_magic_project_start</li><li>custom tooltip = magic_homunculus_desc_tt</li></ul>

___
##£magic_button_go_back£

###Available if:
<li>is not controlled by the AI</li>

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻magic_ruler.0˼ happens</li></ul><li>clr ruler flag [magic_just_casted_spell](../flags/magic_just_casted_spell.md)</li></ul>
