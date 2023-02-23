#Information
 - Title: Resettlement Plan Fails
 - ID: trade_company_events.2
#Description
Resettlement Plan Fails
#Mean Time to Happen:
Base time = 300 months
 - Multiplied by 1.05 if has trade company size is 10
 - Multiplied by 1.05 if has trade company size is 15
 - Multiplied by 1.05 if has trade company size is 20

#Options

___
##Forget the project

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add province modifier:</li><ul><li>name = trade_company_upset</li><li>duration = 1825</li></ul><li>clr province flag [resettlement_plan](../flags/resettlement_plan.md)</li></ul>

___
##Award some incentives

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add base tax = 1</li><li>change culture = owner</li><li>owner:</li><ul><li>add years of income = -0.25</li><li>add adm power = -25</li><li>add dip power = -25</li></ul><li>clr province flag [resettlement_plan](../flags/resettlement_plan.md)</li></ul>
