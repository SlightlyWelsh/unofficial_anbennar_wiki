#Information
 - Title: Administrating Dameria
 - ID: flavor_wex.2
#Description
Administrating Dameria
#Options

___
##Grant the conquered lands autonomy under local Rose Party nobles.

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>create vassal = Z40</li><li>create subject:</li><ul><li>subject type = autonomous_vassal</li><li>subject = Z40</li></ul><li>Z40:</li><ul><li>remove opinion:</li><ul><li>who = A30</li><li>modifier = released_vassal</li></ul><li>add opinion:</li><ul><li>who = A30</li><li>modifier = wex_loyalist_rule</li></ul></ul><li>create vassal = Z41</li><li>create subject:</li><ul><li>subject type = autonomous_vassal</li><li>subject = Z41</li></ul><li>Z41:</li><ul><li>remove opinion:</li><ul><li>who = A30</li><li>modifier = released_vassal</li></ul><li>add opinion:</li><ul><li>who = A30</li><li>modifier = wex_loyalist_rule</li></ul></ul><li>create vassal = Z42</li><li>create subject:</li><ul><li>subject type = autonomous_vassal</li><li>subject = Z42</li></ul><li>Z42:</li><ul><li>remove opinion:</li><ul><li>who = A30</li><li>modifier = released_vassal</li></ul><li>add opinion:</li><ul><li>who = A30</li><li>modifier = wex_loyalist_rule</li></ul></ul><li>set country flag [lothane_benevolent](../flags/lothane_benevolent.md)</li></ul>

___
##Crush the rebellions; stamp out all resistance.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>If every owned province has province id is 2, and has province id is 5, and has province id is 276, and has province id is 281, and has province id is 330, and has province id is 910; and does not have core is A30:</li><ul><li>add devastation = 50</li><li>add core = A30</li><li>custom tooltip = wex_rebellion_tt</li><li>hidden effect:</li><ul><li>add province modifier:</li><ul><li>name = wex_rebellious_damerians</li><li>duration = -1</li><li>desc = desc_wex_rebellious_damerians</li></ul></ul></ul><li>add stability = 1</li><li>set country flag [lothane_conqueror](../flags/lothane_conqueror.md)</li></ul>
