#Information
 - Title: Social Mobility
 - ID: burghers_estate_events.10
#Description
Social Mobility
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We must not stand in the way of these new men.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_NEW_MEN</li><li>influence = 10</li><li>duration = 7300</li></ul><li>country gets the modifier "new_men" for 10 years</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -20</li></ul></ul><li>add meritocracy effect = yes</li></ul>

___
##We must protect the ancient rights of the other Estates.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 85


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BARRED_FROM_CAREERS</li><li>influence = -10</li><li>duration = 7300</li></ul><li>country gets the modifier "held_back_commoners" for 15 years</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul><li>add army tradition = -15</li><li>add navy tradition = -15</li></ul><li>If has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = 15</li></ul><li>add corruption = 1</li></ul><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>add adm power = -75</li></ul><li>reduce meritocracy effect = yes</li></ul>
