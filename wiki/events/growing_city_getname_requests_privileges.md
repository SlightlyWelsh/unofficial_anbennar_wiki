#Information
 - Title: [growing_city.GetName] Requests Privileges
 - ID: burghers_estate_events.4
#Description
[growing_city.GetName] Requests Privileges
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 0.5 if does not have religion group is christian
 - Multiplied by 1.2 if has any owned province is not overseas, and any owned province is not a capital, and any owned province does not have seat in parliament, and has development is 10, and has province has center of trade of level is 1; and any owned province has river estuary trigger is yes, and any owned province is city

#Options

___
##Accept the Petition.

###Efects:<ul><li>give estate land share medium:</li><ul><li>estate = estate_burghers</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>event target:growing city:</li><ul><li>add base tax = 2</li></ul></ul>

___
##Reject the Petition.

###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_CITY_PRIVILEGES_DENIED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
