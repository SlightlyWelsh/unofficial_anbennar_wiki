#Information
 - Title: Extended Privileges for the $ESTATE_BURGHERS$
 - ID: burghers_estate_events.7
#Description
Extended Privileges for the $ESTATE_BURGHERS$
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let us remove these obstacles!

###AI weighting:
AI weights this option at 25
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_RIGHTS_EXTENDED</li><li>influence = 10</li><li>duration = 5475</li></ul><li>If every owned province has province flag is [extended_burgher_privileges](../flags/extended_burgher_privileges.md):</li><ul><li>add local autonomy = 33</li><li>clr province flag [extended_burgher_privileges](../flags/extended_burgher_privileges.md)</li></ul></ul>

___
##The $ESTATE_BURGHERS$ need to know their place!

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 85


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_RIGHTS_REFUSED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
