#Information
 - Title: Anticlericalism
 - ID: church_estate_events.4
#Description
Anticlericalism
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Then we must force them to pay!

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate church, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate is estate burghers, and does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate is estate burghers, and  has estate influence has estate is estate burghers, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate is estate vaisyas, and does not have estate loyalty has estate is estate vaisyas, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate is estate vaisyas, and  has estate influence has estate is estate vaisyas, and estate influence has influence is 60


###Efects:<ul><li>add years of income = 0.2</li><li>If has estate is estate burghers, and  has any owned province has local autonomy is 25, and has owner has government is republic; and has development is 10, and has province trade power is 5:</li><ul><li>If random owned province has local autonomy is 25, and has owner has government is republic; and has development is 10, and has province trade power is 5:</li><ul><li>add local autonomy = -25</li></ul></ul><li>If has estate is estate vaisyas, and  has any owned province has local autonomy is 25, and has owner has government is republic; and has development is 7, and has province trade power is 5:</li><ul><li>If random owned province has local autonomy is 25, and has owner has government is republic; and has development is 7, and has province trade power is 5:</li><ul><li>add local autonomy = -25</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_vaisyas</li><li>loyalty = -15</li></ul></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_TITHES_DEFENDED</li><li>influence = 10</li><li>duration = 5475</li></ul><li>If has estate is estate burghers:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_TITHES_DEFENDED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul><li>If has estate is estate vaisyas:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_vaisyas</li><li>desc = EST_VAL_TITHES_DEFENDED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul></ul>

___
##A mild reprimand will be enough.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate church, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_church</li><li>desc = EST_VAL_TITHES_UNDERMINED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
