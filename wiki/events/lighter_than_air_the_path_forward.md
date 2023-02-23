#Information
 - Title: Lighter than Air: The Path Forward
 - ID: flavor_feiten.211
#Description
Lighter than Air: The Path Forward
#Options

___
##This... 'electrolysis' of water seems very promising, if expensive.

###Efects:<ul><li>If has check variable has which is MaxArtificePoints, and check variable has value is 100:</li><ul><li>add mil power = -50</li><li>add years of income = -0.5</li><li>debuff artifice points 5 = yes</li></ul><li>Else if has check variable has which is MaxArtificePoints, and check variable has value is 50:</li><ul><li>add mil power = -100</li><li>add years of income = -1</li><li>debuff artifice points 5 = yes</li></ul><li>else:</li><ul><li>add mil power = -200</li><li>add years of income = -2</li><li>debuff artifice points 5 = yes</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 1</li></ul></ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 0</li></ul></ul></ul></ul></ul>

___
##Oil of vitriol is well characterized and easy to make - it will serve us well.

###Available if:
<li>has estate estate_mages</li>

###Efects:<ul><li>If has estate influence has estate is estate mages, and estate influence has influence is 66:</li><ul><li>add adm power = -50</li><li>add years of income = -0.5</li></ul><li>Else if has estate influence has estate is estate mages, and estate influence has influence is 33:</li><ul><li>add adm power = -100</li><li>add years of income = -1</li></ul><li>else:</li><ul><li>add adm power = -200</li><li>add years of income = -2</li></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 2</li></ul></ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 1</li></ul></ul></ul></ul></ul>

___
##Coal into gas - the most ambitious concept yet. I like it!

###Available if:
<li>coal is at least 1</li>

###Efects:<ul><li>If has num of owned provinces with has value is 3, and num of owned provinces with has trade goods is coal, and num of owned provinces with has building is university, and num of owned provinces with has production building trigger is yes, and num of owned provinces with has manufactory trigger is yes:</li><ul><li>add adm power = -100</li><li>add years of income = -1</li></ul><li>Else if has num of owned provinces with has value is 2, and num of owned provinces with has trade goods is coal, and num of owned provinces with has building is university, and num of owned provinces with has production building trigger is yes, and num of owned provinces with has manufactory trigger is yes:</li><ul><li>add adm power = -200</li><li>add years of income = -2</li></ul><li>else:</li><ul><li>add adm power = -400</li><li>add years of income = -4</li></ul><li>If every owned province has trade goods is coal:</li><ul><li>add province modifier:</li><ul><li>name = feiten_coal_gasification</li><li>duration = -1</li></ul></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 2</li></ul></ul><li>1:</li><ul><li>change variable:</li><ul><li>which = feiten_lighter_than_air_tracker</li><li>value = 3</li></ul></ul></ul></ul></ul>
