#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.3
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_prepare£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If does not have province flag is [expedition_in_progress](../flags/expedition_in_progress.md):</li><ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul><li>else:</li><ul><li>custom tooltip = expedition_in_progress_tooltip</li><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul></ul>

___
##£event_button_expedition_reset_preparation_all£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>manpower = yes</li><li>morale = yes</li><li>effectiveness = yes</li><li>supplies = yes</li><li>rewards = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul>

___
##£event_button_expedition_launch£

###Available if:
<li>check variable:</li><ul><li>partyManpower is at least 1</li></ul><li>None of the following:</li><ul><li>has province flag [expedition_in_progress](../flags/expedition_in_progress.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = start_expedition_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>set province flag [sent_expedition_@owner](../flags/sent_expedition_owner.md)</li><li>set province flag [expedition_in_progress](../flags/expedition_in_progress.md)</li><li>set variable:</li><ul><li>which = rewardsFactor</li><li>which = partyRewards</li></ul><li>divide variable:</li><ul><li>which = rewardsFactor</li><li>which = lootEstimate</li></ul><li>If does not have check variable has rewardsFactor is 0.01:</li><ul><li>set variable:</li><ul><li>rewardsFactor = 0.01</li></ul></ul><li>If has province flag is [explorable_dungeon](../flags/explorable_dungeon.md):</li><ul><li>fire province event [diggy_dungeons.2](diggy_dungeons.2_slug) in 30 days</li><li>fire province event [diggy_dungeons.3](diggy_dungeons.3_slug) immediately </li></ul><li>else:</li><ul><li>fire province event [diggy_expedition.2000](diggy_expedition.2000_slug) in 30 days</li><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul><li>save party preparation = yes</li></ul></ul>

___
##£event_button_expedition_launch_g£

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 1</li></ul></ul><li>has province flag [expedition_in_progress](../flags/expedition_in_progress.md)</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>If does not have check variable has partyManpower is 1:</li><ul><li>custom tooltip = not_enough_men_expedition_tooltip</li></ul><li>If has province flag is [expedition_in_progress](../flags/expedition_in_progress.md):</li><ul><li>custom tooltip = expedition_in_progress_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1005](diggy_expedition.1005_slug) immediately </li></ul></ul>

___
##£event_button_close£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>owner:</li><ul><li>clr country flag [debug_menu](../flags/debug_menu.md)</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue_1.md)
