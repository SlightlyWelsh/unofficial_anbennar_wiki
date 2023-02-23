#Information
 - Title: Demands of the $ESTATE_NOMADIC_TRIBES$
 - ID: tribal_estate_events.14
#Description
Demands of the $ESTATE_NOMADIC_TRIBES$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Agree.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier "no_tribal_leaders" for 5 years</li><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_TRIBES_DEMANDING</li><li>estate = estate_nomadic_tribes</li><li>influence = 10</li><li>duration = 1825</li></ul></ul>

___
##They will do no such thing!

###AI weighting:
AI weights this option at 99
 - Multiplied by 0.01 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 45


###Efects:<ul><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_TRIBES_REFUSED_DEMANDING</li><li>estate = estate_nomadic_tribes</li><li>influence = -10</li><li>duration = 1825</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -20</li></ul></ul>
