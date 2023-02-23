#Information
 - Title: Bring down the Monopolies
 - ID: hoardcurse.13
#Description
Bring down the Monopolies
#Options

___
##Metal Monopolies

###Available if:
<li>None of the following:</li><ul><li>has country flag [hoard_monopolies_metal](../flags/hoard_monopolies_metal.md)</li></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>custom tooltip = pay_year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻hoardcurse.14˼ happens</li></ul></ul>

___
##Food Monopolies

###Available if:
<li>None of the following:</li><ul><li>has country flag [hoard_monopolies_food](../flags/hoard_monopolies_food.md)</li></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>custom tooltip = pay_year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻hoardcurse.15˼ happens</li></ul></ul>

___
##Textile Monopolies

###Available if:
<li>None of the following:</li><ul><li>has country flag [hoard_monopolies_textile](../flags/hoard_monopolies_textile.md)</li></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>custom tooltip = pay_year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻hoardcurse.16˼ happens</li></ul></ul>

___
##All Done

###Available if:
<li>has country flag [hoard_monopolies_food](../flags/hoard_monopolies_food.md)</li><li>has country flag  hoard_monopolies_metal</li><li>has country flag   hoard_monopolies_textile</li>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>add prestige = 15</li><li>custom tooltip = pay_0.5year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = HalfYearOfIncome</li></ul><li>hidden effect:</li><ul><li>set country flag [hoard_monopolies_reform](../flags/hoard_monopolies_reform.md)</li></ul><li>hidden effect:</li><ul><li>clr country flag [hoard_monopolies_food](../flags/hoard_monopolies_food.md)</li><li>clr country flag [hoard_monopolies_metal](../flags/hoard_monopolies_metal.md)</li><li>clr country flag [hoard_monopolies_textile](../flags/hoard_monopolies_textile.md)</li></ul></ul>

___
##Go Back

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [hoardcurse_reforming](../flags/hoardcurse_reforming.md)</li></ul></ul>
