#Information
 - Title: Noble Birth
 - ID: nobles_estate_events.1
#Description
Noble Birth
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Guarantee their right to command our armies.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.2 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 60
 - Multiplied by 0.2 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30
 - Multiplied by 0.2 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 30
 - Multiplied by 0.2 if has estate is estate eunuchs, and does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 30


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -20</li></ul></ul><li>country gets the modifier "only_noble_officers" for 20 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_EXCLUSIVE_RIGHT_TO_BE_OFFICERS_NOBLES</li><li>influence = 10</li><li>duration = 7300</li></ul></ul>

___
##We cannot commit to such promises.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.1 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 40
 - Multiplied by 0.1 if has estate is estate eunuchs, and does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = 15</li></ul></ul><li>If has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = 15</li></ul></ul><li>add army professionalism = 0.02</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NO_EXCLUSIVE_RIGHT_TO_BE_OFFICERS_NOBLES</li><li>influence = -10</li><li>duration = 7300</li></ul></ul>
