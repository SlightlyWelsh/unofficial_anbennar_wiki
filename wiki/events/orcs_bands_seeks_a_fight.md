#Information
 - Title: Orcs Bands Seeks a Fight
 - ID: orcish_tolerance_events.3
#Description
Orcs Bands Seeks a Fight
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Recruit them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to decrease tolerance orcish is yes


###Efects:<ul><li>add years of income = -0.05</li><li>If has max manpower is 20:</li><ul><li>add manpower = 1</li></ul><li>If does not have max manpower is 20:</li><ul><li>add yearly manpower = 0.5</li></ul><li>small increase of orcish tolerance effect = yes</li><li>event target:orcish recruitment province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is orcish recruitment province; and does not have province modifier is orcish angry about assumptions; and  has orcish minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = orcish_recruitment_province</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##We can't afford it

###AI weighting:
AI weights this option at 50


___
##It'd be like hiring our enemies to tell us of their plans...

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance orcish is yes
 - Multiplied by 0.1 if has wants to increase tolerance orcish is yes


###Efects:<ul><li>add prestige = 5</li><li>small decrease of orcish tolerance effect = yes</li><li>event target:orcish recruitment province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is orcish recruitment province; and does not have province modifier is orcish angry about assumptions; and  has orcish minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = orcish_angry_about_assumptions</li><li>duration = 1825</li></ul></ul></ul></ul>
