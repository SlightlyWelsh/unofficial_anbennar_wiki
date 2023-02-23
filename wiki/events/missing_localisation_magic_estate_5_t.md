#Information
 - Title: Missing localisation: magic_estate_5_t
 - ID: acolyte_estate.5
#Description

#Options

___
##Missing localisation: magic_estate_5_a

###Available if:
<li>any rival country:</li><ul><li>exists</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has estate influence has estate is estate acolytes, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_3 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 30</li></ul><li>ROOT:</li><ul><li>add spy network from:</li><ul><li>who = PREV</li><li>value = -30</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate acolytes, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_2 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 20</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -20</li></ul></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_1 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 10</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -10</li></ul></ul></ul><li>add years of income = -0.5</li><li>add adm power = -30</li><li>add dip power = -30</li></ul>

___
##Missing localisation: magic_estate_5_b

###Available if:
<li>any country:</li><ul><li>is neighbor of is this nation</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If every country is neighbor of is ROOT:</li><ul><li>remove fow = 120</li></ul><li>If has estate influence has estate is estate acolytes, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_3 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_3</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>Else if has estate influence has estate is estate acolytes, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_2 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_2</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_1 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_1</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>If has neighbor is ahead in institution is yes:</li><ul><li>add years of income = -1.5</li><li>add adm power = -60</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add adm power = -60</li></ul></ul>

___
##Missing localisation: magic_estate_5_c

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has estate influence has estate is estate acolytes, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_3 for 10 years</li></ul><li>Else if has estate influence has estate is estate acolytes, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_2 for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_1 for 10 years</li></ul><li>add years of income = -0.5</li><li>add adm power = -60</li></ul>

___
##Missing localisation: magic_estate_5_dd

###Available if:
<li>is at war</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has estate influence has estate is estate acolytes, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_3 for 10 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>Else if has estate influence has estate is estate acolytes, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_2 for 5 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_1 for 1 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>add years of income = -1</li><li>add adm power = -30</li><li>add mil power = -30</li></ul>

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>the event [    Acolytes Estate Magic\n£estate_magic_acolytes_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorAcolytes]                                   ](../events/acolytes_estate_magic_npsestate_magic_acolytes_bgps_n_n_n_n_root_getspellstrengthindicatoracolytes.md) happens</li></ul>
