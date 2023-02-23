#Information
 - Title: Conflict between Nobles and [Root.GetEunuchsName]
 - ID: eunuchs_estate_events.6
#Description
Conflict between Nobles and [Root.GetEunuchsName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Favor the [Root.GetEunuchsName].

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35; and does not have estate loyalty has estate is estate uppercastes, and estate loyalty has loyalty is 35
 - Multiplied by 0.5 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45; and has estate loyalty has estate is estate uppercastes, and estate loyalty has loyalty is 45


###Efects:<ul><li>country gets the modifier "eunuch_dominated_bureaucracy" for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_VAL_EUNUCH_PRIMACY</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_SPURNED</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_uppercastes</li><li>desc = EST_VAL_UPPERCASTES_SPURNED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Favor the $ESTATE_NOBLES$.

###Available if:
<li>has estate estate_nobles</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35
 - Multiplied by 0.5 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 45


###Efects:<ul><li>country gets the modifier "noble_dominated_bureaucracy" for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLE_PRIMACY</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_VAL_EUNUCHS_SPURNED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Favor the Upper Castes.

###Available if:
<li>has estate estate_uppercastes</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate uppercastes, and estate loyalty has loyalty is 35
 - Multiplied by 0.5 if has estate loyalty has estate is estate uppercastes, and estate loyalty has loyalty is 45


###Efects:<ul><li>country gets the modifier "noble_dominated_bureaucracy" for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_UPPERCASTE_PRIMACY</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_eunuchs</li><li>desc = EST_VAL_EUNUCHS_SPURNED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
