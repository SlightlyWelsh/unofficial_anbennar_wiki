#Information
 - Title: Temple Lands
 - ID: church_estate_events.101
#Description
Temple Lands
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Make it clear that they need to contribute.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add years of income = 0.35</li><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_DEMANDED_CHURCH_MONEY</li><li>influence = -10</li><li>duration = 9125</li></ul></ul>

___
##We will find the money elsewhere.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add prestige = 5</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_DIDNT_DEMAND_CHURCH_MONEY</li><li>influence = 10</li><li>duration = 9125</li></ul></ul>
