#Information
 - Title: A Special Dispensation
 - ID: consort_events.203
#Description
A Special Dispensation
#Options

___
##Not a day too early!

###Efects:<ul><li>custom tooltip = consort_events.203.a.tt</li><li>add prestige = -15</li><li>If random country has given consort to is ROOT:</li><ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = offended_by_divorce</li></ul><li>add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_insult</li><li>months = 60</li></ul></ul><li>hidden effect:</li><ul><li>the event [The Gravest of Insults](../events/the_gravest_of_insults.md) happens</li></ul></ul><li>If random owned province has province modifier is domain of spouses family:</li><ul><li>add province modifier:</li><ul><li>name = angered_nobles</li><li>duration = 7300</li></ul></ul><li>If has heir, and  has heir can be child of consort:</li><ul><li>add heir claim = -30</li></ul><li>hidden effect:</li><ul><li>If does not have any country has given consort to is ROOT:</li><ul><li>remove consort = yes</li></ul><li>the event [none](../events/none.md) happens</li></ul></ul>

___
##Perhaps we acted rashly. [Root.Consort.GetTitle] [Root.Consort.GetName] can stay for now.

###Efects:<ul><li>custom tooltip = consort_events.203.b.tt</li></ul>
