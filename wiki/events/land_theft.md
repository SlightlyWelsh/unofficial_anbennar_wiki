#Information
 - Title: Land Theft
 - ID: church_estate_events.8
#Description
Land Theft
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Side with the $ESTATE_CHURCH$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>scaled estate church land share effect = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_CHURCH_PROPERTIES_DEFENDED</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_CHURCH_PROPERTIES_DEFENDED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Side with the $ESTATE_NOBLES$.

###Available if:
<li>has estate estate_nobles</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>scaled estate nobles land share effect = yes</li><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>scaled estate eunuchs land share effect = yes</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_LAND_THEFT</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_LAND_THEFT</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>

___
##Favor neither party.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>If does not have estate is estate nobles; and  has estate is estate eunuchs:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -15</li></ul></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_LAND_THEFT</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_LAND_THEFT</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
