#Information
 - Title: Foreign Military Expert
 - ID: random_event.11
#Description
Foreign Military Expert
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Ask him to train our officers.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.5 if does not have years of income is 0.5


###Efects:<ul><li>add years of income = -0.15</li><li>add army tradition = 10</li><li>If does not have monthly income is 15:</li><ul><li>define advisor:</li><ul><li>name = foreign_military_expert</li><li>type = army_reformer</li><li>religion = event_target:advisor_origin_country</li><li>culture = event_target:advisor_origin_country</li><li>skill = 1</li><li>discount = yes</li></ul></ul><li>Else if does not have monthly income is 25:</li><ul><li>define advisor:</li><ul><li>name = foreign_military_expert</li><li>type = army_reformer</li><li>religion = event_target:advisor_origin_country</li><li>culture = event_target:advisor_origin_country</li><li>skill = 2</li><li>discount = yes</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>name = foreign_military_expert</li><li>type = army_reformer</li><li>religion = event_target:advisor_origin_country</li><li>culture = event_target:advisor_origin_country</li><li>skill = 3</li><li>discount = yes</li></ul></ul></ul>

___
##Put him in command of our armies.

###AI weighting:
AI weights this option at 33
 - Multiplied by 0.5 if does not have years of income is 0.25


###Efects:<ul><li>add years of income = -0.15</li><li>create general:</li><ul><li>name = foreign_military_expert</li><li>tradition = 70</li></ul></ul>

___
##We do not need foreign aid!

###AI weighting:
AI weights this option at 33


###Efects:<ul><li>If has years of income is 0.15:</li><ul><li>add legitimacy = 10</li></ul><li>else:</li><ul><li>add legitimacy = 5</li></ul></ul>
