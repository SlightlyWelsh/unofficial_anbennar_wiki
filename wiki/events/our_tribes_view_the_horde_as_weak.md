#Information
 - Title: Our Tribes view the Horde as weak!
 - ID: tribal_estate_events.7
#Description
Our Tribes view the Horde as weak!
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Rely on the $ESTATE_NOMADIC_TRIBES$!

###AI weighting:
AI weights this option at 75
 - Multiplied by 0.25 if has estate influence has estate is estate nomadic tribes, and estate influence has influence is 60


###Efects:<ul><li>add army tradition = 10</li><li>add estate influence modifier:</li><ul><li>estate = estate_nomadic_tribes</li><li>desc = EST_VAL_TRIBES_ARMY</li><li>influence = 10</li><li>duration = 7300</li></ul></ul>

___
##We do not need their help.

###AI weighting:
AI weights this option at 25
 - Multiplied by 2.0 if does not have estate loyalty has estate is estate nomadic tribes, and estate loyalty has loyalty is 35


###Efects:<ul><li>set country flag [refused_tribal_armies](../flags/refused_tribal_armies.md)</li><li>add estate loyalty:</li><ul><li>estate = estate_nomadic_tribes</li><li>loyalty = -10</li></ul></ul>
