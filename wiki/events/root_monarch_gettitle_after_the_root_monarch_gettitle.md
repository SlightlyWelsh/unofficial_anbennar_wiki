#Information
 - Title: [Root.Monarch.GetTitle] after the [Root.Monarch.GetTitle]
 - ID: tribal_estate_events.11
#Description
[Root.Monarch.GetTitle] after the [Root.Monarch.GetTitle]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##A new heir it is!

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has heir:</li><ul><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul><li>define heir:</li><ul><li>dynasty = ROOT</li><li>claim = 15</li><li>age = 45</li></ul><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_KINGMAKERS</li><li>estate = estate_nomadic_tribes</li><li>influence = 10</li><li>duration = 3650</li></ul></ul>

___
##These tribes must know their place!

###AI weighting:
AI weights this option at 99
 - Multiplied by 0.01 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 45


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -20</li></ul><li>add estate influence modifier:</li><ul><li>desc = EST_VAL_REFUSED_TO_ALTER_SUCCESSION</li><li>estate = estate_nomadic_tribes</li><li>influence = -10</li><li>duration = 3650</li></ul></ul>
