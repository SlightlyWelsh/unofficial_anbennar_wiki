#Information
 - Title:     Khelorvalshi Magic Menu\n£estate_magic_khelorvalshi_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorKhelorvalshi]                                   
 - ID: flavor_azjakuma.1255
#Description
    Khelorvalshi Magic Menu\n£estate_magic_khelorvalshi_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorKhelorvalshi]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_khelorvalshi_cast_magic</li></ul><li>else:</li><ul><li>set country flag [remove_azjakuma_casting_spells](../flags/remove_azjakuma_casting_spells.md)</li></ul><li>the event [Cast Shirgrii Magic](../events/cast_shirgrii_magic.md) happens</li></ul>

___
##£spell_drain_defenders£

###Available if:
<li>is at war</li><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.375</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul><li>else:</li><ul><li>add years of income = -0.25</li><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>event target:spell target province:</li><ul><li>add devastation = 70</li><li>add province modifier:</li><ul><li>name = estate_khelorvalshi_siege_magic_mod</li><li>duration = 14</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_drain_defenders_desc_tt</li></ul>

___
##£spell_drain_defenders_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>is not at war</li><li>None of the following:</li><ul><li>any army:</li><ul><li>location:</li><ul><li>fort level is at least 1</li><li>sieged by is this nation</li></ul></ul></ul></ul>

###Efects:<ul><li>set country flag [khelorvalshi_menu](../flags/khelorvalshi_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1256_t](../events/missing_localisation_flavor_azjakuma_1256_t.md) happens</li></ul><li>custom tooltip = magic_army_sieging_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add years of income = -0.375</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add mil power = -20</li></ul><li>else:</li><ul><li>add years of income = -0.25</li><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>custom tooltip = magic_if_siege_magic_succeeds_tt</li><li>add province modifier:</li><ul><li>name = estate_khelorvalshi_siege_magic_mod</li><li>duration = 14</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_drain_defenders_desc_tt</li></ul>

___
##£spell_drain_pop£

###Available if:
<li>calc true if:</li><ul><li>amount is at least 2</li><li>all owned province:</li><ul><li>base tax is at least 2</li><li>base production is at least 2</li><li>base manpower is at least 2</li><li>None of the following:</li><ul><li>devastation is at least 50</li></ul></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>event target:khelorvalshi drain target 1:</li><ul><li>add devastation = 85</li><li>add base tax = -2</li><li>add base production = -1</li><li>add base manpower = -2</li></ul><li>event target:khelorvalshi drain target 2:</li><ul><li>add devastation = 85</li><li>add base tax = -2</li><li>add base production = -1</li><li>add base manpower = -2</li></ul></ul><li>else:</li><ul><li>event target:khelorvalshi drain target 1:</li><ul><li>add devastation = 70</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>event target:khelorvalshi drain target 2:</li><ul><li>add devastation = 70</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul></ul><li>If has estate influence has estate is estate khelorvalshi, and estate influence has influence is 66:</li><ul><li>add adm power = 150</li><li>add dip power = 150</li><li>add mil power = 150</li></ul><li>Else if has estate influence has estate is estate khelorvalshi, and estate influence has influence is 33:</li><ul><li>add adm power = 100</li><li>add dip power = 100</li><li>add mil power = 100</li></ul><li>else:</li><ul><li>add adm power = 50</li><li>add dip power = 50</li><li>add mil power = 50</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_drain_populace_desc_tt</li></ul>

___
##£spell_drain_pop_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>calc true if:</li><ul><li>amount is at least 2</li><li>all owned province:</li><ul><li>base tax is at least 2</li><li>base production is at least 2</li><li>base manpower is at least 2</li><li>None of the following:</li><ul><li>devastation is at least 50</li></ul></ul></ul></ul>

###Efects:<ul><li>set country flag [khelorvalshi_menu](../flags/khelorvalshi_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1256_t](../events/missing_localisation_flavor_azjakuma_1256_t.md) happens</li></ul><li>custom tooltip = magic_two_drainable_provinces_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>event target:khelorvalshi drain target 1:</li><ul><li>add devastation = 85</li><li>add base tax = -2</li><li>add base production = -1</li><li>add base manpower = -2</li></ul><li>event target:khelorvalshi drain target 2:</li><ul><li>add devastation = 85</li><li>add base tax = -2</li><li>add base production = -1</li><li>add base manpower = -2</li></ul></ul><li>else:</li><ul><li>event target:khelorvalshi drain target 1:</li><ul><li>add devastation = 70</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>event target:khelorvalshi drain target 2:</li><ul><li>add devastation = 70</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul></ul><li>add adm power = 150</li><li>add dip power = 150</li><li>add mil power = 150</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_drain_populace_desc_tt</li></ul>

___
##£spell_blood_ritual£

###Available if:
<li>Any of the following:</li><ul><li>employed advisor:</li><ul><li>category is ADM</li></ul><li>employed advisor:</li><ul><li>category is DIP</li></ul><li>employed advisor:</li><ul><li>category is MIL</li></ul></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add dip power = -25</li></ul><li>kill advisor = random</li><li>tooltip:</li><ul><li>If has estate influence has estate is estate khelorvalshi, and estate influence has influence is 66:</li><ul><li>add war exhaustion = -12</li></ul><li>Else if has estate influence has estate is estate khelorvalshi, and estate influence has influence is 33:</li><ul><li>add war exhaustion = -10</li></ul><li>else:</li><ul><li>add war exhaustion = -8</li></ul></ul><li>hidden effect:</li><ul><li>If has employed advisor has category is ADM; and has employed advisor has category is DIP; and has employed advisor has category is MIL:</li><ul><li>If has estate influence has estate is estate khelorvalshi, and estate influence has influence is 66:</li><ul><li>add war exhaustion = -12</li></ul><li>Else if has estate influence has estate is estate khelorvalshi, and estate influence has influence is 33:</li><ul><li>add war exhaustion = -10</li></ul><li>else:</li><ul><li>add war exhaustion = -8</li></ul></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_blood_ritual_desc_tt</li></ul>

___
##£spell_blood_ritual_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>employed advisor:</li><ul><li>category is ADM</li></ul></ul><li>NOT:</li><ul><li>employed advisor:</li><ul><li>category is DIP</li></ul></ul><li>NOT:</li><ul><li>employed advisor:</li><ul><li>category is MIL</li></ul></ul>

###Efects:<ul><li>set country flag [khelorvalshi_menu](../flags/khelorvalshi_menu.md)</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1256_t](../events/missing_localisation_flavor_azjakuma_1256_t.md) happens</li></ul><li>custom tooltip = magic_has_employed_advisor_tt</li><li>custom tooltip = magic_effect_separator_tt</li><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add dip power = -25</li></ul><li>tooltip:</li><ul><li>kill advisor = random</li><li>If has estate influence has estate is estate khelorvalshi, and estate influence has influence is 66:</li><ul><li>add war exhaustion = -12</li></ul><li>Else if has estate influence has estate is estate khelorvalshi, and estate influence has influence is 33:</li><ul><li>add war exhaustion = -10</li></ul><li>else:</li><ul><li>add war exhaustion = -8</li></ul></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_blood_ritual_desc_tt</li></ul>

___
##£spell_spirit_consumption£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [azjakuma_two_magics_allowed](../flags/azjakuma_two_magics_allowed.md), and  has calc true if has estate privilege is estate shinukhorchi cast magic, and calc true if has estate privilege is estate chumijemoya cast magic, and calc true if has estate privilege is estate ajgriijarul cast magic, and calc true if has estate privilege is estate kabiurgarko cast magic, and calc true if has estate privilege is estate khelorvalshi cast magic, and calc true if has amount is 2:</li><ul><li>custom tooltip = azjakuma_more_expensive_magic_tooltip</li><li>add dip power = -20</li><li>add prestige = -20</li></ul><li>else:</li><ul><li>add dip power = -10</li><li>add prestige = -10</li></ul><li>If has estate influence has estate is estate khelorvalshi, and estate influence has influence is 66:</li><ul><li>set country flag [spell_1](../flags/spell_1.md)</li><li>random list:</li><ul><li>80:</li><ul><li>custom tooltip = azjakuma_add_random_skill_tt</li></ul><li>20:</li><ul></ul></ul></ul><li>Else if has estate influence has estate is estate khelorvalshi, and estate influence has influence is 33:</li><ul><li>set country flag [spell_2](../flags/spell_2.md)</li><li>random list:</li><ul><li>70:</li><ul><li>custom tooltip = azjakuma_add_random_skill_tt</li></ul><li>25:</li><ul></ul><li>5:</li><ul><li>custom tooltip = azjakuma_lose_random_skill_tt</li></ul></ul></ul><li>else:</li><ul><li>set country flag [spell_3](../flags/spell_3.md)</li><li>random list:</li><ul><li>60:</li><ul><li>custom tooltip = azjakuma_add_random_skill_tt</li></ul><li>30:</li><ul></ul><li>10:</li><ul><li>custom tooltip = azjakuma_lose_random_skill_tt</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_azjakuma_1262_t](../events/missing_localisation_flavor_azjakuma_1262_t.md) happens</li></ul><li>clr country flag [azjakuma_magic_menu_opened](../flags/azjakuma_magic_menu_opened.md)</li><li>custom tooltip = magic_spirit_consumption_desc_tt</li></ul>
