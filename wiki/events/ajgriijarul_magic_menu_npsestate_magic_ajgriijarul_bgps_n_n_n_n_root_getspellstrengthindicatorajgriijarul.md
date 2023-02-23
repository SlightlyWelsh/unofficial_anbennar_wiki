#Information
 - Title:     Ajgriijarul Magic Menu\n£estate_magic_ajgriijarul_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorAjgriijarul]                                   
 - ID: flavor_azjakuma.1253
#Description
    Ajgriijarul Magic Menu\n£estate_magic_ajgriijarul_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorAjgriijarul]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_khelorvalshi_cast_magic</li></ul><li>else:</li><ul><li>set country flag [remove_azjakuma_casting_spells](../flags/remove_azjakuma_casting_spells.md)</li></ul><li>the event ˻flavor_azjakuma.1250˼ happens</li></ul>

___
##£spell_warrior_mist£

###Available if:
<li>any known country:</li><ul><li>war with is this nation</li><li>ROOT:</li><ul><li>None of the following:</li><ul><li>army strength:</li><ul><li>PREV</li><li>value is at least 0.90</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add mil power = -45</li></ul><li>else:</li><ul><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate ajgriijarul, and estate influence has influence is 66:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl3_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl3_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate ajgriijarul, and estate influence has influence is 33:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl2_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl2_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl1_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl1_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_demon_hills_desc_tt</li></ul>

___
##£spell_warrior_mist_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>any known country:</li><ul><li>war with is this nation</li><li>ROOT:</li><ul><li>None of the following:</li><ul><li>army strength:</li><ul><li>PREV</li><li>value is at least 0.90</li></ul></ul></ul></ul></ul>

###Efects:<ul><li>set country flag [ajgriijarul_menu](../flags/ajgriijarul_menu.md)</li><li>hidden effect:</li><ul><li>the event ˻flavor_azjakuma.1256˼ happens</li></ul><li>custom tooltip = magic_is_at_war_with_powerful_enemy_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add mil power = -45</li></ul><li>else:</li><ul><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate ajgriijarul, and estate influence has influence is 66:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl3_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl3_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate ajgriijarul, and estate influence has influence is 33:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl2_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl2_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = estate_ajgriijarul_defend_demon_hills_mod_lvl1_tooltp</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_ajgriijarul_defend_demon_hills_lvl1_mod</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_demon_hills_desc_tt</li></ul>

___
##£spell_dominate_unruly£

###Available if:
<li>has country flag [unlock_ajgriijarul_rebel_supression](../flags/unlock_ajgriijarul_rebel_supression.md)</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add dip power = -15</li><li>add mil power = -45</li></ul><li>else:</li><ul><li>add dip power = -10</li><li>add mil power = -30</li></ul><li>custom tooltip = azjakuma_clear_rebels_tt</li><li>hidden effect:</li><ul><li>every owned province:</li><ul><li>clear rebels = yes</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_dominate_unruly_desc_tt</li></ul>

___
##£spell_rage£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add mil power = -60</li></ul><li>else:</li><ul><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate ajgriijarul, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_ajgriijarul_trance_induced_rage_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate ajgriijarul, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_ajgriijarul_trance_induced_rage_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_ajgriijarul_trance_induced_rage_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_trance_rage_desc_tt</li></ul>

___
##£spell_soul_ignition£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add manpower = -5</li><li>add mil power = -30</li></ul><li>else:</li><ul><li>add manpower = -3</li><li>add mil power = -15</li></ul><li>If has estate influence has estate is estate ajgriijarul, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_ajgriijarul_soul_ignition_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate ajgriijarul, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_ajgriijarul_soul_ignition_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_ajgriijarul_soul_ignition_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_soul_ignition_desc_tt</li></ul>
