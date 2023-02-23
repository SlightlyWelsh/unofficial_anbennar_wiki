#Information
 - Title: Goblins Flee From Country
 - ID: racial_pop_events_goblin.21
#Description
Goblins Flee From Country
#Mean Time to Happen:
Base time = 1825 days
 - Multiplied by 0.5 if has country modifier is racial focus goblin
 - Multiplied by 0.1 if has calc true if has all owned province has goblin minority trigger is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has goblin minority trigger is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has goblin minority trigger is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has always

#Options

___
##Good Riddance!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove goblin minority size effect = yes</li><li>add devastation = 10</li></ul><li>If does not have low tolerance goblin race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Goblin Refugees From [From.GetName]](../events/goblin_refugees_from_from_getname.md) happens</li></ul></ul><li>medium decrease of goblin tolerance effect = yes</li></ul>
