#Information
 - Title: Temple Heart Discovered!
 - ID: spirits.012
#Description
Temple Heart Discovered!
#Options

___
##Give it to the Artificers for their studies

###Available if:
<li>owner:</li><ul><li>has estate estate_artificers</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has owner has estate influence has estate is estate artificers, and estate influence has influence is 30
 - Multiplied by 2 if has owner has estate influence has estate is estate artificers, and estate influence has influence is 40
 - Multiplied by 2 if has owner has estate influence has estate is estate artificers, and estate influence has influence is 50


###Efects:<ul><li>owner:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_GAVE_HEART_TO_ARTIFICERS_LOY</li><li>loyalty = 10</li><li>duration = 7300</li></ul><li>mission reward artifice points 2 = yes</li></ul><li>ruin temple = yes</li></ul>

___
##Let the Mages have it

###Available if:
<li>owner:</li><ul><li>has estate estate_mages</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has owner has estate influence has estate is estate mages, and estate influence has influence is 30
 - Multiplied by 2 if has owner has estate influence has estate is estate mages, and estate influence has influence is 40
 - Multiplied by 2 if has owner has estate influence has estate is estate mages, and estate influence has influence is 50


###Efects:<ul><li>owner:</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_GAVE_HEART_TO_MAGES_LOY</li><li>loyalty = 10</li><li>duration = 7300</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_GAVE_HEART_TO_MAGES</li><li>influence = 33</li><li>duration = 730</li></ul></ul><li>ruin temple = yes</li></ul>

___
##Mine and sell it

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has owner has num of loans is 1
 - Multiplied by 2 if has owner has num of loans is 2
 - Multiplied by 2 if has owner has num of loans is 3
 - Multiplied by 2 if has owner has num of loans is 4


###Efects:<ul><li>owner:</li><ul><li>add treasury = 5000</li></ul><li>ruin temple = yes</li></ul>

___
##We're smart lads - let's leave it alone

###AI weighting:
AI weights this option at 2
 - Multiplied by 30 if has owner has religion group is halessi
 - Multiplied by 100 if has owner has religion group is raheni
 - Multiplied by 0 if does not have owner has religion group is halessi

