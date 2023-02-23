#Information
 - Title: Grant Export Licenses
 - ID: 5072
#Description
Grant Export Licenses
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has trader is 2
 - Multiplied by 2.0 if is lucky
 - Multiplied by 0.66 if does not have advisor is trader

#Options

___
##Grant privileges.

###AI weighting:
AI weights this option at 55
 - Multiplied by 1.5 if has legitimacy or horde unity is 90
 - Multiplied by 0.5 if has reform is steppe horde, and does not have legitimacy or horde unity is 50
 - Multiplied by 0.5 if has government is republic, and does not have republican tradition is 60
 - Multiplied by 0.25 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>event target:neighbour country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_granted_privileges</li></ul></ul><li>add legitimacy = -10</li><li>add horde unity = -10</li><li>add republican tradition = -5</li><li>add devotion = -5</li><li>reduce mandate effect = yes</li><li>country gets the modifier "tax_income_boost" for 20 years</li><li>add estate nobles loyalty effect = yes</li><li>reduce estate burghers loyalty effect = yes</li></ul>

___
##Privileges have to be earned.

###AI weighting:
AI weights this option at 45
 - Multiplied by 1.5 if has government is monarchy, and does not have legitimacy or horde unity is 60
 - Multiplied by 0.25 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>reduce estate nobles loyalty effect = yes</li><li>add estate burghers loyalty effect = yes</li><li>add legitimacy = 10</li><li>add devotion = 5</li><li>add horde unity = 5</li><li>add republican tradition = 5</li><li>add mandate effect = yes</li><li>event target:neighbour country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_not_grant_privileges</li></ul></ul></ul>
