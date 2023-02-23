This page has the same name as others. For full listing see bottom of [the base page](rightful_ownership.md).

#Information
 - Title: Rightful Ownership
 - ID: subject_interaction_events.41
#Description
Rightful Ownership
#Options

___
##It is theirs by right

###AI weighting:
AI weights this option at 25
 - Multiplied by 0 if has event target:rightful province has development is 20
 - Multiplied by 0.5 if has event target:rightful province has development is 15
 - Multiplied by 1.25 if has event target:rightful province does not have owner culture
 - Multiplied by 1.5 if has event target:rightful province is core is FROM


###Efects:<ul><li>event target:rightful province:</li><ul><li>remove core = ROOT</li><li>remove claim = ROOT</li><li>cede province = FROM</li></ul><li>FROM:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_gave_province</li></ul></ul></ul>

___
##It is ours and always will be

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add prestige = 10</li><li>FROM:</li><ul><li>tooltip:</li><ul><li>add liberty desire = 15</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_tyrant_overlord</li></ul></ul><li>hidden effect:</li><ul><li>the event [Rightful Ownership Refused!](../events/rightful_ownership_refused.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_tyrant_overlord</li></ul></ul></ul></ul>
