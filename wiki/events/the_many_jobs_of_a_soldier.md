#Information
 - Title: The many jobs of a Soldier
 - ID: army_professionalism_events.5
#Description
The many jobs of a Soldier
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 1.1 if does not have had recent war is 20

#Options

___
##They must not be allowed to do dabble in the roles other occupations.

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>add years of income = -0.45</li></ul>

___
##We will allow it for now.

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>goto = soldier_province</li><li>add army professionalism = -0.05</li><li>event target:soldier province:</li><ul><li>If area has owned by is ROOT:</li><ul><li>add province modifier:</li><ul><li>name = "soldiers_stimulating_local_economy"</li><li>duration = 3650</li></ul></ul></ul></ul>
