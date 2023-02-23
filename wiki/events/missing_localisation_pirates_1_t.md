#Information
 - Title: Missing localisation: pirates_1_t
 - ID: pirates.1
#Description

#Options

___
##Missing localisation: pirates_1_keep

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has country flag [pirate_death_election](../flags/pirate_death_election.md)</li></ul>

###AI weighting:
AI weights this option at 60
 - Multiplied by 0 if does not have republican tradition is 25
 - Multiplied by 0.5 if does not have republican tradition is 50
 - Multiplied by 0.5 if does not have republican tradition is 75
 - Multiplied by 2.0 if has republican tradition is 90


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add adm power = 50</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add dip power = 50</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add mil power = 50</li></ul>

###Efects:<ul><li>custom tooltip = remains_ruler</li><li>If has ruler has personality is legendary pirate personality, and has ruler flag is [historical_pirate](../flags/historical_pirate.md):</li><ul><li>custom tooltip = historical_pirate_tooltip</li></ul><li>If has government attribute is reelection increases absolutism:</li><ul><li>tooltip:</li><ul><li>add absolutism = 10</li></ul><li>custom tooltip = ADD_ABSOLUTISM_BASED_ON_ELECTION_TERM</li><li>hidden effect:</li><ul><li>for variable amount:</li><ul><li>variable = election_term</li><li>effect = "</li><li>add absolutism = 10</li></ul></ul><li>hidden effect:</li><ul><li>change variable:</li><ul><li>which = election_term</li><li>value = 1</li></ul></ul></ul><li>change adm = 1</li><li>change dip = 1</li><li>change mil = 1</li><li>If does not have ruler flag is [historical_pirate](../flags/historical_pirate.md); and does not have ruler has personality is legendary pirate personality:</li><ul><li>If has country flag is [increased_election_cost](../flags/increased_election_cost.md):</li><ul><li>add scaled republican tradition = -15</li><li>clr country flag [increased_election_cost](../flags/increased_election_cost.md)</li></ul><li>else:</li><ul><li>add scaled republican tradition = -10</li></ul></ul><li>If has faction in power is pr buccaneers:</li><ul><li>add faction influence:</li><ul><li>faction = pr_buccaneers</li><li>influence = -10</li></ul></ul><li>add karma = -5</li></ul>

___
##Missing localisation: pirates_1_a

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has active policy is mandatory service:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to adm faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li></ul>

___
##Missing localisation: pirates_1_b

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has active policy is mandatory service:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to dip faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li></ul>

___
##Missing localisation: pirates_1_c

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has active policy is mandatory service:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to mil faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li></ul>

___
##Missing localisation: pirates_1_d

###Available if:
<li>None of the following:</li><ul><li>has global flag [blackbeard_flag](../flags/blackbeard_flag.md)</li></ul><li>is year is at least 1700</li><li>NOT:</li><ul><li>is year is at least 1720</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>define ruler:</li><ul><li>name = "Edward 'Blackbeard' Teach"</li><li>adm = 3</li><li>dip = 3</li><li>mil = 6</li><li>culture = english</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Queen Anne's Revenge"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Queen Anne's Revenge"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [blackbeard_flag](../flags/blackbeard_flag.md)</li></ul>

___
##Missing localisation: pirates_1_e

###Available if:
<li>None of the following:</li><ul><li>has global flag [calico_jack](../flags/calico_jack.md)</li></ul><li>is year is at least 1702</li><li>NOT:</li><ul><li>is year is at least 1720</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "'Calico' Jack Rackham"</li><li>adm = 2</li><li>dip = 4</li><li>mil = 4</li><li>culture = english</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Kingston"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Kingston"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [calico_jack](../flags/calico_jack.md)</li></ul>

___
##Missing localisation: pirates_1_f

###Available if:
<li>None of the following:</li><ul><li>has global flag [anne_bonny](../flags/anne_bonny.md)</li></ul><li>is year is at least 1716</li><li>NOT:</li><ul><li>is year is at least 1782</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Anne Bonny"</li><li>adm = 4</li><li>dip = 2</li><li>mil = 5</li><li>culture = irish</li><li>female = yes</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "William"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "William"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [anne_bonny](../flags/anne_bonny.md)</li></ul>

___
##Missing localisation: pirates_1_g

###Available if:
<li>None of the following:</li><ul><li>has global flag [mary_read](../flags/mary_read.md)</li></ul><li>is year is at least 1703</li><li>NOT:</li><ul><li>is year is at least 1721</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Mary Read"</li><li>adm = 3</li><li>dip = 3</li><li>mil = 5</li><li>culture = english</li><li>female = yes</li></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [mary_read](../flags/mary_read.md)</li></ul>

___
##Missing localisation: pirates_1_h

###Available if:
<li>None of the following:</li><ul><li>has global flag [charles_vane](../flags/charles_vane.md)</li></ul><li>is year is at least 1702</li><li>NOT:</li><ul><li>is year is at least 1720</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Charles Vane"</li><li>adm = 2</li><li>dip = 3</li><li>mil = 5</li><li>culture = english</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Ranger"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Ranger"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [charles_vane](../flags/charles_vane.md)</li></ul>

___
##Missing localisation: pirates_1_i

###Available if:
<li>None of the following:</li><ul><li>has global flag [black_caesar](../flags/black_caesar.md)</li></ul><li>is year is at least 1702</li><li>NOT:</li><ul><li>is year is at least 1720</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Black Caesar"</li><li>adm = 4</li><li>dip = 3</li><li>mil = 5</li><li>culture = yorumba</li></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [black_caesar](../flags/black_caesar.md)</li></ul>

___
##Missing localisation: pirates_1_j

###Available if:
<li>None of the following:</li><ul><li>has global flag [ching_shih](../flags/ching_shih.md)</li></ul><li>is year is at least 1795</li><li>capital scope:</li><ul><li>Any of the following:</li><ul><li>superregion is east_indies_superregion</li><li>superregion  is china_superregion</li><li>superregion   is far_east_superregion</li></ul></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Ching Shih"</li><li>adm = 5</li><li>dip = 5</li><li>mil = 6</li><li>culture = cantonese</li><li>female = yes</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Red Flag"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Red Flag"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [ching_shih](../flags/ching_shih.md)</li></ul>

___
##Missing localisation: pirates_1_k

###Available if:
<li>None of the following:</li><ul><li>has global flag [jack_ward](../flags/jack_ward.md)</li></ul><li>is year is at least 1605</li><li>NOT:</li><ul><li>is year is at least 1610</li></ul><li>capital scope:</li><ul><li>region is maghreb_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Jack Ward"</li><li>adm = 3</li><li>dip = 3</li><li>mil = 5</li><li>culture = english</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Gift"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Gift"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [jack_ward](../flags/jack_ward.md)</li></ul>

___
##Missing localisation: pirates_1_l

###Available if:
<li>None of the following:</li><ul><li>has global flag [laurens_de_graaf](../flags/laurens_de_graaf.md)</li></ul><li>is year is at least 1682</li><li>NOT:</li><ul><li>is year is at least 1704</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Laurens de Graaf"</li><li>adm = 2</li><li>dip = 4</li><li>mil = 5</li><li>culture = dutch</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Tigre"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Tigre"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [laurens_de_graaf](../flags/laurens_de_graaf.md)</li></ul>

___
##Missing localisation: pirates_1_m

###Available if:
<li>None of the following:</li><ul><li>has global flag [michel_de_gramont](../flags/michel_de_gramont.md)</li></ul><li>is year is at least 1670</li><li>NOT:</li><ul><li>is year is at least 1686</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Michel de Grammont"</li><li>adm = 3</li><li>dip = 3</li><li>mil = 5</li><li>culture = cosmopolitan_french</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Hardi"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Hardi"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [michel_de_gramont](../flags/michel_de_gramont.md)</li></ul>

___
##Missing localisation: pirates_1_n

###Available if:
<li>None of the following:</li><ul><li>has global flag [piet_hein](../flags/piet_hein.md)</li></ul><li>is year is at least 1607</li><li>NOT:</li><ul><li>is year is at least 1629</li></ul><li>primary culture is dutch</li>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Piet Heyn"</li><li>adm = 3</li><li>dip = 4</li><li>mil = 5</li><li>culture = dutch</li></ul><li>If has or building flagship is no, and  has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create flagship:</li><ul><li>name = "Hollandia"</li><li>type = heavy_ship</li></ul></ul></ul><li>Else if has capital scope has port:</li><ul><li>capital scope:</li><ul><li>create named ship:</li><ul><li>name = "Hollandia"</li><li>type = heavy_ship</li></ul></ul></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [piet_hein](../flags/piet_hein.md)</li></ul>

___
##Missing localisation: pirates_1_p

###Available if:
<li>None of the following:</li><ul><li>has global flag [francois_olonnais](../flags/francois_olonnais.md)</li></ul><li>is year is at least 1650</li><li>NOT:</li><ul><li>is year is at least 1669</li></ul><li>capital scope:</li><ul><li>region is carribeans_region</li></ul>

###AI weighting:
AI weights this option at 500


###Efects:<ul><li>define ruler:</li><ul><li>name = "Franï¿½ois l'Olonnais"</li><li>adm = 3</li><li>dip = 1</li><li>mil = 5</li><li>culture = cosmopolitan_french</li></ul><li>custom tooltip = historical_pirate_tooltip</li><li>set ruler flag [historical_pirate](../flags/historical_pirate.md)</li><li>add ruler personality = legendary_pirate_personality</li><li>set global flag [francois_olonnais](../flags/francois_olonnais.md)</li></ul>

___
##A feared Xhazobkult priest

###Available if:
<li>has faction mykx_xhazobkult</li>

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has active policy is mandatory service:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>If has faction is mykx xhazobkult:</li><ul><li>add faction influence:</li><ul><li>faction = mykx_xhazobkult</li><li>influence = 20</li></ul></ul></ul>
