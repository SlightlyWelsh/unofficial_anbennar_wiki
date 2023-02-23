This page has the same name as others. For full listing see bottom of [the base page](missing_localisation_spirits_502_t22.md).

#Information
 - Title: Missing localisation: spirits_502_t
 - ID: spirits.517
#Description

#Options

___
##Unnamed Option

###AI weighting:
AI weights this option at 10
 - Multiplied by 1.1 if has country flag is [party_leader_is_monk](../flags/party_leader_is_monk.md), and has country flag is party leader is bard
 - Multiplied by 1.2 if has country flag is [party_leader_is_barbarian](../flags/party_leader_is_barbarian.md), and has country flag is party leader is artificer
 - Multiplied by 1.3 if has country flag is [party_leader_is_fighter](../flags/party_leader_is_fighter.md)
 - Multiplied by 1.5 if has country flag is [party_leader_is_evoker](../flags/party_leader_is_evoker.md)


###Efects:<ul><li>the event [Missing localisation: spirits_502_t](../events/missing_localisation_spirits_502_t.md) happens</li><li>the event [Missing localisation: spirits_502_t](../events/missing_localisation_spirits_502_t.md) happens</li><li>If has religion is lefthand path:</li><ul><li>the event [Temple Quest - Heart Chamber Discovered!](../events/temple_quest_heart_chamber_discovered.md) happens</li></ul><li>else:</li><ul><li>the event [Temple Quest - Heart Chamber Discovered!](../events/temple_quest_heart_chamber_discovered.md) happens</li></ul></ul>

___
##Unnamed Option_1

###AI weighting:
AI weights this option at 5
 - Multiplied by 1.1 if does not have check variable has which is TempleQuestPartySize, and check variable has value is 4
 - Multiplied by 1.5 if does not have check variable has which is TempleQuestPartySize, and check variable has value is 3
 - Multiplied by 1.8 if does not have check variable has which is TempleQuestPartySize, and check variable has value is 2
 - Multiplied by 0.5 if has event target:temple quest target has province modifier is temple heart trail


###Efects:<ul><li>the event [Expedition Presumed Dead](../events/expedition_presumed_dead.md) happens</li><li>If does not have event target:temple quest target has province modifier is temple heart trail:</li><ul><li>event target:temple quest target:</li><ul><li>add province modifier:</li><ul><li>name = temple_heart_trail</li><li>duration = -1</li><li>hidden = yes</li></ul></ul></ul></ul>
