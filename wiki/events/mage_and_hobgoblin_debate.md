#Information
 - Title: Mage and Hobgoblin Debate
 - ID: hobgoblin_tolerance_events.2
#Description
Mage and Hobgoblin Debate
#Options

___
##Control the mages

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance hobgoblin is yes


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -10</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_HOBGOBLIN_SIDED_HOBGOBLIN</li><li>influence = -10</li><li>duration = 3650</li></ul><li>largest increase of hobgoblin tolerance effect = yes</li></ul>

___
##Argue somewhere else

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>small increase of hobgoblin tolerance effect = yes</li><li>reduce estate mages loyalty effect = yes</li></ul>

___
##We will not tolerate this!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to increase tolerance hobgoblin is yes


###Efects:<ul><li>medium decrease of hobgoblin tolerance effect = yes</li><li>add estate mages loyalty effect = yes</li><li>add estate influence modifier:</li><ul><li>estate = estate_mages</li><li>desc = EST_VAL_HOBGOBLIN_SIDED_MAGES</li><li>influence = 10</li><li>duration = 3650</li></ul><li>country gets the modifier hobgoblin_mages_rebellion for 10 years</li></ul>
