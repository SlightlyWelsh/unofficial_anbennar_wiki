This page has the same name as others. For full listing see bottom of [the base page](the_elder_pact.md).

#Information
 - Title: The Elder Pact
 - ID: long_lived_emperor.2
#Description
The Elder Pact
#Options

___
##We shall give up the crown.

###Available if:
<li>None of the following:</li><ul><li>hre elector majority:</li><ul><li>Country is this nation</li></ul></ul>

###AI weighting:
AI weights this option at 9


###Efects:<ul><li>add prestige = 15</li><li>add legitimacy = 20</li><li>set emperor = no</li></ul>

___
##Come and take it!

###Available if:
<li>None of the following:</li><ul><li>hre elector majority:</li><ul><li>Country is this nation</li></ul></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>reduce stability or adm power = yes</li><li>add imperial influence = -10</li><li>add ruler modifier:</li><ul><li>name = elder_pact_broken</li><li>duration = -1</li></ul><li>custom tooltip = broke_elder_pact_tooltip</li><li>hidden effect:</li><ul><li>If every known country is part of hre:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = broke_elder_pact</li></ul></ul><li>event target:elector target:</li><ul><li>the event [Enforce the Elder Pact](../events/enforce_the_elder_pact.md) happens</li></ul></ul><li>custom tooltip = war_of_the_throne_tooltip</li><li>hidden effect:</li><ul><li>clr ruler flag [long_lived_emperor](../flags/long_lived_emperor.md)</li></ul></ul>

___
##The electors are still voting for me.

###Available if:
<li>hre elector majority:</li><ul><li>Country is this nation</li></ul>

###AI weighting:
AI weights this option at 9000


###Efects:<ul><li>highlight = yes</li><li>add imperial influence = 10</li><li>hidden effect:</li><ul><li>set ruler flag [long_lived_emperor](../flags/long_lived_emperor.md)</li></ul></ul>
