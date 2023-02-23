#Information
 - Title: Rogue Traders Ignoring Company Monopoly
 - ID: investment_events.9
#Description
Rogue Traders Ignoring Company Monopoly
#Mean Time to Happen:
Base time = 1 days

#Options

___
##[monopoly_ignored_country.GetName] must trade only with the Company.

###Efects:<ul><li>add mercantilism = 1</li><li>event target:monopoly ignored province:</li><ul><li>add province modifier:</li><ul><li>name = monopoly_enforced</li><li>duration = 7300</li></ul></ul><li>event target:monopoly ignored country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_monopoly_enforced_company</li></ul></ul></ul>

___
##We will prosecute the rogue traders ourselves.

###Efects:<ul><li>country gets the modifier rogue_traders_prosecuted for 20 years</li><li>event target:monopoly ignored province:</li><ul><li>add province modifier:</li><ul><li>name = province_rogue_traders_prosecuted</li><li>duration = 7300</li></ul></ul></ul>
