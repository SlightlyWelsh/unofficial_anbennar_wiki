#Information
 - Title: Centaurs Flee From Country
 - ID: racial_pop_events_centaur.21
#Description
Centaurs Flee From Country
#Mean Time to Happen:
Base time = 1825 days
 - Multiplied by 0.5 if has country modifier is racial focus centaur
 - Multiplied by 0.1 if has calc true if has all owned province has centaur minority trigger is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has centaur minority trigger is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has centaur minority trigger is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has always

#Options

___
##Good Riddance!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove centaur minority size effect = yes</li><li>add devastation = 10</li></ul><li>If does not have low tolerance centaur race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Centaur Refugees From [From.GetName]](../events/centaur_refugees_from_from_getname.md) happens</li></ul></ul><li>medium decrease of centaur tolerance effect = yes</li></ul>
