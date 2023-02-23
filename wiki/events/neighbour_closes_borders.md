#Information
 - Title: Neighbour Closes Borders
 - ID: blood_lotus_rebellion.223
#Description
Neighbour Closes Borders
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Traitors, all of them!

###Efects:<ul><li>blood lotus hardline stance change small:</li><ul><li>harimarihardline = yes</li></ul><li>add opinion:</li><ul><li>who = event_target:target_country</li><li>modifier = blood_lotus_rebellion_closed_borders</li></ul><li>If every owned province has any neighbor province has owned by is event target:target country:</li><ul><li>add province modifier:</li><ul><li>name = blood_lotus_rebellion_closed_borders_mod</li><li>duration = 3650</li></ul></ul></ul>

___
##Try to negotiate with the [target_country.Monarch.GetTitle] of [target_country.GetName]

###Efects:<ul><li>blood lotus hardline stance change small:</li><ul><li>neutral = yes</li></ul><li>event target:target country:</li><ul><li>the event [Border Negotiations](../events/border_negotiations.md) happens</li></ul></ul>

___
##Set up camps for the fleeing civilians, it's the least we can do

###Efects:<ul><li>blood lotus hardline stance change small:</li><ul><li>humanhardline = yes</li></ul><li>If every owned province has any neighbor province has owned by is event target:target country:</li><ul><li>add province modifier:</li><ul><li>name = blood_lotus_rebellion_set_up_border_camps_mod</li><li>duration = 3650</li></ul></ul></ul>
