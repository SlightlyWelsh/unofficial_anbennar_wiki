#Information
 - Title: Anatomical Theater
 - ID: innovativeness_events.3
#Description
Anatomical Theater
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.2 if has religion group is christian

#Options

___
##Reprimand and restrict the doctors.

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>reduce innovativeness small effect = yes</li></ul>

___
##They can dissect the bodies of the convicted.

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>goto = doctor_province</li><li>event target:doctor province:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "unpopular_dissections"</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Let us work to secure a constant supply of bodies for their work.

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>goto = doctor_province</li><li>add innovativeness small effect = yes</li><li>add prestige = -10</li><li>event target:doctor province:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "unpopular_dissections"</li><li>duration = 3650</li></ul></ul></ul></ul>
