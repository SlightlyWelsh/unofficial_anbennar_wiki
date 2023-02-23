#Information
 - Title: Triumph of the $ESTATE_CHURCH$?
 - ID: church_estate_events.6
#Description
Triumph of the $ESTATE_CHURCH$?
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Follow the recommendations of the $ESTATE_CHURCH$.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>country gets the modifier "religious_court_life" for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_ACCEPTED_HOLY_LAW</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add karma = 10</li></ul>

___
##Reject their authority.

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add stability = -1</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_REJECTED_HOLY_LAW</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
