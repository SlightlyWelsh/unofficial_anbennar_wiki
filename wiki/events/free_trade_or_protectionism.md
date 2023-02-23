#Information
 - Title: Free Trade or Protectionism?
 - ID: artificers_estate_events.3
#Description
Free Trade or Protectionism?
#Options

___
##The $ESTATE_BURGHERS$ are right: we need free trade.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate artificers, and estate influence has influence is 65
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>event target:target province:</li><ul><li>add base tax = 1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_ARTIFICERS_FREE_TRADE</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_BURGHERS_FREE_TRADE</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add mercantilism = -1</li><li>add dip power = 20</li></ul>

___
##The $ESTATE_ARTIFICERS$ are right: we need protectionism

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate artificers, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 1.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>event target:target province:</li><ul><li>add base production = 1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -15</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_ARTIFICERS_PROTECTIONISM</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHERS_PROTECTIONISM</li><li>influence = -10</li><li>duration = 5475</li></ul><li>add mercantilism = 1</li><li>add dip power = -20</li></ul>

___
##Try to please both by combining free trade with manufacturing subsidies.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate artificers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate artificers, and estate influence has influence is 65
 - Multiplied by 0.5 if does not have years of income is 0.5
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 40
 - Multiplied by 0.5 if has estate influence has estate is estate burghers, and estate influence has influence is 65


###Efects:<ul><li>event target:target province:</li><ul><li>add base production = 1</li><li>add base tax = 1</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 5</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_artificers</li><li>desc = EST_VAL_ARTIFICERS_PROTECTIONISM</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_burghers</li><li>desc = EST_VAL_BURGHERS_FREE_TRADE</li><li>influence = 10</li><li>duration = 5475</li></ul><li>add mercantilism = 1</li><li>add dip power = 20</li><li>add years of income = -0.5</li></ul>
