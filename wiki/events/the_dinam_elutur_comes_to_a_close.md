#Information
 - Title: The Dinam Elutur Comes to a Close
 - ID: new_sun_cult.39
#Description
The Dinam Elutur Comes to a Close
#Options

___
##Ok.

###Available if:
<li>None of the following:</li><ul><li>has country flag [dinam_elutur_lost](../flags/dinam_elutur_lost.md)</li></ul><li>is not controlled by the AI</li>

###Efects:<ul><li>add stability or adm power = yes</li><li>add stability or adm power = yes</li><li>decrease nsc isolation level = yes</li><li>If isolationism is 3:</li><ul><li>decrease nsc isolation level = yes</li></ul><li>custom tooltip = nsc_dinam_elutur_will_be_back_tt</li><li>remove country modifier = nsc_army_more_paid</li></ul>

___
##Ok.

###Available if:
<li>has country flag [dinam_elutur_lost](../flags/dinam_elutur_lost.md)</li><li>is not controlled by the AI</li>

###Efects:<ul><li>add prestige = -50</li><li>custom tooltip = nsc_dinam_elutur_will_be_back_tt</li><li>clr country flag [dinam_elutur_lost](../flags/dinam_elutur_lost.md)</li><li>clr country flag [locked_racial_administration](../flags/locked_racial_administration.md)</li><li>If has continent is north america, and has continent is south america:</li><ul><li>change primary culture = dawn_elf</li></ul><li>else:</li><ul><li>change primary culture = sun_elf</li><li>If does not have government is monarchy:</li><ul><li>change government = monarchy</li></ul><li>add government reform = phoenix_akalate</li></ul><li>If has heir, and does not have heir culture is sun elf; and does not have heir culture is dawn elf:</li><ul><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul><li>If has consort, and does not have consort culture is sun elf; and does not have consort culture is dawn elf:</li><ul><li>remove consort = yes</li></ul><li>If does not have ruler culture is sun elf; and does not have ruler culture is dawn elf:</li><ul><li>kill ruler = yes</li></ul><li>If does not have country modifier is elven administration:</li><ul><li>clear racial administration = yes</li><li>country gets the modifier restructuring_administration for 10 years</li><li>country gets the modifier elven_administration until otherwise removed</li></ul><li>set country flag [locked_racial_administration](../flags/locked_racial_administration.md)</li><li>If has tag is F52:</li><ul><li>If has religion is bulwari sun cult, and does not have exists is F38:</li><ul><li>change tag = F38</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>swap non generic missions = yes</li><li>If has idea is F52 independent judicial system:</li><ul><li>swap free idea group = yes</li></ul><li>set country flag [restored_phoenix_empire_flag](../flags/restored_phoenix_empire_flag.md)</li><li>lock racial admin = yes</li></ul><li>Else if has religion is the jadd, and does not have exists is F51:</li><ul><li>change tag = F51</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>swap non generic missions = yes</li><li>If has idea is F52 independent judicial system:</li><ul><li>swap free idea group = yes</li></ul><li>If does not have government is monarchy:</li><ul><li>change government = monarchy</li></ul><li>add government reform = jadd_empire</li><li>If has dlc is "Dharma":</li><ul><li>add government reform = jadd_nobility</li></ul><li>the event [The Seat of the Court](../events/the_seat_of_the_court.md) happens</li><li>set country flag [formed_jadd_empire_flag](../flags/formed_jadd_empire_flag.md)</li></ul></ul><li>remove country modifier = nsc_army_more_paid</li></ul>

___
##Missing localisation: new_sun_cult_39_c

###Available if:
<li>is controlled by the AI</li>

###Efects:<ul><li>decrease nsc isolation level = yes</li></ul>
