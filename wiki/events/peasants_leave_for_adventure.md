#Information
 - Title: Peasants Leave for Adventure
 - ID: adventurers_estate_events.4
#Description
Peasants Leave for Adventure
#Mean Time to Happen:
Base time = 1 days

#Options

___
##These Serfs must be brought back.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_SERFS_HUNTED</li><li>influence = -10</li><li>duration = 3650</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_SERFS_BROUGHT_BACK</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##No one can resist the Call to Adventure!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>goto = serfs_are_arriving_province</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_SERFS_TO_COSSACKS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_SERFS_DEFECTING</li><li>influence = -10</li><li>duration = 3650</li></ul><li>event target:serfs are fleeing province:</li><ul><li>add base production = -1</li></ul><li>event target:serfs are arriving province:</li><ul><li>add base manpower = 1</li></ul></ul>
