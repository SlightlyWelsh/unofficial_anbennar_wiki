#Information
 - Title: Internal Migration of Halfling Minority
 - ID: racial_pop_events_halfling.6
#Description
Internal Migration of Halfling Minority
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Welcome to [racial_pop_province_target.GetName]!

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>event target:racial pop province origin:</li><ul><li>remove halfling minority size effect = yes</li></ul><li>event target:racial pop province target:</li><ul><li>add halfling minority size effect = yes</li></ul><li>If has has large halfling minority trigger is yes, and has halfling majority trigger is yes:</li><ul><li>event target:racial pop province target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add base production = 1</li></ul></ul></ul></ul>

___
##Prevent further migration

###Available if:


###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has wants to decrease tolerance halfling is yes
 - Multiplied by 3 if has country modifier is racial pop halfling purge, and has country modifier is racial pop halfling expulsion


###Efects:<ul><li>add adm power = -10</li><li>small decrease of halfling tolerance effect = yes</li></ul>