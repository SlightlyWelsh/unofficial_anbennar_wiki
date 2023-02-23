#Information
 - Title: Nobles Demand Increased Pensions
 - ID: 5071
#Description
Nobles Demand Increased Pensions
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if does not have stability is 0
 - Multiplied by 0.5 if is lucky
 - Multiplied by 0.66 if has stability is 3

#Options

___
##Accept their demands.

###AI weighting:
AI weights this option at 55


###Efects:<ul><li>country gets the modifier "tax_income_loss" for 20 years</li><li>add estate nobles loyalty effect = yes</li><li>If has country flag is [tyrant_system_initialized](../flags/tyrant_system_initialized.md):</li><ul><li>increase tyrant benevolent 1 = yes</li></ul></ul>

___
##Refuse their demands.

###AI weighting:
AI weights this option at 45
 - Multiplied by 1.5 if does not have stability is 1
 - Multiplied by 0 if has estate is estate nobles, and does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 30


###Efects:<ul><li>If does not have stability is -2:</li><ul><li>add adm power = -100</li></ul><li>If has stability is -2:</li><ul><li>add stability = -1</li></ul><li>reduce estate nobles loyalty effect = yes</li></ul>

___
##Let the [Root.Monarch.GetTitle] negotiate a better deal.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is charismatic_negotiator</li></ul>

###Efects:<ul><li>highlight = yes</li><li>country gets the modifier "tax_income_loss" for 15 years</li><li>add estate nobles loyalty effect = yes</li></ul>
