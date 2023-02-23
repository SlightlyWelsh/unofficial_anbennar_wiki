#Information
 - Title: Republican Scheming in [province_to_revolution.GetName]
 - ID: center_of_revolution.10
#Description
Republican Scheming in [province_to_revolution.GetName]
#Options

___
##They shall have our support.

###Efects:<ul><li>add revolutionary zeal = 5</li><li>add mil power = -50</li><li>tooltip:</li><ul><li>event target:province to revolution:</li><ul><li>set revolution in province = yes</li></ul></ul><li>event target:neighbour country:</li><ul><li>tooltip:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_revolutionary_coup_in_our_province</li></ul></ul><li>the event [Coup in [province_to_revolution.GetName]](../events/coup_in_province_to_revolution_getname.md) happens</li></ul></ul>

___
##We should not intervene in [neighbour_country.GetAdjective] affairs.

###Efects:<ul><li>add revolutionary zeal = -5</li><li>event target:neighbour country:</li><ul><li>add opinion:</li><ul><li>who = root</li><li>modifier = opinion_non_intervention</li></ul></ul></ul>
