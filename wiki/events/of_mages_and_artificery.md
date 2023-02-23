#Information
 - Title: Of Mages and Artificery
 - ID: mages_estate_events.3
#Description
Of Mages and Artificery
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Support the $ESTATE_ARTIFICERS$

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_MAGIC_DEBATE_ARTIFICERS</li><li>influence = -5</li><li>duration = 3650</li></ul></ul>

___
##Support the $ESTATE_MAGES$

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_MAGIC_DEBATE_MAGES</li><li>influence = -5</li><li>duration = 3650</li></ul></ul>
