#Information
 - Title: Goblin Majority Purged
 - ID: racial_pop_events_goblin.20
#Description
Goblin Majority Purged
#Mean Time to Happen:
Base time = 5475 days
 - Multiplied by 0.5 if has country modifier is racial focus goblin
 - Multiplied by 0.1 if has calc true if has all owned province has goblin majority trigger is yes, and all owned province has culture is goblin is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has goblin majority trigger is yes, and all owned province has culture is goblin is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has goblin majority trigger is yes, and all owned province has culture is goblin is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has country flag is [mithradhum_purging](../flags/mithradhum_purging.md)
 - Multiplied by 0.5 if has always

#Options

___
##Finally got rid of them!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>add devastation = 50</li><li>change culture = ROOT</li><li>change religion = ROOT</li><li>random list:</li><ul><li>1:</li><ul><li>add base tax = -2</li></ul><li>1:</li><ul><li>add base production = -2</li></ul><li>1:</li><ul><li>add base manpower = -2</li></ul></ul><li>add permanent province modifier:</li><ul><li>name = purge_unrest_modifier</li><li>duration = 9125</li></ul><li>hidden effect:</li><ul><li>remove province modifier = goblin_majority_oppressed</li><li>remove province modifier = goblin_majority_coexisting</li><li>remove province modifier = goblin_majority_integrated</li></ul></ul><li>large decrease of goblin tolerance effect = yes</li></ul>
