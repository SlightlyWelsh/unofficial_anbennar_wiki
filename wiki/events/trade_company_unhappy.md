#Information
 - Title: Trade Company Unhappy
 - ID: trade_company_events.9
#Description
Trade Company Unhappy
#Options

___
##Renew the promise

###Available if:
<li>None of the following:</li><ul><li>has province flag [renewed_promise](../flags/renewed_promise.md)</li></ul>

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>goto = root</li><li>add province modifier:</li><ul><li>name = trade_company_annoyed</li><li>duration = 1825</li></ul><li>set province flag [renewed_promise](../flags/renewed_promise.md)</li><li>hidden effect:</li><ul><li>40:</li><ul><li>fire province event [trade_company_events.9](trade_company_events.9_slug) in 365 days</li></ul></ul></ul>

___
##Support them in other ways

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>owner:</li><ul><li>add dip power = -25</li><li>add mil power = -25</li></ul><li>clr province flag [renewed_promise](../flags/renewed_promise.md)</li><li>hidden effect:</li><ul><li>event target:claim province:</li><ul><li>clr province flag [claimed_for_trade_company](../flags/claimed_for_trade_company.md)</li></ul></ul></ul>

___
##Ignore their concerns

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>goto = root</li><li>add province modifier:</li><ul><li>name = trade_company_greatly_upset</li><li>duration = 3650</li></ul><li>clr province flag [trade_company_claimer](../flags/trade_company_claimer.md)</li><li>clr province flag [renewed_promise](../flags/renewed_promise.md)</li><li>hidden effect:</li><ul><li>event target:claim province:</li><ul><li>clr province flag [claimed_for_trade_company](../flags/claimed_for_trade_company.md)</li></ul></ul></ul>
