#Information
 - Title: Expand Trade Company
 - ID: trade_company_events.8
#Description
Expand Trade Company
#Mean Time to Happen:
Base time = 300 months
 - Multiplied by 1.1 if has trade company size is 10
 - Multiplied by 1.25 if has trade company size is 15
 - Multiplied by 1.5 if has trade company size is 20

#Options

___
##Go ahead and claim it

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = claim_province</li><li>event target:claim province:</li><ul><li>add claim = ROOT</li><li>set province flag [claimed_for_trade_company](../flags/claimed_for_trade_company.md)</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>40:</li><ul><li>fire province event [trade_company_events.9](trade_company_events.9_slug) in 1095 days</li></ul><li>40:</li><ul><li>fire province event [trade_company_events.9](trade_company_events.9_slug) in 1825 days</li></ul><li>20:</li><ul><li>fire province event [trade_company_events.9](trade_company_events.9_slug) in 3650 days</li></ul></ul></ul><li>custom tooltip = trade_company_events.EVTTOOLTIP8</li><li>set province flag [trade_company_claimer](../flags/trade_company_claimer.md)</li></ul>

___
##Ignore their demand

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add province modifier:</li><ul><li>name = trade_company_upset</li><li>duration = 1825</li></ul></ul>
