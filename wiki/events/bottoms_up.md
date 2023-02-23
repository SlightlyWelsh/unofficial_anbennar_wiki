#Information
 - Title: Bottoms Up
 - ID: flavor_krakazol.300
#Description
Bottoms Up
#Options

___
##Call it off

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>clr country flag [krakazol_drinking_menu_open](../flags/krakazol_drinking_menu_open.md)</li><li>hidden effect:</li><ul><li>country gets the modifier krakazol_drink_fix for 2 days</li></ul><li>add prestige = -3</li></ul>

___
##Iron Belly

###Available if:
<li>owns 4284</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4284</li><li>If has 4284 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking iron perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4284:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_iron](../flags/krakazol_ruler_drinking_iron.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip1</li></ul>

___
##Dwarovar Dark

###Available if:
<li>owns 4266</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4266</li><li>If has 4266 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking dark perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4266:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_dark](../flags/krakazol_ruler_drinking_dark.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip2</li></ul>

___
##Beard Turner

###Available if:
<li>owns 4462</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4462</li><li>If has 4462 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking beard perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4462:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_beard](../flags/krakazol_ruler_drinking_beard.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip3</li></ul>

___
##Digger's Delight

###Available if:
<li>mission completed is krakazol_am_dwarf</li><li>has saved event target mithril_province</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = mithril_province</li><li>If has event target:mithril province has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking digging perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>event target:mithril province:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_digging](../flags/krakazol_ruler_drinking_digging.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip4</li></ul>

___
##Heart Burner

###Available if:
<li>mission completed is krakazol_spicing_up</li><li>owns 4446</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4446</li><li>If has 4446 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking heart perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4446:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_heart](../flags/krakazol_ruler_drinking_heart.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip5</li></ul>

___
##Yellow Jelly

###Available if:
<li>mission completed is krakazol_gold_malt</li><li>owns 4269</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4269</li><li>If has event target:gold province has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking yellow perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4269:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_yellow](../flags/krakazol_ruler_drinking_yellow.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip6</li></ul>

___
##Gizzard's Green

###Available if:
<li>mission completed is krakazol_seeing_green</li><li>owns 4350</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4350</li><li>If has 4350 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking gizzard perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4350:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_gizzard](../flags/krakazol_ruler_drinking_gizzard.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip7</li></ul>

___
##Shattered Nose

###Available if:
<li>mission completed is krakazol_cant_be_serious</li><li>owns 4265</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4265</li><li>If has 4265 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking shattered perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4265:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_shattered](../flags/krakazol_ruler_drinking_shattered.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip8</li></ul>

___
##Gut Smoker

###Available if:
<li>mission completed is krakazol_explosive_personality</li><li>owns 4247</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4247</li><li>If has 4247 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking gut perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4247:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_gut](../flags/krakazol_ruler_drinking_gut.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip9</li></ul>

___
##Drinker's Dispute

###Available if:
<li>mission completed is krakazol_fragrant_tusks</li><li>owns 4539</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4539</li><li>If has 4539 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking dispute perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4539:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_dispute](../flags/krakazol_ruler_drinking_dispute.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip10</li></ul>

___
##Belly Breath

###Available if:
<li>mission completed is krakazol_belly_beast</li><li>owns 4325</li>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = 4325</li><li>If has 4325 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking belly perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>4325:</li><ul><li>save event target as = drinking_province</li></ul><li>set ruler flag [krakazol_ruler_drinking_belly](../flags/krakazol_ruler_drinking_belly.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip11</li></ul>

___
##Ancestor's Ale

###Available if:
<li>mission completed is krakazol_pure_spirits</li><li>Any of the following:</li><ul><li>owns 4465</li><li>owns  4450</li></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>goto = spirit_province</li><li>If has 4465 has local autonomy is 30; and  has 4450 has local autonomy is 30:</li><ul><li>custom tooltip = krakazol_drinking_high_autonomy_tooltip</li><li>hidden effect:</li><ul><li>the event [Missing localisation: flavor_krakazol_350_t](../events/missing_localisation_flavor_krakazol_350_t.md) happens</li></ul></ul><li>else:</li><ul><li>If has country modifier is krakazol drinking ancestor perm:</li><ul><li>custom tooltip = krakazol_drinking_lose_perm_tooltip</li></ul><li>hidden effect:</li><ul><li>If does not have local autonomy is 30:</li><ul><li>4465:</li><ul><li>save event target as = drinking_province</li></ul></ul><li>else:</li><ul><li>4450:</li><ul><li>save event target as = drinking_province</li></ul></ul><li>set ruler flag [krakazol_ruler_drinking_ancestor](../flags/krakazol_ruler_drinking_ancestor.md)</li><li>the event [First Round](../events/first_round.md) happens</li></ul></ul><li>custom tooltip = flavor_krakazol.300.tooltip12</li></ul>
