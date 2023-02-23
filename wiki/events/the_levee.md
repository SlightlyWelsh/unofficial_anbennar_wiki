#Information
 - Title: The Levee
 - ID: nobles_estate_events.7
#Description
The Levee
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let's keep it at a modest level.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.3 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35
 - Multiplied by 1.5 if has estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 60


###Efects:<ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul><li>set country flag [normal_court_life](../flags/normal_court_life.md)</li></ul>

___
##An elaborate and lengthy ceremony for the most influential.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.0 if does not have years of income is 0.5
 - Multiplied by 1.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>add years of income = -0.4</li><li>country gets the modifier "elaborate_court_ceremonies" for 25 years</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 20</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_ELABORATE_COURT_CEREMONIES</li><li>influence = -15</li><li>duration = 9125</li></ul></ul>

___
##We have no need of such things.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.5 if does not have estate loyalty has estate is estate nobles, and estate loyalty has loyalty is 35


###Efects:<ul><li>add prestige = -5</li><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -15</li></ul><li>add estate influence modifier:</li><ul><li>estate = estate_nobles</li><li>desc = EST_VAL_NOBLES_DENIED_ACCESS_TO_ROYAL_BEDROOM</li><li>influence = -10</li><li>duration = 9125</li></ul></ul>
