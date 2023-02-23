#Information
 - Title: Local Noble's Power Grows
 - ID: 884
#Description
Local Noble's Power Grows
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Ignore him.

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>add prestige = -10</li><li>event target:local noble province:</li><ul><li>add province modifier:</li><ul><li>name = "powerful_noble"</li><li>duration = 240</li></ul><li>add local autonomy = 20</li></ul><li>add estate nobles loyalty effect = yes</li></ul>

___
##Outwit him at court.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.5 if does not have stability is 1
 - Multiplied by 0.25 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add prestige = 5</li><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Order his arrest.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add prestige = 5</li><li>event target:local noble province:</li><ul><li>spawn large scaled rebels:</li><ul><li>type = pretender_rebels</li><li>saved name = local_noble_name</li></ul></ul><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##Curtail his influence through legislation.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is lawgiver</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>add adm power = -50</li></ul>

___
##Negotiate with the Noble.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>add dip power = -50</li></ul>

___
##Intimidate the Noble.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is cruel_personality</li><li>ruler has personality  is malevolent_personality</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>add mil power = -50</li></ul>
