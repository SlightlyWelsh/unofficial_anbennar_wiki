#Information
 - Title: [Root.GetName] Massacre
 - ID: trade_company_events.6
#Description
[Root.GetName] Massacre
#Mean Time to Happen:
Base time = 500 months
 - Multiplied by 0.95 if has trade company size is 15
 - Multiplied by 0.95 if has trade company size is 20
 - Multiplied by 0.95 if has trade company size is 25
 - Multiplied by 0.75 if does not have owned by is ROOT; and any neighbor province is owned by trade company, and any neighbor province does not have alliance with is ROOT; and is rival is ROOT, and has war with is ROOT

#Options

___
##Imprison the governor

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add province modifier:</li><ul><li>name = trade_company_greatly_upset</li><li>duration = 3650</li></ul></ul>

___
##Support the governor

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>owner:</li><ul><li>tooltip:</li><ul><li>reverse add opinion:</li><ul><li>who = event_target:enemy_country</li><li>modifier = beheaded_governor</li></ul></ul></ul><li>hidden effect:</li><ul><li>event target:target province:</li><ul><li>fire province event [trade_company_events.7](trade_company_events.7_slug) in 1 days</li></ul></ul></ul>
