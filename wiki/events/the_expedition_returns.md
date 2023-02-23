#Information
 - Title: The Expedition Returns
 - ID: diggy_expedition.12
#Description
The Expedition Returns
#Options

___
##Repay them in full and give them leave so that they can rest.

###Available if:
<li>hidden trigger:</li><ul><li>check variable:</li><ul><li>partyLoot is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>currency effect expedition:</li><ul><li>currency = treasury</li><li>cash = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = adm_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = dip_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = mil_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>hidden effect:</li><ul><li>If while has check variable has partyManpower is 1000:</li><ul><li>subtract variable:</li><ul><li>partyManpower = 1000</li></ul><li>owner:</li><ul><li>add manpower = 1</li></ul></ul></ul><li>custom tooltip = back_to_manpower_tooltip</li><li>custom tooltip = base_expedition_loot_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul></ul>

___
##Repay them in full and send them back out!

###Available if:
<li>hidden trigger:</li><ul><li>check variable:</li><ul><li>partyLoot is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>hidden effect:</li><ul><li>If while has check variable has partyManpower is 1000:</li><ul><li>subtract variable:</li><ul><li>partyManpower = 1000</li></ul><li>owner:</li><ul><li>infantry = PREV</li></ul></ul><li>owner:</li><ul><li>add manpower = 1</li></ul></ul><li>currency effect expedition:</li><ul><li>currency = treasury</li><li>cash = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = adm_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = dip_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>currency effect expedition:</li><ul><li>currency = mil_power</li><li>mana = yes</li><li>addTo = owner</li></ul><li>custom tooltip = back_to_manpower_unit_tooltip</li><li>custom tooltip = base_expedition_loot_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul></ul>

___
##Their loot leaves much to be desired, but that is not their fault. Let us cover their losses and rest.

###Available if:
<li>hidden trigger:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyLoot is at least 1</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>hidden effect:</li><ul><li>If while has check variable has partyManpower is 1000:</li><ul><li>subtract variable:</li><ul><li>partyManpower = 1000</li></ul><li>owner:</li><ul><li>add manpower = 1</li></ul></ul></ul><li>custom tooltip = pay_the_difference_tooltip</li><li>currency effect expedition:</li><ul><li>currency = treasury</li><li>badLoot = yes</li><li>takeFrom = owner</li></ul><li>custom tooltip = back_to_manpower_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul></ul>

___
##Their loot leaves much to be desired, but that is not their fault. Let us cover their losses and send them back out!

###Available if:
<li>hidden trigger:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyLoot is at least 1</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>hidden effect:</li><ul><li>If while has check variable has partyManpower is 1000:</li><ul><li>subtract variable:</li><ul><li>partyManpower = 1000</li></ul><li>owner:</li><ul><li>infantry = PREV</li></ul></ul><li>owner:</li><ul><li>add manpower = 1</li></ul></ul><li>custom tooltip = pay_the_difference_tooltip</li><li>currency effect expedition:</li><ul><li>currency = treasury</li><li>badLoot = yes</li><li>takeFrom = owner</li></ul><li>custom tooltip = back_to_manpower_unit_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul></ul>

___
##There is not enough valuables to cover to pay them for their services… They should have found more, then.

###Available if:
<li>hidden trigger:</li><ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>partyLoot is at least 1</li></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>special reward expedition = yes</li><li>owner:</li><ul><li>country gets the modifier dwarovar_expedition_douche for 10 years</li></ul><li>custom tooltip = dont_pay_the_difference_tooltip</li><li>If has check variable has ancientDwarvenKnowledge is 1:</li><ul><li>fire province event [diggy_expedition.14](diggy_expedition.14_slug) immediately </li></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>clear expedition effect = yes</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [the_expedition_returns_1](the_expedition_returns_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_expedition_returns_1](the_expedition_returns_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [the_expedition_returns_1](the_expedition_returns_1.md)
