#Information
 - Title: Human Minority Expelled
 - ID: racial_pop_events_human.17
#Description
Human Minority Expelled
#Mean Time to Happen:
Base time = 1825 days
 - Multiplied by 0.5 if has country modifier is racial focus human
 - Multiplied by 0.1 if has calc true if has all owned province has human minority trigger is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has human minority trigger is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has human minority trigger is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has always

#Options

___
##Good Riddance!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove human minority size effect = yes</li><li>add devastation = 10</li></ul><li>If does not have low tolerance human race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Human Refugees From [From.GetName]](../events/human_refugees_from_from_getname.md) happens</li></ul></ul><li>medium decrease of human tolerance effect = yes</li></ul>

___
##They sure left a lot behind...

###Available if:
<li>ruler has personality is greedy_personality</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>event target:racial pop province origin:</li><ul><li>remove human minority size effect = yes</li><li>add devastation = 10</li></ul><li>If does not have low tolerance human race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Human Refugees From [From.GetName]](../events/human_refugees_from_from_getname.md) happens</li></ul></ul><li>If has event target:racial pop province origin has development is 20:</li><ul><li>add treasury = 50</li></ul><li>else:</li><ul><li>add treasury = 10</li></ul><li>medium decrease of human tolerance effect = yes</li></ul>
