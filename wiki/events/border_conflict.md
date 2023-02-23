#Information
 - Title: Border Conflict
 - ID: trade_company_events.5
#Description
Border Conflict
#Mean Time to Happen:
Base time = 300 months
 - Multiplied by 0.95 if has trade company size is 10
 - Multiplied by 0.95 if has trade company size is 15
 - Multiplied by 0.95 if has trade company size is 20

#Options

___
##Force them to stand down

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add province modifier:</li><ul><li>name = trade_company_upset</li><li>duration = 1825</li></ul></ul>

___
##Endorse their behavior

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>goto = target_province</li><li>event target:target province:</li><ul><li>add claim = ROOT</li></ul></ul>
