#Information
 - Title: Insubordinate [Root.GetEunuchsName]
 - ID: eunuchs_estate_events.9
#Description
Insubordinate [Root.GetEunuchsName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Unfortunate.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier "disloyal_eunuch_officers" for 10 years</li></ul>

___
##It is high time we replaced them with men of true ability.

###Available if:
<li>has estate estate_burghers</li><li>estate loyalty:</li><ul><li>estate is estate_burghers</li><li>loyalty is at least 60</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 35


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_BURGHER_OFFICERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>

___
##It is high time we replaced them with men we can trust.

###Available if:
<li>has estate estate_church</li><li>religion is righteous_path</li><li>estate loyalty:</li><ul><li>estate is estate_church</li><li>loyalty is at least 60</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_CHURCH_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_CHURCH_OFFICERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
