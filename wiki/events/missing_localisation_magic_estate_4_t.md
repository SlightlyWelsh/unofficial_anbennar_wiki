#Information
 - Title: Missing localisation: magic_estate_4_t
 - ID: acolyte_estate.4
#Description

#Options

___
##Missing localisation: magic_estate_4_a

###Available if:
<li>any owned province:</li><ul><li>plant growth target is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has check variable has which is amount of owned provinces, and check variable has value is 100


###Efects:<ul><li>If has estate influence has estate is estate acolytes, and estate influence has influence is 66:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 3650</li></ul></ul></ul><li>Else if has estate influence has estate is estate acolytes, and estate influence has influence is 33:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_1</li><li>duration = 3650</li></ul></ul></ul><li>If does not have check variable has which is amount of farm good provinces, and check variable has value is 0.1:</li><ul><li>add dip power = -10</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.1; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.2:</li><ul><li>add dip power = -20</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.2; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.3:</li><ul><li>add dip power = -30</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.3; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.4:</li><ul><li>add dip power = -40</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.4; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.5:</li><ul><li>add dip power = -50</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.5; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.6:</li><ul><li>add dip power = -60</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.6; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.7:</li><ul><li>add dip power = -70</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.7; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.8:</li><ul><li>add dip power = -80</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.8; and does not have check variable has which is amount of farm good provinces, and check variable has value is 0.9:</li><ul><li>add dip power = -90</li></ul><li>else:</li><ul><li>add dip power = -100</li></ul><li>custom tooltip = plant_growth_devastation_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_100_t](../events/missing_localisation_magic_estate_100_t.md) happens</li></ul></ul>

___
##Missing localisation: magic_estate_4_b

###Available if:
<li>None of the following:</li><ul><li>any owned province:</li><ul><li>plant growth target is yes</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>the event [    Acolytes Estate Magic\n£estate_magic_acolytes_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorAcolytes]                                   ](../events/acolytes_estate_magic_npsestate_magic_acolytes_bgps_n_n_n_n_root_getspellstrengthindicatoracolytes.md) happens</li></ul>

___
##Go back

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>the event [    Acolytes Estate Magic\n£estate_magic_acolytes_bg£\n\n\n\n[Root.GetSpellStrengthIndicatorAcolytes]                                   ](../events/acolytes_estate_magic_npsestate_magic_acolytes_bgps_n_n_n_n_root_getspellstrengthindicatoracolytes.md) happens</li></ul>
