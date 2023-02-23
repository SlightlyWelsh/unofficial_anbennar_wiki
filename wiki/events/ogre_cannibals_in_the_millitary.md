#Information
 - Title: Ogre Cannibals In the Millitary
 - ID: ogre_tolerance_events.6
#Description
Ogre Cannibals In the Millitary
#Options

___
##Ogres need to eat

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.1 if has wants to increase tolerance ogre is yes


###Efects:<ul><li>add mil power = -50</li><li>country gets the modifier ogre_ritual_cannibalism_allowed for 10 years</li><li>medium increase of ogre tolerance effect = yes</li></ul>

___
##Keep the rituals discrete

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>country gets the modifier ogre_ritual_cannibalism_restricted for 10 years</li><li>small decrease of ogre tolerance effect = yes</li></ul>

___
##People aren't food!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to increase tolerance ogre is yes


###Efects:<ul><li>country gets the modifier ogre_ritual_cannibalism_outlawed for 10 years</li><li>medium decrease of ogre tolerance effect = yes</li></ul>

___
##Those are potential recruits! Don't eat them!

###Available if:
<li>has country modifier undead_military</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>country gets the modifier ogre_ritual_cannibalism_outlawed for 10 years</li><li>add yearly manpower = 0.5</li><li>medium decrease of ogre tolerance effect = yes</li></ul>
