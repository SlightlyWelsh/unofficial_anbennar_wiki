#Information
 - Title: Expansion of a Trade Factory
 - ID: institution_events.52
#Description
Expansion of a Trade Factory
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Grant them the right to expand their business.

###Efects:<ul><li>add years of income = 0.1</li><li>add prestige = -10</li><li>event target:trade company country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_traders_in_x</li></ul><li>the event ˻institution_events.53˼ happens</li></ul><li>event target:trade company province:</li><ul><li>add province modifier:</li><ul><li>name = "trade_company_factory"</li><li>duration = -1</li></ul><li>event target:trade company country:</li><ul><li>add claim = PREV</li></ul><li>add institution embracement:</li><ul><li>which = "global_trade"</li><li>value = 100</li></ul><li>set province flag [foreign_factory](../flags/foreign_factory.md)</li><li>If area has owned by is ROOT, and does not have province id is PREV:</li><ul><li>add institution embracement:</li><ul><li>which = "global_trade"</li><li>value = 10</li></ul><li>set province flag [foreign_factory](../flags/foreign_factory.md)</li></ul></ul></ul>

___
##We cannot allow this!

###Efects:<ul><li>add prestige = 10</li><li>event target:trade company country:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_refused_traders_in_x</li></ul><li>the event ˻institution_events.54˼ happens</li></ul></ul>
