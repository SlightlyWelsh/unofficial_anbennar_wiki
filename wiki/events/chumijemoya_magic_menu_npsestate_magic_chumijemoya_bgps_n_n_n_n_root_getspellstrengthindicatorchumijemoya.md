#Information
 - Title:     Chumijemoya Magic Menu\n£estate_magic_chumijemoya_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorChumijemoya]                                   
 - ID: flavor_azjakuma.1252
#Description
    Chumijemoya Magic Menu\n£estate_magic_chumijemoya_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorChumijemoya]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_khelorvalshi_cast_magic</li></ul><li>else:</li><ul><li>set country flag [remove_azjakuma_casting_spells](../flags/remove_azjakuma_casting_spells.md)</li></ul><li>the event ˻flavor_azjakuma.1250˼ happens</li></ul>

___
##£spell_numbing_haze£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>else:</li><ul><li>add adm power = -10</li><li>add dip power = -10</li><li>add mil power = -10</li></ul><li>If has estate influence has estate is estate chumijemoya, and estate influence has influence is 66:</li><ul><li>custom tooltip = azjakuma_lost_in_mist_3_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region:</li><ul><li>add province modifier:</li><ul><li>name = estate_chumijemoya_magic_lost_in_mist_lvl3_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate chumijemoya, and estate influence has influence is 33:</li><ul><li>custom tooltip = azjakuma_lost_in_mist_2_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region:</li><ul><li>add province modifier:</li><ul><li>name = estate_chumijemoya_magic_lost_in_mist_lvl2_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = azjakuma_lost_in_mist_1_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region:</li><ul><li>add province modifier:</li><ul><li>name = estate_chumijemoya_magic_lost_in_mist_lvl1_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_mist_desc_tt</li></ul>

___
##£spell_mind_clouding£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -1.5</li><li>add dip power = -15</li></ul><li>else:</li><ul><li>add years of income = -1</li><li>add dip power = -10</li></ul><li>If has estate influence has estate is estate chumijemoya, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_chumijemoya_mind_control_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate chumijemoya, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_chumijemoya_mind_control_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_chumijemoya_mind_control_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_mind_control_desc_tt</li></ul>

___
##£spell_mist_whispers£

###Available if:
<li>has country flag [oni_silent_mist_privilege](../flags/oni_silent_mist_privilege.md)</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.75</li><li>add dip power = -15</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add dip power = -10</li></ul><li>If has estate influence has estate is estate chumijemoya, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate chumijemoya, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_spynetworks_desc_tt</li></ul>

___
##£spell_mist_whispers_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>has country flag [oni_silent_mist_privilege](../flags/oni_silent_mist_privilege.md)</li></ul>

###Efects:<ul><li>set country flag [chumijemoya_menu](../flags/chumijemoya_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻flavor_azjakuma.1256˼ happens</li></ul><li>custom tooltip = azjakuma_has_silent_mist_privilege_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.75</li><li>add dip power = -15</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add dip power = -10</li></ul><li>If has estate influence has estate is estate chumijemoya, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate chumijemoya, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_chumijemoya_spymasters_lvl1_mod for 10 years</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_spynetworks_desc_tt</li></ul>

___
##£spell_fog_unravelling£

###Available if:
<li>is at war</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul><li>else:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_fow_desc_tt</li></ul>

___
##£spell_fog_unravelling_r£

###Available if:
<li>is not controlled by the AI</li><li>is not at war</li>

###Efects:<ul><li>set country flag [chumijemoya_menu](../flags/chumijemoya_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻flavor_azjakuma.1256˼ happens</li></ul><li>custom tooltip = magic_is_at_war_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul><li>else:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul></ul><li>custom tooltip = azjakuma_remove_fow_tt</li><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_fow_desc_tt</li></ul>
