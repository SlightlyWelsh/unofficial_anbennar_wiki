#Information
 - Title: Cessation of Church Functions
 - ID: 5066
#Description
Cessation of Church Functions
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has num of loans is 2, and is bankrupt
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has advisor is treasurer

#Options

___
##Accept.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.25 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>add years of income = 0.50</li><li>country gets the modifier "church_functions" for 20 years</li><li>reduce estate church loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li><li>If has estate is estate nobles, and  has estate is estate church:</li><ul><li>change estate land share:</li><ul><li>estate = estate_church</li><li>share = -5</li></ul><li>change estate land share:</li><ul><li>estate = estate_nobles</li><li>share = 5</li></ul></ul></ul>

___
##Decline.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.25 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>add stability or adm power = yes</li><li>add estate church loyalty effect = yes</li><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##We have been undercharging them.

###Available if:
<li>ruler has personality is sinner_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add years of income = 0.65</li><li>reduce estate church loyalty effect = yes</li><li>add estate nobles loyalty effect = yes</li></ul>
