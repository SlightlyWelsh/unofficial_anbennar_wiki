#Information
 - Title: Orcish Slave Market
 - ID: orc_slavery.4
#Description
Orcish Slave Market
#Mean Time to Happen:
Base time = 25 years
 - Multiplied by 0.5 if has global flag is [orcish_slave_trade_banned_in_cannor](../flags/orcish_slave_trade_banned_in_cannor.md)
 - Multiplied by 0.8 if is prosperous
 - Multiplied by 0.75 if has development is 20
 - Multiplied by 1.5 if has owner has num of owned provinces with has value is 1, and num of owned provinces with has trade goods is slaves
 - Multiplied by 10 if has owner has num of owned provinces with has value is 5, and num of owned provinces with has trade goods is slaves

#Options

___
##Open for Business!

###AI weighting:
AI weights this option at 5


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base tax = 1</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base production = 1</li></ul>

###Efects:<ul><li>change trade goods = slaves</li><li>add permanent province modifier:</li><ul><li>name = orcish_slave_boom</li><li>duration = 9125</li></ul><li>add orcish minority size effect = yes</li><li>owner:</li><ul><li>large decrease of orcish tolerance effect = yes</li></ul><li>set add orc slaves count = yes</li></ul>

___
##Just sell your excess slaves

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>owner:</li><ul><li>add years of income = 0.5</li><li>medium decrease of orcish tolerance effect = yes</li></ul></ul>
