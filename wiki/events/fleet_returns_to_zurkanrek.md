#Information
 - Title: Fleet Returns to Zurkanrek
 - ID: treasurefleet.102
#Description
Fleet Returns to Zurkanrek
#Options

___
##Welcome home, weary sailors.

###Efects:<ul><li>JY LF pirate status = yes</li><li>JY LF clear damage = yes</li><li>If has global flag is [JY_LF_som_loot](../flags/jy_lf_som_loot.md):</li><ul><li>clr global flag [JY_LF_som_loot](../flags/jy_lf_som_loot.md)</li><li>custom tooltip = JY_LF_som_loot_t</li><li>add treasury = 25</li><li>add adm power = 25</li><li>add dip power = 25</li><li>add mil power = 25</li></ul><li>If has 4990 does not have country flag is [JY_LF_no_native](../flags/jy_lf_no_native.md); and does not have city:</li><ul><li>custom tooltip = JY_LF_tuuchuweg_trade</li><li>add treasury = 10</li></ul><li>If has global flag is [JY_LF_somyonghon_caught_first](../flags/jy_lf_somyonghon_caught_first.md):</li><ul><li>the event [Caught Looting Island](../events/caught_looting_island.md) happens</li></ul><li>custom tooltip = JY_LF_cash</li><li>currency effect:</li><ul><li>currency = treasury</li><li>addTo = ROOT</li><li>which = JY_LF_total</li></ul><li>If has global flag is [JY_LF_new_institution](../flags/jy_lf_new_institution.md):</li><ul><li>clr global flag [JY_LF_new_institution](../flags/jy_lf_new_institution.md)</li><li>custom tooltip = JY_LF_spread</li><li>add treasury = -40</li></ul><li>FROM:</li><ul><li>JY LF teach self = yes</li></ul><li>If has tag is J33, and  has global flag is [JY_LF_institution_speed_2](../flags/jy_lf_institution_speed_2.md):</li><ul><li>If random owned province has development is 15:</li><ul><li>JY LF teach = yes</li></ul></ul><li>If has global flag is [JY_LF_monopoly_Y15](../flags/jy_lf_monopoly_y15.md):</li><ul><li>custom tooltip = JY_LF_Y15_monopoly</li></ul><li>If has country flag is [treasure_fleet_level_1](../flags/treasure_fleet_level_1.md), and has country flag is treasure fleet level 2, and has country flag is treasure fleet level 3:</li><ul><li>5226:</li><ul><li>add province triggered modifier = boons_from_fleet_trigger</li></ul></ul></ul>
