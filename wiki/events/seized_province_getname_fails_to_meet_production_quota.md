#Information
 - Title: [seized_province.GetName] Fails to Meet Production Quota
 - ID: flavor_gawed.15
#Description
[seized_province.GetName] Fails to Meet Production Quota
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must punish them!

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>event target:seized province:</li><ul><li>add province modifier:</li><ul><li>name = nl_harsh_quotas</li><li>duration = 1825</li></ul></ul><li>add faction influence:</li><ul><li>faction = nl_cooperatists</li><li>influence = 5</li></ul><li>add faction influence:</li><ul><li>faction = nl_trade_barons</li><li>influence = -5</li></ul></ul>

___
##The town must be allowed to prosper, free from unjust restrictions.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:seized province:</li><ul><li>add province modifier:</li><ul><li>name = nl_unfulfilled_quotas</li><li>duration = 1825</li></ul></ul><li>add faction influence:</li><ul><li>faction = nl_cooperatists</li><li>influence = -5</li></ul><li>add faction influence:</li><ul><li>faction = nl_trade_barons</li><li>influence = 5</li></ul></ul>
