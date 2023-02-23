#Information
 - Title: Loyalties of [Root.Monarch.GetName] and [Root.Heir.GetName]
 - ID: elective_monarchy.14
#Description
Loyalties of [Root.Monarch.GetName] and [Root.Heir.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Assure them that the Sejm stays loyal to the [Root.Monarch.Dynasty.GetName] line.

###Efects:<ul><li>add heir support = -10</li></ul>

___
##Admit that a shift is necessary.

###Efects:<ul><li>add heir support = 10</li><li>If random known country has dynasty is ROOT, and  is not lesser in union, and  does not have heir nationality is PREV:</li><ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sided_with_foreign_heir</li></ul></ul><li>hidden effect:</li><ul><li>the event ˻elective_monarchy.15˼ happens</li></ul></ul><li>If random known country does not have dynasty is ROOT; and  has ROOT has heir nationality is PREV:</li><ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = sided_with_supported_heir</li></ul></ul><li>hidden effect:</li><ul><li>the event ˻elective_monarchy.16˼ happens</li></ul></ul></ul>

___
##Stay neutral. The Sejm owes allegiance only to [Root.GetName].

###Efects:<ul><li>add prestige = 10</li></ul>
