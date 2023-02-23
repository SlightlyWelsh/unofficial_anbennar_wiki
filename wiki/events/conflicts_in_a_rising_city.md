#Information
 - Title: Conflicts in a Rising City
 - ID: artificers_estate_events.10
#Description
Conflicts in a Rising City
#Options

___
##Side with the $ESTATE_ARTIFICERS$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>If random owned province is not overseas, and  is not a capital, and  is not a colony, and  is not territory, and  has base production is 10, and  has base tax is 10, and  does not have seat in parliament, and  is state core is ROOT:</li><ul><li>add base production = 1</li></ul><li>add estate artificers loyalty effect = yes</li><li>reduce estate burghers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_CITY_GRANTED_TO_ARTIFICERS</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_CITY_GRANTED_TO_ARTIFICERS</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>

___
##Side with the $ESTATE_BURGHERS$.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 45
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>If random owned province is not overseas, and  is not a capital, and  is not a colony, and  is not territory, and  has base production is 10, and  has base tax is 10, and  does not have seat in parliament:</li><ul><li>add base tax = 1</li></ul><li>reduce estate artificers loyalty effect = yes</li><li>add estate burghers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_CITY_GRANTED_TO_MERCHANTS</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_CITY_GRANTED_TO_MERCHANTS</li><li>influence = 10</li><li>duration = 5475</li></ul></ul>

___
##Favor neither to retain control of the city.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 45
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 60
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 60


###Efects:<ul><li>reduce estate artificers loyalty effect = yes</li><li>reduce estate burghers loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_CITY_NOT_GRANTED</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_CITY_NOT_GRANTED</li><li>influence = -10</li><li>duration = 5475</li></ul></ul>
