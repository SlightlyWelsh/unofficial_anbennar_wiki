#Information
 - Title: Investigators From [From.GetName] are Getting Disrespectful
 - ID: new_sun_cult.187
#Description
Investigators From [From.GetName] are Getting Disrespectful
#Options

___
##Just a little longer, just a little longer.

###AI weighting:
AI weights this option at 0.75


###Efects:<ul><li>reduce stability or adm power = yes</li><li>add legitimacy = -15</li><li>country gets the modifier nsc_disrespected_by_investigators for 25 years</li><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_disrespectful_investigators</li></ul></ul>

___
##*Loud incoherent sounds of royal displeasure*

###AI weighting:
AI weights this option at 250
 - Multiplied by 0.001 if does not have check variable has which is armyStrengthRatio, and check variable has value is 0.2
 - Multiplied by 0 if has calc true if has all known country has war with is ROOT; and calc true if has amount is 3
 - Multiplied by 0 if has any known country has war with is ROOT, and any known country has war score against has who is ROOT, and war score against has value is 50


###Efects:<ul><li>add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_disrespectful_investigators</li></ul><li>reverse add opinion:</li><ul><li>who = FROM</li><li>modifier = nsc_expelled_investigators</li></ul><li>custom tooltip = nsc_they_might_declare_war_tt</li><li>hidden effect:</li><ul><li>clr country flag [nsc_is_investigated_by_@FROM](../flags/nsc_is_investigated_by_from.md)</li><li>clr country flag [nsc_@FROM_diplomat_sent](../flags/nsc_from_diplomat_sent.md)</li><li>set country flag [nsc_has_expelled_@FROM](../flags/nsc_has_expelled_from.md)</li><li>FROM:</li><ul><li>the event [Investigators Expelled](../events/investigators_expelled.md) happens</li></ul><li>change variable:</li><ul><li>which = investigationAgainstVar</li><li>value = -1</li></ul></ul></ul>
