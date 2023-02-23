#Information
 - Title: Political Crisis
 - ID: 5054
#Description
Political Crisis
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has revolt percentage is 0.1
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has advisor is statesman

#Options

___
##Given time, a solution will present itself.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Reputation isn't everything.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0.5 if has government is republic, and does not have republican tradition is 80
 - Multiplied by 0.5 if has government is monarchy, and does not have legitimacy or horde unity is 80


###Efects:<ul><li>add republican tradition = -10</li><li>add horde unity = -25</li><li>add legitimacy = -25</li><li>reduce mandate large effect = yes</li></ul>

___
##Let the [Root.Monarch.GetTitle] attempt to soften the impact.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is righteous</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add legitimacy = -10</li><li>add republican tradition = -5</li><li>add horde unity = -10</li><li>reduce mandate effect = yes</li></ul>

___
##Allow our [Root.Monarch.GetTitle] to see if there is a solution to the benefit of everyone.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is just</li></ul>

###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add prestige = 5</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add republican tradition = -10</li><li>add horde unity = -25</li><li>add legitimacy = -25</li><li>reduce mandate large effect = yes</li></ul>

###Efects:<ul><li>highlight = yes</li></ul>
