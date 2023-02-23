This page has the same name as others. For full listing see bottom of [the base page](missing_localisation_spirits_502_t2.md).

#Information
 - Title: Missing localisation: spirits_502_t
 - ID: spirits.511
#Description

#Options

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 0</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 14
 - Multiplied by 1.1 if has country flag is [party_leader_is_barbarian](../flags/party_leader_is_barbarian.md), and has country flag is party leader is bard
 - Multiplied by 1.2 if has country flag is [party_leader_is_monk](../flags/party_leader_is_monk.md)
 - Multiplied by 1.3 if has country flag is [party_leader_is_rogue](../flags/party_leader_is_rogue.md)
 - Multiplied by 1.5 if has country flag is [party_leader_is_diviner](../flags/party_leader_is_diviner.md)


###Efects:<ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 0</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 7


###Efects:<ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>change variable:</li><ul><li>which = WoundedPartyMembers</li><li>value = 1</li></ul><li>set country flag [temple_quest_party_member_wounded](../flags/temple_quest_party_member_wounded.md)</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 0</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul></ul>

###AI weighting:
AI weights this option at 3


###Efects:<ul><li>If has check variable has which is RaiseDeadRemaining, and check variable has value is 1:</li><ul><li>subtract variable:</li><ul><li>which = RaiseDeadRemaining</li><li>value = 1</li></ul><li>set country flag [necromancer_raised_dead](../flags/necromancer_raised_dead.md)</li></ul><li>else:</li><ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul></ul><li>set country flag [temple_quest_lost_party_member](../flags/temple_quest_lost_party_member.md)</li><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul></ul>

###AI weighting:
AI weights this option at 12
 - Multiplied by 1.1 if has country flag is [party_leader_is_barbarian](../flags/party_leader_is_barbarian.md), and has country flag is party leader is bard
 - Multiplied by 1.2 if has country flag is [party_leader_is_monk](../flags/party_leader_is_monk.md)
 - Multiplied by 1.3 if has country flag is [party_leader_is_rogue](../flags/party_leader_is_rogue.md)
 - Multiplied by 1.5 if has country flag is [party_leader_is_diviner](../flags/party_leader_is_diviner.md)


###Efects:<ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul></ul>

###AI weighting:
AI weights this option at 8


###Efects:<ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>change variable:</li><ul><li>which = WoundedPartyMembers</li><li>value = 1</li></ul><li>set country flag [temple_quest_party_member_wounded](../flags/temple_quest_party_member_wounded.md)</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 1</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul></ul>

###AI weighting:
AI weights this option at 4


###Efects:<ul><li>If has check variable has which is RaiseDeadRemaining, and check variable has value is 1:</li><ul><li>subtract variable:</li><ul><li>which = RaiseDeadRemaining</li><li>value = 1</li></ul><li>set country flag [necromancer_raised_dead](../flags/necromancer_raised_dead.md)</li></ul><li>else:</li><ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul></ul><li>set country flag [temple_quest_lost_party_member](../flags/temple_quest_lost_party_member.md)</li><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 1.1 if has country flag is [party_leader_is_barbarian](../flags/party_leader_is_barbarian.md), and has country flag is party leader is bard
 - Multiplied by 1.2 if has country flag is [party_leader_is_monk](../flags/party_leader_is_monk.md)
 - Multiplied by 1.3 if has country flag is [party_leader_is_rogue](../flags/party_leader_is_rogue.md)
 - Multiplied by 1.5 if has country flag is [party_leader_is_diviner](../flags/party_leader_is_diviner.md)


###Efects:<ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul></ul>

###AI weighting:
AI weights this option at 9


###Efects:<ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>change variable:</li><ul><li>which = WoundedPartyMembers</li><li>value = 1</li></ul><li>set country flag [temple_quest_party_member_wounded](../flags/temple_quest_party_member_wounded.md)</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul></ul>

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>If has check variable has which is RaiseDeadRemaining, and check variable has value is 1:</li><ul><li>subtract variable:</li><ul><li>which = RaiseDeadRemaining</li><li>value = 1</li></ul><li>set country flag [necromancer_raised_dead](../flags/necromancer_raised_dead.md)</li></ul><li>else:</li><ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul></ul><li>set country flag [temple_quest_lost_party_member](../flags/temple_quest_lost_party_member.md)</li><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 2</li></ul><li>None of the following:</li><ul><li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul></ul>

###AI weighting:
AI weights this option at 8
 - Multiplied by 1.1 if has country flag is [party_leader_is_barbarian](../flags/party_leader_is_barbarian.md), and has country flag is party leader is bard
 - Multiplied by 1.2 if has country flag is [party_leader_is_monk](../flags/party_leader_is_monk.md)
 - Multiplied by 1.3 if has country flag is [party_leader_is_rogue](../flags/party_leader_is_rogue.md)
 - Multiplied by 1.5 if has country flag is [party_leader_is_diviner](../flags/party_leader_is_diviner.md)


###Efects:<ul><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>the event ˻spirits.506˼ happens</li><li>change variable:</li><ul><li>which = WoundedPartyMembers</li><li>value = 1</li></ul><li>set country flag [temple_quest_party_member_wounded](../flags/temple_quest_party_member_wounded.md)</li><li>the event ˻spirits.505˼ happens</li></ul></ul>

___
##Missing localisation: spirits_500_a

###Available if:
<li>check variable:</li><ul><li>which is TempleQuestFloor</li><li>value is at least 3</li></ul>

###AI weighting:
AI weights this option at 6


###Efects:<ul><li>If has check variable has which is RaiseDeadRemaining, and check variable has value is 1:</li><ul><li>subtract variable:</li><ul><li>which = RaiseDeadRemaining</li><li>value = 1</li></ul><li>set country flag [necromancer_raised_dead](../flags/necromancer_raised_dead.md)</li></ul><li>else:</li><ul><li>subtract variable:</li><ul><li>which = TempleQuestPartySize</li><li>value = 1</li></ul></ul><li>If does not have check variable has which is TempleQuestPartySize, and check variable has value is 1:</li><ul><li>the event ˻spirits.503˼ happens</li></ul><li>else:</li><ul><li>set country flag [temple_quest_lost_party_member](../flags/temple_quest_lost_party_member.md)</li><li>the event ˻spirits.506˼ happens</li><li>the event ˻spirits.505˼ happens</li></ul></ul>
