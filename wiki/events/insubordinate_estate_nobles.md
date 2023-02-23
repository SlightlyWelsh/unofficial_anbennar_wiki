#Information
 - Title: Insubordinate $ESTATE_NOBLES$
 - ID: nobles_estate_events.9
#Description
Insubordinate $ESTATE_NOBLES$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Unfortunate.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier "disloyal_noble_officers" for 10 years</li></ul>

___
##It is high time we replaced them with men of true ability.

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has estate estate_burghers</li><li>estate loyalty:</li><ul><li>estate is estate_burghers</li><li>loyalty is at least 60</li></ul></ul><li>AND:</li><ul><li>has estate estate_vaisyas</li><li>estate loyalty:</li><ul><li>estate is estate_vaisyas</li><li>loyalty is at least 60</li></ul></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>If has estate is estate burghers:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_vaisyas</li><li>desc = EST_VAL_BURGHER_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_BURGHER_OFFICERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>

___
##It is high time we replaced them with men we can trust.

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>religion group is muslim</li><li>has estate estate_brahmins</li><li>estate loyalty:</li><ul><li>estate is estate_brahmins</li><li>loyalty is at least 60</li></ul></ul><li>AND:</li><ul><li>has estate estate_dhimmi</li><li>estate loyalty:</li><ul><li>estate is estate_dhimmi</li><li>loyalty is at least 60</li></ul></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>If has estate is estate dhimmi:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_dhimmi</li><li>desc = EST_VAL_DHIMMI_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>If has estate is estate brahmins:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_brahmins</li><li>desc = EST_VAL_DHIMMI_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_DHIMMI_OFFICERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>

___
##Let us consult the Brahmins, some of these learned men are clearly fit to lead.

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has estate estate_church</li><li>religion is hinduism</li><li>estate loyalty:</li><ul><li>estate is estate_church</li><li>loyalty is at least 60</li></ul></ul><li>AND:</li><ul><li>has estate estate_brahmins</li><li>religion is hinduism</li><li>estate loyalty:</li><ul><li>estate is estate_brahmins</li><li>loyalty is at least 60</li></ul></ul></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>If has estate is estate church:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_CHURCH_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>If has estate is estate brahmins:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_brahmins</li><li>desc = EST_VAL_CHURCH_OFFICERS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_CHURCH_OFFICERS</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
