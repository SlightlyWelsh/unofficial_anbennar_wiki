#Information
 - Title: Nepotism in the $ESTATE_ARTIFICERS$ Guilds is Holding Back Our Economy.
 - ID: artificers_estate_events.7
#Description
Nepotism in the $ESTATE_ARTIFICERS$ Guilds is Holding Back Our Economy.
#Options

___
##Let them.

###AI weighting:
AI weights this option at 40
 - Multiplied by 2 if has estate influence has estate is estate artificers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_ARTIFICERS_NEPOTISM</li><li>influence = -10</li><li>duration = 7300</li></ul><li>If every owned province has province flag is [needs_more_workers](../flags/needs_more_workers.md):</li><ul><li>add province modifier:</li><ul><li>name = "thankful_guilds"</li><li>duration = 3650</li></ul><li>clr province flag [needs_more_workers](../flags/needs_more_workers.md)</li></ul></ul>

___
##Force them to accept new personnel!

###AI weighting:
AI weights this option at 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 35


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_ARTIFICERS_NEW_PERSONNEL</li><li>influence = 10</li><li>duration = 7300</li></ul><li>If every owned province has province flag is [needs_more_workers](../flags/needs_more_workers.md):</li><ul><li>add base production = 1</li><li>clr province flag [needs_more_workers](../flags/needs_more_workers.md)</li></ul></ul>

___
##Go around them by sponsoring new workshops.

###AI weighting:
AI weights this option at 20
 - Multiplied by 2 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 35
 - Multiplied by 2 if does not have estate influence has estate is estate artificers, and estate influence has influence is 30
 - Multiplied by 0.5 if does not have years of income is 0.75


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_ARTIFICERS_NEW_PERSONNEL</li><li>influence = 10</li><li>duration = 7300</li></ul><li>If every owned province has province flag is [needs_more_workers](../flags/needs_more_workers.md):</li><ul><li>add base production = 1</li><li>clr province flag [needs_more_workers](../flags/needs_more_workers.md)</li></ul><li>add years of income = -0.75</li></ul>
