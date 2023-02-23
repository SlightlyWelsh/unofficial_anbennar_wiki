#Information
 - Title: $ESTATE_CHURCH$ Insulted
 - ID: artificers_estate_events.5
#Description
$ESTATE_CHURCH$ Insulted
#Options

___
##Then we will force the university to fire him.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul><li>reduce estate artificers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_CHURCH_DEFENDED</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_CHURCH_DEFENDED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##A mild reprimand will be enough.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>reduce estate church loyalty effect = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 5</li></ul><li>add legitimacy = -5</li><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_CHURCH_RIDICULIZED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
