#Information
 - Title: Diplomatic Move
 - ID: 5024
#Description
Diplomatic Move
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has advisor is diplomat
 - Multiplied by 2.0 if is lucky

#Options

___
##Appoint new diplomats.

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>add dip power = 30</li></ul>

___
##Improve relations with neighboring states.

###Available if:
<li>any known country:</li><ul><li>is neighbor of is this nation</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>add dip power = 10</li><li>If random country is neighbor of is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_improved_relations</li></ul></ul></ul>

___
##Nothing is really beyond my control!

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add dip power = 50</li></ul>

___
##We are a diplomatic superpower!

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul><li>any known country:</li><ul><li>is neighbor of is this nation</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add dip power = 25</li><li>If every country is neighbor of is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_good_relations</li></ul></ul></ul>
