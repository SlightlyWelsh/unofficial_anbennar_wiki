#Information
 - Title: Anti-Government Teachings in Magical Schools
 - ID: mages_estate_events.24
#Description
Anti-Government Teachings in Magical Schools
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let them say what they want

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_ANTI_GOVERNMENT_TEACHINGS</li><li>loyalty = -10</li><li>duration = 7300</li></ul></ul>

___
##Listen to their concerns

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has adm power is 50, and  has dip power is 50, and  has mil power is 50


###Efects:<ul><li>add adm power = -25</li><li>add dip power = -25</li><li>add mil power = -25</li><li>add estate loyalty modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_ANTI_GOVERNMENT_TEACHINGS</li><li>loyalty = -10</li><li>duration = 3650</li></ul></ul>

___
##Fire the faculty, and hire loyalists!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 25
 - Multiplied by 2 if has estate loyalty has estate is estate mages, and estate loyalty has loyalty is 75


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_INEXPERIENCED_PROFESSORS</li><li>influence = -20</li><li>duration = 7300</li></ul></ul>
