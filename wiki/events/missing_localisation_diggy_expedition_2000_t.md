#Information
 - Title: Missing localisation: diggy_expedition_2000_t
 - ID: diggy_expedition.2000
#Description

#Options

___
##Missing localisation: diggy_expedition_2000_a

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>progress advancement = yes</li><li>If does not have check variable has progressFloor is 100; and  has check variable has partyManpower is 1:</li><ul><li>If has check variable has progressFloor is 80; and does not have check variable has nbEncounters is 1; and does not have province flag is [forced_floor_encounter](../flags/forced_floor_encounter.md); and does not have province flag is [encounter_happening](../flags/encounter_happening.md):</li><ul><li>set province flag [forced_floor_encounter](../flags/forced_floor_encounter.md)</li><li>change variable:</li><ul><li>nbEncounters = 1</li></ul><li>set province flag [encounter_happening](../flags/encounter_happening.md)</li><li>launch encounter = yes</li></ul><li>Else if does not have check variable has nbEncounters is 3; and does not have province flag is [encounter_happening](../flags/encounter_happening.md):</li><ul><li>random list:</li><ul><li>10:</li><ul><li>modifier:</li><ul><li>factor = 1.4</li><li>check variable:</li><ul><li>dangerLevel = 2</li></ul></ul><li>modifier:</li><ul><li>factor = 1.4</li><li>check variable:</li><ul><li>dangerLevel = 3</li></ul></ul><li>modifier:</li><ul><li>factor = 1.4</li><li>check variable:</li><ul><li>dangerLevel = 4</li></ul></ul><li>modifier:</li><ul><li>factor = 1.4</li><li>check variable:</li><ul><li>dangerLevel = 5</li></ul></ul><li>modifier:</li><ul><li>factor = 1.4</li><li>owner:</li><ul><li>NOT:</li><ul><li>num of cities = 2</li></ul></ul></ul><li>change variable:</li><ul><li>nbEncounters = 1</li></ul><li>set province flag [encounter_happening](../flags/encounter_happening.md)</li><li>launch encounter = yes</li></ul><li>90:</li><ul><li>fire province event [diggy_expedition.2000](diggy_expedition.2000_slug) in 30 days</li></ul></ul></ul><li>Else if has province flag is [encounter_happening](../flags/encounter_happening.md):</li><ul><li>clr province flag [encounter_happening](../flags/encounter_happening.md)</li><li>fire province event [diggy_expedition.2000](diggy_expedition.2000_slug) in 30 days</li></ul><li>else:</li><ul><li>fire province event [diggy_expedition.2000](diggy_expedition.2000_slug) in 30 days</li></ul></ul><li>Else if does not have check variable has partyManpower is 1:</li><ul><li>fire province event [diggy_expedition.13](diggy_expedition.13_slug) immediately </li></ul><li>else:</li><ul><li>change variable:</li><ul><li>clearedFloor = 1</li></ul><li>If does not have variable equal has which is nbFloor, and is variable equal has which is clearedFloor:</li><ul><li>fire province event [diggy_expedition.11](diggy_expedition.11_slug) immediately </li></ul><li>else:</li><ul><li>fire province event [diggy_expedition.12](diggy_expedition.12_slug) immediately </li></ul></ul></ul>
