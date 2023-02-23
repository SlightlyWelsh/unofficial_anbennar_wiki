#Information
 - Title: The Hidden Struggle
 - ID: flavor_arverynn.20
#Description
The Hidden Struggle
#Options

___
##That statue of [g35_revolt_leader.Monarch.GetName] in the noble district? I'm afraid we'll have to tear it down…

###Available if:
<li>has saved event target g35_revolt_leader</li>

###AI weighting:
AI weights this option at 1
 - Multiplied by 3 if does not have calc true if has all subject country is subject of type is ynnic iosahar, and all subject country has liberty desire is 50; and calc true if has amount is 3


###Efects:<ul><li>event target:g35 revolt leader:</li><ul><li>add liberty desire = 10</li><li>add prestige = -10</li></ul><li>random:</li><ul><li>chance = 50</li><li>custom tooltip = G35_nobles_revolt_tt</li><li>hidden effect:</li><ul><li>the event [Disloyal Iosahar Declare War](../events/disloyal_iosahar_declare_war.md) happens</li></ul></ul></ul>

___
##Send arms and troops to our subjects' subjects

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>add years of income = -0.5</li><li>If every subject country is subject of type is ynnic iosahar:</li><ul><li>country gets the modifier G35_rebellious_barons for 25 years</li></ul></ul>

___
##Baron Armynn of Poelnebo, my good friend! I have great plans for you…

###Available if:
<li>has saved event target g35_claimant_province</li>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>event target:g35 claimant province:</li><ul><li>add core = ROOT</li></ul><li>add legitimacy = -5</li></ul>

___
##Our vassals have been exceedingly loyal, let us reward them

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>add years of income = -0.5</li><li>If every subject country is subject of type is ynnic iosahar:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = 5</li><li>mutual = yes</li></ul></ul></ul>
