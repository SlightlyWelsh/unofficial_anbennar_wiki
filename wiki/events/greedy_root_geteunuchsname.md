#Information
 - Title: Greedy [Root.GetEunuchsName]
 - ID: eunuchs_estate_events.4
#Description
Greedy [Root.GetEunuchsName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.1 if has estate influence has estate is estate eunuchs, and estate influence has influence is 80

#Options

___
##Turn a blind eye.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 35


###Efects:<ul><li>If random owned province is not territory, and  has base tax is 2, and  is city:</li><ul><li>add base tax = -1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = 15</li></ul></ul>

___
##Chastise the landowner.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.0 if does not have estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 35
 - Multiplied by 1.5 if has estate loyalty has estate is estate eunuchs, and estate loyalty has loyalty is 70


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_eunuchs</li><li>loyalty = -15</li></ul></ul>
