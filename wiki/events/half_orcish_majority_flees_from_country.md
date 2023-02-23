#Information
 - Title: Half-orcish Majority Flees From Country
 - ID: racial_pop_events_half_orcish.22
#Description
Half-orcish Majority Flees From Country
#Mean Time to Happen:
Base time = 2555 days
 - Multiplied by 0.5 if has country modifier is racial focus half orcish
 - Multiplied by 0.1 if has calc true if has all owned province has half orcish majority trigger is yes, and all owned province has culture is half orcish is yes; and calc true if has amount is 100
 - Multiplied by 0.5 if has calc true if has all owned province has half orcish majority trigger is yes, and all owned province has culture is half orcish is yes; and calc true if has amount is 50
 - Multiplied by 0.75 if has calc true if has all owned province has half orcish majority trigger is yes, and all owned province has culture is half orcish is yes; and calc true if has amount is 25
 - Multiplied by 0.5 if has always

#Options

___
##Good Riddance!

###Available if:


###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>add devastation = 30</li><li>change culture = ROOT</li><li>change religion = ROOT</li><li>random list:</li><ul><li>1:</li><ul><li>add base tax = -1</li></ul><li>1:</li><ul><li>add base production = -1</li></ul><li>1:</li><ul><li>add base manpower = -1</li></ul></ul><li>hidden effect:</li><ul><li>remove province modifier = half_orcish_majority_oppressed</li><li>remove province modifier = half_orcish_majority_coexisting</li><li>remove province modifier = half_orcish_majority_integrated</li></ul></ul><li>If does not have low tolerance half orcish race trigger is yes:</li><ul><li>event target:racial pop migration country:</li><ul><li>the event [Half-orcish Refugees From [From.GetName]](../events/half_orcish_refugees_from_from_getname.md) happens</li></ul></ul><li>medium decrease of half orcish tolerance effect = yes</li></ul>
