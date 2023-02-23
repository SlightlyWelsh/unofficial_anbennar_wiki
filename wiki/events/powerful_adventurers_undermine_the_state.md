#Information
 - Title: Powerful Adventurers Undermine the State
 - ID: adventurers_estate_events.18
#Description
Powerful Adventurers Undermine the State
#Mean Time to Happen:
Base time = 1 days

#Options

___
##They are too powerful, we must appease them for now

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have prestige is 30
 - Multiplied by 0 if does not have estate influence has estate is estate adventurers, and estate influence has influence is 80


###Efects:<ul><li>add prestige = -50</li><li>add estate adventurers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_UNDERMINING_THE_STATE</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##Remind them who they're speaking to!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have mil power is 100
 - Multiplied by 0 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 10
 - Multiplied by 1.25 if has estate influence has estate is estate adventurers, and estate influence has influence is 90


###Efects:<ul><li>add mil power = -100</li><li>reduce estate adventurers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_PUT_INTO_PLACE</li><li>influence = -20</li><li>duration = 3650</li></ul></ul>
