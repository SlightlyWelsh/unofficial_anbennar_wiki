#Information
 - Title: The Fate of the Border
 - ID: reveria.10
#Description
The Fate of the Border
#Options

___
##Cede the provinces and move all non-halflings to our capital

###Available if:
<li>A05:</li><ul><li>owns core province 144</li><li>owns core province  141</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>141:</li><ul><li>cede province = A97</li></ul><li>144:</li><ul><li>cede province = A97</li></ul><li>add trust:</li><ul><li>who = A97</li><li>value = 50</li><li>mutual = yes</li></ul><li>add historical friend = A97</li><li>A97:</li><ul><li>add historical friend = A05</li></ul><li>capital scope:</li><ul><li>add base tax = 3</li><li>add base production = 3</li><li>add base manpower = 3</li></ul><li>A97:</li><ul><li>the event [Reverian Diplomacy](../events/reverian_diplomacy.md) happens</li><li>144:</li><ul><li>add core = A97</li></ul><li>141:</li><ul><li>add core = A97</li></ul><li>144:</li><ul><li>remove core = A05</li></ul><li>141:</li><ul><li>remove core = A05</li></ul></ul></ul>

___
##Let the halflings leave, compensate them and the state

###Available if:
<li>A05:</li><ul><li>owns core province 144</li><li>owns core province  141</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add treasury = -300</li><li>A97:</li><ul><li>add treasury = 200</li></ul><li>141:</li><ul><li>change culture = reverian</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>144:</li><ul><li>change culture = reverian</li><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>A97:</li><ul><li>capital scope:</li><ul><li>add base tax = 2</li><li>add base production = 2</li><li>add base manpower = 2</li></ul></ul><li>add historical friend = A97</li><li>A97:</li><ul><li>add historical friend = A05</li></ul><li>add trust:</li><ul><li>who = A97</li><li>value = 10</li><li>mutual = yes</li></ul><li>A97:</li><ul><li>the event [Reverian Diplomacy](../events/reverian_diplomacy.md) happens</li></ul></ul>

___
##If only we even held the provinces of Manerd and Turnwell

###Available if:
<li>Any of the following:</li><ul><li>None of the following:</li><ul><li>owns core province 144</li></ul><li>NOT:</li><ul><li>owns core province 141</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>add historical friend = A97</li><li>A97:</li><ul><li>add historical friend = A05</li></ul></ul>
