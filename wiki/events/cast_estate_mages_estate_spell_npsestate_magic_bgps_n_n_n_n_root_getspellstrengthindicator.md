#Information
 - Title:     Cast $ESTATE_MAGES$ Estate Spell\n£estate_magic_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   
 - ID: magic_estate.1
#Description
    Cast $ESTATE_MAGES$ Estate Spell\n£estate_magic_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>highlight = yes</li><li>If does not have estate privilege is estate mages cast spells:</li><ul><li>remove country modifier = magic_cooldown</li></ul><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_mages_cast_spells</li></ul><li>else:</li><ul><li>set country flag [revoke_mage_estate_spells](../flags/revoke_mage_estate_spells.md)</li></ul></ul>

___
##£spell_feast_e£

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai diplomat


###Efects:<ul><li>add years of income = -0.5</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_magnificent_feast_3 for 10 years</li></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_magnificent_feast_2 for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier magic_estate_magnificent_feast_1 for 10 years</li></ul><li>custom tooltip = magic_feast_desc_tt</li></ul>

___
##£spell_plant_e£

###Available if:
<li>any owned province:</li><ul><li>plant growth target is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist
 - Multiplied by 0 if has check variable has which is amount of owned provinces, and check variable has value is 100


###Efects:<ul><li>If has check variable has which is amount of farm good provinces, and check variable has value is 1:</li><ul><li>add dip power = -100</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.9:</li><ul><li>add dip power = -90</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.8:</li><ul><li>add dip power = -80</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.7:</li><ul><li>add dip power = -70</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.6:</li><ul><li>add dip power = -60</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.5:</li><ul><li>add dip power = -50</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.4:</li><ul><li>add dip power = -40</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.3:</li><ul><li>add dip power = -30</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.2:</li><ul><li>add dip power = -20</li></ul><li>else:</li><ul><li>add dip power = -10</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>custom tooltip = plant_growth_3_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>custom tooltip = plant_growth_2_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = plant_growth_1_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_1</li><li>duration = 3650</li></ul></ul></ul></ul><li>custom tooltip = plant_growth_devastation_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_100_t](../events/missing_localisation_magic_estate_100_t.md) happens</li></ul><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_plant_e_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>any owned province:</li><ul><li>plant growth target is yes</li></ul></ul>

###Efects:<ul><li>custom tooltip = magic_need_valid_target_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_2_t](../events/missing_localisation_magic_estate_2_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>If has check variable has which is amount of farm good provinces, and check variable has value is 1:</li><ul><li>add dip power = -100</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.9:</li><ul><li>add dip power = -90</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.8:</li><ul><li>add dip power = -80</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.7:</li><ul><li>add dip power = -70</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.6:</li><ul><li>add dip power = -60</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.5:</li><ul><li>add dip power = -50</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.4:</li><ul><li>add dip power = -40</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.3:</li><ul><li>add dip power = -30</li></ul><li>Else if has check variable has which is amount of farm good provinces, and check variable has value is 0.2:</li><ul><li>add dip power = -20</li></ul><li>else:</li><ul><li>add dip power = -10</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>custom tooltip = plant_growth_3_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_3</li><li>duration = 3650</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>custom tooltip = plant_growth_2_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_2</li><li>duration = 3650</li></ul></ul></ul></ul><li>else:</li><ul><li>custom tooltip = plant_growth_1_tooltip</li><li>hidden effect:</li><ul><li>If every owned province has plant growth target is yes:</li><ul><li>add province modifier:</li><ul><li>name = magic_realm_transmutation_plant_growth_1</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>custom tooltip = plant_growth_devastation_tooltip</li><li>custom tooltip = magic_plant_growth_desc_tt</li></ul>

___
##£spell_scrying_rivals_e£

###Available if:
<li>any rival country:</li><ul><li>exists</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = -0.5</li><li>add adm power = -30</li><li>add dip power = -30</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_3 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 30</li></ul><li>ROOT:</li><ul><li>add spy network from:</li><ul><li>who = PREV</li><li>value = -30</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_2 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 20</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -20</li></ul></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_1 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 10</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -10</li></ul></ul></ul></ul>

___
##£spell_scrying_rivals_e_r£

###Available if:
<li>is not controlled by the AI</li><li>None of the following:</li><ul><li>any rival country:</li><ul><li>exists</li></ul></ul>

###Efects:<ul><li>custom tooltip = magic_need_valid_target_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_2_t](../events/missing_localisation_magic_estate_2_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add years of income = -0.5</li><li>add adm power = -30</li><li>add dip power = -30</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_3 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 30</li></ul><li>ROOT:</li><ul><li>add spy network from:</li><ul><li>who = PREV</li><li>value = -30</li></ul></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_2 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 20</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -20</li></ul></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_rivals_1 for 10 years</li><li>every rival country:</li><ul><li>remove fow = 120</li><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 10</li></ul><li>add spy network in:</li><ul><li>who = ROOT</li><li>value = -10</li></ul></ul></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_neighbours_e£

###Available if:
<li>any country:</li><ul><li>is neighbor of is this nation</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has neighbor is ahead in institution is yes:</li><ul><li>add years of income = -1.5</li><li>add adm power = -60</li></ul><li>else:</li><ul><li>add years of income = -0.5</li><li>add adm power = -60</li></ul><li>If every country is neighbor of is ROOT:</li><ul><li>remove fow = 120</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_3 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_3</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_2 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_2</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_neighbours_1 for 10 years</li><li>If has neighbor is ahead in institution is yes:</li><ul><li>capital scope:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_scrying_stealing_institution_1</li><li>duration = 3650</li></ul></ul></ul></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_dissidents_e£

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = -0.5</li><li>add adm power = -60</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_3 for 10 years</li></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_2 for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_internal_dissidents_1 for 10 years</li></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_combattants_e£

###Available if:
<li>is at war</li>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has country flag is [command_enslaved_the_oracle_flag](../flags/command_enslaved_the_oracle_flag.md):</li><ul><li>add years of income = -0.5</li><li>add adm power = -15</li><li>add mil power = -15</li></ul><li>else:</li><ul><li>add years of income = -1</li><li>add adm power = -30</li><li>add mil power = -30</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_3 for 10 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33; and has country flag is [command_enslaved_the_oracle_flag](../flags/command_enslaved_the_oracle_flag.md):</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_2 for 5 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_1 for 1 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_scrying_combattants_e_r£

###Available if:
<li>is not controlled by the AI</li><li>is not at war</li>

###Efects:<ul><li>custom tooltip = magic_need_valid_target_tt</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_2_t](../events/missing_localisation_magic_estate_2_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add years of income = -1</li><li>add adm power = -30</li><li>add mil power = -30</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_3 for 10 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_2 for 5 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul><li>else:</li><ul><li>country gets the modifier magic_estate_scrying_military_intelligence_1 for 1 years</li><li>If every country has war with is ROOT:</li><ul><li>remove fow = 120</li></ul></ul></ul><li>custom tooltip = magic_scrying_desc_tt</li></ul>

___
##£spell_construction_e£

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has any owned province has construction progress is 0.1
 - Multiplied by 0.25 if has years of income is 0.5


###Efects:<ul><li>add years of income = -0.5</li><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>country gets the modifier magic_estate_aiding_construction_3 for 10 years</li></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>country gets the modifier magic_estate_aiding_construction_2 for 10 years</li></ul><li>else:</li><ul><li>country gets the modifier magic_estate_aiding_construction_1 for 10 years</li></ul><li>custom tooltip = magic_construction_desc_tt</li></ul>

___
##£spell_broad_ward_e£

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if is at war
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>If has check variable has which is amount of broad ward provinces, and check variable has value is 0.9:</li><ul><li>add mil power = -100</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.8:</li><ul><li>add mil power = -90</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.7:</li><ul><li>add mil power = -80</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.6:</li><ul><li>add mil power = -70</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.5:</li><ul><li>add mil power = -60</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.4:</li><ul><li>add mil power = -50</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.3:</li><ul><li>add mil power = -40</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.2:</li><ul><li>add mil power = -30</li></ul><li>Else if has check variable has which is amount of broad ward provinces, and check variable has value is 0.1:</li><ul><li>add mil power = -20</li></ul><li>else:</li><ul><li>add mil power = -10</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has fort level is 2, and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_broad_ward_3</li><li>duration = 3650</li></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has fort level is 2, and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_broad_ward_2</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has fort level is 2, and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_broad_ward_1</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_narrow_ward_e£

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if is at war
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>If has check variable has which is amount of narrow ward provinces, and check variable has value is 0.9:</li><ul><li>add mil power = -200</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.8:</li><ul><li>add mil power = -180</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.7:</li><ul><li>add mil power = -160</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.6:</li><ul><li>add mil power = -140</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.5:</li><ul><li>add mil power = -120</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.4:</li><ul><li>add mil power = -100</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.3:</li><ul><li>add mil power = -80</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.2:</li><ul><li>add mil power = -60</li></ul><li>Else if has check variable has which is amount of narrow ward provinces, and check variable has value is 0.1:</li><ul><li>add mil power = -40</li></ul><li>else:</li><ul><li>add mil power = -20</li></ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has AND has building is ramparts, and AND has fort level is 2; and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_ward_3</li><li>duration = 3650</li></ul></ul></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has AND has building is ramparts, and AND has fort level is 2; and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_ward_2</li><li>duration = 3650</li></ul></ul></ul><li>else:</li><ul><li>If every owned province has no ward province modifiers is yes, and  is city, and has AND has building is ramparts, and AND has fort level is 2; and is a capital:</li><ul><li>add province modifier:</li><ul><li>name = magic_estate_ward_1</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = magic_ward_desc_tt</li></ul>

___
##£spell_conception_e£

###Available if:
<li>has consort</li><li>has government attribute heir</li><li>is not lesser in union</li><li>None of the following:</li><ul><li>ruler is immortal is yes</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has ruler has mage personality is yes
 - Multiplied by 0.5 if has heir
 - Multiplied by 0.8 if has adm is 6, and has dip is 6, and has mil is 6
 - Multiplied by 0.25 if has years of income is 1.5


###Efects:<ul><li>add years of income = -1</li><li>If has heir:</li><ul><li>add legitimacy = -10</li></ul><li>custom tooltip = magic_estate_rite_of_conception_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_9_t](../events/missing_localisation_magic_estate_9_t.md) happens</li></ul><li>custom tooltip = magic_conception_desc_tt</li></ul>

___
##£spell_conception_e_r£

###Available if:
<li>is not controlled by the AI</li><li>Any of the following:</li><ul><li>does not have consort</li><li>None of the following:</li><ul><li>has government attribute heir</li></ul><li>is lesser in union</li><li>ruler is immortal is yes</li></ul>

###Efects:<ul><li>If does not have consort:</li><ul><li>custom tooltip = magic_need_consort_tt</li></ul><li>If does not have government attribute is heir:</li><ul><li>custom tooltip = magic_government_allow_heirs_tt</li></ul><li>If is lesser in union:</li><ul><li>custom tooltip = magic_is_not_in_lesser_union_tt</li></ul><li>If has ruler is immortal is yes:</li><ul><li>custom tooltip = magic_ruler_is_mortal_tt</li></ul><li>hidden effect:</li><ul><li>the event [Missing localisation: magic_estate_2_t](../events/missing_localisation_magic_estate_2_t.md) happens</li></ul><li>custom tooltip = magic_effect_separator_tt</li><li>tooltip:</li><ul><li>add years of income = -1</li><li>If has heir:</li><ul><li>add legitimacy = -10</li></ul></ul><li>custom tooltip = magic_estate_rite_of_conception_tooltip</li><li>custom tooltip = magic_conception_desc_tt</li></ul>
