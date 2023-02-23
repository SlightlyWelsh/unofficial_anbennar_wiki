#Information
 - Title: Mages Suggest Necromantic Methods to Combat Zombies
 - ID: aw_zombies.122
#Description
Mages Suggest Necromantic Methods to Combat Zombies
#Options

___
##Very well, we will try this thing - but this is not a blanket endorsement of necromancy!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>owner:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_AW_STATE_OWES_FAVOURS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>If has province modifier is aw zombies 3:</li><ul><li>remove province modifier = aw_zombies_3</li><li>add permanent province modifier:</li><ul><li>name = aw_zombies_2</li><li>duration = -1</li></ul></ul><li>Else if has province modifier is aw zombies 2:</li><ul><li>remove province modifier = aw_zombies_2</li><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul><li>Else if has province modifier is aw zombies 1:</li><ul><li>remove province modifier = aw_zombies_1</li></ul></ul>

___
##These small mages think they are in a position to bargain? Make them kneel.

###Available if:
<li>owner:</li><ul><li>has ruler modifier witch_king_modifier</li></ul>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = tooltip_witch_king</li><li>owner:</li><ul><li>add mil power = -10</li></ul><li>If has province modifier is aw zombies 3:</li><ul><li>remove province modifier = aw_zombies_3</li><li>add permanent province modifier:</li><ul><li>name = aw_zombies_2</li><li>duration = -1</li></ul></ul><li>Else if has province modifier is aw zombies 2:</li><ul><li>remove province modifier = aw_zombies_2</li><li>add permanent province modifier:</li><ul><li>name = aw_zombies_1</li><li>duration = -1</li></ul></ul><li>Else if has province modifier is aw zombies 1:</li><ul><li>remove province modifier = aw_zombies_1</li></ul></ul>
