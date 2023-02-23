#Information
 - Title: $ESTATE_ADVENTURERS$ Insult the $ESTATE_CHURCH$
 - ID: adventurers_estate_events.6
#Description
$ESTATE_ADVENTURERS$ Insult the $ESTATE_CHURCH$
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.5 if has religion is ravelian, and has religion is corinite, and has religion is bulwari sun cult, and has religion is khetist, and has religion is high philosophy

#Options

___
##Punish the $ESTATE_ADVENTURERS$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has estate influence has estate is estate adventurers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -20</li></ul></ul>

___
##Words are words, let them go

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 70


###Efects:<ul><li>add estate adventurers loyalty effect = yes</li><li>reduce estate church loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_UNDERMINED_BY_ADVENTURERS</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
