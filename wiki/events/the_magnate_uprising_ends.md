#Information
 - Title: The Magnate Uprising Ends
 - ID: magnate_uprising.2
#Description
The Magnate Uprising Ends
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Glory to the Magnates!

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [chose_magnates](../flags/chose_magnates.md)</li><li>None of the following:</li><ul><li>has country flag [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md)</li></ul></ul><li>AND:</li><ul><li>has country flag [chose_crown](../flags/chose_crown.md)</li><li>has country flag  just_lost_to_rebels_nl</li></ul></ul>

###Efects:<ul><li>If has country flag is [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md), and  is not controlled by the AI:</li><ul><li>add stability or adm power = yes</li><li>country gets the modifier magnates_enforced_control_lose for 50 years</li><li>define ruler:</li><ul><li>name = "Magnate Council"</li><li>dynasty = ""</li><li>adm = 2</li><li>dip = 2</li><li>mil = 2</li><li>age = 20</li></ul><li>exile heir as = cannot_return</li><li>the event [The Declaration of the Northern League](../events/the_declaration_of_the_northern_league.md) happens</li></ul><li>else:</li><ul><li>add stability or adm power = yes</li><li>add stability or adm power = yes</li><li>add republican tradition = 30</li><li>country gets the modifier magnates_enforced_control_win for 50 years</li><li>If is controlled by the AI, and  has country flag is [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md):</li><ul><li>define ruler:</li><ul><li>name = "Magnate Council"</li><li>dynasty = ""</li><li>adm = 2</li><li>dip = 2</li><li>mil = 2</li><li>age = 20</li></ul><li>exile heir as = cannot_return</li><li>the event [The Declaration of the Northern League](../events/the_declaration_of_the_northern_league.md) happens</li></ul></ul></ul>

___
##Glory to the Crown!

###Available if:
<li>Any of the following:</li><ul><li>All of the following:</li><ul><li>has country flag [chose_crown](../flags/chose_crown.md)</li><li>None of the following:</li><ul><li>has country flag [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md)</li></ul></ul><li>AND:</li><ul><li>has country flag [chose_magnates](../flags/chose_magnates.md)</li><li>has country flag  just_lost_to_rebels_nl</li></ul></ul>

###Efects:<ul><li>If has country flag is [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md), and  is not controlled by the AI:</li><ul><li>add stability or adm power = yes</li><li>country gets the modifier crown_enforced_control_lose for 50 years</li><li>change government = monarchy</li><li>set ruler = magnate_uprising_exiled_king</li><li>set heir = magnate_uprising_exiled_heir</li><li>override country name = ""</li></ul><li>else:</li><ul><li>add stability or adm power = yes</li><li>add stability or adm power = yes</li><li>add legitimacy = 30</li><li>country gets the modifier crown_enforced_control_win for 50 years</li><li>If is controlled by the AI, and  has country flag is [just_lost_to_rebels_nl](../flags/just_lost_to_rebels_nl.md):</li><ul><li>change government = monarchy</li><li>set ruler = magnate_uprising_exiled_king</li><li>set heir = magnate_uprising_exiled_heir</li><li>override country name = ""</li></ul></ul></ul>
