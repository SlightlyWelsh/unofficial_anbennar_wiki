#Information
 - Title: The Horde is not unified!
 - ID: tribal_estate_events.8
#Description
The Horde is not unified!
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Rely on the $ESTATE_NOMADIC_TRIBES$!

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.25 if has estate influence has estate is estate nomadic tribes, and estate influence has influence is 60


###Efects:<ul><li>add horde unity = 20</li><li>add estate influence modifier:</li><ul><li>estate = estate_nomadic_tribes</li><li>desc = EST_VAL_TRIBES_UNITY</li><li>influence = 10</li><li>duration = 7300</li></ul></ul>

___
##We do not need their help.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 35


###Efects:<ul><li>set country flag [refused_tribal_unity_aid](../flags/refused_tribal_unity_aid.md)</li><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -10</li></ul></ul>
