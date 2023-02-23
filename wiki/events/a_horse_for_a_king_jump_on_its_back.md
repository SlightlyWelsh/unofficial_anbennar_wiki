#Information
 - Title: A Horse for a King: Jump on its back!
 - ID: flavor_adenica.13
#Description
A Horse for a King: Jump on its back!
#Options

___
##Keep holding on.

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has mil is 4
 - Multiplied by 0 if has ruler has personality is craven personality
 - Multiplied by 0 if has ruler has personality is careful personality


###Efects:<ul><li>add prestige = 10</li><li>set country flag [horse_hold](../flags/horse_hold.md)</li><li>If has mil is 4, and does not have mil is 5:</li><ul><li>random:</li><ul><li>chance = 25</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul></ul></ul><li>Else if has mil is 5, and does not have mil is 6:</li><ul><li>random:</li><ul><li>chance = 15</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul></ul></ul><li>Else if has mil is 6:</li><ul><li>random:</li><ul><li>chance = 5</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul></ul></ul><li>else:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add ruler modifier:</li><ul><li>name = adenica_injured</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Drop off in disgrace.

###Efects:<ul><li>add prestige = -10</li><li>set country flag [horse_drop](../flags/horse_drop.md)</li></ul>
