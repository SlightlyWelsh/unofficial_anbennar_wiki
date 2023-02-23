This page has the same name as others. For full listing see bottom of [the base page](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2.md).

#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.6
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_drill_the_troops£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul></ul><li>owner:</li><ul><li>adm power is at least 5</li><li>dip power is at least 5</li><li>mil power is at least 5</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -5</li><li>add dip power = -5</li><li>add mil power = -5</li></ul><li>change party effectiveness:</li><ul><li>add = 3</li><li>adm cost = 5</li><li>dip cost = 5</li><li>mil cost = 5</li><li>add tooltip = yes</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_drill_the_troops_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 5</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>dip power is at least 5</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 5</li></ul></ul></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has check variable has partyEffectiveness is 200:</li><ul><li>custom tooltip = max_effectiveness_tooltip</li></ul><li>If does not have adm power is 5; and does not have dip power is 5; and does not have mil power is 5:</li><ul><li>custom tooltip = not_enough_mana_tooltip</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_draft_plans£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul></ul><li>owner:</li><ul><li>adm power is at least 15</li><li>dip power is at least 15</li><li>mil power is at least 15</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -15</li><li>add dip power = -15</li><li>add mil power = -15</li></ul><li>change party effectiveness:</li><ul><li>add = 9</li><li>adm cost = 15</li><li>dip cost = 15</li><li>mil cost = 15</li><li>add tooltip = yes</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_draft_plans_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 15</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>dip power is at least 15</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 15</li></ul></ul></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has check variable has partyEffectiveness is 200:</li><ul><li>custom tooltip = max_effectiveness_tooltip</li></ul><li>If does not have adm power is 15; and does not have dip power is 15; and does not have mil power is 15:</li><ul><li>custom tooltip = not_enough_mana_tooltip</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_map_the_terrain£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul></ul><li>owner:</li><ul><li>adm power is at least 25</li><li>dip power is at least 25</li><li>mil power is at least 25</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add adm power = -25</li><li>add dip power = -25</li><li>add mil power = -25</li></ul><li>change party effectiveness:</li><ul><li>add = 15</li><li>adm cost = 25</li><li>dip cost = 25</li><li>mil cost = 25</li><li>add tooltip = yes</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_map_the_terrain_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyEffectiveness is at least 200</li></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>adm power is at least 25</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>dip power is at least 25</li></ul></ul><li>owner:</li><ul><li>None of the following:</li><ul><li>mil power is at least 25</li></ul></ul></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If has check variable has partyEffectiveness is 200:</li><ul><li>custom tooltip = max_effectiveness_tooltip</li></ul><li>If does not have adm power is 25; and does not have dip power is 25; and does not have mil power is 25:</li><ul><li>custom tooltip = not_enough_mana_tooltip</li></ul><li>custom tooltip = effectiveness_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>effectiveness = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_reset_preparation£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1001](diggy_expedition.1001_slug) immediately </li></ul></ul>

___
##£event_button_expedition_go_back£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul>
