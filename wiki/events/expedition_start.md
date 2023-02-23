#Information
 - Title: Expedition Start
 - ID: flavor_castanor.50
#Description
Expedition Start
#Options

___
##Send mages to explore the underwater ruins

###Efects:<ul><li>hidden effect:</li><ul><li>If has ruler is legendary in divination, and has court mage is 5, and has estate loyalty has estate is estate mages, and estate loyalty has loyalty is 80:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 4</li></ul></ul><li>Else if has estate loyalty has estate is estate mages, and estate loyalty has loyalty is 70; and has ruler is renowned in divination, and has court mage is 4:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 3</li></ul></ul><li>Else if has estate loyalty has estate is estate mages, and estate loyalty has loyalty is 60; and has ruler is talented in divination, and has court mage is 3:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 2</li></ul></ul><li>Else if has estate loyalty has estate is estate mages, and estate loyalty has loyalty is 50; and has court mage is 2:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 1</li></ul></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -5</li></ul><li>set country flag [south_citadel_expedition_mages_exploration](../flags/south_citadel_expedition_mages_exploration.md)</li></ul>

___
##Send adventurers into the depths of the lower passages

###Efects:<ul><li>hidden effect:</li><ul><li>If has country flag is [patrician_castanor](../flags/patrician_castanor.md), and has ruler modifier is patrician castan, and has estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 80:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 4</li></ul></ul><li>Else if has estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 70:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 3</li></ul></ul><li>Else if has estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 60:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 2</li></ul></ul><li>Else if has estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 50:</li><ul><li>change variable:</li><ul><li>which = southCitadelExpeditionSuccess</li><li>value = 1</li></ul></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -5</li></ul><li>set country flag [south_citadel_expedition_adventurer_exploration](../flags/south_citadel_expedition_adventurer_exploration.md)</li></ul>
