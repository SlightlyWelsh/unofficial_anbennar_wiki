#Information
 - Title: Cities Demand Old Rights
 - ID: 5076
#Description
Cities Demand Old Rights
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has revolt percentage is 0.1
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has stability is 3

#Options

___
##Deny them their old rights!

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have stability is 1
 - Multiplied by 0 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>reduce estate burghers loyalty effect = yes</li><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Accept their demands.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if has government is monarchy, and does not have legitimacy or horde unity is 70
 - Multiplied by 0.5 if has government is republic, and does not have republican tradition is 70
 - Multiplied by 0.5 if has government is theocracy, and does not have prestige is 25


###Efects:<ul><li>add estate burghers loyalty effect = yes</li><li>If has completed all reforms trigger is yes:</li><ul><li>add legitimacy = -20</li><li>add horde unity = -20</li><li>add republican tradition = -10</li><li>add devotion = -10</li></ul><li>else:</li><ul><li>reduce reform progress small effect = yes</li></ul><li>reduce mandate effect = yes</li></ul>

___
##The [Root.Monarch.GetTitle] shall make a new list of rights.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is lawgiver</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = -25</li></ul>
