#Information
 - Title: The Fate of Malacnar
 - ID: flavor_malacnar.200
#Description
The Fate of Malacnar
#Options

___
##Let us appoint a loyal elf to rule the reformed Lordship of Malacnar.

###Available if:
<li>None of the following:</li><ul><li>Country is Amacimst</li><li>Country was Amacimst</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 0.5 if has G32 has num of cities is 5
 - Multiplied by 0 if has G32 has num of cities is 10


###Efects:<ul><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>FROM:</li><ul><li>kill ruler = yes</li><li>add prestige = -25</li><li>change government = monarchy</li><li>add government reform = feudalism_reform</li></ul><li>If every known country has core claim is G32, and  has exists, and does not have tag is ROOT:</li><ul><li>the event [[From.GetName] Seizes Our Land](../events/from_getname_seizes_our_land.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul></ul>

___
##Let us split Malacnar into several loyal lordships.

###Available if:
<li>FROM:</li><ul><li>any owned province:</li><ul><li>None of the following:</li><ul><li>is core is this nation</li></ul><li>any core country:</li><ul><li>None of the following:</li><ul><li>Country is Malacnar</li></ul><li>does not exist</li></ul></ul></ul><li>None of the following:</li><ul><li>Country is Amacimst</li><li>Country was Amacimst</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if has G32 has num of cities is 5
 - Multiplied by 10 if has G32 has num of cities is 10


###Efects:<ul><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>custom tooltip = malacnar_restore_tooltip</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>If every owned province does not have area is malacnar area; and  does not have tag is G32; and any core country has does not exist:</li><ul><li>If random core country has does not exist:</li><ul><li>FROM:</li><ul><li>release = PREV</li></ul><li>hidden effect:</li><ul><li>change government = monarchy</li><li>add government reform = feudalism_reform</li><li>change religion = ROOT</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = saved_us_from_warlord</li></ul><li>every core province:</li><ul><li>remove core = G32</li></ul></ul><li>the event [Missing localisation: ynn_events_20_t](../events/missing_localisation_ynn_events_20_t.md) happens</li></ul></ul></ul></ul><li>FROM:</li><ul><li>kill ruler = yes</li><li>add prestige = -25</li><li>change government = monarchy</li><li>add government reform = feudalism_reform</li></ul><li>If every known country has core claim is G32, and  has exists, and does not have tag is ROOT; and does not have tag is FROM:</li><ul><li>the event [[From.GetName] Seizes Our Land](../events/from_getname_seizes_our_land.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul></ul>

___
##Let us partition Malacnar between its neighbours.

###Available if:
<li>G32:</li><ul><li>is controlled by the AI</li></ul><li>None of the following:</li><ul><li>Country is Amacimst</li><li>Country was Amacimst</li></ul>

###AI weighting:
AI weights this option at 1
 - Multiplied by 2 if has G32 has num of cities is 5
 - Multiplied by 10 if has G32 has num of cities is 10


###Efects:<ul><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>custom tooltip = malacnar_partition_tooltip</li><li>hidden effect:</li><ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT; and  has religion group is ynnic:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random known country does not have tag is ROOT; and  has core claim is FROM:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>event target:malacnar partitioner:</li><ul><li>the event [Partitioning Malacnar](../events/partitioning_malacnar.md) happens</li><li>set country flag [malacnar_partitioner_flag](../flags/malacnar_partitioner_flag.md)</li></ul></ul></ul>

___
##Let us annex Malacnar's lands into our demesne.

###Available if:
<li>G32:</li><ul><li>is controlled by the AI</li></ul><li>None of the following:</li><ul><li>Country is Amacimst</li><li>Country was Amacimst</li></ul>

###AI weighting:
AI weights this option at 2
 - Multiplied by 0.5 if has G32 has num of cities is 5
 - Multiplied by 0 if has G32 has num of cities is 10


###Efects:<ul><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>If malacnar area has owned by is G32:</li><ul><li>cede province = ROOT</li></ul><li>custom tooltip = malacnar_annex_and_restore_tooltip</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>If every owned province does not have area is malacnar area; and  does not have tag is G32; and any core country has does not exist:</li><ul><li>If random core country has does not exist:</li><ul><li>FROM:</li><ul><li>release = PREV</li></ul><li>hidden effect:</li><ul><li>change government = monarchy</li><li>add government reform = feudalism_reform</li><li>change religion = ynn_river_worship</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = saved_us_from_warlord</li></ul><li>every core province:</li><ul><li>remove core = G32</li></ul></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>If has G32 does not have core is ROOT, and does not have area is malacnar area:</li><ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT; and  has religion group is ynnic:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random known country does not have tag is ROOT; and  has core claim is FROM:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>event target:malacnar partitioner:</li><ul><li>the event [Partitioning Malacnar](../events/partitioning_malacnar.md) happens</li><li>set country flag [malacnar_partitioner_flag](../flags/malacnar_partitioner_flag.md)</li></ul></ul></ul><li>If every known country is core is 1168, and is core is 1169, and is core is 2808; and  has exists, and does not have tag is ROOT; and does not have tag is FROM:</li><ul><li>the event [[From.GetName] Seizes Our Land](../events/from_getname_seizes_our_land.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul></ul>

___
##The Battleguards shall take over and turn this into a fine march.

###Available if:
<li>any hired mercenary company:</li><ul><li>template is merc_malacnar_battleguards</li></ul>

###AI weighting:
AI weights this option at 3
 - Multiplied by 0.5 if has G32 has num of cities is 5
 - Multiplied by 0 if has G32 has num of cities is 10


###Efects:<ul><li>highlight = yes</li><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>FROM:</li><ul><li>kill ruler = yes</li><li>add prestige = -25</li><li>change government = theocracy</li><li>add government reform = secular_order_reform</li><li>country gets the modifier G32_ruled_by_battleguards until otherwise removed</li></ul><li>create subject:</li><ul><li>subject type = march</li><li>subject = G32</li></ul><li>If random hired mercenary company has template is merc malacnar battleguards:</li><ul><li>disband mercenary company = THIS</li></ul><li>custom tooltip = ynn_malacnar_battleguards_lose_tt</li><li>If every known country has core claim is G32, and  has exists, and does not have tag is ROOT:</li><ul><li>the event [[From.GetName] Seizes Our Land](../events/from_getname_seizes_our_land.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul></ul>

___
##Let us restore the rightful status quo.

###Available if:
<li>Any of the following:</li><ul><li>Country is Amacimst</li><li>Country was Amacimst</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has core claim is FROM:</li><ul><li>FROM:</li><ul><li>If every owned province is core is ROOT:</li><ul><li>cede province = ROOT</li><li>remove core = G32</li></ul></ul></ul><li>FROM:</li><ul><li>If every owned province has province id is 1168:</li><ul><li>cede province = ROOT</li></ul><li>If every subject country does not have tag is G25:</li><ul><li>grant independence = yes</li></ul></ul><li>FROM:</li><ul><li>kill ruler = yes</li><li>add prestige = -25</li><li>change government = monarchy</li><li>add government reform = feudalism_reform</li><li>set country flag [G32_amacimst_partition_keep_malacnar_flag](../flags/g32_amacimst_partition_keep_malacnar_flag.md)</li></ul><li>custom tooltip = malacnar_restore_tooltip_G26</li><li>hidden effect:</li><ul><li>FROM:</li><ul><li>If every owned province does not have area is malacnar area; and  does not have tag is G32; and any core country has does not exist:</li><ul><li>If random core country has does not exist:</li><ul><li>FROM:</li><ul><li>release = PREV</li></ul><li>hidden effect:</li><ul><li>change government = monarchy</li><li>add government reform = feudalism_reform</li><li>change religion = ynn_river_worship</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = saved_us_from_warlord</li></ul><li>every core province:</li><ul><li>remove core = G32</li></ul></ul></ul></ul></ul></ul><li>hidden effect:</li><ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random neighbor country does not have tag is ROOT; and  has religion group is ynnic:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>G32:</li><ul><li>If random known country does not have tag is ROOT; and  has core claim is FROM:</li><ul><li>save event target as = malacnar_partitioner</li></ul></ul><li>event target:malacnar partitioner:</li><ul><li>the event [Partitioning Malacnar](../events/partitioning_malacnar.md) happens</li><li>set country flag [malacnar_partitioner_flag](../flags/malacnar_partitioner_flag.md)</li></ul></ul><li>If every known country is core is 1169, and is core is 2808; and  has exists, and does not have tag is ROOT; and does not have tag is FROM:</li><ul><li>the event [[From.GetName] Seizes Our Land](../events/from_getname_seizes_our_land.md) happens</li><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = opinion_disappointed</li></ul></ul></ul>
