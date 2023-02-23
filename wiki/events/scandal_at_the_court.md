#Information
 - Title: Scandal at the Court
 - ID: 5017
#Description
Scandal at the Court
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.5 if has ruler has personality ancestor has key is careful
 - Multiplied by 1.25 if has ruler has personality is drunkard personality, and has ruler has personality is babbling buffoon personality

#Options

___
##The House of [Root.Monarch.Dynasty.GetName] is shaken!

###Available if:
<li>Any of the following:</li><ul><li>has country flag [court_scandal_1](../flags/court_scandal_1.md)</li><li>has country flag  court_scandal_4</li><li>has country flag   court_scandal_5</li></ul>

###AI weighting:
AI weights this option at 45
 - Multiplied by 1.5 if has stability is 1
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Take the blame and move on.

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has country flag [court_scandal_1](../flags/court_scandal_1.md)</li><li>has country flag  court_scandal_4</li><li>has country flag   court_scandal_5</li></ul></ul>

###AI weighting:
AI weights this option at 45
 - Multiplied by 1.5 if has stability is 1
 - Multiplied by 0.5 if does not have stability is 1


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul></ul>

___
##Some gifts will help the rumors die down.

###Available if:
<li>Any of the following:</li><ul><li>has country flag [court_scandal_1](../flags/court_scandal_1.md)</li><li>has country flag  court_scandal_4</li><li>has country flag   court_scandal_5</li></ul>

###AI weighting:
AI weights this option at 55
 - Multiplied by 1.5 if does not have stability is 1; and  has years of income is 0.4


###Efects:<ul><li>add corruption = 0.5</li><li>reduce meritocracy effect = yes</li><li>add years of income = -0.2</li></ul>

___
##Bribe an advisor to take the blame.

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has country flag [court_scandal_1](../flags/court_scandal_1.md)</li><li>has country flag  court_scandal_4</li><li>has country flag   court_scandal_5</li></ul></ul>

###AI weighting:
AI weights this option at 55
 - Multiplied by 1.5 if does not have stability is 1; and  has years of income is 0.4


###Efects:<ul><li>add corruption = 0.5</li><li>reduce meritocracy effect = yes</li><li>add years of income = -0.2</li></ul>

___
##Don't Panic!

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is calm</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = -10</li></ul>

___
##Attempt to lessen the impact.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is silver_tongue</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add dip power = -25</li></ul>

___
##Is anyone really surprised?

###Available if:
<li>ruler has personality is babbling_buffoon_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = -5</li></ul>
