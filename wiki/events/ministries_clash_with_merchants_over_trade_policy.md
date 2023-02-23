#Information
 - Title: Ministries clash with Merchants over trade policy
 - ID: rajministries.2
#Description
Ministries clash with Merchants over trade policy
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The Ministers have determined what is best for the nation

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_raj_ministries</li><li>desc = EST_VAL_MINISTER_TRADING_POLICY</li><li>influence = 10</li><li>duration = 3650</li></ul><li>If has estate is estate middlecastes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_middlecastes</li><li>loyalty = -15</li></ul></ul><li>Else if has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul></ul><li>country gets the modifier raj_ministries_minister_trade_policy for 10 years</li></ul>

___
##The Merchants know their business

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = -15</li></ul><li>If has estate is estate middlecastes:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_middlecastes</li><li>desc = EST_VAL_MERCHANTS_OVER_MINISTERS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_middlecastes</li><li>loyalty = 15</li></ul></ul><li>Else if has estate is estate burghers:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_MERCHANTS_OVER_MINISTERS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul></ul><li>country gets the modifier raj_ministries_merchant_trade_policy for 10 years</li></ul>
