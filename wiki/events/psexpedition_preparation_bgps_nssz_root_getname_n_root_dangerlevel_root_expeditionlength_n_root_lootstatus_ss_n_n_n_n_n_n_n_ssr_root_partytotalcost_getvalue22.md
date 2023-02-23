This page has the same name as others. For full listing see bottom of [the base page](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost.md).

#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.7
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_organize_a_feast£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyMorale is at least 30</li></ul></ul><li>owner:</li><ul><li>adm power is at least 5</li><li>dip power is at least 5</li><li>mil power is at least 5</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -5</li><li>add dip power = -5</li><li>add mil power = -5</li></ul><li>change party morale:</li><ul><li>add = 0.5</li><li>adm cost = 5</li><li>dip cost = 5</li><li>mil cost = 5</li><li>add tooltip = yes</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_organize_a_feast_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyMorale is at least 30</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 5</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>dip power is at least 5</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 5</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyMorale is 30:</li><ul><li>custom tooltip = max_morale_tooltip</li></ul><li>If does not have adm power is 5; and does not have dip power is 5; and does not have mil power is 5:</li><ul><li>custom tooltip = not_enough_mana_tooltip</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_lot_of_love£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyMorale is at least 30</li></ul></ul><li>owner:</li><ul><li>adm power is at least 15</li><li>dip power is at least 15</li><li>mil power is at least 15</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>change party morale:</li><ul><li>add = 1.5</li><li>adm cost = 15</li><li>dip cost = 15</li><li>mil cost = 15</li><li>add tooltip = yes</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_lot_of_love_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyMorale is at least 30</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 15</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>dip power is at least 15</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 15</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyMorale is 30:</li><ul><li>custom tooltip = max_morale_tooltip</li></ul><li>If does not have adm power is 15; and does not have dip power is 15; and does not have mil power is 15:</li><ul><li>custom tooltip = not_enough_mana_tooltip</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_upfront_payment£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyMorale is at least 30</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add treasury = -100</li></ul><li>change party morale:</li><ul><li>add = 1.5</li><li>cash cost = 100</li><li>add tooltip = yes</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_upfront_payment_g£

###Available if:
<li>check variable:</li><ul><li>partyMorale is at least 30</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyMorale is 30:</li><ul><li>custom tooltip = max_morale_tooltip</li></ul><li>custom tooltip = morale_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_reset_preparation£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>morale = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1002](diggy_expedition.1002_slug) immediately </li></ul></ul>

___
##£event_button_expedition_go_back£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue22_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue22_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue22_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue22_1.md)
