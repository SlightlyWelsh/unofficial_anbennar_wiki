#Information
 - Title: Burrows in the Way of New Building
 - ID: kobold_tolerance_events.9
#Description
Burrows in the Way of New Building
#Options

___
##Bribe them to leave

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to decrease tolerance kobold is yes
 - Multiplied by 0.1 if does not have years of income is 0.33


###Efects:<ul><li>add years of income = -0.33</li><li>small increase of kobold tolerance effect = yes</li><li>event target:kobold burrows province:</li><ul><li>add province modifier:</li><ul><li>name = kobold_burrows</li><li>duration = 3650</li></ul></ul></ul>

___
##Scare them away

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to increase tolerance kobold is yes


###Efects:<ul><li>small decrease of kobold tolerance effect = yes</li><li>event target:kobold burrows province:</li><ul><li>add province modifier:</li><ul><li>name = kobold_burrows</li><li>duration = 1825</li></ul></ul></ul>

___
##Kick them out!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance kobold is yes


###Efects:<ul><li>add mil power = -20</li><li>large decrease of kobold tolerance effect = yes</li></ul>
