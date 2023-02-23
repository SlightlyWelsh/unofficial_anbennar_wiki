This page has the same name as others. For full listing see bottom of [the base page](growth_of_the_administration.md).

#Information
 - Title: Growth of the Administration
 - ID: nobles_estate_events.10
#Description
Growth of the Administration
#Mean Time to Happen:
Base time = 1 days

#Options

___
##With a great pedigree come great abilities.

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "noble_minister" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = -20</li></ul></ul><li>If does not have estate is estate vaisyas; and does not have estate is estate burghers:</li><ul><li>add mercantilism = -1</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_MINISTER_NOBLES</li><li>influence = 15</li><li>duration = 3650</li></ul></ul>

___
##Self-made men are what we need to run this country.

###Available if:
<li>Any of the following:</li><ul><li>has estate estate_burghers</li><li>has estate  estate_vaisyas</li></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate is estate burghers, and  has estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate burghers, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate is estate vaisyas, and  has estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate vaisyas, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "burgher_minister" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_MINISTER_BURGHERS</li><li>influence = 15</li><li>duration = 3650</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_vaisyas</li><li>desc = EST_VAL_MINISTER_BURGHERS</li><li>influence = 15</li><li>duration = 3650</li></ul></ul></ul>

___
##Let us turn to the $ESTATE_CHURCH$ instead.

###Available if:
<li>has estate estate_church</li><li>None of the following:</li><ul><li>All of the following:</li><ul><li>religion is hinduism</li><li>has estate estate_brahmins</li></ul></ul>

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate loyalty has estate is estate church, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "church_minister" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_MINISTER_CHURCH</li><li>influence = 15</li><li>duration = 3650</li></ul></ul>

___
##Let us turn to the Brahmins instead.

###Available if:
<li>has estate estate_brahmins</li><li>religion is hinduism</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate brahmins, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "church_minister" for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_brahmins</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_brahmins</li><li>desc = EST_VAL_MINISTER_CHURCH</li><li>influence = 15</li><li>duration = 3650</li></ul></ul>

___
##Let us turn to the Brahmins instead.

###Available if:
<li>has estate estate_brahmins</li><li>religion group is muslim</li>

###AI weighting:
AI weights this option at 25
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 50; and does not have estate loyalty has estate is estate brahmins, and estate loyalty has loyalty is 60; and does not have estate influence has estate is estate brahmins, and estate influence has influence is 60


###Efects:<ul><li>country gets the modifier "dhimmi_minister" for 10 years</li><li>add estate influence modifier:</li><ul><li>estate = estate_brahmins</li><li>desc = EST_VAL_MINISTER_DHIMMI</li><li>influence = 15</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -20</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_brahmins</li><li>loyalty = 15</li></ul></ul>
