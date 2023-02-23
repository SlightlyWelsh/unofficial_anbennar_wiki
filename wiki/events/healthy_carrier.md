#Information
 - Title: Healthy Carrier
 - ID: serpent_rot.21
#Description
Healthy Carrier
#Options

___
##Use him to try to find a cure

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = pay_year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻serpent_rot.23˼ happens</li><li>hidden effect:</li><ul><li>REB:</li><ul><li>change variable:</li><ul><li>which = serpentCureGlobal</li><li>value = 5</li></ul></ul><li>change variable:</li><ul><li>which = serpentCureNational</li><li>value = 5</li></ul></ul></ul></ul>

___
##There is no time, Mycos Caurak must burn!

###Available if:
<li>any owned province:</li><ul><li>has province flag [caurak_collapse](../flags/caurak_collapse.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>custom tooltip = pay_0.5year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = HalfYearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻serpent_rot.22˼ happens</li><li>the event ˻serpent_rot.23˼ happens</li></ul></ul>
