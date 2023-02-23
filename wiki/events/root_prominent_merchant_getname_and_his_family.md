#Information
 - Title: [Root.prominent_merchant.GetName] and his Family
 - ID: trade_policy_events.9
#Description
[Root.prominent_merchant.GetName] and his Family
#Mean Time to Happen:
Base time = 560 months

#Options

___
##Let us use their influence to extract maps of [foreign_province_owner.GetAdjective] hinterlands.

###Available if:
<li>event target:foreign province:</li><ul><li>any neighbor province:</li><ul><li>None of the following:</li><ul><li>has discovered this nation</li></ul></ul></ul>

###Efects:<ul><li>event target:foreign province:</li><ul><li>every neighbor province:</li><ul><li>ROOT:</li><ul><li>discover province = PREV</li></ul></ul><li>owner:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = 50</li></ul></ul></ul><li>hidden effect:</li><ul><li>clear saved name = prominent_merchant</li></ul></ul>

___
##We should not ask what they can do for us. What is good for them is good for us.

###Efects:<ul><li>event target:foreign province:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 3650</li><li>power = 10</li><li>key = influential_trading_family</li></ul></ul><li>hidden effect:</li><ul><li>clear saved name = prominent_merchant</li></ul></ul>

___
##Let us make [Root.prominent_merchant.GetName] a the new architect for our trade policies.

###Efects:<ul><li>If does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>name = prominent_merchant</li><li>type = trader</li><li>skill = 2</li><li>discount = yes</li><li>culture = event_target:merchant_family_province</li><li>religion = event_target:merchant_family_province</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>name = prominent_merchant</li><li>type = trader</li><li>skill = 2</li><li>discount = yes</li><li>culture = event_target:merchant_family_province</li><li>religion = event_target:merchant_family_province</li></ul></ul></ul>
