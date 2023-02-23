#Information
 - Title: Temple Quest - Traps!
 - ID: spirits.505
#Description
Temple Quest - Traps!
#Options

___
##Keep searching, but watch for traps.

###Available if:
<li>None of the following:</li><ul><li>religion is lefthand_path</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if has check variable has which is TempleQuestPartySize, and check variable has value is 4


###Efects:<ul><li>custom tooltip = temple_quest_deeper_tooltip</li><li>hidden effect:</li><ul><li>temple quest roll next encounter = yes</li></ul></ul>

___
##Keep going - we must find the Heart!

###Available if:
<li>religion is lefthand_path</li>

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if has check variable has which is TempleQuestPartySize, and check variable has value is 4


###Efects:<ul><li>custom tooltip = temple_quest_deeper_tooltip</li><li>hidden effect:</li><ul><li>temple quest roll next encounter = yes</li></ul></ul>

___
##Let's rest before continuing.

###Available if:
<li>check variable:</li><ul><li>which is WoundedPartyMembers</li><li>value is at least 1</li></ul><li>check variable:</li><ul><li>which is RestsRemaining</li><li>value is at least 1</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 2 if has check variable has which is WoundedPartyMembers, and check variable has value is 2
 - Multiplied by 10 if has check variable has which is WoundedPartyMembers, and check variable has value is 3


###Efects:<ul><li>custom tooltip = temple_quest_rest_tooltip</li><li>hidden effect:</li><ul><li>subtract variable:</li><ul><li>which = RestsRemaining</li><li>value = 1</li></ul><li>temple quest rest = yes</li><li>temple quest roll next encounter = yes</li></ul></ul>

___
##We've taken a beating - it's time to go home.

###Available if:
<li>None of the following:</li><ul><li>religion is lefthand_path</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 10 if does not have check variable has which is RestsRemaining, and check variable has value is 1; and does not have check variable has which is TempleQuestPartySize, and check variable has value is 2


###Efects:<ul><li>custom tooltip = temple_quest_voluntary_end_tooltip</li><li>hidden effect:</li><ul><li>end temple quest = yes</li><li>temple quest cash out = yes</li></ul></ul>
