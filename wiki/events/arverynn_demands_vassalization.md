#Information
 - Title: Arverynn Demands Vassalization
 - ID: flavor_arvezl.0
#Description
Arverynn Demands Vassalization
#Options

___
##Welcome back our rightful overlord.

###AI weighting:
AI weights this option at 2
 - Multiplied by 10 if has opinion has who is event target:u24 old overlord, and has opinion has value is 20
 - Multiplied by 0 if does not have trust has who is event target:u24 old overlord, and trust has value is 40
 - Multiplied by 0.5 if has army size is event target:u24 old overlord


###Efects:<ul><li>tooltip:</li><ul><li>event target:u24 old overlord:</li><ul><li>create subject:</li><ul><li>subject type = ynnic_iosahar</li><li>subject = ROOT</li></ul></ul></ul><li>add historical friend = event_target:u24_old_overlord</li><li>remove historical friend = G36</li><li>hidden effect:</li><ul><li>event target:u24 old overlord:</li><ul><li>the event [Arvezl Rejoins](../events/arvezl_rejoins.md) happens</li></ul></ul></ul>

___
##Those pacts are no longer valid, send them away.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:u24 old overlord:</li><ul><li>the event [Arvezl Defies Us](../events/arvezl_defies_us.md) happens</li><li>add trust:</li><ul><li>who = ROOT</li><li>value = -10</li><li>mutual = no</li></ul></ul><li>reverse add opinion:</li><ul><li>who = event_target:u24_old_overlord</li><li>modifier = opinion_betrayal</li></ul></ul>
