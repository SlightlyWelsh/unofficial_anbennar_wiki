#Information
 - Title: Assassination of Noble
 - ID: 5065
#Description
Assassination of Noble
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has aristocracy ideas is 5
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has advisor is statesman

#Options

___
##Let them solve it among themselves.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have legitimacy or horde unity is 70


###Efects:<ul><li>add legitimacy = -15</li><li>add horde unity = -15</li><li>reduce mandate effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Take control of the situation.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add adm power = -50</li><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##The [Root.Monarch.GetTitle] can intimidate them into keeping their peace.

###Available if:
<li>ruler has personality is cruel_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add legitimacy = 5</li><li>add horde unity = 5</li><li>add mandate effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>

___
##Our [Root.Monarch.GetTitle] must solve the conflict.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is just</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add adm power = -25</li><li>add estate nobles loyalty effect = yes</li></ul>
