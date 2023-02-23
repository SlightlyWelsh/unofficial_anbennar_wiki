#Information
 - Title: Immoral Prices
 - ID: burghers_estate_events.5
#Description
Immoral Prices
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has inflation is 5

#Options

___
##Force the Merchants to lower their prices.

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md):</li><ul><li>clr province flag [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md)</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_PRICE_MEDDLING</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##We should not meddle in these things.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_FREE_OF_MEDDLING</li><li>influence = 10</li><li>duration = 5475</li></ul><li>If every owned province has province flag is [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md):</li><ul><li>clr province flag [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md)</li><li>spawn rebels:</li><ul><li>type = anti_tax_rebels</li><li>size = 1</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul></ul>

___
##We must pay for and distribute what bread there is.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have years of income is 0.2
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>add years of income = -0.15</li><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_FREE_OF_MEDDLING</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md):</li><ul><li>clr province flag [bread_revolt_vs_burghers](../flags/bread_revolt_vs_burghers.md)</li></ul></ul></ul>
