#Information
 - Title: Missionaries Arrive in [company_missionary_province.GetName]
 - ID: investment_events.6
#Description
Missionaries Arrive in [company_missionary_province.GetName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if has full idea group is religious ideas
 - Multiplied by 1.5 if has full idea group is humanist ideas

#Options

___
##[company_missionary_province.GetName] must follow the true faith.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>increase religious currency effect = yes</li><li>event target:company missionary province:</li><ul><li>change religion = ROOT</li><li>add province modifier:</li><ul><li>name = company_missionary_activity</li><li>duration = 7300</li></ul></ul></ul>

___
##Tolerance is necessary to Company operations.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>reduce religious currency effect = yes</li><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li></ul></ul><li>country gets the modifier "restricted_company_missionaries" for 20 years</li></ul>
