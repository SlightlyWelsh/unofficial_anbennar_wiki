#Information
 - Title: Nobles Demand Old Rights
 - ID: 5075
#Description
Nobles Demand Old Rights
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have adm is 1
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has adm is 5

#Options

___
##Accept demands

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has completed all reforms trigger is yes:</li><ul><li>country gets the modifier "old_rights_granted_to_nobility" for 10 years</li></ul><li>else:</li><ul><li>reduce reform progress small effect = yes</li></ul><li>add estate nobles loyalty effect = yes</li></ul>

___
##Reject demands

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have stability is 1
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul></ul>

___
##The [Root.Monarch.GetTitle] shall make a new list of rights.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is lawgiver</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = -25</li></ul>
