#Information
 - Title: The Angry Man from [william_jones_province.GetName]
 - ID: center_of_revolution.2
#Description
The Angry Man from [william_jones_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Let them leave, we are better off without them.

###AI weighting:
AI weights this option at 60


###Efects:<ul><li>event target:william jones province:</li><ul><li>add base tax = -1</li><li>add base production = -1</li><li>add base manpower = -1</li></ul><li>event target:destination country:</li><ul><li>capital scope:</li><ul><li>add base tax = 1</li><li>add base production = 1</li><li>add base manpower = 1</li></ul><li>If is colonial nation of is root:</li><ul><li>add liberty desire = 20</li></ul><li>else:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_hostile_expats</li></ul></ul></ul></ul>

___
##We cannot permit this migration to the colonies.

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:william jones province:</li><ul><li>random list:</li><ul><li>1:</li><ul><li>If has root has num of cities is 12:</li><ul><li>If area has owned by is root, and does not have province modifier is no revolution here dummy:</li><ul><li>set revolution in province = yes</li></ul></ul><li>else:</li><ul><li>set revolution in province = yes</li></ul></ul><li>1:</li><ul><li>If has root has num of cities is 12:</li><ul><li>If area has owned by is root:</li><ul><li>add unrest = 6</li></ul></ul><li>else:</li><ul><li>add unrest = 6</li></ul></ul></ul></ul></ul>
