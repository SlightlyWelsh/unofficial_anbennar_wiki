#Information
 - Title: Vizier Actions\n£raj_vizier_window£
 - ID: rahenraj.3005
#Description
Vizier Actions\n£raj_vizier_window£
#Options

___
##£event_button_sway_senaptia£

###Available if:
<li>check variable:</li><ul><li>which is rajNbSenaptiHalf</li><li>value is at least 1</li></ul><li>check variable:</li><ul><li>which is numSwayedSenaptia</li><li>which  is rajNbSenaptiHalf</li></ul><li>mil power is at least 250</li><li>None of the following:</li><ul><li>has country flag [raj_swayed_senaptia](../flags/raj_swayed_senaptia.md)</li></ul>

###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>add mil power = -250</li><li>overlord:</li><ul><li>the event ˻rahenraj.2107˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_swayed_senaptia_opinion</li></ul><li>If every subject country is subject of type is great daimyo vassal, and  has opinion has value is 150, and has opinion has who is ROOT; and does not have check variable has which is rajaOpinion, and check variable has which is vizierOpinion:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_swayed_senapti_opinion</li></ul></ul></ul><li>set country flag [raj_swayed_senaptia](../flags/raj_swayed_senaptia.md)</li><li>custom tooltip = raj_option_available_tt</li><li>custom tooltip = raj_has_250_mil_tt</li><li>custom tooltip = raj_more_than_half_senaptia_tt</li><li>custom tooltip = raj_vizier_action_not_used_before_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_sway_senaptia_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is rajNbSenaptiHalf</li><li>value is at least 1</li></ul></ul><li>NOT:</li><ul><li>check variable:</li><ul><li>which is numSwayedSenaptia</li><li>which  is rajNbSenaptiHalf</li></ul></ul><li>NOT:</li><ul><li>mil power is at least 250</li></ul><li>has country flag [raj_swayed_senaptia](../flags/raj_swayed_senaptia.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_option_unavailable_tt</li><li>If has mil power is 250:</li><ul><li>custom tooltip = raj_has_250_mil_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_250_mil_tt</li></ul><li>If has check variable has which is numSwayedSenaptia, and check variable has which is rajNbSenaptiHalf:</li><ul><li>custom tooltip = raj_more_than_half_senaptia_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_more_than_half_senaptia_tt</li></ul><li>If does not have country flag is [raj_swayed_senaptia](../flags/raj_swayed_senaptia.md):</li><ul><li>custom tooltip = raj_vizier_action_not_used_before_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_vizier_action_used_before_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3006˼ happens</li></ul></ul>

___
##£event_button_ministries_support£

###Available if:
<li>estate loyalty:</li><ul><li>estate is estate_raj_ministries</li><li>loyalty is at least 60</li></ul><li>estate influence:</li><ul><li>estate is estate_raj_ministries</li><li>influence is at least 60</li></ul><li>adm power is at least 250</li><li>None of the following:</li><ul><li>has country flag [raj_gathered_ministries](../flags/raj_gathered_ministries.md)</li></ul>

###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>overlord:</li><ul><li>the event ˻rahenraj.2108˼ happens</li></ul><li>add adm power = -250</li><li>add estate influence modifier:</li><ul><li>estate = estate_raj_ministries</li><li>desc = raj_ministries_support_vizier</li><li>influence = 10</li><li>duration = 7300</li></ul><li>set country flag [raj_gathered_ministries](../flags/raj_gathered_ministries.md)</li><li>custom tooltip = raj_option_available_tt</li><li>custom tooltip = raj_has_250_mil_tt</li><li>custom tooltip = raj_more_than_half_senaptia_tt</li><li>custom tooltip = raj_vizier_action_not_used_before_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_ministries_support_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>estate loyalty:</li><ul><li>estate is estate_raj_ministries</li><li>loyalty is at least 60</li></ul></ul><li>NOT:</li><ul><li>estate influence:</li><ul><li>estate is estate_raj_ministries</li><li>influence is at least 60</li></ul></ul><li>NOT:</li><ul><li>adm power is at least 250</li></ul><li>has country flag [raj_gathered_ministries](../flags/raj_gathered_ministries.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_option_unavailable_tt</li><li>If has adm power is 250:</li><ul><li>custom tooltip = raj_has_250_adm_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_250_adm_tt</li></ul><li>If has estate loyalty has estate is estate raj ministries, and estate loyalty has loyalty is 60:</li><ul><li>custom tooltip = raj_ministries_loyalty_60_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_ministries_loyalty_not_60_tt</li></ul><li>If has estate influence has estate is estate raj ministries, and estate influence has influence is 60:</li><ul><li>custom tooltip = raj_ministries_influence_60_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_ministries_influence_not_60_tt</li></ul><li>If does not have country flag is [raj_gathered_ministries](../flags/raj_gathered_ministries.md):</li><ul><li>custom tooltip = raj_vizier_action_not_used_before_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_vizier_action_used_before_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3006˼ happens</li></ul></ul>

___
##£event_button_outmaneuver_raja£

###Available if:
<li>dip power is at least 250</li><li>diplomatic reputation is at least 4</li><li>check variable:</li><ul><li>which is vizierDipRepDiff</li><li>value is at least 2</li></ul><li>None of the following:</li><ul><li>has country flag [raj_outmaneuvered_raja](../flags/raj_outmaneuvered_raja.md)</li></ul>

###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>overlord:</li><ul><li>the event ˻rahenraj.2109˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_outmaneuvered_by_vizier_opinion</li></ul><li>country gets the modifier raj_was_outmaneuvered for 10 years</li></ul><li>add dip power = -250</li><li>set country flag [raj_outmaneuvered_raja](../flags/raj_outmaneuvered_raja.md)</li><li>custom tooltip = raj_option_available_tt</li><li>custom tooltip = raj_has_250_dip_tt</li><li>custom tooltip = raj_has_4_diprep_tt</li><li>custom tooltip = raj_more_diprep_than_raja_tt</li><li>custom tooltip = raj_vizier_action_not_used_before_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_outmaneuver_raja_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>dip power is at least 250</li></ul><li>NOT:</li><ul><li>diplomatic reputation is at least 4</li></ul><li>NOT:</li><ul><li>check variable:</li><ul><li>which is vizierDipRepDiff</li><li>value is at least 2</li></ul></ul><li>has country flag [raj_outmaneuvered_raja](../flags/raj_outmaneuvered_raja.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_option_unavailable_tt</li><li>If has dip power is 250:</li><ul><li>custom tooltip = raj_has_250_dip_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_250_dip_tt</li></ul><li>If has diplomatic reputation is 4:</li><ul><li>custom tooltip = raj_has_4_diprep_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_has_4_diprep_tt</li></ul><li>If has check variable has which is vizierDipRepDiff, and check variable has value is 2:</li><ul><li>custom tooltip = raj_more_diprep_than_raja_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_more_diprep_than_raja_tt</li></ul><li>If does not have country flag is [raj_outmaneuvered_raja](../flags/raj_outmaneuvered_raja.md):</li><ul><li>custom tooltip = raj_vizier_action_not_used_before_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_vizier_action_used_before_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3006˼ happens</li></ul></ul>

___
##£event_button_discredit_raja£

###Available if:
<li>treasury is at least 500</li><li>overlord:</li><ul><li>has spy network from:</li><ul><li>this nation</li><li>value is at least 60</li></ul></ul><li>None of the following:</li><ul><li>has country flag [raj_discredited_raja](../flags/raj_discredited_raja.md)</li></ul>

###Efects:<ul><li>raj vizier sway change:</li><ul><li>amount = 5</li></ul><li>overlord:</li><ul><li>the event ˻rahenraj.2110˼ happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = raj_discredited_by_vizier_opinion</li></ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -60</li></ul></ul><li>raj cohesion change absolute:</li><ul><li>amount = -5</li></ul><li>add treasury = -500</li><li>set country flag [raj_discredited_raja](../flags/raj_discredited_raja.md)</li><li>custom tooltip = raj_option_available_tt</li><li>custom tooltip = raj_has_1_year_of_income_tt</li><li>custom tooltip = raj_has_60_spy_network_on_raja_tt</li><li>custom tooltip = raj_vizier_action_not_used_before_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_discredit_raja_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>treasury is at least 500</li></ul><li>NOT:</li><ul><li>overlord:</li><ul><li>has spy network from:</li><ul><li>this nation</li><li>value is at least 60</li></ul></ul></ul><li>has country flag [raj_discredited_raja](../flags/raj_discredited_raja.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_option_unavailable_tt</li><li>If has treasury is 500:</li><ul><li>custom tooltip = raj_has_1_year_of_income_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_1_year_of_income_tt</li></ul><li>If has overlord has spy network from has who is ROOT, and has spy network from has value is 60:</li><ul><li>custom tooltip = raj_has_60_spy_network_on_raja_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_60_spy_network_on_raja_tt</li></ul><li>If does not have country flag is [raj_discredited_raja](../flags/raj_discredited_raja.md):</li><ul><li>custom tooltip = raj_vizier_action_not_used_before_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_vizier_action_used_before_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3006˼ happens</li></ul></ul>

___
##£event_button_become_confident£

###Available if:
<li>reverse has opinion:</li><ul><li>event_target:raja_target</li><li>value is at least 150</li></ul><li>prestige is event_target:raja_target</li><li>marriage with is event_target:raja_target</li><li>None of the following:</li><ul><li>has country flag [raj_became_raja_confident](../flags/raj_became_raja_confident.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_confident_event_chain_start_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.2104˼ happens</li></ul><li>set country flag [raj_became_raja_confident](../flags/raj_became_raja_confident.md)</li><li>custom tooltip = raj_option_available_tt</li><li>custom tooltip = raj_has_150_relations_with_raja_tt</li><li>custom tooltip = raj_has_more_prestige_than_raja_tt</li><li>custom tooltip = raj_has_marriage_with_raja_tt</li><li>custom tooltip = raj_vizier_action_not_used_before_tt</li><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>

___
##£event_button_become_confident_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>reverse has opinion:</li><ul><li>event_target:raja_target</li><li>value is at least 150</li></ul></ul><li>NOT:</li><ul><li>prestige is event_target:raja_target</li></ul><li>NOT:</li><ul><li>marriage with is event_target:raja_target</li></ul><li>has country flag [raj_became_raja_confident](../flags/raj_became_raja_confident.md)</li></ul>

###Efects:<ul><li>custom tooltip = raj_option_unavailable_tt</li><li>If has reverse has opinion has who is event target:raja target, and reverse has opinion has value is 150:</li><ul><li>custom tooltip = raj_has_150_relations_with_raja_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_150_relations_with_raja_tt</li></ul><li>If has prestige is event target:raja target:</li><ul><li>custom tooltip = raj_has_more_prestige_than_raja_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_more_prestige_than_raja_tt</li></ul><li>If has marriage with is event target:raja target:</li><ul><li>custom tooltip = raj_has_marriage_with_raja_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_not_marriage_with_raja_tt</li></ul><li>If does not have country flag is [raj_became_raja_confident](../flags/raj_became_raja_confident.md):</li><ul><li>custom tooltip = raj_vizier_action_not_used_before_tt</li></ul><li>else:</li><ul><li>custom tooltip = raj_vizier_action_used_before_tt</li></ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3006˼ happens</li></ul></ul>

___
##£event_button_mandate_back_rajmenu£

###Efects:<ul><li>hidden effect:</li><ul><li>the event ˻rahenraj.3000˼ happens</li></ul></ul>
