#Information
 - Title: Orcish Majority Expelled
 - ID: racial_pop_events_orcish.18
#Description
Orcish Majority Expelled
#Mean Time to Happen:
Base time = 2737 days
 - Multiplied by 0.5 if has country modifier is racial focus orcish
 - Multiplied by 0.1 if has calc true if has all owned province has orcish majority trigger is yes, and all owned province has culture is orcish is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has orcish majority trigger is yes, and all owned province has culture is orcish is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has orcish majority trigger is yes, and all owned province has culture is orcish is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has always

#Options

___
##Off you go!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>change culture = ROOT</li><li>change religion = ROOT</li><li>add devastation = 30</li><li>random list:</li><ul><li>1:</li><ul><li>add base tax = -1</li></ul><li>1:</li><ul><li>add base production = -1</li></ul><li>1:</li><ul><li>add base manpower = -1</li></ul></ul><li>add permanent province modifier:</li><ul><li>name = expulsion_unrest_modifier</li><li>duration = 18250</li></ul></ul><li>If does not have low tolerance orcish race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Orcish Refugees From [From.GetName]](../events/orcish_refugees_from_from_getname.md) happens</li></ul></ul><li>medium decrease of orcish tolerance effect = yes</li></ul>
