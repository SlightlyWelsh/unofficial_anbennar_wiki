#Information
 - Title: An offer from the Naqtazan
 - ID: flavour_bulwar_tag.33
#Description
An offer from the Naqtazan
#Options

___
##These heretics must be purged!

###Available if:
<li>is subject</li>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>overlord:</li><ul><li>save event target as = kalib_overlord</li></ul><li>grant independence = yes</li><li>event target:kalib overlord:</li><ul><li>the event [Kalib joins the Naqtazan](../events/kalib_joins_the_naqtazan.md) happens</li><li>declare war with cb:</li><ul><li>who = F44</li><li>casus belli = cb_vassalize_mission</li></ul></ul><li>FROM:</li><ul><li>vassalize = F44</li><li>hidden effect:</li><ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>add truce with = F44</li></ul></ul></ul>

___
##Missing localisation: flavour_bulwar_tag_30_b

###Available if:
<li>is not subject</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0 if has army strength has who is FROM, and army strength has value is 1


###Efects:<ul><li>FROM:</li><ul><li>vassalize = F44</li><li>hidden effect:</li><ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour</li></ul><li>reverse remove opinion:</li><ul><li>who = F44</li><li>modifier = nsc_suspicious_behaviour_big</li></ul><li>add truce with = F44</li></ul></ul></ul>

___
##Missing localisation: flavour_bulwar_tag_30_c

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if is subject
 - Multiplied by 0 if does not have army strength has who is FROM, and army strength has value is 0.3
 - Multiplied by 4 if has army strength has who is FROM, and army strength has value is 0.5
 - Multiplied by 2.5 if has army strength has who is FROM, and army strength has value is 0.75


###Efects:<ul><li>FROM:</li><ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulwar_refused_naqtazan</li></ul><li>add casus belli:</li><ul><li>target = ROOT</li><li>type = cb_vassalize_mission</li><li>months = 120</li></ul></ul></ul>
