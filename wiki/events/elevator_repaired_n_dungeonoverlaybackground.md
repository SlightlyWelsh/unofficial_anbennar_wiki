#Information
 - Title: Elevator Repaired\n[DungeonOverlayBackground]
 - ID: diggy_dungeons.722
#Description
Elevator Repaired\n[DungeonOverlayBackground]
#Options

___
##Expedition complete.

###Available if:
<li>always</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>currency effect expedition:</li><ul><li>currency = treasury</li><li>cash = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = adm_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = dip_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = mil_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>hidden effect:</li><ul><li>If while has check variable has partyManpower is 1000:</li><ul><li>subtract variable:</li><ul><li>partyManpower = 1000</li></ul><li>owner:</li><ul><li>add manpower = 1</li></ul></ul></ul><li>custom tooltip = back_to_manpower_tooltip</li><li>custom tooltip = base_expedition_loot_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul><li>hidden effect:</li><ul><li>set province flag [floor_explored](../flags/floor_explored.md)</li></ul></ul>
