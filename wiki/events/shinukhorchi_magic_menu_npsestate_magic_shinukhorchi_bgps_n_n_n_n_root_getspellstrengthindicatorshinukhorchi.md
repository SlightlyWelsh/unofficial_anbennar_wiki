#Information
 - Title:     Shinukhorchi Magic Menu\n£estate_magic_shinukhorchi_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorShinukhorchi]                                   
 - ID: flavor_azjakuma.1251
#Description
    Shinukhorchi Magic Menu\n£estate_magic_shinukhorchi_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorShinukhorchi]                                   
#Options

___
##£magic_button_go_back£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_khelorvalshi_cast_magic</li></ul><li>else:</li><ul><li>set country flag [remove_azjakuma_casting_spells](../flags/remove_azjakuma_casting_spells.md)</li></ul><li>the event [Cast Shirgrii Magic](../events/cast_shirgrii_magic.md) happens</li></ul>

___
##£spell_talisman£

###Available if:
<li>has country flag [korashi_talismans_unlocked](../flags/korashi_talismans_unlocked.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 20 if is at war


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul><li>else:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>country gets the modifier estate_shinukhorchi_korashi_talisman_mod for 10 years</li><li>5430:</li><ul><li>add province modifier:</li><ul><li>name = estate_shinukhorchi_magic_korashi_talismans_prod_mod</li><li>duration = 3650</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_korashi_talisman_desc_tt</li></ul>

___
##£spell_fertility£

###Available if:
<li>has consort</li><li>has government attribute heir</li><li>is not lesser in union</li><li>None of the following:</li><ul><li>ruler is immortal is yes</li></ul><li>has reform demon_empire_reform</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has ruler has mage personality is yes
 - Multiplied by 0.5 if has heir
 - Multiplied by 0.8 if has adm is 6, and has dip is 6, and has mil is 6
 - Multiplied by 0.25 if has years of income is 1.5


###Efects:<ul><li>add years of income = -1</li><li>If has heir:</li><ul><li>add legitimacy = -10</li></ul><li>custom tooltip = shinukhorchi_estate_rite_of_conception_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1257_t](../events/missing_localisation_flavor_azjakuma_1257_t.md) happens</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_fertility_desc_tt</li></ul>

___
##£spell_fertility_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>does not have consort</li><li>None of the following:</li><ul><li>has government attribute heir</li></ul><li>is lesser in union</li><li>ruler is immortal is yes</li><li>NOT:</li><ul><li>has reform demon_empire_reform</li></ul></ul>

###Efects:<ul><li>If does not have reform is demon empire reform:</li><ul><li>custom tooltip = magic_need_demon_empire_reform_tt</li></ul><li>If does not have consort:</li><ul><li>custom tooltip = magic_need_consort_tt</li></ul><li>If does not have government attribute is heir:</li><ul><li>custom tooltip = magic_government_allow_heirs_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If has ruler is immortal is yes:</li><ul><li>custom tooltip = magic_ruler_is_mortal_tt</li></ul><li>set country flag [shinukhorchi_menu](../flags/shinukhorchi_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1256_t](../events/missing_localisation_flavor_azjakuma_1256_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add years of income = -1</li><li>If has heir:</li><ul><li>add legitimacy = -10</li></ul></ul><li>custom tooltip = shinukhorchi_estate_rite_of_conception_tooltip</li><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_fertility_desc_tt</li></ul>

___
##£spell_vassal_domination£

###Available if:
<li>has country flag [vassal_acceptance_magic_unlocked](../flags/vassal_acceptance_magic_unlocked.md)</li>

###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.75</li><li>add dip power = -30</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add dip power = -20</li></ul><li>If has estate influence has estate is estate shinukhorchi, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_shinukhorchi_vassal_acceptance_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate shinukhorchi, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_shinukhorchi_vassal_acceptance_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_shinukhorchi_vassal_acceptance_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_vassal_domination_desc_tt</li></ul>

___
##£spell_blazing_soul£

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has average unrest is 0
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>add adm power = -25</li><li>add mil power = -25</li><li>If has estate influence has estate is estate shinukhorchi, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_shinukhorchi_blazing_souls_3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate shinukhorchi, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_shinukhorchi_blazing_souls_2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_shinukhorchi_blazing_souls_1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_blazing_field_desc_tt</li></ul>
