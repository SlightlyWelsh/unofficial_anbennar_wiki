#Information
 - Title: Religious Mages and the Clergy
 - ID: mages_estate_events.23
#Description
Religious Mages and the Clergy
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Magic users must bow to religious authority.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_MAGIC_DEBATE_CLERGY</li><li>influence = -5</li><li>duration = 3650</li></ul></ul>

___
##Magic is special, and their users must be treated that way too

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_MAGIC_DEBATE_MAGES</li><li>influence = -5</li><li>duration = 3650</li></ul></ul>
