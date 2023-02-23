#Information
 - Title: Halfling Crime Runs Rampant
 - ID: halfling_tolerance_events.5
#Description
Halfling Crime Runs Rampant
#Options

___
##Crime is crime

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>small increase of halfling tolerance effect = yes</li><li>event target:high halfling crime province:</li><ul><li>add province modifier:</li><ul><li>name = high_halfling_crime</li><li>duration = 730</li></ul></ul></ul>

___
##Double the guards!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>add mil power = -20</li><li>small decrease of halfling tolerance effect = yes</li><li>event target:high halfling crime province:</li><ul><li>add province modifier:</li><ul><li>name = high_halfling_crime</li><li>duration = 730</li></ul></ul></ul>

___
##All halflings are thieves! Arrest them all!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>large decrease of halfling tolerance effect = yes</li><li>event target:high halfling crime province:</li><ul><li>add province modifier:</li><ul><li>name = high_halfling_crime</li><li>duration = 365</li></ul></ul></ul>

___
##Make a deal with the crime syndicates

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is greedy_personality</li><li>ruler has personality  is embezzler_personality</li></ul>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>medium increase of halfling tolerance effect = yes</li><li>event target:high halfling crime province:</li><ul><li>add province modifier:</li><ul><li>name = high_halfling_crime</li><li>duration = 1825</li></ul></ul><li>add years of income = 0.3</li></ul>
