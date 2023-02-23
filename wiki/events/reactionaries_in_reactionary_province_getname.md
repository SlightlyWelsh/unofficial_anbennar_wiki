#Information
 - Title: Reactionaries in [reactionary_province.GetName]!
 - ID: center_of_revolution.9
#Description
Reactionaries in [reactionary_province.GetName]!
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2 if has country modifier is the reign of terror
 - Multiplied by 0.5 if has all owned province has revolution in province

#Options

___
##We shall crush these enemies of the people!

###AI weighting:
AI weights this option at 1
 - Multiplied by 0 if has num of rebel armies is 5, and has num of rebel controlled provinces is 5


###Efects:<ul><li>event target:reactionary province:</li><ul><li>spawn rebels:</li><ul><li>size = 1.5</li><li>type = pretender_rebels</li></ul></ul></ul>

___
##They are not worthy of our attention.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>event target:reactionary province:</li><ul><li>remove revolution from province effect = yes</li></ul><li>add revolutionary zeal = -5</li></ul>
