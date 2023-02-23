#Information
 - Title: Hurtful Trade Policies
 - ID: burghers_estate_events.8
#Description
Hurtful Trade Policies
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must support the $ESTATE_BURGHERS$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "burgher_favorable_trade_laws" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_BYPASSING_EMBARGO</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##We cannot let our trade policy be decided by these peddlers.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "burgher_unfavorable_trade_laws" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_DENIED_BYPASS_OF_EMBARGO</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
