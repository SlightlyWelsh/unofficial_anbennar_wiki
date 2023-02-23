#Information
 - Title: Overhaul the Banks
 - ID: hoardcurse.9
#Description
Overhaul the Banks
#Options

___
##Nationalize them

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>has reform khug_asra_reform_republic</li><li>has reform  khug_asra_reform_monarchy</li></ul></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>custom tooltip = pay_3year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = 3YearOfIncome</li></ul><li>hidden effect:</li><ul><li>the event ˻hoardcurse.10˼ happens</li></ul></ul>

___
##We can leave this to the Asra Bank!

###Available if:
<li>Any of the following:</li><ul><li>has reform khug_asra_reform_republic</li><li>has reform  khug_asra_reform_monarchy</li></ul>

###AI weighting:
AI weights this option at 90


###Efects:<ul><li>highlight = yes</li><li>hidden effect:</li><ul><li>the event ˻hoardcurse.60˼ happens</li></ul></ul>

___
##Force them to collect debt

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>reduce stability or adm power = yes</li><li>hidden effect:</li><ul><li>the event ˻hoardcurse.11˼ happens</li></ul></ul>

___
##Go Back

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [hoardcurse_reforming](../flags/hoardcurse_reforming.md)</li></ul></ul>
