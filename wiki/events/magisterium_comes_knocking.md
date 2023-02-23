#Information
 - Title: Magisterium Comes knocking
 - ID: flavor_varaine.302
#Description
Magisterium Comes knocking
#Options

___
##Give them the potions

###Efects:<ul><li>A85:</li><ul><li>the event [Potions from Varainé](../events/potions_from_varaine.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A99_magisterium_helped</li></ul></ul></ul>

___
##Sell them the potions

###Efects:<ul><li>A85:</li><ul><li>the event [Potions from Varainé](../events/potions_from_varaine.md) happens</li></ul><li>add treasury = 200</li></ul>

___
##Refuse and use the potions for our own mages

###Efects:<ul><li>A85:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = A99_magisterium_denied_help</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>influence = 15</li><li>duration = 7300</li><li>desc = A99_mages_with_potions</li></ul></ul>
