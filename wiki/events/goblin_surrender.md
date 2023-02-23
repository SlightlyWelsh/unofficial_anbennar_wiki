#Information
 - Title: Goblin Surrender
 - ID: aw_goblins.120
#Description
Goblin Surrender
#Options

___
##They can stay so long as they obey.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_AW_RESOLVED_ADVENTURERS_WANTED_ENCOUNTER</li><li>duration = 3650</li><li>influence = 5</li></ul></ul><li>If has province modifier is aw goblins 1, and has province modifier is aw goblins 2:</li><ul><li>add goblin minority size effect = yes</li></ul><li>Else if has province modifier is aw goblins 3:</li><ul><li>add goblin minority size effect = yes</li><li>add goblin minority size effect = yes</li></ul><li>remove province modifier = aw_goblins_1</li><li>remove province modifier = aw_goblins_2</li><li>remove province modifier = aw_goblins_3</li></ul>

___
##No, take their possessions and send them away.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_AW_RESOLVED_ADVENTURERS_WANTED_ENCOUNTER</li><li>duration = 3650</li><li>influence = 5</li></ul></ul><li>remove province modifier = aw_goblins_1</li><li>remove province modifier = aw_goblins_2</li><li>remove province modifier = aw_goblins_3</li><li>owner:</li><ul><li>add years of income = 0.5</li></ul></ul>
