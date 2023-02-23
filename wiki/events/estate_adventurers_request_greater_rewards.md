#Information
 - Title: $ESTATE_ADVENTURERS$ Request Greater Rewards
 - ID: adventurers_estate_events.19
#Description
$ESTATE_ADVENTURERS$ Request Greater Rewards
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Fine, pay them a greater sum

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have years of income is 1.25
 - Multiplied by 0 if does not have estate influence has estate is estate adventurers, and estate influence has influence is 80


###Efects:<ul><li>add years of income = -1</li><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = EST_VAL_FORCED_COUNTRY_TO_GIVE_GREAT_REWARDS</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##Refuse to pay

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have estate loyalty has estate is estate adventurers, and estate loyalty has loyalty is 30


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_adventurers</li><li>loyalty = -20</li></ul></ul>
