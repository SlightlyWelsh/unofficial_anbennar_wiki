This page has the same name as others. For full listing see bottom of [the base page](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost.md).

#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.9
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_100_more_crowns£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyRewards is at least 2000</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party rewards:</li><ul><li>add tooltip = yes</li><li>add = 100</li></ul><li>custom tooltip = rewards_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_100_more_crowns_g£

###Available if:
<li>check variable:</li><ul><li>partyRewards is at least 2000</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = max_rewards_tooltip</li><li>custom tooltip = rewards_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_500_more_crowns£

###Available if:
<li>None of the following:</li><ul><li>check variable:</li><ul><li>partyRewards is at least 2000</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party rewards:</li><ul><li>add tooltip = yes</li><li>add = 500</li></ul><li>custom tooltip = rewards_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_500_more_crowns_g£

###Available if:
<li>check variable:</li><ul><li>partyRewards is at least 2000</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>custom tooltip = max_rewards_tooltip</li><li>custom tooltip = rewards_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_reset_preparation£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>rewards = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1004](diggy_expedition.1004_slug) immediately </li></ul></ul>

___
##£event_button_expedition_go_back£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul>
