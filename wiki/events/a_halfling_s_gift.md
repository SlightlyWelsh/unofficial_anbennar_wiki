#Information
 - Title: A Halfling's Gift
 - ID: halfling_tolerance_events.3
#Description
A Halfling's Gift
#Options

___
##Accept their gift

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>reduce legitimacy small effect = yes</li><li>add prestige = -2</li><li>add years of income = 0.02</li></ul>

___
##This is indeed suspicious...

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has event target:gift halfling province has unrest is 1
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>small decrease of halfling tolerance effect = yes</li><li>event target:gift halfling province:</li><ul><li>add province modifier:</li><ul><li>name = halfling_angry_over_not_accepting_gift</li><li>duration = 1460</li></ul></ul></ul>

___
##We should reward them for their generosity!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>add dip power = 10</li><li>add years of income = -0.025</li><li>small increase of halfling tolerance effect = yes</li><li>event target:gift halfling province:</li><ul><li>add unrest = -1</li></ul></ul>

___
##...this has to be a trap! Guards get them!

###Available if:
<li>ruler has personality is craven_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.8 if has event target:gift halfling province has unrest is 1
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>add mil power = -10</li><li>small decrease of halfling tolerance effect = yes</li><li>event target:gift halfling province:</li><ul><li>add province modifier:</li><ul><li>name = halfling_punishment_of_local_traitors</li><li>duration = 730</li></ul></ul></ul>
