#Information
 - Title: Parallel Authority
 - ID: burghers_estate_events.6
#Description
Parallel Authority
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Side with the $ESTATE_BURGHERS$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 65


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_AUTHORITY_ASSERTED</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_BURGHER_AUTHORITY_ASSERTED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Side with the $ESTATE_CHURCH$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 65


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_AUTHORITY_QUESTIONED</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_BURGHER_AUTHORITY_QUESTIONED</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
