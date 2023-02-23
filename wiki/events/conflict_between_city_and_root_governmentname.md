#Information
 - Title: Conflict between City and [Root.GovernmentName]
 - ID: devotion_events.100
#Description
Conflict between City and [Root.GovernmentName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Sooner or later they will come to their senses.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.25 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40


###Efects:<ul><li>add adm power = 50</li><li>reduce estate church loyalty effect = yes</li><li>add estate burghers loyalty effect = yes</li></ul>

___
##Enforce our authority!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.25 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40


###Efects:<ul><li>add devotion = 10</li><li>reduce estate burghers loyalty effect = yes</li><li>add estate church loyalty effect = yes</li><li>If random owned province has local autonomy is 25, and  is state:</li><ul><li>add local autonomy = -10</li><li>add province modifier:</li><ul><li>name = add_unrest_5_modifier</li><li>duration = 3650</li></ul></ul></ul>
