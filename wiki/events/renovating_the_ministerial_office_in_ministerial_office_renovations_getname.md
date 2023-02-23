#Information
 - Title: Renovating the Ministerial Office in [ministerial_office_renovations.GetName]
 - ID: rajministries.10
#Description
Renovating the Ministerial Office in [ministerial_office_renovations.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let's set aside some funds for the restorations

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has event target:ministerial office renovations has building is courthouse:</li><ul><li>add treasury = -50</li></ul><li>else:</li><ul><li>add treasury = -100</li></ul><li>event target:ministerial office renovations:</li><ul><li>add province modifier:</li><ul><li>name = raj_ministries_renovated_offices</li><li>duration = 9125</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = 5</li></ul><li>raj cohesion change:</li><ul><li>amount = 10</li><li>ministries events = yes</li></ul></ul>

___
##The building is in a perfectly fine state as it is

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:ministerial office renovations:</li><ul><li>add province modifier:</li><ul><li>name = raj_ministries_delapidated_offices</li><li>duration = 9125</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_raj_ministries</li><li>loyalty = -5</li></ul><li>raj cohesion change:</li><ul><li>amount = -10</li><li>ministries events = yes</li></ul></ul>
