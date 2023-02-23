#Information
 - Title: $ESTATE_BURGHERS$ Refuse to Pay $ESTATE_ADVENTURERS$
 - ID: adventurers_estate_events.5
#Description
$ESTATE_BURGHERS$ Refuse to Pay $ESTATE_ADVENTURERS$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##A quest is a quest. Force the merchant to pay.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = 10</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_SUPPORTED_ADVENTURERS</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_SUPPORTED_ADVENTURERS</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##If the adventurers did a poor job, then let them suffer

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_SUPPORTED_BURGHERS_VS_ADVENTURERS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_SUPPORTED_BURGHERS_VS_ADVENTURERS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
