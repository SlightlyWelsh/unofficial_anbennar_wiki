#Information
 - Title: Urbanization
 - ID: burghers_estate_events.13
#Description
Urbanization
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Attempt to improve conditions.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>add years of income = -0.25</li><li>If every owned province has province flag is [urbanisation](../flags/urbanisation.md):</li><ul><li>add base tax = 1</li><li>clr province flag [urbanisation](../flags/urbanisation.md)</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>influence = 10</li><li>desc = EST_VAL_SUPPORTED_CITY_GROWTH</li><li>duration = 7300</li></ul></ul>

___
##This is nothing unusual, the $ESTATE_BURGHERS$ can handle it.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>If every owned province has province flag is [urbanisation](../flags/urbanisation.md):</li><ul><li>add province modifier:</li><ul><li>name = "unsanitary_suburbs"</li><li>duration = 7300</li></ul><li>clr province flag [urbanisation](../flags/urbanisation.md)</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>influence = -10</li><li>desc = EST_VAL_NOT_SUPPORTING_CITY_GROWTH</li><li>duration = 7300</li></ul></ul>
