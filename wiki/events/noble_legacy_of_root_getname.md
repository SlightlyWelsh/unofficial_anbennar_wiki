#Information
 - Title: Noble Legacy of [Root.GetName]
 - ID: republic_factions.8
#Description
Noble Legacy of [Root.GetName]
#Mean Time to Happen:
Base time = 800 months

#Options

___
##War perhaps, but who said anything about misery?

###Efects:<ul><li>owner:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 10</li><li>perform readjustment = no</li></ul><li>add faction influence:</li><ul><li>faction = mr_traders</li><li>influence = -10</li><li>perform readjustment = no</li></ul></ul><li>If random neighbor province does not have owner has tag is ROOT; and does not have claim is ROOT:</li><ul><li>add claim = ROOT</li></ul></ul>

___
##They are right. We should put these petty squabbles behind us.

###Efects:<ul><li>owner:</li><ul><li>add faction influence:</li><ul><li>faction = mr_traders</li><li>influence = 10</li><li>perform readjustment = no</li></ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = -10</li><li>perform readjustment = no</li></ul></ul><li>add province modifier:</li><ul><li>name = "trade_with_neighbor"</li><li>duration = 1095</li></ul><li>If random neighbor province does not have owner has tag is ROOT:</li><ul><li>owner:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = goods_crossing_borders</li></ul></ul></ul></ul>
