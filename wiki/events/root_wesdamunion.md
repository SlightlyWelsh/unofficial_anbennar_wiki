#Information
 - Title: [Root.WesdamUnion]
 - ID: flavor_wesdam.6
#Description
[Root.WesdamUnion]
#Options

___
##They accepted!

###Available if:
<li>has country flag [accepted_pu](../flags/accepted_pu.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add prestige = 15</li><li>add trust:</li><ul><li>who = FROM</li><li>value = 25</li><li>mutual = yes</li></ul><li>create union = FROM</li><li>hidden effect:</li><ul><li>clr country flag [accepted_pu](../flags/accepted_pu.md)</li></ul></ul>

___
##They refused.

###Available if:
<li>has country flag [refused_pu](../flags/refused_pu.md)</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add prestige = -15</li><li>add opinion:</li><ul><li>modifier = opinion_spurned_pu</li><li>who = FROM</li></ul><li>add trust:</li><ul><li>who = FROM</li><li>value = -20</li><li>mutual = yes</li></ul><li>add casus belli:</li><ul><li>target = FROM</li><li>type = cb_restore_personal_union</li><li>months = 120</li></ul><li>hidden effect:</li><ul><li>clr country flag [refused_pu](../flags/refused_pu.md)</li></ul></ul>
