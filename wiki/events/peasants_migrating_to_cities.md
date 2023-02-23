#Information
 - Title: Peasants Migrating to Cities
 - ID: artificers_estate_events.4
#Description
Peasants Migrating to Cities
#Options

___
##Enforce serfdom, send the peasants back.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 65
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 65


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_PEASANTS_RETURNED</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_PEASANTS_RETURNED</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>

___
##It isn't my problem their peasants are running away!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate artificers, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 65


###Efects:<ul><li>If random owned province has development is 15:</li><ul><li>add base production = 1</li></ul><li>If random owned province does not have development is 10; and  has base manpower is 2:</li><ul><li>add base manpower = -1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_PEASANTS_MIGRATED_TO_CITIES</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_PEASANTS_MIGRATED_TO_CITIES</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>
