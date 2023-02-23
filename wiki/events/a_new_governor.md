#Information
 - Title: A New Governor
 - ID: colonial_nation.183
#Description
A New Governor
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We should take their advice.

###Efects:<ul><li>exile ruler as:</li><ul><li>name = colonial_exiled_governor</li></ul><li>define ruler:</li><ul><li>culture = ROOT</li><li>change adm = 4</li><li>change dip = 3</li><li>change mil = 3</li></ul><li>random:</li><ul><li>chance = 50</li><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 1</li></ul></ul></ul></ul>

___
##[Root.Monarch.GetName] can still rule.

###Available if:
<li>None of the following:</li><ul><li>has ruler modifier colonial_corrupted_governor</li></ul>

###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul><li>random:</li><ul><li>chance = 50</li><li>random owned province:</li><ul><li>spawn rebels:</li><ul><li>type = nationalist_rebels</li><li>size = 1</li></ul></ul></ul></ul>
