#Information
 - Title: Release original Ravelian capital
 - ID: ravelian.23
#Description
Release original Ravelian capital
#Mean Time to Happen:
Base time = 2 months
 - Multiplied by 0.95 if has num of cardinals is 1
 - Multiplied by 0.95 if has num of cardinals is 2
 - Multiplied by 0.75 if has idea group is religious ideas
 - Multiplied by 0.9 if is defender of faith
 - Multiplied by 1.1 if does not have defender of faith
 - Multiplied by 1.1 if does not have advisor is theologian
 - Multiplied by 0.9 if has theologian is 2

#Options

___
##Refuse

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add prestige = -10</li><li>add stability = -1</li><li>If every country has religion is ravelian, and does not have tag is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_declined_independent_state_support</li></ul></ul><li>set country flag [no_support](../flags/no_support.md)</li></ul>

___
##Accept

###AI weighting:
AI weights this option at 75
 - Multiplied by 0 if is core is 118


###Efects:<ul><li>If random owned province has province flag is [ravelian_state_capital](../flags/ravelian_state_capital.md):</li><ul><li>add core = Z97</li><li>cede province = Z97</li><li>If is core is ROOT:</li><ul><li>remove core = ROOT</li></ul></ul><li>add prestige = 25</li><li>Z97:</li><ul><li>change religion = ravelian</li></ul></ul>
