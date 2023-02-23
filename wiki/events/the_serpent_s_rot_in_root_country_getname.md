#Information
 - Title: The Serpent's Rot in [Root.Country.GetName]
 - ID: serpent_rot.4
#Description
The Serpent's Rot in [Root.Country.GetName]
#Mean Time to Happen:
Base time = 3 months

#Options

___
##It only gets worse...

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier serpent_rot_outbreak for 15 years</li><li>the event [The Serpent's Rot](../events/the_serpent_s_rot.md) happens</li></ul>

___
##This is of little concern to us, the disease will not leave the Serpentspine

###Available if:
<li>None of the following:</li><ul><li>Any of the following:</li><ul><li>capital scope:</li><ul><li>continent is serpentspine</li></ul><li>All of the following:</li><ul><li>Any of the following:</li><ul><li>any owned province:</li><ul><li>has terrain dwarven_hold</li></ul><li>any owned province:</li><ul><li>has terrain dwarven_hold_surface</li></ul></ul><li>OR:</li><ul><li>has country modifier dwarven_administration</li><li>has country modifier  goblin_administration</li><li>has country modifier   orcish_administration</li></ul></ul></ul></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = pay_0.5year_of_income</li><li>currency effect:</li><ul><li>currency = treasury</li><li>takeFrom = ROOT</li><li>which = HalfYearOfIncome</li></ul><li>If every owned province has continent is serpentspine:</li><ul><li>add unrest = 20</li></ul><li>hidden effect:</li><ul><li>country gets the modifier ignoring_serpent_rot for 10 years</li><li>REB:</li><ul><li>subtract variable:</li><ul><li>which = countryInfectedVariable</li><li>value = 1</li></ul></ul></ul></ul>
