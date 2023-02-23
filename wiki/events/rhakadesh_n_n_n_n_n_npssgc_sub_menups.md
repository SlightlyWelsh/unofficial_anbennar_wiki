#Information
 - Title: Rhakadesh\n\n\n\n\n\n£sgc_sub_menu£
 - ID: flavor_seghdihr.130
#Description
Rhakadesh\n\n\n\n\n\n£sgc_sub_menu£
#Options

___
##£event_button_close_green£

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>highlight = yes</li><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Update Tax Code

###Available if:
<li>has country flag [sgc_rhak_fullaccess](../flags/sgc_rhak_fullaccess.md)</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = flavor_seghdihr.130.tooltip</li><li>If does not have country modifier is seghdihr sgc rhak busy; and does not have country flag is [sgc_rhak_uni1_complete](../flags/sgc_rhak_uni1_complete.md); and has any known country has culture is ghankedhen, and any known country has opinion has who is ROOT, and has opinion has value is 100; and does not have any known country has culture is ghankedhen; and AND has adm power is 300; and  has treasurer is 3:</li><ul><li>If does not have any known country has culture is ghankedhen, and any known country has opinion has who is ROOT, and has opinion has value is 100:</li><ul><li>add adm power = -300</li></ul><li>kill advisor = treasurer</li><li>country gets the modifier seghdihr_sgc_rhak_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rhak_uni1_complete](../flags/sgc_rhak_uni1_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rhak busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>If does not have any known country has culture is ghankedhen, and any known country has opinion has who is ROOT, and has opinion has value is 100:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_opinion_ghank</li></ul><li>Else if does not have adm power is 300:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_300adm</li></ul><li>If does not have treasurer is 3:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_treasurer3</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Sponsor Mercenaries

###Available if:
<li>has country flag [sgc_rhak_fullaccess](../flags/sgc_rhak_fullaccess.md)</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = flavor_seghdihr.130.tooltip2</li><li>If does not have country modifier is seghdihr sgc rhak busy; and does not have country flag is [sgc_rhak_uni2_complete](../flags/sgc_rhak_uni2_complete.md); and  has treasury is 2000, and  has mil power is 100:</li><ul><li>add treasury = -2000</li><li>add mil power = -100</li><li>country gets the modifier seghdihr_sgc_rhak_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rhak_uni2_complete](../flags/sgc_rhak_uni2_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rhak busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>If does not have treasury is 2000:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_2000g</li></ul><li>If does not have mil power is 100:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_100mil</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Build an Ostkopan

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_ostkopan_tooltip</li><li>If has seghdihr sgc adm req is yes, and does not have country modifier is seghdihr sgc rhak busy; and does not have country flag is [sgc_rhak_adm_complete](../flags/sgc_rhak_adm_complete.md):</li><ul><li>seghdihr sgc adm cost = yes</li><li>country gets the modifier seghdihr_sgc_rhak_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rhak_adm_complete](../flags/sgc_rhak_adm_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rhak busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc adm missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Support Local Business

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_investment_tooltip</li><li>If has seghdihr sgc dip req is yes, and does not have country modifier is seghdihr sgc rhak busy; and does not have country flag is [sgc_rhak_dip_complete](../flags/sgc_rhak_dip_complete.md):</li><ul><li>seghdihr sgc dip cost = yes</li><li>country gets the modifier seghdihr_sgc_rhak_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rhak_dip_complete](../flags/sgc_rhak_dip_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rhak busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc dip missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Establish Highway Patrol

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_patrols_tooltip</li><li>If has seghdihr sgc mil req is yes, and does not have country modifier is seghdihr sgc rhak busy; and does not have country flag is [sgc_rhak_mil_complete](../flags/sgc_rhak_mil_complete.md):</li><ul><li>seghdihr sgc mil cost = yes</li><li>country gets the modifier seghdihr_sgc_rhak_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rhak_mil_complete](../flags/sgc_rhak_mil_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rhak busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc mil missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>
