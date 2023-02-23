#Information
 - Title: Cottage Industry
 - ID: burghers_estate_events.9
#Description
Cottage Industry
#Mean Time to Happen:
Base time = 1 days

#Options

___
##We cannot stand in the way of progress.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>If every owned province has province flag is [putting_out_system](../flags/putting_out_system.md):</li><ul><li>add base production = 1</li><li>add province modifier:</li><ul><li>name = "conflict_within_city"</li><li>duration = 3650</li></ul><li>clr province flag [putting_out_system](../flags/putting_out_system.md)</li></ul></ul>

___
##We must safeguard the guild privileges.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHER_PROTO_CAPITALISTS</li><li>influence = 10</li><li>duration = 3650</li></ul><li>If every owned province has province flag is [putting_out_system](../flags/putting_out_system.md):</li><ul><li>add province modifier:</li><ul><li>name = "thankful_guilds"</li><li>duration = 3650</li></ul><li>clr province flag [putting_out_system](../flags/putting_out_system.md)</li></ul></ul>
