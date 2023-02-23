#Information
 - Title: Middle Rahen\n\n\n\n\n\n£sgc_sub_menu£
 - ID: flavor_seghdihr.140
#Description
Middle Rahen\n\n\n\n\n\n£sgc_sub_menu£
#Options

___
##£event_button_close_green£

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>highlight = yes</li><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Purchase Elephant Caravans

###Available if:
<li>has country flag [sgc_rahen_fullaccess](../flags/sgc_rahen_fullaccess.md)</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = flavor_seghdihr.140.tooltip</li><li>If does not have country modifier is seghdihr sgc rahen busy; and does not have country flag is [sgc_rahen_uni1_complete](../flags/sgc_rahen_uni1_complete.md); and  has 4485 has has opinion has who is ROOT, and has opinion has value is 100; and has AND is rival is ROOT, and AND has ROOT has adm power is 200; and  has treasury is 5000:</li><ul><li>add treasury = -5000</li><li>If has 4485 has owner is rival is ROOT:</li><ul><li>add adm power = -200</li></ul><li>country gets the modifier seghdihr_sgc_rahen_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rahen_uni1_complete](../flags/sgc_rahen_uni1_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rahen busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>If does not have treasury is 5000:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_5000g</li></ul><li>If has 4485 does not have opinion has who is ROOT, and has opinion has value is 100; and does not have rival is ROOT:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_opinion_sharaa</li></ul><li>Else if does not have adm power is 200:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_200adm</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Gifts for the Tiger Lords

###Available if:
<li>has country flag [sgc_rahen_fullaccess](../flags/sgc_rahen_fullaccess.md)</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = flavor_seghdihr.140.tooltip2</li><li>If does not have country modifier is seghdihr sgc rahen busy; and does not have country flag is [sgc_rahen_uni2_complete](../flags/sgc_rahen_uni2_complete.md); and  has treasury is 1000, and  has adm power is 50, and  has dip power is 50, and  has mil power is 50:</li><ul><li>add treasury = -1000</li><li>add adm power = -50</li><li>add dip power = -50</li><li>add mil power = -50</li><li>country gets the modifier seghdihr_sgc_rahen_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rahen_uni2_complete](../flags/sgc_rahen_uni2_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rahen busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>If does not have treasury is 1000:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_1000g</li></ul><li>If does not have adm power is 50:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_50adm</li></ul><li>If does not have dip power is 50:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_50dip</li></ul><li>If does not have mil power is 50:</li><ul><li>custom tooltip = seghdihr_sgc_missing_req_50mil</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Build an Ostkopan

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_ostkopan_tooltip</li><li>If has seghdihr sgc adm req is yes, and does not have country modifier is seghdihr sgc rahen busy; and does not have country flag is [sgc_rahen_adm_complete](../flags/sgc_rahen_adm_complete.md):</li><ul><li>seghdihr sgc adm cost = yes</li><li>country gets the modifier seghdihr_sgc_rahen_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rahen_adm_complete](../flags/sgc_rahen_adm_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rahen busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc adm missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Support Local Business

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_investment_tooltip</li><li>If has seghdihr sgc dip req is yes, and does not have country modifier is seghdihr sgc rahen busy; and does not have country flag is [sgc_rahen_dip_complete](../flags/sgc_rahen_dip_complete.md):</li><ul><li>seghdihr sgc dip cost = yes</li><li>country gets the modifier seghdihr_sgc_rahen_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rahen_dip_complete](../flags/sgc_rahen_dip_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rahen busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc dip missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>

___
##Establish Highway Patrol

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>custom tooltip = sgc_patrols_tooltip</li><li>If has seghdihr sgc mil req is yes, and does not have country modifier is seghdihr sgc rahen busy; and does not have country flag is [sgc_rahen_mil_complete](../flags/sgc_rahen_mil_complete.md):</li><ul><li>seghdihr sgc mil cost = yes</li><li>country gets the modifier seghdihr_sgc_rahen_busy for 5 years</li><li>hidden effect:</li><ul><li>the event [Improvement Complete](../events/improvement_complete.md) happens</li></ul></ul><li>else:</li><ul><li>If has country flag is [sgc_rahen_mil_complete](../flags/sgc_rahen_mil_complete.md):</li><ul><li>custom tooltip = seghdihr_sgc_improved_max</li></ul><li>Else if has country modifier is seghdihr sgc rahen busy:</li><ul><li>custom tooltip = seghdihr_sgc_node_busy</li></ul><li>else:</li><ul><li>seghdihr sgc mil missing req = yes</li></ul></ul><li>hidden effect:</li><ul><li>the event [\n\n\n\n\n\n\n£sgc_main_menu£](../events/n_n_n_n_n_n_npssgc_main_menups.md) happens</li></ul></ul>
