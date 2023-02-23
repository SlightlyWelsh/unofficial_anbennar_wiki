#Information
 - Title: Investigators From [From.GetName] are Getting Nosy
 - ID: new_sun_cult.186
#Description
Investigators From [From.GetName] are Getting Nosy
#Options

___
##Bear with them, it will not be much longer.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add legitimacy = -10</li><li>country gets the modifier nsc_intrusive_investigators for 25 years</li><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_nosy_investigators</li></ul></ul>

___
##Get them out of my sight! I want them gone from my lands!

###AI weighting:
AI weights this option at 1000
 - Multiplied by 0 if does not have check variable has which is armyStrengthRatio, and check variable has value is 0.4
 - Multiplied by 0 if has calc true if has all known country has war with is ROOT; and calc true if has amount is 3
 - Multiplied by 0 if has any known country has war with is ROOT, and any known country has war score against has who is ROOT, and war score against has value is 50


###Efects:<ul><li>custom tooltip = nsc_they_might_declare_war_tt</li><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_nosy_investigators</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_expelled_investigators</li></ul><li>hidden effect:</li><ul><li>clr country flag [nsc_is_investigated_by_@FROM](../flags/nsc_is_investigated_by_from.md)</li><li>clr country flag [nsc_@FROM_diplomat_sent](../flags/nsc_from_diplomat_sent.md)</li><li>set country flag [nsc_has_expelled_@FROM](../flags/nsc_has_expelled_from.md)</li><li>FROM:</li><ul><li>the event [Investigators Expelled](../events/investigators_expelled.md) happens</li></ul><li>change variable:</li><ul><li>which = investigationAgainstVar</li><li>value = -1</li></ul></ul></ul>
