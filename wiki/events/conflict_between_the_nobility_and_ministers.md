#Information
 - Title: Conflict Between the Nobility and Ministers
 - ID: rajministries.5
#Description
Conflict Between the Nobility and Ministers
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The ministers know best

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_raj_ministries</li><li>desc = EST_VAL_MINISTERS_OVER_NOBLES_IN_PROVINCIAL_MANAGEMENT</li><li>influence = 10</li><li>duration = 3650</li></ul><li>If has estate is estate uppercastes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = -15</li></ul></ul><li>Else if has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul></ul><li>raj cohesion change:</li><ul><li>amount = 20</li><li>ministries events = yes</li></ul><li>event target:ministers nobles conflict:</li><ul><li>add province modifier:</li><ul><li>name = raj_ministries_dominant_ministerial_office</li><li>duration = 7300</li></ul></ul></ul>

___
##Let the nobles manage it, it's their ancestral land

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = -15</li></ul><li>If has estate is estate uppercastes:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_uppercastes</li><li>desc = EST_VAL_NOBLES_OVER_MINISTERS_IN_PROVINCIAL_MANAGEMENT</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_uppercastes</li><li>loyalty = 15</li></ul></ul><li>Else if has estate is estate nobles:</li><ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_OVER_MINISTERS_IN_PROVINCIAL_MANAGEMENT</li><li>influence = 10</li><li>duration = 3650</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 15</li></ul></ul><li>raj cohesion change:</li><ul><li>amount = -20</li><li>ministries events = yes</li></ul><li>event target:ministers nobles conflict:</li><ul><li>add province modifier:</li><ul><li>name = raj_ministries_dominant_noble_estate</li><li>duration = 7300</li></ul></ul></ul>
