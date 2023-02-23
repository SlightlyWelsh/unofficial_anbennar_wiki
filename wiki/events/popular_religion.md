#Information
 - Title: Popular Religion
 - ID: church_estate_events.9
#Description
Popular Religion
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Attempt to root out this syncretism.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "campaign_against_syncretism" for 15 years</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_FOUGHT_SYNCRETISM</li><li>influence = 10</li><li>duration = 5475</li></ul><li>reduce estate dhimmi loyalty effect = yes</li><li>add karma = -5</li></ul>

___
##Better let this run its course.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 65


###Efects:<ul><li>country gets the modifier "missionary_syncretism" for 15 years</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_SYNCRETISM</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate dhimmi loyalty effect = yes</li><li>add karma = 5</li></ul>
