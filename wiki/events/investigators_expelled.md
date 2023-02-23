#Information
 - Title: Investigators Expelled
 - ID: new_sun_cult.188
#Description
Investigators Expelled
#Options

___
##They had reason to accuse you then? Sounds suspicious!

###Available if:
<li>None of the following:</li><ul><li>is in war:</li><ul><li>casus belli is cb_nsc_investigation</li><li>attacker leader is FROM</li></ul></ul>

###AI weighting:
AI weights this option at 99
 - Multiplied by 0 if does not have check variable has which is armyStrengthRatio, and check variable has value is 0.5
 - Multiplied by 0 if has FROM is not controlled by the AI; and does not have check variable has which is armyStrengthRatio, and check variable has value is 0.7
 - Multiplied by 0 if has calc true if has all known country has war with is ROOT; and calc true if has amount is 3


###Efects:<ul><li>declare war with cb:</li><ul><li>who = FROM</li><li>casus belli = cb_nsc_investigation</li></ul><li>custom tooltip = nsc_1v1_tt</li><li>hidden effect:</li><ul><li>If has country flag is [nsc_is_investigated_by_@FROM](../flags/nsc_is_investigated_by_from.md):</li><ul><li>clr country flag [nsc_is_investigated_by_@FROM](../flags/nsc_is_investigated_by_from.md)</li><li>FROM:</li><ul><li>the event [Investigators Expelled](../events/investigators_expelled.md) happens</li></ul></ul><li>If is not controlled by the AI, and  has FROM is controlled by the AI:</li><ul><li>FROM:</li><ul><li>set country flag [nsc_was_at_war_with_@ROOT](../flags/nsc_was_at_war_with_root.md)</li></ul></ul><li>If is controlled by the AI, and  has FROM is not controlled by the AI:</li><ul><li>set country flag [nsc_was_at_war_with_@FROM](../flags/nsc_was_at_war_with_from.md)</li></ul></ul></ul>

___
##Nothing we can do about it then, they should've had more tact.

###Available if:
<li>None of the following:</li><ul><li>is in war:</li><ul><li>casus belli is cb_nsc_investigation</li><li>attacker leader is FROM</li></ul></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add prestige = -5</li></ul>

___
##Ok.

###Available if:
<li>is in war:</li><ul><li>casus belli is cb_nsc_investigation</li><li>attacker leader is FROM</li></ul>
