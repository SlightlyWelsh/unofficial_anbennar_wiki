#Information
 - Title: Goblin Squatters Found!
 - ID: blorc.103
#Description
Goblin Squatters Found!
#Options

___
##Kill them all!

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:blorc squatter event target:</li><ul><li>remove province modifier = goblin_minority_oppressed_small</li><li>remove province modifier = goblin_minority_oppressed_large</li><li>remove province modifier = goblin_minority_coexisting_small</li><li>remove province modifier = goblin_minority_coexisting_large</li><li>remove province modifier = goblin_minority_integrated_small</li><li>remove province modifier = goblin_minority_integrated_large</li><li>spawn rebels:</li><ul><li>type = cave_goblin_rebel</li><li>culture = cave_goblin</li><li>size = 2</li></ul></ul><li>add prestige = 5</li><li>large decrease of goblin tolerance effect = yes</li></ul>

___
##They will work in the capital!

###Available if:
<li>medium tolerance goblin race trigger is yes</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>capital scope:</li><ul><li>If has event target:blorc squatter event target has province modifier is goblin minority oppressed small:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add goblin minority size effect = yes</li><li>add unrest = 2</li></ul><li>If has event target:blorc squatter event target has province modifier is goblin minority oppressed large:</li><ul><li>add base tax = 2</li><li>add base production = 2</li><li>add goblin minority size effect = yes</li><li>add unrest = 4</li></ul><li>If has event target:blorc squatter event target has province modifier is goblin minority coexisting small:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add goblin minority size effect = yes</li></ul><li>If has event target:blorc squatter event target has province modifier is goblin minority coexisting large:</li><ul><li>add base tax = 2</li><li>add base production = 2</li><li>add goblin minority size effect = yes</li></ul><li>If has event target:blorc squatter event target has province modifier is goblin minority integrated small:</li><ul><li>add base tax = 2</li><li>add base production = 2</li><li>add goblin minority size effect = yes</li></ul><li>If has event target:blorc squatter event target has province modifier is goblin minority integrated large:</li><ul><li>add base tax = 3</li><li>add base production = 3</li><li>add goblin minority size effect = yes</li></ul></ul><li>event target:blorc squatter event target:</li><ul><li>remove province modifier = goblin_minority_oppressed_small</li><li>remove province modifier = goblin_minority_oppressed_large</li><li>remove province modifier = goblin_minority_coexisting_small</li><li>remove province modifier = goblin_minority_coexisting_large</li><li>remove province modifier = goblin_minority_integrated_small</li><li>remove province modifier = goblin_minority_integrated_large</li></ul><li>small decrease of goblin tolerance effect = yes</li></ul>

___
##They can join the plunderers.

###Available if:
<li>high tolerance goblin race trigger is yes</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>event target:blorc squatter event target:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li><li>add goblin minority size effect = yes</li></ul><li>large increase of goblin tolerance effect = yes</li></ul>
