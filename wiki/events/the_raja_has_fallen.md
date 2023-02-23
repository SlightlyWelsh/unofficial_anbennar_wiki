#Information
 - Title: The Raja Has Fallen!
 - ID: rahenraj.1
#Description
The Raja Has Fallen!
#Options

___
##We are the heirs to the Harimraj.

###Available if:
<li>owner:</li><ul><li>has reform raja_reform</li></ul>

###Efects:<ul><li>custom tooltip = claiming_the_raj_tooltip</li><li>owner:</li><ul><li>If has country flag is [raj_was_vizier](../flags/raj_was_vizier.md):</li><ul><li>raj cohesion change absolute:</li><ul><li>amount = 15</li></ul><li>clr country flag [raj_was_vizier](../flags/raj_was_vizier.md)</li></ul><li>else:</li><ul><li>raj cohesion change absolute:</li><ul><li>amount = 20</li></ul></ul><li>the event ˻rahenraj.2100˼ happens</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>remove country modifier = raj_opened_senapti_ranks</li><li>remove country modifier = raj_closed_senapti_ranks</li></ul></ul></ul>

___
##An era comes to a close.

###Available if:
<li>owner:</li><ul><li>None of the following:</li><ul><li>has reform raja_reform</li></ul></ul>

###Efects:<ul><li>owner:</li><ul><li>add prestige = 20</li><li>add adm power = 50</li><li>add dip power = 50</li><li>add mil power = 50</li><li>set global flag [destroyed_raj](../flags/destroyed_raj.md)</li><li>4411:</li><ul><li>remove province modifier = rahen_corrupt_ministery_of_agriculture</li><li>remove province modifier = rahen_corrupt_ministery_of_philosophy</li><li>remove province modifier = rahen_corrupt_ministery_of_internal_relations</li><li>remove province modifier = rahen_corrupt_ministery_of_foreign_relations</li></ul></ul><li>hidden effect:</li><ul><li>rahen superregion:</li><ul><li>rahen clear court disaster province modifiers = yes</li></ul><li>FROM:</li><ul><li>remove country modifier = raj_opened_senapti_ranks</li><li>remove country modifier = raj_closed_senapti_ranks</li></ul></ul></ul>
