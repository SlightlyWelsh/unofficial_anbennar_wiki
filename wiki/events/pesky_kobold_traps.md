#Information
 - Title: Pesky Kobold Traps!
 - ID: kobold_tolerance_events.10
#Description
Pesky Kobold Traps!
#Options

___
##Hire willing kobold to dismantle them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to decrease tolerance kobold is yes
 - Multiplied by 0.5 if does not have years of income is -0.2


###Efects:<ul><li>add years of income = -0.2</li><li>small increase of kobold tolerance effect = yes</li></ul>

___
##Dismantle them ourselves

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>event target:kobold traps province:</li><ul><li>add province modifier:</li><ul><li>name = kobold_pesky_traps</li><li>duration = 1825</li></ul></ul></ul>

___
##Send a force to smoke the perpetrators out

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to increase tolerance kobold is yes
 - Multiplied by 0.5 if does not have manpower percentage is 0.5


###Efects:<ul><li>If has max manpower is 20:</li><ul><li>add manpower = -1</li></ul><li>If does not have max manpower is 20:</li><ul><li>add yearly manpower = -0.5</li></ul><li>medium decrease of kobold tolerance effect = yes</li></ul>
