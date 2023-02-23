#Information
 - Title: The Dukeldar Comes to a Close
 - ID: new_sun_cult.26
#Description
The Dukeldar Comes to a Close
#Options

___
##The Sun Elves have stood for centuries and will stand centuries more.

###Available if:
<li>None of the following:</li><ul><li>has country flag [dukedal_lost](../flags/dukedal_lost.md)</li></ul><li>is not controlled by the AI</li>

###Efects:<ul><li>add stability or adm power = yes</li><li>add stability or adm power = yes</li><li>increase nsc isolation level = yes</li><li>If does not haveolationism is 2:</li><ul><li>increase nsc isolation level = yes</li></ul><li>custom tooltip = nsc_dukeldar_will_be_back_tt</li><li>remove country modifier = nsc_army_more_paid</li><li>remove country modifier = nsc_clergy_support</li></ul>

___
##The True will of Surael will at last be the law of the land.

###Available if:
<li>has country flag [dukedal_lost](../flags/dukedal_lost.md)</li><li>is not controlled by the AI</li>

###Efects:<ul><li>add prestige = -50</li><li>custom tooltip = nsc_dukeldar_will_be_back_tt</li><li>clr country flag [locked_racial_administration](../flags/locked_racial_administration.md)</li><li>If has primary culture is sun elf, and has primary culture is dawn elf:</li><ul><li>If has capital scope has region is far bulwar region:</li><ul><li>change primary culture = surani</li></ul><li>Else if has capital scope has region is bahar region:</li><ul><li>change primary culture = bahari</li></ul><li>else:</li><ul><li>change primary culture = zanite</li></ul></ul><li>If has heir culture is sun elf, and has heir culture is dawn elf:</li><ul><li>kill heir:</li><ul><li>allow new heir = no</li></ul></ul><li>If has consort culture is sun elf, and has consort culture is dawn elf:</li><ul><li>remove consort = yes</li></ul><li>If has ruler culture is sun elf, and has ruler culture is dawn elf:</li><ul><li>kill ruler = yes</li></ul><li>If does not have country modifier is human administration:</li><ul><li>clear racial administration = yes</li><li>country gets the modifier restructuring_administration for 10 years</li><li>country gets the modifier human_administration until otherwise removed</li></ul><li>If has tag is F38:</li><ul><li>If does not have primary culture is sun elf; and does not have religion is the jadd; and does not have exists is F52:</li><ul><li>change tag = F52</li><li>swap non generic missions = yes</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>If has idea is F38 mantle of the conqueror:</li><ul><li>swap free idea group = yes</li></ul><li>lock racial admin = yes</li><li>set country flag [formed_great_bulwar_flag](../flags/formed_great_bulwar_flag.md)</li></ul><li>Else if has religion is the jadd, and does not have exists is F51:</li><ul><li>change tag = F51</li><li>hidden effect:</li><ul><li>restore country name = yes</li></ul><li>swap non generic missions = yes</li><li>If has idea is F38 mantle of the conqueror:</li><ul><li>swap free idea group = yes</li></ul><li>If does not have government is monarchy:</li><ul><li>change government = monarchy</li></ul><li>add government reform = jadd_empire</li><li>If has dlc is "Dharma":</li><ul><li>add government reform = jadd_nobility</li></ul><li>the event [The Seat of the Court](../events/the_seat_of_the_court.md) happens</li><li>set country flag [formed_jadd_empire_flag](../flags/formed_jadd_empire_flag.md)</li></ul></ul><li>remove country modifier = nsc_army_more_paid</li><li>remove country modifier = nsc_clergy_support</li></ul>

___
##Missing localisation: new_sun_cult_26_c

###Available if:
<li>is controlled by the AI</li>

###Efects:<ul><li>increase nsc isolation level = yes</li></ul>
