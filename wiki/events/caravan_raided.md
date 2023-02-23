#Information
 - Title: Caravan Raided
 - ID: new_sun_cult.167
#Description
Caravan Raided
#Options

___
##Help the merchants recover.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has num of loans is 5


###Efects:<ul><li>set country flag [nsc_caravan_raided](../flags/nsc_caravan_raided.md)</li><li>nsc increase tension small effect = yes</li><li>add treasury = -50</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 10</li></ul><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -15</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour</li></ul></ul>

___
##We can't afford to pay for their loss.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if does not have estate loyalty has estate is estate burghers, and estate loyalty has loyalty is 30


###Efects:<ul><li>set country flag [nsc_caravan_raided](../flags/nsc_caravan_raided.md)</li><li>nsc increase tension small effect = yes</li><li>country gets the modifier nsc_raided_merchants for 10 years</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li></ul><li>add trust:</li><ul><li>who = event_target:nsc_target_country</li><li>value = -15</li><li>mutual = no</li></ul><li>add opinion:</li><ul><li>who = event_target:nsc_target_country</li><li>modifier = nsc_suspicious_behaviour</li></ul></ul>
