#Information
 - Title: Bandits in [banditprovince.GetName]
 - ID: trade_policy_events.5
#Description
Bandits in [banditprovince.GetName]
#Mean Time to Happen:
Base time = 560 months

#Options

___
##We will divert the necessary resources.

###Efects:<ul><li>add years of income = -0.1</li><li>tooltip:</li><ul><li>event target:banditprovince owner:</li><ul><li>add opinion:</li><ul><li>modifier = helped_clear_out_bandits</li><li>who = ROOT</li></ul></ul><li>event target:banditprovince:</li><ul><li>add province modifier:</li><ul><li>name = outsiders_cleared_our_merchants</li><li>duration = 3650</li></ul><li>set province flag [bandits_handled_by_foreigners](../flags/bandits_handled_by_foreigners.md)</li></ul></ul><li>hidden effect:</li><ul><li>event target:banditprovince owner:</li><ul><li>the event [Foreign Traders Intervene in Local Affairs](../events/foreign_traders_intervene_in_local_affairs.md) happens</li></ul></ul></ul>

___
##No, we would just be aiding the [banditprovince_owner.GetAdjective].

###Efects:<ul><li>event target:banditprovince:</li><ul><li>add trade modifier:</li><ul><li>who = root</li><li>duration = 3650</li><li>power = -10</li><li>key = merchants_hampered_by_bandits</li></ul></ul></ul>
