#Information
 - Title: Delayed Salaries
 - ID: army_professionalism_events.4
#Description
Delayed Salaries
#Options

___
##We must pay the elite troops

###AI weighting:
AI weights this option at 75


###Efects:<ul><li>add yearly manpower = -1.5</li></ul>

___
##Let them live off the land

###AI weighting:
AI weights this option at 25


###Efects:<ul><li>goto = delayed_salaries_province</li><li>add army professionalism = -0.05</li><li>event target:delayed salaries province:</li><ul><li>If area has controlled by is ROOT, and has AND has controlled by is event target:enemy country, and AND has any neighbor province has controlled by is ROOT:</li><ul><li>add devastation = 45</li></ul></ul></ul>
