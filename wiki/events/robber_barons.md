#Information
 - Title: Robber Barons
 - ID: burghers_estate_events.2
#Description
Robber Barons
#Mean Time to Happen:
Base time = 1 days

#Options

___
##They only take what is their right.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 65
 - Multiplied by 1.5 if does not have estate is estate nobles; and does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate is estate nobles; and  has estate influence has estate is estate eunuchs, and estate influence has influence is 65


###Efects:<ul><li>event target:robber baron province:</li><ul><li>add base tax = 1</li></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul></ul><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = 15</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHERS_ROBBER_BARONS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>If has estate is estate nobles:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_ROBBER_BARONS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_VAL_NOBLES_ROBBER_BARONS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul></ul>

___
##We must curb such excesses!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have estate is estate nobles; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if does not have estate is estate nobles; and  has estate influence has estate is estate nobles, and estate influence has influence is 65


###Efects:<ul><li>event target:robber baron province:</li><ul><li>add base production = 1</li></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul></ul><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -15</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>If has estate is estate nobles:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_DEFEATED_ROBBER_BARONS</li><li>influence = -10</li><li>duration = 5475</li></ul></ul><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_VAL_NOBLES_DEFEATED_ROBBER_BARONS</li><li>influence = -10</li><li>duration = 5475</li></ul></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHERS_DEFEATED_ROBBER_BARONS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
