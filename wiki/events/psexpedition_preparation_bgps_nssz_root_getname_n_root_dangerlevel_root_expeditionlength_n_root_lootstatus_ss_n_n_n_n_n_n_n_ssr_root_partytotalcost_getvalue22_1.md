This page has the same name as others. For full listing see bottom of [the base page](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue22.md).

#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.8
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_prepare_equipment£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partySupplies is at least 100</li></ul></ul><li>owner:</li><ul><li>mil power is at least 10</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add mil power = -10</li></ul><li>change party supplies:</li><ul><li>add = 20</li><li>mil cost = 10</li><li>add tooltip = yes</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_prepare_equipment_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partySupplies is at least 100</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 10</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partySupplies is 100:</li><ul><li>custom tooltip = max_supplies_tooltip</li></ul><li>If does not have mil power is 10:</li><ul><li>custom tooltip = not_enough_mil_power_tooltip</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_preserve_the_food£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partySupplies is at least 100</li></ul></ul><li>owner:</li><ul><li>adm power is at least 10</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -10</li></ul><li>change party supplies:</li><ul><li>add = 20</li><li>adm cost = 10</li><li>add tooltip = yes</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_preserve_the_food_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partySupplies is at least 100</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 10</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partySupplies is 100:</li><ul><li>custom tooltip = max_supplies_tooltip</li></ul><li>If does not have adm power is 10:</li><ul><li>custom tooltip = not_enough_adm_power_tooltip</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_give_them_money£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partySupplies is at least 100</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add treasury = -100</li></ul><li>change party supplies:</li><ul><li>add = 20</li><li>cash cost = 100</li><li>add tooltip = yes</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_give_them_money_g£

###Available if:
<li>check variable:</li><ul><li>partySupplies is at least 100</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partySupplies is 100:</li><ul><li>custom tooltip = max_supplies_tooltip</li></ul><li>custom tooltip = supplies_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_reset_preparation£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>supplies = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1003](diggy_expedition.1003_slug) immediately </li></ul></ul>

___
##£event_button_expedition_go_back£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul>
