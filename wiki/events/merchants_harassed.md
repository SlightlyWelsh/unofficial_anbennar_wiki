#Information
 - Title: Merchants harassed
 - ID: 5088
#Description
Merchants harassed
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if has idea is merchant adventures, and  has government attribute is is merchant republic
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has advisor is trader

#Options

___
##Escalate complaint.

###AI weighting:
AI weights this option at 55


###Efects:<ul><li>event target:harassing merchants nation:</li><ul><li>reverse add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_insult</li><li>months = 12</li></ul></ul><li>add estate burghers loyalty effect = yes</li></ul>

___
##Seek a diplomatic solution.

###AI weighting:
AI weights this option at 45
 - Multiplied by 0 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>event target:harassing merchants nation:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_diplomatic_solution</li></ul></ul><li>reduce estate burghers loyalty effect = yes</li></ul>

___
##Use this opportunity to reconcile with our neighbors.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul>

###Efects:<ul><li>highlight = yes</li><li>If every country is neighbor of is ROOT, and does not have opinion has who is ROOT, and has opinion has value is 50:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_diplomatic_solution</li></ul></ul><li>reduce estate burghers loyalty effect = yes</li></ul>
