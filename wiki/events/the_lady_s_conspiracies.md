#Information
 - Title: The Lady's Conspiracies
 - ID: vampires_estate_events.500
#Description
The Lady's Conspiracies
#Mean Time to Happen:
Base time = 15 years
 - Multiplied by 0.6 if has estate loyalty has estate is estate vampires, and estate loyalty has loyalty is 50
 - Multiplied by 0.6 if has estate loyalty has estate is estate vampires, and estate loyalty has loyalty is 70
 - Multiplied by 2 if does not have estate loyalty has estate is estate vampires, and estate loyalty has loyalty is 40
 - Multiplied by 2 if does not have estate loyalty has estate is estate vampires, and estate loyalty has loyalty is 20

#Options

___
##There's nothing quite like a good heist!

###Efects:<ul><li>If every known country has spy network from has who is ROOT, and has spy network from has value is 65:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -30</li></ul><li>add years of income = -1</li></ul><li>add years of income = 1</li><li>add estate influence modifier:</li><ul><li>estate = estate_vampires</li><li>desc = EST_VAMPIRES_MINOR_OPERATIONS</li><li>influence = 5</li><li>duration = 1825</li></ul></ul>

___
##There's nothing quite like a good heist!

###Efects:<ul><li>If every known country has spy network from has who is ROOT, and has spy network from has value is 65:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -30</li></ul><li>export to variable:</li><ul><li>which = yearly_income</li><li>value = monthly_income</li></ul><li>multiply variable:</li><ul><li>which = yearly_trade_income</li><li>value = 12</li></ul><li>If while has check variable has which is yearly income, and check variable has value is 1:</li><ul><li>add treasury = -1</li><li>ROOT:</li><ul><li>add treasury = 1</li></ul><li>subtract variable:</li><ul><li>which = yearly_income</li><li>value = 1</li></ul></ul></ul><li>add estate influence modifier:</li><ul><li>estate = estate_vampires</li><li>desc = EST_VAMPIRES_MINOR_OPERATIONS</li><li>influence = 5</li><li>duration = 1825</li></ul></ul>

___
##Perhaps there are some valuable secrets to be found?

###Efects:<ul><li>If every known country has spy network from has who is ROOT, and has spy network from has value is 65:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -40</li></ul><li>add adm power = -30</li><li>add dip power = -30</li><li>add mil power = -30</li></ul><li>add adm power = 30</li><li>add dip power = 30</li><li>add mil power = 30</li><li>add estate influence modifier:</li><ul><li>estate = estate_vampires</li><li>desc = EST_VAMPIRES_MINOR_OPERATIONS</li><li>influence = 5</li><li>duration = 2555</li></ul></ul>

___
##Give their nobles a taste for blood...

###Efects:<ul><li>If every known country has spy network from has who is ROOT, and has spy network from has value is 65:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -50</li></ul><li>add corruption = 3</li><li>country gets the modifier ravenmarch_ladysbirds_corrupt for 10 years</li></ul></ul>

___
##A murder in their royal council will do nicely.

###Efects:<ul><li>If every known country has spy network from has who is ROOT, and has spy network from has value is 65:</li><ul><li>add spy network from:</li><ul><li>who = ROOT</li><li>value = -65</li></ul><li>kill advisor = random</li><li>reduce stability or adm power = yes</li></ul></ul>
