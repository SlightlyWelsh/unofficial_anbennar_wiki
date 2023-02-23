#Information
 - Title: Kobold Hoard Found by Mob
 - ID: kobold_tolerance_events.7
#Description
Kobold Hoard Found by Mob
#Options

___
##Anyone, regardless of race, has a right to their own belongings. Disperse the crowd

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to decrease tolerance kobold is yes


###Efects:<ul><li>small increase of kobold tolerance effect = yes</li><li>event target:kobold personal hoard province:</li><ul><li>add unrest = 5</li></ul></ul>

___
##And what do you want me to do about it?

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has wants to maintain tolerance kobold is yes


###Efects:<ul><li>add prestige = -10</li></ul>

___
##'Redistribute' the wealth to the people - after skimming a little off the top, of course

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has ruler has personality is greedy personality
 - Multiplied by 0.1 if has wants to increase tolerance kobold is yes


###Efects:<ul><li>medium decrease of kobold tolerance effect = yes</li><li>add corruption = 0.5</li><li>add years of income = 0.3</li></ul>

___
##The poor thing - let's humour it

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is kind_hearted_personality</li><li>ruler has personality  is tolerant_personality</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>medium increase of kobold tolerance effect = yes</li><li>add years of income = -0.3</li><li>If every owned province has kobold minority trigger is yes:</li><ul><li>add unrest = -3</li></ul></ul>
