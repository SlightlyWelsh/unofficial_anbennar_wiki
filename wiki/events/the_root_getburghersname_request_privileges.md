#Information
 - Title: The [Root.GetBurghersName] Request Privileges
 - ID: 5082
#Description
The [Root.GetBurghersName] Request Privileges
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.25 if does not have government attribute is is merchant republic
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has stability is 3

#Options

___
##Grant them privileges.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.25 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add adm power = -50</li><li>add estate burghers loyalty effect = yes</li><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##Deny them privileges.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.25 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add dip power = -50</li><li>reduce estate burghers loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Attempt to open up new opportunities without upsetting old elites.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul><li>ruler has personality ancestor:</li><ul><li>key is silver_tongue</li></ul></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = -20</li><li>add dip power = -20</li><li>add estate burghers loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>
