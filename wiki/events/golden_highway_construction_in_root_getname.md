#Information
 - Title: Golden Highway Construction in [Root.GetName]
 - ID: golden_highway.1
#Description
Golden Highway Construction in [Root.GetName]
#Mean Time to Happen:
Base time = 1500 days
 - Multiplied by 0.75 if has owner has full idea group is economic ideas
 - Multiplied by 0.8 if has owner has full idea group is administrative ideas
 - Multiplied by 0.9 if has development is 10
 - Multiplied by 0.9 if has development is 15
 - Multiplied by 0.8 if has development is 20
 - Multiplied by 0.7 if has development is 30
 - Multiplied by 0.7 if is prosperous
 - Multiplied by 2 if has devastation is 1

#Options

___
##A splendid advancement!

###Available if:
<li>None of the following:</li><ul><li>has province modifier golden_highway</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>owner:</li><ul><li>add treasury = -50</li></ul></ul>

___
##Pause it for now, we don't have the funds.

###Available if:
<li>None of the following:</li><ul><li>has province modifier golden_highway</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>remove province modifier = golden_highway_under_construction</li><li>add permanent province modifier:</li><ul><li>name = golden_highway_construction_stalled</li><li>duration = -1</li></ul><li>owner:</li><ul><li>add prestige = -5</li></ul></ul>

___
##It's complete!

###Available if:
<li>has province modifier golden_highway</li>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>owner:</li><ul><li>add prestige = 2</li></ul></ul>
