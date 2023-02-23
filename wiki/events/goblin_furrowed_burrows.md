#Information
 - Title: Goblin Furrowed Burrows
 - ID: aw_goblins.200
#Description
Goblin Furrowed Burrows
#Options

___
##The damage was not as bad as reported

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>REB:</li><ul><li>check variable:</li><ul><li>which is goblin_tax</li><li>value is at least 1</li></ul></ul></ul><li>NOT:</li><ul><li>base tax is at least 2</li></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add devastation = 5</li></ul>

___
##We will have to lower our taxes in [Root.GetName].

###Available if:
<li>REB:</li><ul><li>check variable:</li><ul><li>which is goblin_tax</li><li>value is at least 1</li></ul></ul><li>base tax is at least 2</li>

###AI weighting:
AI weights this option at 80


###Efects:<ul><li>add base tax = -1</li></ul>

___
##Tax them just the same!

###Available if:
<li>None of the following:</li><ul><li>REB:</li><ul><li>check variable:</li><ul><li>which is goblin_tax</li><li>value is at least 1</li></ul></ul></ul><li>NOT:</li><ul><li>devastation is at least 71</li></ul><li>base tax is at least 2</li>

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>add devastation = 30</li></ul>
