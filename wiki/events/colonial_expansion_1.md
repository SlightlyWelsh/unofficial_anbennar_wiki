This page has the same name as others. For full listing see bottom of [the base page](colonial_expansion.md).

#Information
 - Title: Colonial Expansion
 - ID: colonial_nation.12
#Description
Colonial Expansion
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Restrict it!

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>event target:restricted colonial expansion country:</li><ul><li>tooltip:</li><ul><li>add liberty desire = 25</li><li>country gets the modifier "restricted_colonial_expansion" for 5 years</li></ul><li>hidden effect:</li><ul><li>the event [Restricted Colonial Expansion](../events/restricted_colonial_expansion.md) happens</li></ul><li>If every neighbor country is primitives:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = restricted_colonial_expansion_opinion</li></ul></ul></ul></ul>

___
##Let them expand freely

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>event target:restricted colonial expansion country:</li><ul><li>If every neighbor country is primitives:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = non_restricted_colonial_expansion_opinion</li></ul></ul></ul></ul>
