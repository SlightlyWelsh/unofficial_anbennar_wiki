#Information
 - Title: Magical Succession within the Nobility?
 - ID: mages_estate_events.4
#Description
Magical Succession within the Nobility?
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Succession is succession, no matter what

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate mages, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_TRADITIONAL_NOBILITY_SUPPORTED</li><li>influence = -10</li><li>duration = 3650</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_TRADITIONAL_NOBILITY_SUPPORTED</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##Accept the petition

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has reform is magical elite reform
 - Multiplied by 0.2 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate mages, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate nobles, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_MAGICAL_NOBILITY_SUPPORTED</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_MAGICAL_NOBILITY_SUPPORTED</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
