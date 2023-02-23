#Information
 - Title: Kobold Bands
 - ID: kobold_tolerance_events.1
#Description
Kobold Bands
#Options

___
##Scare them into submission

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have manpower percentage is 0.4
 - Multiplied by 0.5 if has wants to maintain tolerance kobold is yes
 - Multiplied by 0.1 if has wants to increase tolerance kobold is yes


###Efects:<ul><li>add mil power = -25</li><li>If has max manpower is 25:</li><ul><li>add manpower = -1</li></ul><li>If does not have max manpower is 25:</li><ul><li>add yearly manpower = -0.4</li></ul><li>small decrease of kobold tolerance effect = yes</li><li>event target:kobold causing havoc province:</li><ul><li>If area does not have province modifier is kobold bands recruited; and does not have province modifier is kobold scared into submission; and does not have province modifier is kobold angered by attempts to submit; and  has kobold minority trigger is yes:</li><ul><li>random list:</li><ul><li>80:</li><ul><li>add province modifier:</li><ul><li>name = kobold_scared_into_submission</li><li>duration = 1095</li></ul></ul><li>20:</li><ul><li>add province modifier:</li><ul><li>name = kobold_angered_by_attempts_to_submit</li><li>duration = 1095</li></ul></ul></ul></ul></ul></ul>

___
##Swiftly enforce our will on them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have manpower percentage is 0.4


###Efects:<ul><li>add mil power = -20</li><li>If has max manpower is 25:</li><ul><li>add manpower = -1.25</li></ul><li>If does not have max manpower is 25:</li><ul><li>add yearly manpower = -0.5</li></ul><li>event target:kobold causing havoc province:</li><ul><li>If area does not have province modifier is kobold bands recruited; and does not have province modifier is kobold scared into submission; and does not have province modifier is kobold angered by attempts to submit; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_angered_by_attempts_to_submit</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Find a way to recruit them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have years of income is 0.5
 - Multiplied by 0.5 if has wants to maintain tolerance kobold is yes
 - Multiplied by 0.1 if has wants to decrease tolerance kobold is yes


###Efects:<ul><li>add prestige = -10</li><li>If does not have monthly income is 20:</li><ul><li>add years of income = -0.25</li></ul><li>If has monthly income is 20:</li><ul><li>add treasury = -60</li></ul><li>add yearly manpower = 0.025</li><li>small increase of kobold tolerance effect = yes</li><li>event target:kobold causing havoc province:</li><ul><li>If area does not have province modifier is kobold bands recruited; and does not have province modifier is kobold scared into submission; and does not have province modifier is kobold angered by attempts to submit; and  has kobold minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = kobold_bands_recruited</li><li>duration = 1825</li></ul></ul></ul></ul>
