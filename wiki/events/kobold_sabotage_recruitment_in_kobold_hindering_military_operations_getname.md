#Information
 - Title: Kobold Sabotage Recruitment in [kobold_hindering_military_operations.GetName]
 - ID: kobold_tolerance_events.2
#Description
Kobold Sabotage Recruitment in [kobold_hindering_military_operations.GetName]
#Options

___
##Punish all of them!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.2 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.8 if does not have manpower percentage is 0.5
 - Multiplied by 0.5 if has wants to maintain tolerance kobold is yes
 - Multiplied by 0.1 if has wants to increase tolerance kobold is yes


###Efects:<ul><li>add prestige = 5</li><li>increase legitimacy small effect = yes</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>If has max manpower is 25:</li><ul><li>add manpower = -1.25</li></ul><li>If does not have max manpower is 25:</li><ul><li>add yearly manpower = -0.5</li></ul><li>small decrease of kobold tolerance effect = yes</li><li>event target:kobold hindering military operations:</li><ul><li>If area does not have province modifier is kobold bands punished harshly; and does not have province modifier is kobold bands punished; and does not have province modifier is kobold bands not punished; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_bands_punished_harshly</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Punish the kobolds found guilty

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have manpower percentage is 0.5


###Efects:<ul><li>If has max manpower is 25:</li><ul><li>add manpower = -1</li></ul><li>If does not have max manpower is 25:</li><ul><li>add yearly manpower = -0.4</li></ul><li>event target:kobold hindering military operations:</li><ul><li>If area does not have province modifier is kobold bands punished harshly; and does not have province modifier is kobold bands punished; and does not have province modifier is kobold bands not punished; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_bands_punished</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Ignore them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40


###Efects:<ul><li>add prestige = -10</li><li>reduce estate nobles loyalty effect = yes</li><li>event target:kobold hindering military operations:</li><ul><li>If area does not have province modifier is kobold bands punished harshly; and does not have province modifier is kobold bands punished; and does not have province modifier is kobold bands not punished; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_bands_not_punished</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Maybe they can be recruited?

###Available if:
<li>MIL is at least 2</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has dlc is "The Cossacks", and  has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 50
 - Multiplied by 0.5 if has wants to maintain tolerance kobold is yes
 - Multiplied by 0.1 if has wants to decrease tolerance kobold is yes


###Efects:<ul><li>add prestige = -15</li><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul></ul><li>add years of income = -0.1</li><li>add yearly manpower = 0.15</li><li>small increase of kobold tolerance effect = yes</li><li>event target:kobold hindering military operations:</li><ul><li>If area does not have province modifier is kobold bands punished harshly; and does not have province modifier is kobold bands punished; and does not have province modifier is kobold bands not punished; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_bands_not_punished</li><li>duration = 1825</li></ul></ul></ul></ul>
