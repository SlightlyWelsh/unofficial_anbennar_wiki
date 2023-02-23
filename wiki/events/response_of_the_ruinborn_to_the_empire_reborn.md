#Information
 - Title: Response of the Ruinborn to the Empire Reborn
 - ID: eordand.25
#Description
Response of the Ruinborn to the Empire Reborn
#Options

___
##They will make fine subjects.

###Available if:
<li>FROM:</li><ul><li>has country flag [accepted_vassalization](../flags/accepted_vassalization.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add prestige = 10</li><li>add trust:</li><ul><li>who = FROM</li><li>value = 25</li><li>mutual = yes</li></ul><li>vassalize = FROM</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>clr country flag [accepted_vassalization](../flags/accepted_vassalization.md)</li></ul></ul></ul>

___
##Perhaps they will be of more use on their own.

###Available if:
<li>FROM:</li><ul><li>has country flag [accepted_vassalization](../flags/accepted_vassalization.md)</li></ul>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>add trust:</li><ul><li>who = FROM</li><li>value = 25</li><li>mutual = yes</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>clr country flag [accepted_vassalization](../flags/accepted_vassalization.md)</li></ul></ul></ul>

___
##The audacity, refusing our generous offer?

###Available if:
<li>FROM:</li><ul><li>has country flag [refused_vassalization](../flags/refused_vassalization.md)</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add prestige = -10</li><li>add opinion:</li><ul><li>modifier = scornfully_insulted</li><li>who = FROM</li></ul><li>add trust:</li><ul><li>who = FROM</li><li>value = -20</li><li>mutual = yes</li></ul><li>add casus belli:</li><ul><li>target = FROM</li><li>type = cb_vassalize_mission</li><li>months = 120</li></ul><li>hidden effect:</li><ul><li>FROM:</li><ul><li>clr country flag [refused_vassalization](../flags/refused_vassalization.md)</li></ul></ul></ul>
