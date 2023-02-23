#Information
 - Title:     Kabiurgarko Magic Menu\n£estate_magic_kabiurgarko_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorKabiurgarko]                                   
 - ID: flavor_azjakuma.1254
#Description
    Kabiurgarko Magic Menu\n£estate_magic_kabiurgarko_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorKabiurgarko]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_khelorvalshi_cast_magic</li></ul><li>else:</li><ul><li>set country flag [remove_azjakuma_casting_spells](../flags/remove_azjakuma_casting_spells.md)</li></ul><li>the event ˻flavor_azjakuma.1250˼ happens</li></ul>

___
##£spell_earth_bending£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.75</li></ul><li>else:</li><ul><li>add years of income = -0.5</li></ul><li>If has estate influence has estate is estate kabiurgarko, and estate influence has influence is 66:</li><ul><li>custom tooltip = estate_kabiurgarko_production_lvl3_mod_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_kabiurgarko_production_lvl3_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate kabiurgarko, and estate influence has influence is 33:</li><ul><li>custom tooltip = estate_kabiurgarko_production_lvl2_mod_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_kabiurgarko_production_lvl2_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = estate_kabiurgarko_production_lvl1_mod_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has region is demon hills region, and has terrain is hills, and has terrain is mountain:</li><ul><li>add province modifier:</li><ul><li>name = estate_kabiurgarko_production_lvl1_mod</li><li>duration = 3650</li></ul></ul></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_production_desc_tt</li></ul>

___
##£spell_wood_bending£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.75</li><li>add adm power = -30</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add adm power = -20</li></ul><li>If has estate influence has estate is estate kabiurgarko, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_kabiurgarko_construction_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate kabiurgarko, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_kabiurgarko_construction_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_kabiurgarko_construction_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_contruction_desc_tt</li></ul>

___
##£spell_soul_bending£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -4.5</li><li>add adm power = -45</li><li>add dip power = -45</li><li>add mil power = -45</li></ul><li>else:</li><ul><li>add years of income = -3</li><li>add adm power = -30</li><li>add dip power = -30</li><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate kabiurgarko, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_kabiurgarko_energy_bending_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate kabiurgarko, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_kabiurgarko_energy_bending_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_kabiurgarko_energy_bending_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_energy_bending_desc_tt</li></ul>

___
##£spell_metal_bending£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.5</li><li>add adm power = -45</li><li>add dip power = -45</li><li>add mil power = -45</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add adm power = -30</li><li>add dip power = -30</li><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate kabiurgarko, and estate influence has influence is 66:</li><ul><li>country gets the modifier estate_kabiurgarko_metal_bending_lvl3_mod for 10 years</li></ul><li>Else if has estate influence has estate is estate kabiurgarko, and estate influence has influence is 33:</li><ul><li>country gets the modifier estate_kabiurgarko_metal_bending_lvl2_mod for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier estate_kabiurgarko_metal_bending_lvl1_mod for 10 years</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_metal_bending_desc_tt</li></ul>
