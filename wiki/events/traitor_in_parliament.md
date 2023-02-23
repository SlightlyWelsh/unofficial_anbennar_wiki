#Information
 - Title: Traitor in Parliament
 - ID: random_event.3
#Description
Traitor in Parliament
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Execute him

###Available if:
<li>stability is -2</li>

###AI weighting:
AI weights this option at 5
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>add stability = -1</li></ul>

___
##Try and reduce his involvement

###AI weighting:
AI weights this option at 5
 - Multiplied by 0.5 if has war exhaustion is 8


###Efects:<ul><li>add war exhaustion = 2</li></ul>

___
##The personal agents of [Root.Monarch.GetTitle] will handle this.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is secretive</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add dip power = -25</li></ul>
