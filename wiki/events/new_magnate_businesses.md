#Information
 - Title: New Magnate Businesses
 - ID: flavor_gawed.11
#Description
New Magnate Businesses
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 5 if is year is 1575
 - Multiplied by 2 if has estate influence has estate is estate burghers, and estate influence has influence is 50

#Options

___
##Fantastic!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:business province:</li><ul><li>add permanent province modifier:</li><ul><li>name = new_magnate_business</li><li>duration = 3650</li></ul><li>add local autonomy = 10</li></ul><li>change estate land share:</li><ul><li>estate = estate_burghers</li><li>share = 5</li></ul></ul>

___
##Stop this now!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40:</li><ul><li>event target:business province:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 3</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li></ul></ul><li>else:</li><ul><li>event target:business province:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 4</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li></ul></ul><li>add prestige = -10</li></ul>
