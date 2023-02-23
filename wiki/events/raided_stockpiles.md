#Information
 - Title: Raided Stockpiles
 - ID: flavor_seghdihr.52
#Description
Raided Stockpiles
#Options

___
##What else could happen?

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>If does not have event target:incursion target has province id is 4218:</li><ul><li>event target:incursion target:</li><ul><li>random:</li><ul><li>chance = 50</li><li>If has base production is 2:</li><ul><li>add base production = -1</li></ul><li>else:</li><ul><li>ROOT:</li><ul><li>add dip power = -25</li></ul></ul></ul><li>add devastation = 20</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_supplies_raided</li><li>duration = 3650</li></ul><li>If every neighbor province is city, and  has country or subject holds is ROOT:</li><ul><li>random:</li><ul><li>chance = 50</li><li>If has base production is 2:</li><ul><li>add base production = -1</li></ul><li>else:</li><ul><li>ROOT:</li><ul><li>add dip power = -25</li></ul></ul></ul><li>add devastation = 10</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_supplies_raided</li><li>duration = 1825</li></ul></ul></ul></ul><li>else:</li><ul><li>ozumbrog area:</li><ul><li>add base production = -2</li><li>add devastation = 20</li><li>add unrest = 2</li><li>add province modifier:</li><ul><li>name = seghdihr_incursion_supplies_raided</li><li>duration = 3650</li></ul></ul></ul><li>custom tooltip = seghdihr_incursion_strength_gathered</li><li>hidden effect:</li><ul><li>change variable:</li><ul><li>which = incursion_gathering_strength</li><li>value = 300</li></ul><li>If has check variable has which is incursion gathering strength, and check variable has value is 1100:</li><ul><li>set variable:</li><ul><li>which = incursion_gathering_strength</li><li>value = 1000</li></ul></ul><li>seghdihr calculate incursion strength = yes</li><li>If has H74 has exists, and H74 is controlled by the AI:</li><ul><li>H74:</li><ul><li>add adm power = 300</li><li>add dip power = 300</li><li>add mil power = 300</li><li>add treasury = 500</li></ul></ul></ul></ul>
