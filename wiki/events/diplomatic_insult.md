#Information
 - Title: Diplomatic Insult
 - ID: 5056
#Description
Diplomatic Insult
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.66 if has dip is 5

#Options

___
##We won't forget this.

###AI weighting:
AI weights this option at 55


###Efects:<ul><li>event target:insulted party:</li><ul><li>reverse add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_insult</li><li>months = 12</li></ul></ul></ul>

___
##Try to ease the tension.

###AI weighting:
AI weights this option at 45


###Efects:<ul><li>If every neighbor country is not at war:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_eased_tension</li></ul></ul></ul>

___
##Let our [Root.Monarch.GetTitle] personally handle this.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is silver_tongue</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add estate burghers loyalty effect = yes</li><li>add prestige = 5</li><li>If every neighbor country is not at war:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_more_eased_tension</li></ul></ul></ul>
