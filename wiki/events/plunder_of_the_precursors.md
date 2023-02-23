#Information
 - Title: Plunder of the Precursors
 - ID: flavor_malacnar.112
#Description
Plunder of the Precursors
#Options

___
##Destroy them!

###AI weighting:
AI weights this option at 1
 - Multiplied by 10 if has ruler has personality is zealot personality


###Efects:<ul><li>event target:g32 plunder province:</li><ul><li>add base tax = -1</li><li>add base production = -2</li><li>add devastation = 80</li><li>set from saved trade goods = yes</li></ul><li>If has ynn cannorian thought is yes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul></ul><li>else:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul></ul></ul>

___
##Why shouldn't we keep them?

###AI weighting:
AI weights this option at 5
 - Multiplied by 4 if has ynn cannorian thought is yes


###Efects:<ul><li>goto = 2808</li><li>event target:g32 plunder province:</li><ul><li>add base tax = -1</li><li>add base production = -2</li><li>add devastation = 80</li><li>set from saved trade goods = yes</li></ul><li>2808:</li><ul><li>change trade goods = precursor_relics</li><li>add base production = 2</li></ul><li>If has ynn cannorian thought is yes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -5</li></ul></ul><li>else:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul></ul></ul>
