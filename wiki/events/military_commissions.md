#Information
 - Title: Military Commissions
 - ID: adventurers_estate_events.3
#Description
Military Commissions
#Mean Time to Happen:
Base time = 1 days

#Options

___
##No noble will serve under a commoner.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>reduce estate adventurers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_NO_COMMISSIONS_FOR_ADVENTURERS</li><li>influence = -10</li><li>duration = 3650</li></ul><li>add army tradition = -5</li></ul>

___
##We promote on merit.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>reduce estate nobles loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_COMMISSIONS_FOR_ADVENTURERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
