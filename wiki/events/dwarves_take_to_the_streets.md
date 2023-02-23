#Information
 - Title: Dwarves take to the Streets
 - ID: hoardcurse.11
#Description
Dwarves take to the Streets
#Options

___
##Pay some of their debt to encourage fairness

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>custom tooltip = pay_5year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = 5YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event [Banks in Good Health](../events/banks_in_good_health.md) happens</li></ul></ul>

___
##We'll deal with them with force

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>add stability = -3</li><li>custom tooltip = massive_revolt_tooltip</li><li>hidden effect:</li><ul><li>set variable:</li><ul><li>which = variable:revoltsHoard</li><li>value = 0</li></ul><li>If while does not have check variable has which is variable:revoltsHoard, and check variable has value is 15:</li><ul><li>If random owned province has not has province flag is [hoard_spawned_rebels](../flags/hoard_spawned_rebels.md):</li><ul><li>anti tax rebels = 1</li><li>set province flag [hoard_spawned_rebels](../flags/hoard_spawned_rebels.md)</li></ul><li>change variable:</li><ul><li>which = variable:revoltsHoard</li><li>value = 1</li></ul></ul></ul><li>hidden effect:</li><ul><li>the event [Banks in Good Health](../events/banks_in_good_health.md) happens</li></ul><li>hidden effect:</li><ul><li>If every owned province has province flag is [hoard_spawned_rebels](../flags/hoard_spawned_rebels.md):</li><ul><li>clr province flag [hoard_spawned_rebels](../flags/hoard_spawned_rebels.md)</li></ul></ul></ul>
