#Information
 - Title: Among the Smouldering Rubble
 - ID: new_sun_cult.174
#Description
Among the Smouldering Rubble
#Options

___
##We will do everything in our power to avenge our [Root.getRulerOrHeirAtSamartal]

###Available if:
<li>has country flag [nsc_same_room_as_explosion](../flags/nsc_same_room_as_explosion.md)</li>

###Efects:<ul><li>custom tooltip = nsc_samartal_investigation_starts_tt</li><li>If every known country has religion is bulwari sun cult, and does not have subject of is ROOT; and does not have overlord of is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_tragedy_of_samartal</li></ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -15</li><li>mutual = no</li></ul></ul><li>hidden effect:</li><ul><li>If has country flag is [azka_evran_education_event_will_happen](../flags/azka_evran_education_event_will_happen.md):</li><ul><li>the event [The Education of [Root.Monarch.GetName] [Root.Monarch.Dynasty.GetName]](../events/the_education_of_root_monarch_getname_root_monarch_dynasty_getname.md) happens</li></ul></ul></ul>

___
##This attempt on the life on our [Root.getRulerOrHeirAtSamartal] will not go unpunished

###Available if:
<li>has country flag [nsc_adjacent_room_as_explosion](../flags/nsc_adjacent_room_as_explosion.md)</li>

###Efects:<ul><li>custom tooltip = nsc_samartal_investigation_starts_tt</li><li>If has ruler flag is [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md):</li><ul><li>set ruler flag [nsc_injured](../flags/nsc_injured.md)</li><li>clr ruler flag [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md)</li><li>custom tooltip = nsc_ruler_injured_tt</li><li>hidden effect:</li><ul><li>If has adm is 2:</li><ul><li>change adm = -2</li><li>set ruler flag [nsc_adm_2](../flags/nsc_adm_2.md)</li></ul><li>Else if has adm is 1:</li><ul><li>change adm = -1</li><li>set ruler flag [nsc_adm_1](../flags/nsc_adm_1.md)</li></ul><li>If has dip is 2:</li><ul><li>change dip = -2</li><li>set ruler flag [nsc_dip_2](../flags/nsc_dip_2.md)</li></ul><li>Else if has dip is 1:</li><ul><li>change dip = -1</li><li>set ruler flag [nsc_dip_1](../flags/nsc_dip_1.md)</li></ul><li>If has mil is 2:</li><ul><li>change mil = -2</li><li>set ruler flag [nsc_mil_2](../flags/nsc_mil_2.md)</li></ul><li>Else if has mil is 1:</li><ul><li>change mil = -1</li><li>set ruler flag [nsc_mil_1](../flags/nsc_mil_1.md)</li></ul><li>add ruler modifier:</li><ul><li>name = nsc_wounded_ruler</li><li>duration = 365</li></ul></ul></ul><li>Else if has ruler flag is [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md):</li><ul><li>set heir flag [nsc_injured](../flags/nsc_injured.md)</li><li>clr heir flag [nsc_is_at_samartal](../flags/nsc_is_at_samartal.md)</li><li>custom tooltip = nsc_heir_injured_tt</li><li>hidden effect:</li><ul><li>If has heir adm is 2:</li><ul><li>change heir adm = -2</li><li>set heir flag [nsc_adm_2](../flags/nsc_adm_2.md)</li></ul><li>Else if has heir adm is 1:</li><ul><li>change heir adm = -1</li><li>set heir flag [nsc_adm_1](../flags/nsc_adm_1.md)</li></ul><li>If has heir dip is 2:</li><ul><li>change heir dip = -2</li><li>set heir flag [nsc_dip_2](../flags/nsc_dip_2.md)</li></ul><li>Else if has heir dip is 1:</li><ul><li>change heir dip = -1</li><li>set heir flag [nsc_dip_1](../flags/nsc_dip_1.md)</li></ul><li>If has heir mil is 2:</li><ul><li>change heir mil = -2</li><li>set heir flag [nsc_mil_2](../flags/nsc_mil_2.md)</li></ul><li>Else if has heir mil is 1:</li><ul><li>change heir mil = -1</li><li>set heir flag [nsc_mil_1](../flags/nsc_mil_1.md)</li></ul></ul></ul><li>If every known country has religion is bulwari sun cult, and does not have subject of is ROOT; and does not have overlord of is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_tragedy_of_samartal</li></ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -15</li><li>mutual = no</li></ul></ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>the event [Recovery](../events/recovery.md) happens</li></ul><li>50:</li><ul><li>the event [Death](../events/death.md) happens</li></ul></ul></ul></ul>

___
##This attempt on the life on our [Root.getRulerOrHeirAtSamartal] will not go unpunished

###Available if:
<li>has country flag [nsc_far_from_explosion](../flags/nsc_far_from_explosion.md)</li>

###Efects:<ul><li>custom tooltip = nsc_samartal_investigation_starts_tt</li><li>If every known country has religion is bulwari sun cult, and does not have subject of is ROOT; and does not have overlord of is ROOT:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = nsc_tragedy_of_samartal</li></ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -15</li><li>mutual = no</li></ul></ul></ul>
