#Information
 - Title: My [Root.GovernmentName] of $COUNTRY$: Progress is Magic
 - ID: mages_estate_events.12
#Description
My [Root.GovernmentName] of $COUNTRY$: Progress is Magic
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Follow the wisdom of the $ESTATE_MAGES$.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>country gets the modifier mundane_problems_magical_solutions for 15 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_ACCEPTED_MAGIC_LAW</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>

___
##Reject such backward notions!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate mages, and estate influence has influence is 60


###Efects:<ul><li>add stability = -1</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_REJECTED_MAGIC_LAW</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
