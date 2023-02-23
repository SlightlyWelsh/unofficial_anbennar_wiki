This page has the same name as others. For full listing see bottom of [the base page](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost.md).

#Information
 - Title: £expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
 - ID: diggy_expedition.5
#Description
£expedition_preparation_bg£\n§Z[Root.GetName]\n[Root.DangerLevel]  [Root.ExpeditionLength]                                            \n                                                 [Root.LootStatus]§!\n\n\n\n\n\n\n                                                              §r[Root.partyTotalCost.GetValue]
#Options

___
##£event_button_expedition_send_one_regiment£

###Available if:
<li>infantry in province is at least 1</li><li>infantry in province  is owner</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party manpower:</li><ul><li>add expedition = 1</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_send_one_regiment_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul><li>None of the following:</li><ul><li>infantry in province is owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyManpower is 10000:</li><ul><li>custom tooltip = max_manpower_size_tooltip</li></ul><li>If does not have infantry in province is owner:</li><ul><li>custom tooltip = no_infantry_in_province_tooltip</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_send_five_regiment£

###Available if:
<li>infantry in province is at least 1</li><li>infantry in province  is owner</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party manpower:</li><ul><li>add expedition = 5</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_send_five_regiment_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul><li>None of the following:</li><ul><li>infantry in province is owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyManpower is 10000:</li><ul><li>custom tooltip = max_manpower_size_tooltip</li></ul><li>If does not have infantry in province is owner:</li><ul><li>custom tooltip = no_infantry_in_province_tooltip</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_send_ten_regiment£

###Available if:
<li>infantry in province is at least 1</li><li>infantry in province  is owner</li><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>change party manpower:</li><ul><li>add expedition = 10</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_send_ten_regiment_g£

###Available if:
<li>Any of the following:</li><ul><li>check variable:</li><ul><li>partyManpower is at least 10000</li></ul><li>None of the following:</li><ul><li>infantry in province is owner</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If has check variable has partyManpower is 10000:</li><ul><li>custom tooltip = max_manpower_size_tooltip</li></ul><li>If does not have infantry in province is owner:</li><ul><li>custom tooltip = no_infantry_in_province_tooltip</li></ul><li>custom tooltip = manpower_desc_tooltip</li><li>If has owner has country flag is [sent_first_expedition](../flags/sent_first_expedition.md):</li><ul><li>custom tooltip = previous_expedition_preparation_tooltip</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_empty£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_reset_preparation£

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>refund party preparation:</li><ul><li>manpower = yes</li></ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.1000](diggy_expedition.1000_slug) immediately </li></ul></ul>

___
##£event_button_expedition_go_back£

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>hidden effect:</li><ul><li>fire province event [diggy_expedition.4](diggy_expedition.4_slug) immediately </li></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1](psexpedition_preparation_bgps_nssz_root_getname_n_root_dangerlevel_root_expeditionlength_n_root_lootstatus_ss_n_n_n_n_n_n_n_ssr_root_partytotalcost_getvalue2_1.md)
